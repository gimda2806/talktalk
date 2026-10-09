"""notes/설렘모먼트_장/<제목 폴더>/*.md 와 README 로그 표, zeta/ 작품 파일을 읽어 viewer/dist/index.html 을 만든다.

제목마다 폴더 하나(예: 01_소설_헤테로_우산/)를 두고, 그 폴더 안에 01.md, 02.md… 순으로
회차(이어 쓴 편)를 쌓는다. 폴더 하나가 뷰어의 '작품' 한 편이 된다.

    python3 viewer/build.py            # 브라우저로 바로 여는 완성 문서
    python3 viewer/build.py --fragment # Artifact 게시용 (doctype/head 없이)

제타 탭: zeta/zeta_*.md 의 '### 칸 이름' + ```text 블록 하나가 제타 입력칸 하나다. 블록마다 복사 버튼이 붙는다.
설정집은 zeta/<이름>_설정집.md 를 읽어 '4. 설정집' 자리에 끼워 넣는다.
"""
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH_DIR = ROOT / "notes" / "설렘모먼트_장"
ZETA_DIR = ROOT / "zeta"
ZETA_IMAGE_DIR = ZETA_DIR / "generated"
OUT = Path(__file__).resolve().parent / "dist" / "index.html"


def read_log():
    """README '키워드·인물·수위 로그' 표에서 회차별 키워드·인물·수위를 읽는다."""
    log = {}
    for line in (ROOT / "README.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*([\d-]+)\s*\|\s*\[.*?\]\((.+?)\)\s*\|(.+?)\|(.+?)\|(.+?)\|", line)
        if m:
            link = Path(m.group(2))
            log["/".join(link.parts[-2:])] = (
                [k.strip() for k in m.group(3).split(",") if k.strip()],
                [c.strip() for c in m.group(4).split(",") if c.strip()],
                m.group(5).strip(),
            )
    return log


def merge(lists):
    """여러 목록을 순서를 지키며 중복 없이 합친다."""
    return list(dict.fromkeys(x for xs in lists for x in xs))


def load():
    """제목 폴더 하나 = 작품 하나. 폴더 안 01.md, 02.md… 가 그 작품의 회차가 된다."""
    log = read_log()
    series = []
    for d in sorted(CH_DIR.iterdir()):
        if not d.is_dir():
            continue
        m = re.fullmatch(r"(\d+)_([^_]+)_([^_]+)_(.+)", d.name)
        if not m:
            print(f"건너뜀 (폴더명 형식이 다름): {d.name}", file=sys.stderr)
            continue
        no, fmt, genre, _ = m.groups()
        episodes = []
        for f in sorted(d.glob("*.md")):
            if not f.stem.isdigit():
                print(f"건너뜀 (파일명 형식이 다름): {d.name}/{f.name}", file=sys.stderr)
                continue
            ep = int(f.stem)
            head, _, body = f.read_text(encoding="utf-8").partition("\n")
            title = re.sub(r"\s*\(.*\)\s*$", "", head.split("—")[-1]).strip()
            keywords, cast, heat = log.get(f"{d.name}/{f.name}", ([], [], ""))
            episodes.append(dict(id=f"{no}-{ep}", ep=ep, file=f"{d.name}/{f.name}", title=title,
                                  keywords=keywords, cast=cast, heat=heat, body=body.strip()))
        if not episodes:
            continue
        episodes.sort(key=lambda e: e["ep"])
        s = dict(no=no, format=fmt, genre=genre, episodes=episodes)
        s["title"] = episodes[0]["title"]
        s["keywords"] = merge(e["keywords"] for e in episodes)
        s["cast"] = merge(e["cast"] for e in episodes)
        # 로그에 줄을 안 적은 회차는 작품 전체의 키워드·인물을 보여 준다
        for e in episodes:
            e["keywords"] = e["keywords"] or s["keywords"]
            e["cast"] = e["cast"] or s["cast"]
        series.append(s)
    return sorted(series, key=lambda s: int(s["no"]))


def read_zeta_list():
    """zeta-works-list.md 표에서 파일명 → 작품 정보(날짜·분위기·관계 시작점 등)를 읽는다."""
    rows = {}
    for line in (ZETA_DIR / "zeta-works-list.md").read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 9 or not re.fullmatch(r"[\d-]+", cells[0]):
            continue
        date, name, sub, genre, mood, job, start, device, file = cells
        if file.endswith(".md"):
            rows[file] = dict(date=date, name=name, sub=sub, genre=genre, mood=mood, job=job, start=start, device=device)
    return rows


