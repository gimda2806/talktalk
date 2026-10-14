"""zeta/zeta-production-status.md (제작 현황표)를 다시 만든다.

사용법 (저장소 루트에서):
  python3 zeta/tools/update_production_status.py

무엇을 세는가
- 플롯: zeta/zeta_NNN_이름.md
- 프로필 이미지: zeta/generated/manifest.json + 인물별 폴더(번호_이름/)의 실제 파일
- 3면도·사복 시트·닿기 직전 스틸 이미지·영상용 스틸컷 이미지: git에 올리지 않는 로컬 폴더
  (~/Documents/ChatGPT/이미지 프로필 제작/generated/번호_이름/)의 파일 이름
- 닿기 직전 스틸 프롬프트: 플롯 파일의 '### 닿기 직전' 절
- 영상용 스틸컷 프롬프트: zeta/stillcut/NNN_이름_스틸컷.md

상태가 바뀔 때(이미지 등록, 시트·스틸 생성, 새 플롯 추가)마다 이 스크립트를 돌려 문서를 고치고 같은 커밋으로 푸시한다.
"""
import collections
import datetime
import glob
import json
import os
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
LOCAL = Path.home() / "Documents/ChatGPT/이미지 프로필 제작/generated"
OUT = ROOT / "zeta/zeta-production-status.md"


def folder_files(num):
    files = set()
    for base in (LOCAL, ROOT / "zeta/generated", ROOT / "zeta/generated/닿기_직전_스틸"):
        for d in glob.glob(f"{base}/{num}_*"):
            if os.path.isdir(d):
                files |= {unicodedata.normalize("NFC", x) for x in os.listdir(d)}  # macOS 가 분해형(NFD) 이름으로 저장한 파일도 맞춘다
    for d in glob.glob(f"{LOCAL}/플롯용_프로필/{num}_*"):  # 정리 후 플롯용 프로필 3종
        if os.path.isdir(d):
            files |= {unicodedata.normalize("NFC", x) for x in os.listdir(d)}
    flat = LOCAL / "영상용"  # 플롯별 폴더 없이 한 폴더에 모은 영상용 파일 (번호는 파일 이름 앞 3자리)
    if flat.is_dir():
        files |= {n for n in (unicodedata.normalize("NFC", x) for x in os.listdir(flat)) if n.startswith(f"{num}_")}
    return files


def collect():
    plots = sorted(f for f in os.listdir(ROOT / "zeta") if re.match(r"zeta_\d{3}_.+\.md$", f))
    manifest = json.loads((ROOT / "zeta/generated/manifest.json").read_text(encoding="utf-8"))
    rows = []
    for p in plots:
        num, stem = p[5:8], p[:-3]
        files = folder_files(num)
        prof = set()
        for item in manifest.get(stem, []):
            f = item["file"]
            if f.endswith("-main.png"):
                prof.add("main")
            elif f.endswith("-user-m.png"):
                prof.add("m")
            elif f.endswith("-user-f.png"):
                prof.add("f")
        for f in files:
            if f.endswith("-main.png") and "casual" not in f:
                prof.add("main")
            elif f.endswith("-user-m.png"):
                prof.add("m")
            elif f.endswith("-user-f.png"):
                prof.add("f")
        sheets, casual = set(), set()
        for f in files:
            if "character-sheet" not in f or "reference-copy" in f:
                continue
            kind = "m" if "-user-m-" in f else "f" if "-user-f-" in f else "main"
            m = re.search(r"casual-(spring|summer|autumn|winter)", f)
            if m:
                casual.add((kind, m.group(1)))
            else:
                sheets.add(kind)
        text = (ROOT / "zeta" / p).read_text(encoding="utf-8")
        rows.append(dict(
            n=num, name=stem[9:], prof=prof, sheets=sheets, casual=casual,
            sp="### 닿기 직전" in text,
            stills=sorted(f for f in files if "닿기직전" in f),
            video=sorted(f for f in files if re.match(r"(\d{3}_)?C\d\d_", f)),
            vprompt=bool(glob.glob(str(ROOT / f"zeta/stillcut/{num}_*_스틸컷.md"))),
        ))
    return rows


def duplicate_pairs():
    dup = 0
    if LOCAL.is_dir():
        for d in LOCAL.iterdir():
            if d.is_dir():
                names = set(os.listdir(d))
                for f in names:
                    m = re.match(r"\d{3}_(.+-(main|user-m|user-f)\.png)$", f)
                    if m and m.group(1) in names:
                        dup += 1
    return dup


