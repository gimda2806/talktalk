"""zeta/zeta-local-status.md (로컬 기준 제작 현황표)를 다시 만든다.

사용법 (저장소 루트에서):
  python3 zeta/tools/update_local_status.py          # zeta/zeta-local-status.md  (로컬 작업 폴더 + 드라이브 데스크톱 폴더)
  python3 zeta/tools/update_local_status.py --drive  # zeta/zeta-drive-status.md  (드라이브 데스크톱 폴더만)
내용이 그대로면(기준 시각만 다르면) 파일을 다시 쓰지 않는다.

무엇을 세는가
- 로컬 폴더 ~/Documents/ChatGPT/이미지 프로필 제작/generated/번호_이름/ 와, 드라이브로 옮겨진 파일이 있는
  구글 드라이브 데스크톱 폴더(~/Library/CloudStorage/GoogleDrive-…/내 드라이브/이미지 프로필 제작/번호_이름/)
  안의 실제 파일 이름을 합쳐서 본다. 파일 이름 앞의 번호는 있어도 없어도 된다.
- 플롯 목록은 zeta/zeta_NNN_이름.md.
- 이미지 프로필(주인공·유저 남·유저 여), 3면도, 계절별 사복 3면도(12장), 입맞춤 직전 스틸(닿기 직전 포함),
  입맞춤 스틸, 콘티 스틸(콘티·숏드라마·영상용 컷).
같은 항목의 구글 드라이브 기준 표는 zeta/zeta-drive-status.md.
"""
import datetime
import glob
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
# 로컬 작업 폴더와 구글 드라이브 데스크톱 폴더(드라이브로 옮겨진 파일이 여기 있다)를 함께 본다.
LOCAL = Path.home() / "Documents/ChatGPT/이미지 프로필 제작/generated"
DRIVE_DESKTOP = Path.home() / "Library/CloudStorage/GoogleDrive-hyukgu86@gmail.com/내 드라이브/이미지 프로필 제작"
SOURCES = [LOCAL, DRIVE_DESKTOP]
DRIVE_MODE = "--drive" in sys.argv
if DRIVE_MODE:
    SOURCES = [DRIVE_DESKTOP]
OUT = ROOT / ("zeta/zeta-drive-status.md" if DRIVE_MODE else "zeta/zeta-local-status.md")


def kind(name):
    return "m" if "-user-m" in name else "f" if "-user-f" in name else "main"


def local_files():
    """번호 → 파일 이름 집합 (macOS 분해형 이름도 NFC 로 맞춘다).

    각 폴더(로컬 generated, 드라이브 데스크톱 폴더)에서 세 곳을 함께 본다:
    번호_이름/ (그 작품의 파일), 영상용/ (플롯별 폴더 없이 한 폴더에 모은 메인·남 프로필과 3면도, 번호는 파일 이름 앞 3자리),
    플롯용_프로필/번호_이름/ (프로필 3종)."""
    by = {}
    add = lambda num, names: by.setdefault(num, set()).update(n for n in names if "-확인필요" not in n)  # 드라이브 중복본(-확인필요)은 세지 않는다
    nfc = lambda names: (unicodedata.normalize("NFC", f) for f in names if not f.startswith("."))
    for src in SOURCES:
        if not src.is_dir():
            continue
        dirs = glob.glob(str(src / "[0-9][0-9][0-9]_*")) + glob.glob(str(src / "플롯용_프로필" / "[0-9][0-9][0-9]_*"))
        for d in dirs:
            if os.path.isdir(d):
                add(os.path.basename(d)[:3], nfc(os.listdir(d)))
        flat = src / "영상용"
        if flat.is_dir():
            for n in nfc(os.listdir(flat)):
                if re.match(r"\d{3}_", n):
                    add(n[:3], [n])
    return by


def repo_profiles(num):
    """저장소 zeta/generated/번호_이름/ 에 등록된 프로필 종류 (주인공·유저 남·유저 여)"""
    have = set()
    for d in glob.glob(str(ROOT / f"zeta/generated/{num}_*")):
        for f in os.listdir(d):
            m = re.search(r"-(main|user-m|user-f)\.png$", f)
            if m:
                have.add(kind(f))
    return have