def parse_blocks(text):
    """'## 묶음' 아래를 순서대로 읽어 head(### 소제목) / field(```text 블록 = 복사 칸) / text(설명 글)로 나눈다.

    울타리 바로 앞의 짧은 한 줄(설정집의 제목·키워드·내용)은 칸의 부제(sub)가 된다.
    """
    groups, cur, label, sub, buf, fence, nth = [], None, "", "", [], False, 0

    def group(title=""):
        g = dict(title=title, items=[])
        groups.append(g)
        return g

    for line in text.splitlines():
        if fence:
            if line.startswith("```"):
                fence = False
                if cur["items"] and cur["items"][-1]["kind"] == "head" and cur["items"][-1]["label"] == label:
                    cur["items"].pop()  # 칸 이름으로 쓰이는 소제목은 따로 보여 주지 않는다
                if not label:  # 소제목 없이 바로 울타리가 오는 칸(소개, 에필로그)은 묶음 이름을 쓴다
                    label = re.sub(r"^\d+\.\s*|\s*탭\s*$", "", cur["title"])
                if not sub and label.startswith("항목") and nth < 3:
                    sub = ("제목", "키워드", "내용")[nth]  # 설정집 항목은 울타리 셋이 제목·키워드·내용 순서
                cur["items"].append(dict(kind="field", label=label, sub=sub, text="\n".join(buf).strip()))
                sub, nth = "", nth + 1
            else:
                buf.append(line)
            continue
        if line.startswith("```"):
            cur = cur or group()
            fence, buf = True, []
            continue
        m = re.match(r"##\s+(.+)", line)
        if m:
            cur, label, sub = group(m.group(1).strip()), "", ""
            continue
        m = re.match(r"####\s+(.+)", line)
        if m:  # 넷째 수준 소제목(남성용/여성용)은 칸 부제로
            sub = m.group(1).strip()
            continue
        m = re.match(r"###\s+(.+)", line)
        if m:
            cur = cur or group()
            label, sub, nth = m.group(1).strip(), "", 0
            cur["items"].append(dict(kind="head", label=label))
            continue
        if line.startswith("# ") or cur is None:
            continue
        s = line.strip()
        if s and len(s) <= 6 and s[0] not in "-*`>":
            sub = s
            continue
        if cur["items"] and cur["items"][-1]["kind"] == "text":
            cur["items"][-1]["lines"].append(line)
        else:
            cur["items"].append(dict(kind="text", lines=[line]))
    for g in groups:
        g["items"] = [i for i in g["items"] if i["kind"] != "text" or any(l.strip() for l in i["lines"])]
    return groups


NUM = "②③④⑤⑥⑦⑧⑨⑩"


def split_intro(text):
    """인트로를 말풍선 단위로 나눈다. `@:` 문단은 한 말풍선, `{{char}}:` 문단은 이어지는 대사 문단까지 한 말풍선."""
    bubbles = []
    for p in re.split(r"\n\s*\n", text.strip()):
        if not p.strip():
            continue
        if p.startswith(("@:", "{{char}}:")) or not bubbles:
            bubbles.append(p)
        else:
            bubbles[-1] += "\n\n" + p
    out = []
    for i, b in enumerate(bubbles):
        kind = "내레이터" if b.startswith("@:") else "캐릭터"
        if kind == "내레이터":
            b = b[2:].strip()  # 내레이터 말풍선은 종류로 구분되므로 `@:`를 뺀다
        out.append(dict(kind="field", label=f"{NUM[i] if i < len(NUM) else i + 2} {kind} 말풍선", sub="", text=b, parts=split_parts(b)))
    return out


def split_parts(text):
    """말풍선 하나를 지문·대사 문단으로 나눈다. 앞머리의 `{{char}}:`·`{{user}}:`는 뺀다. 문단이 하나뿐이고 뺄 것도 없으면 빈 목록."""
    body = re.sub(r"^(\{\{char\}\}|\{\{user\}\}|@):\s*", "", text.strip())
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    parts = [dict(label="지문" if p.startswith("*") and p.endswith("*") else "대사", text=p) for p in paras]
    if len(parts) == 1 and parts[0]["text"] == text.strip():
        return []
    return parts


def split_examples(text):
    """상황 예시를 `{{user}}:` 줄과 `{{char}}:` 응답 단위로 나눈다."""
    units = []
    for l in text.strip().split("\n"):
        if l.startswith("{{user}}:"):
            units.append(["유저", [l]])
        elif l.startswith("{{char}}:"):
            units.append(["캐릭터", [l]])
        elif units:
            units[-1][1].append(l)
    out, n = [], 0
    for kind, ls in units:
        n += kind == "유저"
        t = "\n".join(ls).strip()
        out.append(dict(kind="field", label=f"상황 예시 {n} · {kind}", sub="", text=t, parts=split_parts(t)))
    return out


