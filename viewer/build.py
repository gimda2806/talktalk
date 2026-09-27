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
        m = re.match(r"\|\s*(\d+)\s*\|\s*\[.*?\]\((.+?)\)\s*\|(.+?)\|(.+?)\|", line)
        if m:
            log[Path(m.group(2)).name] = (
                [k.strip() for k in m.group(3).split(",") if k.strip()],
                [c.strip() for c in m.group(4).split(",") if c.strip()],
            )
    return log


def load():
    log = read_log()
    chapters = []
    for f in sorted(CH_DIR.glob("*.md")):
        head, _, body = f.read_text(encoding="utf-8").partition("\n")
        title = re.sub(r"\s*\(.*\)\s*$", "", head.split("—")[-1]).strip()
        no, fmt, genre = f.stem.split("_")[:3]
        keywords, cast = log.get(f.name, ([], []))
        chapters.append(dict(no=no, file=f.name, format=fmt, genre=genre, title=title,
                             keywords=keywords, cast=cast, body=body.strip()))
    return chapters


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