def collect():
    works = {}
    for p in glob.glob(str(ROOT / "zeta/zeta_[0-9][0-9][0-9]_*.md")):
        b = os.path.basename(p)
        works[b[5:8]] = b[9:-3]
    by = local_files()
    rows = []
    for no in sorted(works):
        pr, sh, cas, prv = set(), set(), set(), set()
        sb = kd = ct = 0
        for t in by.get(no, ()):
            tl = t.lower()
            if not tl.endswith(".png"):
                continue
            base = re.sub(r"^\d{3}_", "", t)
            if "character-sheet" in tl:
                c = re.search(r"casual-(spring|summer|autumn|winter)", tl)
                if c:
                    cas.add((kind(tl), c.group(1)))
                elif "reference-copy" not in tl:
                    sh.add(kind(tl))
            elif "닿기직전" in t or "입맞춤직전" in t:
                sb += 1
            elif "kiss" in tl or "입맞춤" in t:
                kd += 1
            elif "콘티" in t or "shortdrama" in tl or re.match(r"C\d\d_", base):
                ct += 1
            elif re.search(r"-(main|user-m|user-f)\.png$", tl):
                pr.add(kind(tl))
            elif re.search(r"-(main|user-m|user-f)(-[a-z]+)?-v\d+\.png$", tl):
                prv.add(kind(tl))  # 기본 이름 없이 -v2 만 있는 경우
        pr |= prv  # -v2 만 남은 종류도 있는 것으로 센다 (-prev 이전본은 세지 않는다)
        rows.append(dict(no=no, name=works[no], pr=pr, sh=sh, cas=len(cas), sb=sb, kd=kd, ct=ct, files=len(by.get(no, ())), repo=repo_profiles(no)))
    return rows


