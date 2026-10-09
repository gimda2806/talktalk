// 설렘 모먼트 뷰어의 서버 쪽. 정적 페이지(viewer/dist)는 ASSETS가 그대로 내주고,
// /api/* 만 여기서 처리한다. /api/save 는 뷰어에서 고친 글을 GitHub 저장소 파일의
// 그 울타리(```text 블록)에만 되써서 main 에 커밋한다. 커밋이 올라가면 배포 워크플로가
// 뷰어를 다시 만든다.
//
// 필요한 비밀값 (Cloudflare → Workers → talktalk → Settings → Variables and Secrets):
//   GITHUB_TOKEN   저장소 contents 읽기·쓰기 권한이 있는 토큰 (fine-grained PAT 권장)
//   EDIT_PASSWORD  뷰어에서 저장할 때 묻는 비밀번호
const OWNER = "gimda2806", REPO = "talktalk", BRANCH = "main";

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    if (url.pathname === "/api/ping") return json({ ok: true, editable: !!(env.GITHUB_TOKEN && env.EDIT_PASSWORD) });
    if (url.pathname === "/api/save") return req.method === "POST" ? save(req, env) : json({ error: "POST만 받아요" }, 405);
    return env.ASSETS.fetch(req);
  },
};

async function save(req, env) {
  if (!env.GITHUB_TOKEN || !env.EDIT_PASSWORD) return json({ error: "서버에 GITHUB_TOKEN·EDIT_PASSWORD가 아직 없어요" }, 503);
  if (!safeEqual(req.headers.get("x-edit-password") || "", env.EDIT_PASSWORD)) return json({ error: "비밀번호가 달라요" }, 401);
  let body;
  try { body = await req.json(); } catch { return json({ error: "요청 본문이 JSON이 아니에요" }, 400); }
  const { file, bi, old, new: fresh, label, kind } = body || {};
  const isText = kind === "text";
  if (typeof file !== "string" || !/^zeta\/[^/]+\.md$/.test(file) || (!isText && (!Number.isInteger(bi) || bi < 0)) || typeof old !== "string" || typeof fresh !== "string")
    return json({ error: "file·bi·old·new가 필요해요 (file은 zeta/ 아래 .md)" }, 400);
  if (fresh.trim() === old.trim()) return json({ ok: true, unchanged: true });

  const api = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${encodeURI(file)}`;
  const headers = { Authorization: `Bearer ${env.GITHUB_TOKEN}`, Accept: "application/vnd.github+json", "User-Agent": "talktalk-viewer", "X-GitHub-Api-Version": "2022-11-28" };
  const got = await fetch(`${api}?ref=${BRANCH}`, { headers });
  if (!got.ok) return json({ error: `GitHub에서 파일을 못 읽었어요 (${got.status})` }, 502);
  const meta = await got.json();
  const text = fromBase64(meta.content);

  const r = isText ? replaceText(text, old, fresh) : replaceBlock(text, bi, old, fresh);
  if (r.error) return json({ error: r.error, conflict: true }, 409);
  r.text = markHumanEdit(r.text, label || (isText ? "설명 글" : "칸"));

  const put = await fetch(api, {
    method: "PUT", headers: { ...headers, "Content-Type": "application/json" },
    body: JSON.stringify({ message: `뷰어에서 수정: ${label || "칸"} (${file.replace(/^zeta\//, "")})`, content: toBase64(r.text), sha: meta.sha, branch: BRANCH }),
  });
  if (!put.ok) return json({ error: `GitHub에 저장하지 못했어요 (${put.status})` }, 502);
  const done = await put.json();
  return json({ ok: true, commit: done.commit && done.commit.html_url });
}

// 파일 안의 bi번째 ```text 울타리 속 글이 old와 같으면 fresh로 바꾼다. 다르면 누가 먼저 고친 것이므로 거절한다.
export function replaceBlock(text, bi, old, fresh) {
  const lines = text.split("\n");
  let n = -1, start = -1;
  for (let i = 0; i < lines.length; i++) {
    if (start < 0) {
      if (/^```text\s*$/.test(lines[i])) { n++; if (n === bi) start = i + 1; }
    } else if (/^```\s*$/.test(lines[i])) {
      const cur = lines.slice(start, i).join("\n");
      if (cur.trim() !== old.trim()) return { error: "이 칸이 그사이 다른 곳에서 바뀌었어요. 새로고침한 뒤 다시 고쳐 주세요." };
      const body = fresh.replace(/\r\n/g, "\n").replace(/\s+$/, "").replace(/^\n+/, "");
      return { text: [...lines.slice(0, start), ...body.split("\n"), ...lines.slice(i)].join("\n") };
    }
  }
  return { error: "그 칸을 파일에서 찾지 못했어요. 새로고침한 뒤 다시 고쳐 주세요." };
}

// 울타리 밖 설명 글(기획 요약, 이벤트 같은 것): 파일 안에 그 글이 꼭 한 번 있어야 바꾼다
export function replaceText(text, old, fresh) {
  const o = old.replace(/\r\n/g, "\n").replace(/^\n+|\s+$/g, "");
  if (!o) return { error: "비어 있는 글은 바꿀 수 없어요." };
  const first = text.indexOf(o);
  if (first < 0) return { error: "이 글이 그사이 다른 곳에서 바뀌었어요. 새로고침한 뒤 다시 고쳐 주세요." };
  if (text.indexOf(o, first + 1) >= 0) return { error: "같은 글이 파일에 두 번 있어 어느 쪽인지 알 수 없어요. 조금 더 넓게 잡아 고쳐 주세요." };
  const n = fresh.replace(/\r\n/g, "\n").replace(/^\n+|\s+$/g, "");
  return { text: text.slice(0, first) + n + text.slice(first + o.length) };
}

// 파일 끝의 "## 사람이 고친 곳" 절에 한 줄 남긴다. 루틴·정독은 이 절에 적힌 칸을 규칙보다 위에 둔다.
export function markHumanEdit(text, label) {
  const kst = new Date(Date.now() + 9 * 3600 * 1000);
  const p = n => String(n).padStart(2, "0");
  const when = `${kst.getUTCFullYear()}-${p(kst.getUTCMonth() + 1)}-${p(kst.getUTCDate())} ${p(kst.getUTCHours())}:${p(kst.getUTCMinutes())}`;
  const line = `- ${when} · ${label}`;
  const head = "## 사람이 고친 곳";
  let t = text.replace(/\s+$/, "");
  if (t.includes(`\n${head}\n`)) return t + "\n" + line + "\n";
  return t + `\n\n${head}\n\n뷰어에서 사람이 직접 고친 칸. 여기 적힌 칸은 모든 규칙보다 우선하며, 정독·일괄 치환·재설계 때 되돌리지 않는다.\n\n${line}\n`;
}

function safeEqual(a, b) {
  const ea = new TextEncoder().encode(a), eb = new TextEncoder().encode(b);
  if (ea.length !== eb.length) return false;
  let d = 0; for (let i = 0; i < ea.length; i++) d |= ea[i] ^ eb[i];
  return d === 0;
}
function fromBase64(b64) {
  const bin = atob(b64.replace(/\n/g, "")); const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}
function toBase64(str) {
  const bytes = new TextEncoder().encode(str); let bin = "";
  for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
  return btoa(bin);
}
function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" } });
}
