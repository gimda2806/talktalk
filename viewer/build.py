"""notes/설렘모먼트_장/*.md 와 README 로그 표를 읽어 viewer/dist/index.html 을 만든다.

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
    """README '키워드·인물 로그' 표에서 파일별 키워드와 인물을 읽는다."""
    log = {}
    for line in (ROOT / "README.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*([\d-]+)\s*\|\s*\[.*?\]\((.+?)\)\s*\|(.+?)\|(.+?)\|", line)
        if m:
            log[Path(m.group(2)).name] = (
                [k.strip() for k in m.group(3).split(",") if k.strip()],
                [c.strip() for c in m.group(4).split(",") if c.strip()],
            )
    return log


def merge(lists):
    """여러 목록을 순서를 지키며 중복 없이 합친다."""
    return list(dict.fromkeys(x for xs in lists for x in xs))


def load():
    """같은 번호의 파일을 한 작품으로 묶는다. 01_…_우산.md 는 1화, 01_…_우산_2.md 는 2화."""
    log = read_log()
    series = {}
    for f in CH_DIR.glob("*.md"):
        m = re.fullmatch(r"(\d+)_([^_]+)_([^_]+)_(.+?)(?:_(\d+))?", f.stem)
        if not m:
            print(f"건너뜀 (파일명 형식이 다름): {f.name}", file=sys.stderr)
            continue
        no, fmt, genre, _, ep = m.groups()
        head, _, body = f.read_text(encoding="utf-8").partition("\n")
        title = re.sub(r"\s*\(.*\)\s*$", "", head.split("—")[-1]).strip()
        keywords, cast = log.get(f.name, ([], []))
        s = series.setdefault(no, dict(no=no, format=fmt, genre=genre, episodes=[]))
        s["episodes"].append(dict(id=f"{no}-{ep or 1}", ep=int(ep or 1), file=f.name, title=title,
                                  keywords=keywords, cast=cast, body=body.strip()))
    for s in series.values():
        s["episodes"].sort(key=lambda e: e["ep"])
        first = s["episodes"][0]
        s["title"] = first["title"]
        s["keywords"] = merge(e["keywords"] for e in s["episodes"])
        s["cast"] = merge(e["cast"] for e in s["episodes"])
        # 로그에 줄을 안 적은 회차는 작품 전체의 키워드·인물을 보여 준다
        for e in s["episodes"]:
            e["keywords"] = e["keywords"] or s["keywords"]
            e["cast"] = e["cast"] or s["cast"]
    return [series[k] for k in sorted(series, key=int)]


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
