"""notes/설렘모먼트_장/<제목 폴더>/*.md 와 README 로그 표를 읽어 viewer/dist/index.html 을 만든다.

제목마다 폴더 하나(예: 01_소설_헤테로_우산/)를 두고, 그 폴더 안에 01.md, 02.md… 순으로
회차(이어 쓴 편)를 쌓는다. 폴더 하나가 뷰어의 '작품' 한 편이 된다.

    python3 viewer/build.py            # 브라우저로 바로 여는 완성 문서
    python3 viewer/build.py --fragment # Artifact 게시용 (doctype/head 없이)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH_DIR = ROOT / "notes" / "설렘모먼트_장"
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


def main():
    data = json.dumps(load(), ensure_ascii=False).replace("</", "<\\/")
    page = (Path(__file__).resolve().parent / "template.html").read_text(encoding="utf-8")
    page = page.replace("/*DATA*/", data)
    if "--fragment" not in sys.argv:
        page = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                '</head>\n<body>\n' + page + '\n</body>\n</html>\n')
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} 생성")


if __name__ == "__main__":
    main()
