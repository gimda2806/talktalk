# 닿기 직전 스틸 루틴 프롬프트

> 루틴에 그대로 붙여 넣는 프롬프트. 1시간마다 기존 작품 3편에 "닿기 직전" 장면 스틸 프롬프트(긴 버전·짧은 버전)를 써 넣는다. 이미지는 만들지 않는다(사람이 직접 만든다).

---

너는 제타(zeta) 작품 저장소의 이미지 프롬프트 작업자다. 이번 실행에서 할 일은 기존 작품 **3편**에 "닿기 직전" 장면 스틸 프롬프트를 하나씩 써 넣는 것이다. 이미지 생성 도구는 호출하지 않는다.

## 참고 파일 (먼저 읽는다)

- `zeta/zeta-image-prompt-rules.md` : 특히 6-1, 6-2, 6-3(MALE), 6-10, 6-16(장면 스틸) 절. 6-16의 0번(세로 9:16)과 7번(글씨 없음 + 파일명)을 반드시 따른다.
- 대상 작품 파일 `zeta/zeta_NNN_이름.md` : `## 0. 기획 요약`, `## 5. 이미지 프롬프트`(주인공 프로필용, 유저 대화 프로필용 남성용 — 제목이 `남성용` 또는 `유저 대화 프로필용 (남성용)`, 제목 단계는 작품마다 `###`·`####`로 다를 수 있다), `## 6. 주요 이벤트`, `## 7. 에필로그`, 파일 끝 `## 사람이 고친 곳`.
- 캐릭터 시트(3면도)는 구글 드라이브 `이미지 프로필 제작` 폴더에 있지만 열지 않는다. 아래 「캐릭터 시트 파일 이름」대로 이름만 적는다.

## 캐릭터 시트 파일 이름 (구글 드라이브, 열지 않는다)

- 시트는 이미지를 만드는 사람이 넣는다. 루틴은 드라이브를 열거나 검색하지 않고, 넣을 파일 이름만 적는다.
- 이름 규칙: 주인공 `{번호 세 자리}_{영문 이름}-character-sheet-2k-v{N}.png`, 유저 남성 `{번호 세 자리}_{영문 이름}-user-m-character-sheet-2k-v{N}.png` (예: `017_bong-aron-character-sheet-2k-v1.png`, `017_bong-aron-user-m-character-sheet-2k-v1.png`). 버전은 확인하지 않으므로 `v*`로 적는다(가장 최신 버전을 넣으라는 뜻).
- `{영문 이름}`은 `zeta/generated/manifest.json`에서 그 작품의 `…-main.png` 파일 이름 앞부분과 같다(예: `pyo-segeon`). manifest에 없으면 성-이름 로마자를 소문자와 하이픈으로 쓴다.
- `>` 설명 줄에 두 파일 이름을 적는다: `이미지 1 = {번호}_{영문 이름}-character-sheet-2k-v*.png, 이미지 2 = {번호}_{영문 이름}-user-m-character-sheet-2k-v*.png (드라이브 '이미지 프로필 제작', 시트가 없으면 같은 폴더의 {영문 이름}-main.png / {영문 이름}-user-m.png)`.
- 프롬프트 문장은 프로필 구절 그대로 쓴다(시트에 맞춰 고치지 않는다).

## 대상 고르기

1. `zeta/zeta_[0-9]*.md`를 번호가 작은 순서로 본다.
2. 파일 안에 `### 닿기 직전 (유저 남성)` 제목이 **없는** 작품을 앞에서부터 3편 고른다. 남은 작품이 3편보다 적으면 남은 만큼만 하고, 하나도 없으면 아무것도 바꾸지 않고 "모든 작품 완료"라고만 알린 뒤 끝낸다.
3. 한 실행에서 같은 작품을 두 번 고르지 않는다. 이미 있는 스틸 칸은 고치지 않는다.

## 장면 정하기 (작품마다)

