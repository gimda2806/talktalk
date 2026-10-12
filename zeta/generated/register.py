"""생성한 프로필 이미지를 manifest.json에 등록한다 (프롬프트 지문 포함).

사용법 (저장소 루트에서):
  python3 zeta/generated/register.py zeta_042_송예찬 주인공 song-yechan-main.png
  python3 zeta/generated/register.py zeta_042_송예찬 남성용 song-yechan-user-m.png
  python3 zeta/generated/register.py zeta_042_송예찬 여성용 song-yechan-user-f.png
  python3 zeta/generated/register.py zeta_084_손태윤 조연 son-taeyun-sub.png   # 서브 남주 등 조연 프로필
  python3 zeta/generated/register.py zeta_001_백서율 카메오 baek-seoyul-noh-chanyoung-cameo.png 노찬영
  python3 zeta/generated/register.py --check   # 프롬프트가 바뀐 이미지가 있는지 확인

등록할 때 그 순간의 프롬프트 지문(prompt_sha)을 함께 적어 둔다. 나중에 플롯의 이미지 프롬프트가 바뀌면
지문이 달라지고, 뷰어 갤러리와 --check 가 '프롬프트가 바뀜'이라고 알려 준다. 이미지를 다시 만들어
등록하면 지문이 새로 적힌다.

이미지는 zeta/generated/번호_이름/ (예: 001_백서율/) 한 곳에만 둔다. 루트(zeta/generated/)에 새로 넣은 파일은 등록하면서
해당 작품의 번호_이름 폴더로 자동 이동하고, manifest에는 '번호_이름/파일명'으로 적는다. 이미 어떤 번호_이름 폴더에
있는 파일(예: 다른 쪽 캐릭터 폴더에 둔 카메오)은 옮기지 않고 그 경로로 등록한다. 파일명은 저장소 전체에서 겹치지 않아야 한다.

카메오: 연작의 두 캐릭터가 한 장면에 나오는 이미지. 프롬프트는 작품 파일이 아니라 zeta/zeta-series.md 의
'### … — 이름 × 이름' 제목 아래 첫 ```text 블록(긴 버전)에서 찾는다. 네 번째 인자로 상대 캐릭터 이름을 주면
그 짝의 장면을 고른다. 같은 파일을 두 캐릭터 작품에 각각 등록하면 양쪽 갤러리에 모두 뜬다.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ZETA_DIR = ROOT / "zeta"
SERIES = ZETA_DIR / "zeta-series.md"
MANIFEST = Path(__file__).resolve().parent / "manifest.json"
GENERATED_DIR = Path(__file__).resolve().parent
PLOTS_DIR = GENERATED_DIR  # 번호_이름 폴더가 generated 바로 아래에 있다
KINDS = {
    "주인공": r"^### 주인공 프로필용\n+```text\n(.*?)```",
    "남성용": r"^(?:#{3,4} 남성용|### 유저 대화 프로필용 \(남성용\))\n+```text\n(.*?)```",
    "여성용": r"^(?:#{3,4} 여성용|### 유저 대화 프로필용 \(여성용\))\n+```text\n(.*?)```",
    "조연": r"^### 조연 프로필용 \([^)\n]*\)\n+```text\n(.*?)```",
    "카메오": None,  # zeta-series.md 에서 찾는다 (cameo_block 참고)
}
CAMEO_HEAD = re.compile(r"^### (.+?) — (.+?) × (.+?)\s*$", re.M)


def _sha(text):
    return hashlib.sha256(text.strip().encode("utf-8")).hexdigest()[:12]


def work_name(stem):
    return re.sub(r"^zeta_\d+_", "", stem)


def source_path(file):
    """generated 폴더 안의 상대 경로만 받는다. 파일명만 주면 루트에서, 없으면 번호_이름 폴더 안에서 (하나뿐일 때) 찾는다."""
    relative = Path(file)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("generated 폴더 안의 상대 경로만 사용할 수 있습니다")
    path = GENERATED_DIR / relative
    if not path.is_file() and len(relative.parts) == 1:
        found = [p for p in GENERATED_DIR.glob(f"*/{relative.name}") if p.parent.name[:3].isdigit()]
        if len(found) == 1:
            return found[0]
    return path


def organize_file(stem, file):
    """등록 이미지를 해당 플롯 폴더로 옮기고 manifest용 상대 경로를 돌려준다."""
    source = source_path(file)
    if not source.is_file():
        raise FileNotFoundError(file)
    match = re.match(r"^zeta_(\d+)_", stem)
    if not match:
        raise ValueError(f"플롯 번호를 찾을 수 없습니다: {stem}")
    if source.parent != GENERATED_DIR:  # 이미 어떤 번호_이름 폴더에 있으면 그대로 둔다
        return source.relative_to(GENERATED_DIR).as_posix()
    destination = PLOTS_DIR / f"{match.group(1)}_{work_name(stem)}" / source.name
    if source != destination:
        destination.parent.mkdir(parents=True, exist_ok=True)
        source.replace(destination)  # 다시 만든 이미지는 같은 이름의 기존 파일을 덮어쓴다
    return destination.relative_to(GENERATED_DIR).as_posix()


def cameo_block(name, partner=None):
    """zeta-series.md 에서 name 이 나오는 카메오 장면을 찾아 (장면 제목, 상대 이름, 긴 프롬프트)를 돌려준다."""
    if not SERIES.exists():
        return None
    text = SERIES.read_text(encoding="utf-8")
    heads = list(CAMEO_HEAD.finditer(text))
    for n, h in enumerate(heads):
        title, a, b = (s.strip() for s in h.groups())
        if name not in (a, b):
            continue
        other = b if name == a else a
        if partner and partner != other:
            continue
        end = heads[n + 1].start() if n + 1 < len(heads) else len(text)
        m = re.search(r"```text\n(.*?)```", text[h.end():end], re.S)
        if m:
            return title, other, m.group(1)
    return None


def prompt_sha(stem, kind, item=None):
    """해당 프롬프트 블록(긴 버전)을 찾아 지문을 만든다. 없으면 None. 카메오는 item 의 with(상대 이름)로 장면을 고른다."""
    if kind == "카메오":
        found = cameo_block(work_name(stem), (item or {}).get("with"))
        return _sha(found[2]) if found else None
    path = ZETA_DIR / f"{stem}.md"
    if not path.exists() or kind not in KINDS:
        return None
    m = re.search(KINDS[kind], path.read_text(encoding="utf-8"), re.M | re.S)
    if not m:
        return None
    return _sha(m.group(1))


def guess_kind(item):
    if item.get("prompt") in KINDS:
        return item["prompt"]
    f = item.get("file", "")
    return "카메오" if "cameo" in f else "남성용" if "user-m" in f else "여성용" if "user-f" in f else "조연" if "-sub" in f else "주인공"


def load():
    return json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}


def save(rows):
    MANIFEST.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def check(rows):
    stale = []
    for stem, items in rows.items():
        for it in items:
            kind = guess_kind(it)
            cur = prompt_sha(stem, kind, it)
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
    if len(argv) not in (3, 4) or argv[1] not in KINDS or (len(argv) == 4 and argv[1] != "카메오"):
        print(__doc__)
        return 2
    stem, kind, file = argv[:3]
    partner = argv[3] if len(argv) == 4 else None
    try:
        exists = source_path(file).is_file()
    except ValueError as error:
        print(error)
        return 2
    if not exists:
        print(f"파일이 없음: zeta/generated/{file}")
        return 2
    name = work_name(stem)
    if kind == "카메오":
        found = cameo_block(name, partner)
        if not found:
            print(f"카메오 프롬프트 블록을 찾지 못함: zeta/zeta-series.md · {name}" + (f" × {partner}" if partner else ""))
            return 2
        title, other, prompt = found
        sha = _sha(prompt)
        item = dict(file=file, label=f"카메오 · {title}", prompt=kind, prompt_sha=sha, **{"with": other})
        items = [i for i in rows.get(stem, []) if Path(i.get("file", "")).name != Path(file).name]  # 같은 파일만 바꾸고 다른 카메오는 둔다
    else:
        sha = prompt_sha(stem, kind)
        if not sha:
            print(f"프롬프트 블록을 찾지 못함: zeta/{stem}.md · {kind}")
            return 2
        if kind == "조연":
            h = re.search(r"^### 조연 프로필용 \(([^)\n]*)\)", (ZETA_DIR / f"{stem}.md").read_text(encoding="utf-8"), re.M)
            label = f"조연 · {h.group(1).strip()}" if h else "조연"
        else:
            label = f"주인공 {name}" if kind == "주인공" else ("유저 프로필 · 남성" if kind == "남성용" else "유저 프로필 · 여성")
        item = dict(file=file, label=label, prompt=kind, prompt_sha=sha)
        items = [i for i in rows.get(stem, []) if guess_kind(i) != kind]
    try:
        file = organize_file(stem, file)
    except (ValueError, FileNotFoundError, FileExistsError) as error:
        print(f"파일 정리 실패: {error}")
        return 2
    item["file"] = file
    items.append(item)
    order = list(KINDS)
    rows[stem] = sorted(items, key=lambda i: order.index(guess_kind(i)))
    save(rows)
    print(f"등록: {stem} · {kind} · {file} · 지문 {sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