def split_fields(groups):
    """프롬프트 탭의 상황 예시와 인트로 ②~⑥을 붙여 넣는 단위로 쪼갠다. 원래 덩어리는 두지 않는다."""
    for g in groups:
        items = []
        for i in g["items"]:
            if i["kind"] == "field" and g["title"].startswith("1.") and i["label"].startswith("상황 예시"):
                items += split_examples(i["text"]) or [i]
            elif i["kind"] == "field" and g["title"].startswith("2.") and not i["label"].startswith("①"):
                items += split_intro(i["text"]) or [i]
            else:
                items.append(i)
        g["items"] = items
    return groups


def load_common():
    """zeta-common-lorebook.md 를 목록 맨 위의 항목 하나로 만든다. 모든 작품에 연결하는 설정집이다."""
    f = ZETA_DIR / "zeta-common-lorebook.md"
    if not f.exists():
        return []
    groups = [g for g in parse_blocks(f.read_text(encoding="utf-8")) if not g["title"].startswith("글자 수")]
    items = [i for g in groups for i in g["items"]]
    while items and items[0]["kind"] == "text":
        items.pop(0)
    items.insert(0, dict(kind="text", lines=["모든 작품(플롯)에 연결해서 쓰는 상시형 규칙 모음. 설정집 탭에 항목별로 붙여 넣는다."]))
    return [dict(id="common", file=f"zeta/{f.name}", date="", name="공통 설정집", sub="모든 작품에 연결", genre="", mood="",
                 job="", start="", device="", groups=[dict(title="공통 설정집", items=items)])]


def load_zeta():
    """zeta/zeta_*.md 하나 = 제타 작품 하나. 설정집 파일이 있으면 '4. 설정집' 묶음에 끼워 넣는다."""
    rows = read_zeta_list()
    image_manifest = {}
    manifest = ZETA_IMAGE_DIR / "manifest.json"
    if manifest.exists():
        image_manifest = json.loads(manifest.read_text(encoding="utf-8"))
    works = []
    for f in sorted(ZETA_DIR.glob("zeta_*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.search(r"^#\s*〈(.+?)〉", text, re.M)
        info = rows.get(f.name) or dict(date="", name=m.group(1) if m else f.stem, sub="", genre="", mood="", job="", start="", device="")
        jm = re.search(r"^" + re.escape(info["name"]) + r" \(\d+\)\n([^\n]+)\n", text, re.M)  # 소개 탭의 '이름 (나이)' 다음 줄이 짧은 직업
        info = dict(info, jobShort=jm.group(1).strip() if jm else "")
        groups = parse_blocks(text)
        lore = ZETA_DIR / f"{info['name']}_설정집.md"
        if lore.exists():
            lg = parse_blocks(lore.read_text(encoding="utf-8"))
            items = [i for g in lg if not g["title"].startswith("글자 수") for i in g["items"]]
            while items and items[0]["kind"] == "text":
                items.pop(0)  # 설정집 파일 머리말은 아래 안내문으로 대신한다
            items.insert(0, dict(kind="text", lines=[f"파일: `zeta/{lore.name}` · 설정집 탭에 항목별로 붙여 넣는다. 공통 설정집은 `zeta-common-lorebook.md`를 쓴다."]))
            for g in groups:
                if g["title"].startswith("4."):
                    g["items"] = items
        images = [dict(label=i["label"], url=f"images/{i['file']}") for i in image_manifest.get(f.stem, [])]
        works.append(dict(id=f.stem, file=f"zeta/{f.name}", groups=split_fields(groups), images=images, **info))
    return load_common() + sorted(works, key=lambda w: (w["date"], w["name"]), reverse=True)


def copy_zeta_images():
    """매니페스트에 등록한 생성 이미지를 정적 배포 폴더로 복사한다."""
    manifest = ZETA_IMAGE_DIR / "manifest.json"
    if not manifest.exists():
        return
    rows = json.loads(manifest.read_text(encoding="utf-8"))
    image_out = OUT.parent / "images"
    image_out.mkdir(parents=True, exist_ok=True)
    for items in rows.values():
        for item in items:
            source = ZETA_IMAGE_DIR / item["file"]
            if not source.is_file():
                raise FileNotFoundError(f"이미지 매니페스트 파일이 없음: {source.relative_to(ROOT)}")
            shutil.copy2(source, image_out / source.name)


def main():
    page = (Path(__file__).resolve().parent / "template.html").read_text(encoding="utf-8")
    for key, rows in (("DATA", load()), ("ZETA", load_zeta())):
        page = page.replace(f"/*{key}*/", json.dumps(rows, ensure_ascii=False).replace("</", "<\\/"))
    if "--fragment" not in sys.argv:
        page = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                '</head>\n<body>\n' + page + '\n</body>\n</html>\n')
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    copy_zeta_images()
    print(f"{OUT.relative_to(ROOT)} 생성")


if __name__ == "__main__":
    main()