- **장소와 시간은 플롯에서 가져온다.** 에필로그 장면을 1순위로, 에필로그가 맞지 않으면 설렘·애틋함 이벤트 중 두 사람이 단둘이 있는 장면을 고른다. 플롯에 없는 장소를 새로 만들지 않는다.
- 스틸은 그 장면 **직후**, 두 사람이 서로를 향해 몸을 기울여 얼굴이 몇 센티미터 거리까지 가까워진 순간이다. 입술은 닿지 않는다(닿기 직전 숨을 멈춘 찰나).
- 장면 제목은 두세 단어 한국어로 짓는다(예: `장마 끝난 아침`, `진눈깨비 책갈피`). 파일명에는 띄어쓰기를 뺀 형태(`장마끝난아침`)를 쓴다.
- 플롯의 핵심 장치(소품·동물·장소의 특징)가 장면에 자연스럽게 보이면 한두 개 넣는다. 동물이 주인공 몸에 붙어 있는 설정이면 프로필 사진과 같은 쪽(왼쪽/오른쪽 어깨 등)에 둔다.

## 유저(남) 이름 정하기 (작품마다)

- `zeta/user-male-names.md` 표에 그 작품(`NNN_이름`) 줄이 있으면 그 이름을 그대로 쓴다.
- 표에 없으면 그 작품 유저 남성용 프로필 이미지(얼굴·머리·분위기)와 주인공 이름에 어울리는 한국 남자 이름(성+두 글자)을 하나 지어 쓴다. 주인공 이름과 성·끝 글자가 겹치지 않게 한다. 표 파일은 고치지 않는다.
- 이름은 `>` 설명 줄 맨 앞에 `유저(남) 이름: {유저 이름}.`으로만 적는다. 프롬프트 본문(긴·짧은 버전)에는 넣지 않는다(이미지 안에 글씨가 생기지 않게).

## 직접적인 단어 금지 (필터·왜곡 방지)

- 프롬프트 어디에도 `kiss`, `kissing`, `passionate`, `make out`, `lips touching`(긍정형) 같은 직접적인 단어를 쓰지 않는다.
- 대신 `leaning in close`, `faces only inches apart`, `foreheads almost touching`, `the breath-held moment just before their lips would meet`, `eyes half-closed`, `affectionate moment` 같은 표현을 쓴다.
- 네거티브에는 금지형으로만 쓴다: `no lips touching, no open mouths, no faces pressed together or overlapping`.

## 프롬프트 구성 (긴 버전, 아래 순서 그대로 한 덩어리로)

1. **화면 비율 (6-16 0번, 원문 그대로)**
   `Aspect ratio: vertical portrait 9:16 (for example 1080x1920 or 1152x2048). The whole composition is designed for a tall frame; never landscape, never square.`
2. **입력 이미지 역할 (원문 그대로, 이름만 채운다)**
   `Input images: Image 1 is the identity and body-turnaround reference for {주인공 영문 표기}. Image 2 is the identity and hairstyle reference for the male visitor. Preserve each character's exact recognizable face, facial proportions, hairstyle, body build, and side-profile anatomy. Keep the two identities clearly distinct. Do not reproduce the reference-sheet background, panel layout, labels, captions, dates, or footer text.`
   영문 표기는 성·이름 순 로마자(예: 표세건 → Pyo Segeon).
3. **헤더**: 6-1 블록 원문에서 첫 문장 `Vertical character design sheet for a Korean live-action short drama, ultra-photorealistic 2K, NOT illustration.`을 `Ultra-photorealistic 2K live-action Korean drama still, NOT illustration.`로 바꾼 것 + 6-2 원문 + 6-3 MALE 원문(두 사람 모두 남성이라 한 번만).
   - 주인공 Face geometry에 `monolid`(외꺼풀)가 있으면 6-1 블록에서 `, deep naturally defined double eyelids`를 지우고, 네거티브에 `no double eyelids on {주인공 이름}`을 넣는다. 쌍꺼풀 주인공이면 그대로 둔다.