def render(rows):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    sym = lambda have, keys: "".join("●" if k in have else "○" for k in keys)
    tot = len(rows)
    c = lambda f: sum(1 for r in rows if f(r))
    names = lambda f: ", ".join(f"{r['no']} {r['name']}" for r in rows if f(r)) or "없음"
    L = []
    a = L.append
    a("# 구글 드라이브 기준 제작 현황 (프로필·3면도·사복 3면도·스틸·콘티)" if DRIVE_MODE else "# 로컬 기준 제작 현황 (프로필·3면도·사복 3면도·스틸·콘티)")
    a("")
    if DRIVE_MODE:
        a("공유용 참고 문서입니다. 뷰어에는 표시하지 않습니다. 저장소·로컬이 아니라 **구글 드라이브 \"이미지 프로필 제작\" 폴더(이 컴퓨터의 드라이브 데스크톱 폴더 `내 드라이브/이미지 프로필 제작/번호_이름/`)에 실제로 올라가 있는 파일**을 기준으로 정리했습니다.")
    else:
        a("공유용 참고 문서입니다. 뷰어에는 표시하지 않습니다. 저장소·구글 드라이브 웹이 아니라 **이 컴퓨터에 실제로 있는 파일**을 기준으로 정리했습니다: 로컬 작업 폴더(`이미지 프로필 제작/generated/번호_이름/`)와 구글 드라이브 데스크톱 폴더(`내 드라이브/이미지 프로필 제작/번호_이름/`)를 합쳐서 봅니다.")
    a("")
    a(f"- 기준 시각: {now} (KST) · 플롯 {tot}편 (`zeta/zeta_NNN_이름.md`)")
    a("- 읽는 법: ● 있음 · ○ 없음. 프로필·3면도 칸의 세 글자는 순서대로 **주인공 · 유저 남성 · 유저 여성**.")
    a("- 이미지 프로필: `…-main.png` · `…-user-m.png` · `…-user-f.png` (기본 이름이 없고 `-v2`·`-idol-v2`·`-long-v4`처럼 재생성본만 남은 종류는 그 파일로 인정, `-prev` 이전본은 제외).")
    a("- 3면도: `…character-sheet…png` 중 `casual`이 없는 것(`reference-copy` 제외). 계절별 사복 3면도: `casual-봄·여름·가을·겨울` 시트가 3종×4계절=12장 중 몇 장인지.")
    a("- 입맞춤 직전 스틸: `…_닿기직전_….png`(닿기 직전 스틸)와 `kiss-still-…입맞춤직전….png`의 파일 수(다시 만든 v2도 각각 셈). 입맞춤 스틸: 이름에 `kiss`·`입맞춤`이 있고 `직전`이 아닌 것.")
    a("- 콘티 스틸: `…콘티_….png`(콘티 컷), `…shortdrama….png`(숏드라마 컷), `C01_….png`(영상용 컷)의 파일 수.")
    if DRIVE_MODE:
        a("- 같은 항목의 로컬 기준 표: `zeta/zeta-local-status.md`. 저장소·로컬 섞은 표: `zeta/zeta-production-status.md`.")
    else:
        a("- 같은 항목의 구글 드라이브 기준 표: `zeta/zeta-drive-status.md`. 저장소·로컬 섞은 표: `zeta/zeta-production-status.md`.")
    a("")
    a("## 요약")
    a("")
    a("| 항목 | 개수 |")
    a("| --- | --- |")
    a(f"| 플롯 | **{tot}편** |")
    a(f"| 이미지 프로필 3종 모두 있음 | {c(lambda r: len(r['pr']) == 3)}편 |")
    a(f"| 이미지 프로필 없음 | {c(lambda r: not r['pr'])}편 |")
    if not DRIVE_MODE:
        a(f"| 이미지 프로필이 로컬에는 일부만 있고 저장소에는 3종 모두 있음 | {c(lambda r: 0 < len(r['pr']) < 3 and len(r['repo']) == 3)}편 |")
    a(f"| 3면도 3종 모두 있음 | {c(lambda r: len(r['sh']) == 3)}편 |")
    a(f"| 3면도 일부만 있음 | {c(lambda r: 0 < len(r['sh']) < 3)}편 |")
    a(f"| 3면도 없음 | {c(lambda r: not r['sh'])}편 |")
    a(f"| 계절별 사복 3면도 12장 모두 있음 | {c(lambda r: r['cas'] == 12)}편 |")
    a(f"| 계절별 사복 3면도 일부만 있음 | {c(lambda r: 0 < r['cas'] < 12)}편 |")
    a(f"| 계절별 사복 3면도 없음 | {c(lambda r: r['cas'] == 0)}편 |")
    a(f"| 입맞춤 직전 스틸 있음 | {c(lambda r: r['sb'])}편 ({sum(r['sb'] for r in rows)}장) |")
    a(f"| 입맞춤 스틸 있음 | {c(lambda r: r['kd'])}편 ({sum(r['kd'] for r in rows)}장) |")
    a(f"| 콘티 스틸 있음 | {c(lambda r: r['ct'])}편 ({sum(r['ct'] for r in rows)}장) |")
    a("")
    a("## 작품별 현황")
    a("")
    a("| 번호 | 작품 | 이미지 프로필 | 3면도 | 계절별 사복 3면도 | 입맞춤 직전 스틸 | 입맞춤 스틸 | 콘티 스틸 |")
    a("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for r in rows:
        cas = f"{r['cas']}/12" if r["cas"] else "○"
        n = lambda k: (f"{r[k]}장" if r[k] else "○")
        prc = sym(r["pr"], ["main", "m", "f"])
        if not DRIVE_MODE and 0 < len(r["pr"]) < 3 and len(r["repo"]) == 3:
            prc += " (저장소 ●●●)"
        a(f"| {r['no']} | {r['name']} | {prc} | {sym(r['sh'], ['main', 'm', 'f'])} | {cas} | {n('sb')} | {n('kd')} | {n('ct')} |")
    a("")
    a("## 비어 있는 것")
    a("")
    a(f"- **이미지 프로필 없음 ({c(lambda r: not r['pr'])}편):** {names(lambda r: not r['pr'])}")
    only = [] if DRIVE_MODE else [r for r in rows if 0 < len(r["pr"]) < 3]
    if only:
        a("- **이미지 프로필이 로컬에는 일부만 있는 작품:** " + ", ".join(
            f"{r['no']} {r['name']}(로컬 {sym(r['pr'], ['main', 'm', 'f'])}, 저장소 {sym(r['repo'], ['main', 'm', 'f'])})" for r in only)
            + " — 로컬에서 직접 정리한 것은 의도한 상태이고, 저장소 쪽이 기준이다.")
    a(f"- **3면도 없음 ({c(lambda r: not r['sh'])}편):** {names(lambda r: not r['sh'])}")
    a(f"- **3면도 일부만 ({c(lambda r: 0 < len(r['sh']) < 3)}편):** {names(lambda r: 0 < len(r['sh']) < 3)}")
    part = ", ".join(f"{r['no']} {r['name']}({r['cas']}/12)" for r in rows if 0 < r["cas"] < 12) or "없음"
    a(f"- **계절별 사복 3면도 일부만 ({c(lambda r: 0 < r['cas'] < 12)}편):** {part}")
    a(f"- **입맞춤 직전 스틸 있음 ({c(lambda r: r['sb'])}편):** {names(lambda r: r['sb'])}")
    a(f"- **입맞춤 스틸 있음 ({c(lambda r: r['kd'])}편):** {names(lambda r: r['kd'])}")
    a(f"- **콘티 스틸 있음 ({c(lambda r: r['ct'])}편):** {names(lambda r: r['ct'])}")
    a("")
    a("## 참고")
    a("")
    if DRIVE_MODE:
        a("- 이 표는 드라이브 데스크톱 폴더의 파일 이름으로 만든 스냅샷입니다. `python3 zeta/tools/update_local_status.py --drive`로 다시 만듭니다. 로컬 기준 표는 `zeta/zeta-local-status.md`.")
    else:
        a("- 이 표는 로컬 파일 이름으로 만든 스냅샷입니다. 상태가 바뀌면 `python3 zeta/tools/update_local_status.py`로 다시 만들어 같은 커밋에 올립니다.")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    text = render(collect())
    stamp = re.compile(r"^- 기준 시각: .*$", re.M)
    if OUT.exists() and stamp.sub("", OUT.read_text(encoding="utf-8")) == stamp.sub("", text):
        print(f"변경 없음: {OUT.relative_to(ROOT)}")
    else:
        OUT.write_text(text, encoding="utf-8")
        print(f"갱신: {OUT.relative_to(ROOT)}")
