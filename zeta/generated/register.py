"""생성한 프로필 이미지를 manifest.json에 등록한다 (프롬프트 지문 포함).

사용법 (저장소 루트에서):
  python3 zeta/generated/register.py zeta_042_송예찬 주인공 song-yechan-main.png
  python3 zeta/generated/register.py zeta_042_송예찬 남성용 song-yechan-user-m.png
  python3 zeta/generated/register.py zeta_042_송예찬 여성용 song-yechan-user-f.png
  python3 zeta/generated/register.py zeta_084_손태윤 조연 son-taeyun-sub.png   # 서브 남주 등 조연 프로필
  python3 zeta/generated/register.py --check   # 프롬프트가 바뀐 이미지가 있는지 확인

등록할 때 그 순간의 프롬프트 지문(prompt_sha)을 함께 적어 둔다. 나중에 플롯의 이미지 프롬프트가 바뀌면
지문이 달라지고, 뷰어 갤러리와 --check 가 '프롬프트가 바뀜'이라고 알려 준다. 이미지를 다시 만들어
등록하면 지문이 새로 적힌다.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ZETA_DIR = ROOT / "zeta"
MANIFEST = Path(__file__).resolve().parent / "manifest.json"
KINDS = {
    "주인공": r"^### 주인공 프로필용\n+```text\n(.*?)```",
    "남성용": r"^(?:#### 남성용|### 유저 대화 프로필용 \(남성용\))\n+```text\n(.*?)```",
    "여성용": r"^(?:#### 여성용|### 유저 대화 프로필용 \(여성용\))\n+```text\n(.*?)```",
    "조연": r"^### 조연 프로필용 \([^)\n]*\)\n+```text\n(.*?)```",
}


def prompt_sha(stem, kind):
    """작품 파일에서 해당 프롬프트 블록(긴 버전)을 찾아 지문을 만든다. 없으면 None."""
    path = ZETA_DIR / f"{stem}.md"
    if not path.exists() or kind not in KINDS:
        return None
    m = re.search(KINDS[kind], path.read_text(encoding="utf-8"), re.M | re.S)
    if not m:
        return None
    return hashlib.sha256(m.group(1).strip().encode("utf-8")).hexdigest()[:12]


def guess_kind(item):
    if item.get("prompt") in KINDS:
        return item["prompt"]
    f = item.get("file", "")
    return "남성용" if "user-m" in f else "여성용" if "user-f" in f else "조연" if "-sub" in f else "주인공"


def load():
    return json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}


def save(rows):
    MANIFEST.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def check(rows):
    stale = []
    for stem, items in rows.items():
        for it in items:
            kind = guess_kind(it)
            cur = prompt_sha(stem, kind)
            if it.get("prompt_sha") and cur and it["prompt_sha"] != cur:
                stale.append((stem, kind, it["file"]))
    return stale


def main(argv):
    rows = load()
    if argv[:1] == ["--check"]:
        stale = check(rows)
        for stem, kind, f in stale:
            print(f"⚠ {stem} {kind} ({f}): 이미지를 만든 뒤 프롬프트가 바뀜 → 다시 만들지 확인")
        print("프롬프트가 바뀐 이미지 없음" if not stale else f"{len(stale)}장 확인 필요")
        return 1 if stale else 0
    if len(argv) != 3 or argv[1] not in KINDS:
        print(__doc__)
        return 2
    stem, kind, file = argv
    if not (Path(__file__).resolve().parent / file).is_file():
        print(f"파일이 없음: zeta/generated/{file}")
        return 2
    sha = prompt_sha(stem, kind)
    if not sha:
        print(f"프롬프트 블록을 찾지 못함: zeta/{stem}.md · {kind}")
        return 2
    name = re.sub(r"^zeta_\d+_", "", stem)
    label = f"주인공 {name}" if kind == "주인공" else ("유저 프로필 · 남성" if kind == "남성용" else "유저 프로필 · 여성")
    items = [i for i in rows.get(stem, []) if guess_kind(i) != kind]
    items.append(dict(file=file, label=label, prompt=kind, prompt_sha=sha))
    order = list(KINDS)
    rows[stem] = sorted(items, key=lambda i: order.index(guess_kind(i)))
    save(rows)
    print(f"등록: {stem} · {kind} · {file} · 지문 {sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