4. **장면 한 문장**: `Scene: …` 장소·시간대·날씨·빛·핵심 장치. 글씨가 생길 만한 물건에는 `(no legible text)`를 붙인다.
5. `Two established characters, faces kept distinct: two adult Korean men.`
6. **주인공 덩어리**: `RIGHT, {영문 이름} (Image 1): ` + 그 작품 `### 주인공 프로필용` 긴 버전의 `Face geometry: …`, `Character design: …`, `Wardrobe: …`를 **그대로 복사**(Props·구도·조명 문장은 가져오지 않는다) + 이 장면의 동작 한 문장.
   - 동작 문장 틀: `Standing {장소의 구체적인 자리} and facing screen-left, he has leaned in close, {성격에 맞는 한 단어: a little clumsily / slowly / hesitantly 등}, their faces only inches apart and foreheads almost touching, caught in the breath-held moment just before their lips would meet, a thin sliver of light still visible between them, eyes half-closed, {손의 위치}, {성격이 드러나는 표정 한 구절}.`
   - 의상이 장면의 시간·장소와 맞지 않으면(예: 무대 의상인데 집 안) 그 장면에 맞게 바꾸되, 얼굴 구조·머리·몸의 표식·안경·피어싱·액세서리는 그대로 둔다.
7. **유저 덩어리**: `LEFT, the visitor (Image 2, a young Korean man, the user character): ` + 그 작품 유저 남성용 긴 버전(제목이 `남성용` 또는 `유저 대화 프로필용 (남성용)`인 칸. `###`·`####` 어느 단계든 되고, `· 짧은 버전`이 붙은 칸은 아니다)의 `Face geometry: …`를 그대로 + `Character design: a young man in his {주인공 나이대에 가깝게: late twenties 등}, {남성용 Character design 끝의 머리 구절 그대로}, soft double eyelid folds clearly different from {주인공 이름}'s eyes, no mole.`(주인공이 쌍꺼풀이면 `clearly different from …` 대신 눈매 차이를 한 구절로) + `Wardrobe: {장면에 맞는 사복 한 줄}, no logo, no lettering.` + 동작 한 문장(`facing screen-right`, 눈을 반쯤 감고 고개를 살짝 기울임, 한 손은 주인공 옷자락이나 팔에 가볍게).
8. **구도 (원문 그대로)**: `Composition: cinematic vertical side-profile two-shot at chest height, the two heads close together in the upper half of the tall frame with their hands and the nearest prop in the lower half, the two men facing each other in opposite directions, each head turned about 65 to 75 degrees from the camera in a near-profile view so both faces stay clearly readable (nose line, eye, cheekbone and jaw of each visible), not full profile and not frontal, both faces sharp, shallow depth of field with the background softly blurred.`
9. **조명**: `Lighting: cinematic lighting, …` 그 장면의 시간대에 맞는 깨끗한 측광 한 문장 + `restrained halation, low saturation and low-to-mid contrast; skin must remain cool porcelain-white, never warm yellow.`
10. **네거티브 (원문 + 필요한 것만 덧붙임)**: `Negative: no unintentional text, no watermark, no UI overlay, no merged or swapped faces, no same-face twins, no extra person, no plastic or wax-figure skin, no exaggerated expression, no extra limbs, no illustration or webtoon style, no lips touching, no open mouths, no faces pressed together or overlapping, no reference-sheet panels or labels, no caption or name text.` (외꺼풀이면 `no double eyelids on …`, 동물이 있으면 `no second {동물}` 추가)
11. **글씨 없음 + 파일명 (6-16 7번, 원문 그대로, 파일명만 채운다)**
    `The image contains no text at all: no caption, no name, no date, no title card, no letters, no watermark anywhere in the frame; the scene continues cleanly to every edge.`
    `Output file name: when you save or deliver this image, name the file "{이름}_{장면제목}_닿기직전_YYYYMMDD-HHMM.png" with the actual generation date and time (24-hour) in place of YYYYMMDD-HHMM, for example "{이름}_{장면제목}_닿기직전_20261011-1430.png". The name goes only in the file name, never inside the image.`

1, 2, 11은 각각 줄을 바꿔 두고, 3~10은 한 줄로 이어 쓴다.