def render(rows):
    c = lambda f: sum(1 for r in rows if f(r))
    total = len(rows)
    sym = lambda have, keys: "".join("●" if k in have else "○" for k in keys)
    names = lambda f: ", ".join(f"{r['n']} {r['name']}" for r in rows if f(r)) or "없음"
    s = dict(
        prof3=c(lambda r: len(r["prof"]) == 3), prof0=c(lambda r: not r["prof"]),
        sheet3=c(lambda r: len(r["sheets"]) == 3), sheetpart=c(lambda r: 0 < len(r["sheets"]) < 3),
        sheet0=c(lambda r: not r["sheets"]), cas12=c(lambda r: len(r["casual"]) == 12),
        cas0=c(lambda r: not r["casual"]), sp=c(lambda r: r["sp"]), still=c(lambda r: r["stills"]),
        spnoimg=c(lambda r: r["sp"] and not r["stills"]), vprompt=c(lambda r: r["vprompt"]),
        video=c(lambda r: r["video"]))
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = []
    a = L.append
    a("# 제작 현황표 (플롯·프로필 이미지·3면도·닿기 직전 스틸)")
    a("")
    a("공유용 참고 문서입니다. 뷰어에는 표시하지 않습니다.")
    a("")
    a(f"- 기준 시각: {now} (KST) · 플롯 {total}편 (`zeta/zeta_NNN_이름.md`)")
    a("- 읽는 법: ● 있음 · ○ 없음. 프로필·3면도 칸의 세 글자는 순서대로 **주인공 · 유저 남성 · 유저 여성**.")
    a("- 근거: 프로필 이미지는 `zeta/generated/manifest.json`(등록분) + 인물별 폴더의 실제 파일. 3면도·사복 시트·스틸 이미지는 git에 올리지 않는 로컬 폴더 `이미지 프로필 제작/generated/번호_이름/`의 파일 이름으로 판정했습니다(구글 드라이브 업로드 여부는 반영하지 않음).")
    a("- 3면도: `…-character-sheet-2k-vN.png`(v2·variant 포함, `reference-copy` 제외)가 주인공·유저 남·유저 여 각각 있으면 ●. 사복 시트(`casual-봄·여름·가을·겨울`)는 3종×4계절=12장 중 몇 장이 있는지.")
    a("- 닿기 직전 스틸 프롬프트: 플롯 파일에 `### 닿기 직전` 절이 있으면 ●. 스틸 이미지는 `…_닿기직전_….png` 파일 수(다시 만든 v2도 각각 셈).")
    a("- 영상용 스틸컷: `zeta/stillcut/NNN_이름_스틸컷.md`(컷 프롬프트)와 `NNN_C01_….png`(컷 이미지).")
    a("")
    a("## 요약")
    a("")
    a("| 항목 | 개수 |")
    a("| --- | --- |")
    a(f"| 플롯 | **{total}편** |")
    a(f"| 프로필 이미지 3종 모두 있음 | {s['prof3']}편 |")
    a(f"| 프로필 이미지 없음 | {s['prof0']}편 |")
    a(f"| 3면도 3종 모두 있음 | {s['sheet3']}편 |")
    a(f"| 3면도 일부만 있음 | {s['sheetpart']}편 |")
    a(f"| 3면도 없음 | {s['sheet0']}편 |")
    a(f"| 사복 시트 12장 모두 있음 | {s['cas12']}편 |")
    a(f"| 사복 시트 없음 | {s['cas0']}편 |")
    a(f"| 닿기 직전 스틸 프롬프트 있음 | {s['sp']}편 (없음 {total - s['sp']}편) |")
    a(f"| 닿기 직전 스틸 이미지 있음 | {s['still']}편 (프롬프트는 있는데 이미지 없음 {s['spnoimg']}편) |")
    a(f"| 영상용 스틸컷 프롬프트 / 이미지 있음 | {s['vprompt']}편 / {s['video']}편 |")
    a("")
    a("## 작품별 현황")
    a("")
    a("| 번호 | 작품 | 프로필 | 3면도 | 사복 시트 | 직전 스틸 프롬프트 | 직전 스틸 이미지 | 영상용 스틸컷 |")
    a("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for r in rows:
        st = f"{len(r['stills'])}장" if r["stills"] else "○"
        vid = ("●" if r["vprompt"] else "○") + (f" · {len(r['video'])}컷" if r["video"] else "")
        cas = f"{len(r['casual'])}/12" if r["casual"] else "○"
        a(f"| {r['n']} | {r['name']} | {sym(r['prof'], ['main', 'm', 'f'])} | {sym(r['sheets'], ['main', 'm', 'f'])} | {cas} | {'●' if r['sp'] else '○'} | {st} | {vid} |")
    a("")
    a("## 비어 있는 것")
    a("")
    a(f"- **프로필 이미지 없음 ({s['prof0']}편):** {names(lambda r: not r['prof'])}")
    a(f"- **3면도 없음 ({s['sheet0']}편):** {names(lambda r: not r['sheets'])}")
    a(f"- **3면도 일부만 ({s['sheetpart']}편):** {names(lambda r: 0 < len(r['sheets']) < 3)}")
    a(f"- **닿기 직전 스틸 프롬프트는 있고 이미지가 없음 ({s['spnoimg']}편):** {names(lambda r: r['sp'] and not r['stills'])}")
    a(f"- **닿기 직전 스틸 이미지까지 있음 ({s['still']}편):** {names(lambda r: r['stills'])}")
    a("")
    a("## 참고")
    a("")
    a("- 로컬 폴더는 `generated/번호_이름/` 하나로 통일했고(드라이브와 같은 구조), 파일 이름 앞에 번호를 붙입니다(`001_baek-seoyul-main.png`). 저장소(`zeta/generated/번호_이름/`)에는 번호 없는 원래 이름(`baek-seoyul-main.png`)만 올라갑니다.")
    a("- 이 표는 파일 이름으로 만든 스냅샷입니다. 상태가 바뀌면 `python3 zeta/tools/update_production_status.py`로 다시 만들어 같은 커밋에 올립니다.")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    text = render(collect())
    OUT.write_text(text, encoding="utf-8")
    print(f"갱신: {OUT.relative_to(ROOT)}")