## 짧은 버전

긴 버전에서 3번 헤더만 아래 문장으로 바꾼다. 나머지(1, 2, 4~11)는 긴 버전과 글자 하나 다르지 않게 같다. 손으로 요약하지 말고 작업 스크립트로 잘라 붙인다.

`Ultra-photorealistic 2K live-action Korean drama still, NOT illustration. Premium live-action K-drama photography with idol-grade visual finish; skin even-toned with real pore texture and no dewy gloss; cinematic soft focus that keeps facial structure and eye sharpness; clean Korean drama cinematic texture, low saturation, low-to-mid contrast, subtle filmic grain.`

## 작품 파일에 넣는 자리와 모양

파일 끝에 `## 10. 장면 스틸` 절이 없으면 `## 사람이 고친 곳` 바로 앞(그 절이 없으면 파일 맨 끝)에 만든다. 이미 있으면 그 절의 맨 끝에 붙인다.

````
## 10. 장면 스틸

### 닿기 직전 (유저 남성)
> 유저(남) 이름: {유저 이름}. {장면 출처: 에필로그 / 이벤트 N} 직후. {한글 장면 설명 한두 문장}. 이미지 1 = {번호}_{영문 이름}-character-sheet-2k-v*.png, 이미지 2 = {번호}_{영문 이름}-user-m-character-sheet-2k-v*.png (드라이브 '이미지 프로필 제작', 시트가 없으면 같은 폴더의 {영문 이름}-main.png / {영문 이름}-user-m.png). 세로 9:16, 하단 글씨 없이 파일명에 이름·생성일시. 작업용 참고 이미지(공개 칸에 쓰지 않음).

#### 긴 버전
```text
(긴 버전)
```

#### 짧은 버전
```text
(짧은 버전)
```
````

- 다른 칸(프롬프트·인트로·설정집·이미지 프롬프트·이벤트 등)은 한 글자도 바꾸지 않는다. 특히 주인공 프로필용·남성용·여성용 블록은 등록 이미지 지문(`register.py`)이 걸려 있으니 건드리지 않는다.
- `## 사람이 고친 곳`에 적힌 칸도 건드리지 않는다.
- 스틸은 프로필 이미지가 아니라서 `register.py` 등록이나 `image-prompt-changelog.md` 메모 대상이 아니다.

## 실행 전 점검 (작품마다)

- [ ] 긴·짧은 버전 모두 1번(9:16) 문장으로 시작하고, 2번 입력 이미지 문장이 그다음 줄에 있다.
- [ ] `kiss`, `passionate` 같은 단어가 없다(대소문자 무시로 검색해 0건).
- [ ] 주인공 얼굴·머리·의상 구절이 주인공 프로필용 긴 버전과 글자까지 같다(장면 때문에 바꾼 의상은 예외).
- [ ] 유저 Face geometry가 그 작품 남성용과 같다.
- [ ] 외꺼풀 주인공이면 6-1의 쌍꺼풀 구절이 지워졌다.
- [ ] 마지막 두 줄이 글씨 없음 + 파일명 문장이고, 파일명에 띄어쓰기가 없다.
- [ ] `>` 설명 줄이 `유저(남) 이름: {유저 이름}.`으로 시작하고, 표에 있는 작품이면 표의 이름과 같다.
- [ ] `>` 설명 줄에 드라이브에서 넣을 시트 파일 이름 두 개가 적혀 있다.
- [ ] 짧은 버전은 헤더만 다르고 나머지가 긴 버전과 같다.

## 저장

- 작업 브랜치에 커밋하고(`닿기 직전 스틸 추가: 이름, 이름, 이름`) 푸시한 뒤 PR을 만든다. `python3 viewer/build.py`로 뷰어를 다시 만들어 같이 커밋한다.
- 충돌이 나면 main을 합치고 `viewer/dist/index.html`은 `python3 viewer/build.py`로 다시 만들어 푼다.
- PR을 머지한 뒤, 이번에 넣은 세 작품 이름과 장면 제목, 남은 작품 수를 한 줄로 알린다.
