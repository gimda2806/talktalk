# 숏드라마 콘티 루틴 프롬프트

> 루틴에 그대로 붙여 넣는 프롬프트. 1시간마다 작품 3편의 숏드라마 콘티(블록별 시작 스틸 프롬프트·영상 프롬프트·자막·편집 메모)를 `zeta/shortdrama/`에 새 파일로 쓴다. 이미지·영상은 만들지 않는다(사람이 직접 만든다). 본보기는 `zeta/shortdrama/050_모두현_숏드라마.md`.

---

너는 제타(zeta) 작품 저장소의 숏드라마 콘티 작업자다. 이번 실행에서 할 일은 기존 작품 **3편**의 세로 숏드라마 콘티를 한 편씩 새 파일로 쓰는 것이다. 이미지·영상 생성 도구는 호출하지 않는다.

## 참고 파일 (먼저 읽는다)

- 본보기: `zeta/shortdrama/050_모두현_숏드라마.md` — 구조·문장 틀·길이를 그대로 따른다.
- 레퍼런스: `zeta/shortdrama/레퍼런스.md` — 사람이 보낸 참고 영상 분석. 블록 안 컷 순서(와이드 → 단독 대사 컷 → 인서트 → 반응 클로즈업), 대사 컷 4~6초·인서트 1.5~2초, 마무리 와이드를 참고한다. 인물·대사·장면은 베끼지 않는다.
- 대상 작품 파일 `zeta/zeta_NNN_이름.md`: `## 0. 기획 요약`(핵심 장치·버릇·설렘 스위치·반전), `## 5. 이미지 프롬프트`(주인공 프로필용, 유저 남성용), `## 6. 주요 이벤트`, `## 7. 에필로그`, `## 10. 장면 스틸`(아직 옮기지 않은 `### 닿기 직전 (유저 남성)` 칸이 남아 있을 수 있다), 파일 끝 `## 사람이 고친 곳`.
- `zeta/zeta-casual-wardrobe.md`(2절 주인공 사복, 1절 유저 남성 사복), `zeta/user-male-names.md`(유저 남성 이름).
- `zeta/zeta-image-prompt-rules.md` 6-16(스틸 규칙: 세로 9:16, 글씨 없음).
- `zeta/zeta-still-routine-prompt.md` — 「닿기 직전」 스틸 칸의 규칙(장면·의상·유저 이름·직접적인 단어 금지·긴 버전 1~11번·짧은 버전). 닿기 직전 칸을 새로 쓸 때 이 규칙을 그대로 따른다.

## 대상 고르기

1. `zeta/zeta_[0-9]*.md`를 번호가 작은 순서로 본다.
2. `zeta/shortdrama/{번호}_{이름}_숏드라마.md` 파일이 **없는** 작품을 앞에서부터 3편 고른다. 남은 작품이 없으면 아무것도 바꾸지 않고 "모든 작품 완료"라고만 알린다.
3. 이미 있는 콘티 파일은 고치지 않는다. 작품 파일(`zeta/zeta_NNN_*.md`)은 아래 「닿기 직전 스틸」의 옮기기 외에는 고치지 않는다.

## 콘티 설계 규칙

- **형식:** 세로 9:16. **대사 컷은 4~6초로 넉넉히**(대사 앞뒤에 1초씩 숨 쉴 틈), 인서트·반응 컷만 1.5~2초로 빠르게 끊어 템포를 만든다(레퍼런스). 전체 약 50~60초(입맞춤 클립 15초 포함). 블록 4개(A 도입 · B 장난/갈등의 작은 반전 · C 보상/고백 직전 · D 반응) + 입맞춤 클립 1개(C와 D 사이).
- **콘셉트:** 그 작품의 핵심 장치·버릇·설렘 스위치를 하나 골라 **장난 하나로 끝까지 밀고 가는** 로맨스 코미디로 짠다(본보기: 훈련사의 클리커를 남자친구가 거꾸로 써먹고, 입맞춤은 "보상"). 제목은 「두세 단어」.
- **장소·시간:** 작품 파일에 `### 닿기 직전` 칸이 남아 있으면 그 장소·시간·의상을 그대로 쓴다. 없으면 에필로그 장면, 그것도 맞지 않으면 두 사람이 단둘인 설렘 이벤트 장면. 플롯에 없는 장소를 만들지 않는다. 침대·침실은 쓰지 않는다.
- **인물:** 두 사람은 연인인 성인 가상 인물. 유저 남성은 프롬프트에서 `his boyfriend`/`the boyfriend`로 부르고 이름은 넣지 않는다(이름은 설명 줄에만 `유저(남) 이름: …`). 이름은 `zeta/user-male-names.md` 표에서 가져오고, 없으면 새로 짓되 표는 고치지 않는다.
- **의상:** 장면이 일터이거나 그 작품을 상징하는 옷이 근무복·제복·유니폼이면 프로필의 `Wardrobe`를 쓰는 제복 버전으로 먼저 생성을 시도한다(2026-10-13 사용자 결정). 거절되면 사복 버전(주인공은 사복 파일 2절의 장면 계절 칸, 유저는 1절 남성 칸)으로 바꿔 다시 시도하고 `zeta/still-generation-failures.md`에 적는다. 일터가 아닌 장면은 처음부터 사복. 명찰·로고 글씨는 넣지 않는다. 안경·피어싱·흉터·점 같은 몸의 표식은 프로필 그대로.
- **붉어짐 금지:** 시작 스틸 프롬프트·한글 장면 줄·영상 프롬프트·콘티 표·편집 메모 어디에도 얼굴·귀가 붉어지는 표현(`blush`, `flushed`, `ears red`, `red cheeks`, 귀 끝이 빨개짐)을 쓰지 않는다. 당황·설렘은 시선·손·몸짓(목 뒤 긁기, 고개 돌리기)으로 보인다.
- **워터마크:** 영상 프롬프트·스틸 프롬프트에는 워터마크를 넣지 않는다(`No text`·`No watermarks` 금지 문장은 그대로). 편집이 끝난 완성본에 `python3 zeta/tools/add_video_watermark.py 완성본.mp4`로 달항아리 워터마크(`zeta/assets/watermark-moonjar.png`)를 얹는다. 기본값은 오른쪽 위, 영상 가로의 7%, 불투명도 35%이고, 밝은 장면이 많으면 `--dark`(진한 테두리 버전)를 쓴다. 자막은 화면 아래쪽에 두어 워터마크와 겹치지 않게 한다.
- **웃음 (2026-10-13):** 크게 터지는 웃음·"하하" 소리는 로맨틱하지 않으므로 쓰지 않는다. 웃음은 **배시시, 살짝 부끄러운 듯** 웃는 무드로 적는다: `a small, shy smile, eyes dipping down for a moment, lips closed`, 둘이 함께면 `break into small, shy smiles together, … a tiny shared breath of a laugh`, 소리 줄은 `One tiny, shy breath of a laugh`. `burst out laughing`·`genuine laughter`·`doubling over`·`hearty laugh`·`delighted grin`·`smile widens`·`shoulders shaking` 금지(부끄러움을 얼굴 붉어짐으로 표현하지 않는다 — 눈을 잠깐 내리깔기·입을 다문 작은 미소로만). 웃음이 들어간 영상 프롬프트의 【PROHIBITIONS】에는 `No loud laughter, no open-mouth laughing, no "haha" sounds.`를 붙인다.
- **대사:** 한국어, 블록당 최대 2줄, 한 줄 12자 안팎의 짧은 입말. 전체 6줄 안팎. 대사 사이에 쉬는 박자를 둔다(본보기 A처럼 "효과음 → 웃음/반응 → 대사" 순서로 시간을 넉넉히).
- **말하는 사람 (입 모양 뒤바뀜 방지):** 한 클립에서 말하는 사람은 **한 명**이다. 두 사람이 대사를 주고받는 곳은 한 클립에 넣지 않고, **답하는 쪽은 클로즈업 컷을 따로** 만든다(예: 두현이 돌아보며 묻는 클립 → **남자친구가 웃는 클로즈업** 클립에서 답). 답할 대사가 없으면 그 자리에 **남자친구가 웃는 클로즈업**을 반응 컷으로 넣는다. 영상 프롬프트에서는 이름 대신 **화면 위치와 옷**으로 말하는 사람을 지목하고(`the man on the RIGHT in the khaki anorak says…`), 듣는 사람은 `keeps his lips closed`로 적는다. 돌아보거나 다가가는 동작이 있으면 **동작이 끝난 뒤에** 말하게 하고, 돌아보는 방향을 화면 기준(`toward SCREEN-LEFT`)으로 적는다.
- **목소리:** 두 사람의 목소리 묘사를 파일 맨 위에 한 번 정하고, 모든 영상 프롬프트에 글자 그대로 반복한다(예: `Voice: low, calm, slightly gruff, speaks slowly.`).
- **닿기 직전 스틸 (숏드라마의 일부, 2026-10-13):** 「닿기 직전」 스틸은 콘티 파일 `## 시작 스틸 프롬프트`의 C 다음, D 앞에 `### 닿기 직전 (C 블록의 끝 그림 = 입맞춤 클립의 시작 이미지 · 가장 먼저 만든다)` 칸으로 둔다(별도 스틸 루틴은 닫음). 작품 파일에 `### 닿기 직전 (유저 남성)` 칸이 남아 있으면 그 칸(`>` 설명 줄·긴 버전·짧은 버전)을 **글자 그대로 옮기고**, 작품 파일의 그 자리에는 `> 「닿기 직전」 스틸 프롬프트는 숏드라마의 일부라 콘티 파일 `zeta/shortdrama/{번호}_{이름}_숏드라마.md`의 `### 닿기 직전`으로 옮겼다(2026-10-13).` 한 줄만 남긴다. 없으면 `zeta/zeta-still-routine-prompt.md`의 규칙대로 새로 쓰되, 장소·시간·의상은 이 콘티의 장면과 같게, 두 사람의 자세(손 위치·서 있는 자리)는 C 블록의 끝과 같게 정한다. 칸 맨 위 `>` 줄에 생성 순서(닿기 직전 → A 참고 → B~D는 A 채택 스틸 참고)와 영상에서의 역할(C 끝 프레임 = 입맞춤 시작 이미지)을 적는다.
- **연결 (컷이 이어지게, 2026-10-13):** 한 편이 한 장소·한 의상으로 이어지는 흐름이 되게 한다. ① 생성 순서: 닿기 직전 스틸 → A 시작 스틸(참고 이미지에 닿기 직전 스틸) → B~D(참고 이미지에 A 채택 스틸). ② C 블록 영상은 시작 이미지 = C 스틸, **끝 프레임 = 닿기 직전 스틸**(Kling 3.0 시작·끝 프레임)로 만들고, C의 마지막 동작은 닿기 직전 스틸의 자세·거리로 끝난다(C 영상 칸 머리 `>` 줄에 적는다). ③ 입맞춤 클립의 시작 이미지 = 닿기 직전 스틸이라 C → 입맞춤은 컷 없이 이어 붙인다. ④ D 블록은 입맞춤 클립의 끝(이마를 맞대고 배시시)에서 막 떨어진 순간으로 시작한다(D 영상 칸 머리 `>` 줄에 적는다). ⑤ `## 편집 순서` 맨 위에 이 연결을 한 줄로 적는다.
- **입맞춤 (영상으로만 만든다, 2026-10-13):** 입맞춤 스틸(사진)은 이미지 생성 도구의 출력 검사에서 거의 다 거절되므로 만들지 않는다. 블록 C는 얼굴이 몇 cm까지 가까워진 정적에서 끝나고 입맞춤은 넣지 않는다. 입맞춤 클립은 **「닿기 직전」 스틸을 시작 이미지로** 쓰고(이 콘티의 `### 닿기 직전` 칸으로 만든 이미지), Kling 3.0 · 9:16 · **15초 · 소리 켬**으로 만든다. 프롬프트는 2026-10-13 001에서 생성이 통과한 **짧은 문장형 5컷 틀**을 쓰고 `{ }`만 채운다(인물 외모 묘사·초 단위 시간표·【】 절 제목을 넣지 않는다 — 길게 쓰면 거절되기 쉽다).
  - 5컷 흐름: 1 넓은 화면에서 입이 닿음 → 2 옆얼굴 클로즈업, 입을 다문 입맞춤을 몇 초 유지(입술이 닿으며 살짝 말랑하게, 탱글하게 튀는 효과 없이) → 3 **인서트**(1.5~2초 — 입맞춤을 한 번 끊어 주는 짧은 컷, 2026-10-13 사용자 제안) → 4 한 사람 클로즈업, 떨어져서 수줍게 웃으며 **콘티 대사 한 줄** → 5 미디엄 투샷, 이마를 맞대고 둘 다 배시시 웃음(말 없음). **인서트는 작품마다 다르게, 장면에 어울리게 고른다**(모든 편이 같은 컷이면 공식처럼 보인다, 2026-10-13 사용자 결정): ① 그 작품의 **소품·동물·버릇**이 입맞춤에 반응하는 컷(예: 001 거북이가 등껍질 속으로 머리를 쏙 넣음 = "뚜껑 닫기", 손에서 미끄러지는 펜·호루라기, 꼬리를 흔드는 개) 또는 ② **손** 세 가지 중 그 장면 자세에 맞는 것 — **마주 잡은 손**(`extreme close-up insert of their clasped hands between them, the fingers slowly tightening and lacing together`), **목 뒤를 감싼 손**(`close-up insert of the hand of the man in {옷} resting at the back of the other man's neck, the fingers gently tightening`), **옷자락을 쥔 손**(`extreme close-up insert of the hand of the man in {옷} gripping {상대의 옷자락·끈·소매}, the fingers slowly tightening`). 닿기 직전 스틸에서 손이 실제로 있는 자리와 맞춰 고르고(옷자락을 잡고 있었으면 옷자락, 손이 비어 있었으면 소품이나 마주 잡은 손), 누구의 손·소품인지 옷이나 위치로 적는다. 손이 얼굴을 가리는 그림은 쓰지 않는다.
  - **대사 (2026-10-13 사용자 결정: 소리는 켜고, 대사는 콘티에 있는 것만):** 소리를 켜면 생성 도구가 대사·속삭임·웃음을 지어내므로, 콘티의 **입맞춤 바로 다음 대사**(보통 D 블록 첫 대사) 한 줄을 4컷에 직접 넣어 그 자리를 채운다. 말하는 사람은 이름 대신 **옷**으로 지목하고(`the man in the dark work apron`), 듣는 사람은 `The other man keeps his lips closed.`, 목소리는 `## 목소리`의 그 사람 묘사를 Sound 문장에 옮긴다. 이 대사는 편집에서 D 블록의 같은 대사 대신 쓴다(편집 순서에 적는다). 입맞춤 바로 다음 대사가 없으면 4컷은 웃음만 두고 Sound 문장을 `soft gentle piano and quiet room tone only; no dialogue, no words, no whispering, no laughter.`로 쓴다.
  - A형(한 번 입맞춤) 틀: `Cinematic romantic sequence, multiple camera angles, smooth cuts. Shot 1, wide: the subjects in the image lean in and their lips meet in a gentle kiss. Shot 2, side-profile close-up focused on their lips: a soft closed-mouth kiss held still for a few seconds, their lips gently softening on contact, natural and tender. Shot 3, {인서트 한 문장: 작품마다 다르게, 예: extreme close-up insert of the old tortoise on the floor slowly tucking its head into its shell / extreme close-up insert of the hand of the man in the gray sweater holding the strap of the dark work apron, the fingers slowly tightening}. Shot 4, close-up on the man in {말하는 사람의 옷}: they have slowly parted; he smiles shyly with eyes lowered and says quietly and slowly in Korean: "{대사}" The other man keeps his lips closed. Shot 5, medium two-shot: they rest their foreheads together and both smile shyly, looking down, no talking. Soft natural light on their faces, any colored light only in the background. Lips in sharp focus with natural texture. Shallow depth of field, smooth slow motion, emotionally warm, film-like quality. Sound: only that one Korean line in {목소리 묘사, 예: a low, quiet, slightly hoarse voice}, with soft gentle piano and quiet room tone; no other words, no whispering, no laughter.`
  - **B형 (두 번 입맞춤, 2026-10-13 사용자 제안):** 입을 맞춘 뒤(인서트) 얼굴이 몇 cm 거리에서 마주 본 채 대사 한 줄 → 상대가 다시 짧게 입을 맞춘다. 대사가 상대를 다시 다가오게 하는 말(고백·놀림·약속)일 때 잘 맞는다. 콘티 파일에는 A·B·C형을 모두 적고, 사람이 골라 쓴다. 틀: `Cinematic romantic sequence, multiple camera angles, smooth cuts. Shot 1, wide: the subjects in the image lean in and their lips meet in a gentle kiss. Shot 2, side-profile close-up focused on their lips: a soft closed-mouth kiss held still for a few seconds, their lips gently softening on contact, natural and tender. Shot 3, {인서트 한 문장}. Shot 4, close two-shot in profile: they part just a few centimeters, faces still only inches apart, looking into each other's eyes; the man in {말하는 사람의 옷} says quietly and slowly in Korean: "{대사}" The other man keeps his lips closed and smiles shyly. Shot 5, side-profile close-up: the other man leans back in for a second short, soft closed-mouth kiss, then they rest their foreheads together and both smile shyly, looking down, no talking. Soft natural light on their faces, any colored light only in the background. Lips in sharp focus with natural texture. Shallow depth of field, smooth slow motion, emotionally warm, film-like quality. Sound: only that one Korean line in {목소리 묘사}, with soft gentle piano and quiet room tone; no other words, no whispering, no laughter.`
  - **C형 (대사 없이 떨어졌다 다시 붙기, 2026-10-13 사용자 제안):** 입을 맞춘 뒤(인서트) 몇 cm만 떨어져 말없이 눈을 마주치고 숨 한 번 → 다시 입을 맞춘다. 입맞춤 클립에는 대사가 없으므로 입맞춤 바로 다음 대사는 D 블록에 그대로 둔다(건너뛰지 않는다). 콘티 파일에는 A·B·C형을 모두 적고, 사람이 골라 쓴다. 틀: `Cinematic romantic sequence, multiple camera angles, smooth cuts. Shot 1, wide: the subjects in the image lean in and their lips meet in a gentle kiss. Shot 2, side-profile close-up focused on their lips: a soft closed-mouth kiss held still for a few seconds, their lips gently softening on contact, natural and tender. Shot 3, {인서트 한 문장}. Shot 4, close two-shot in profile: their lips part just a few centimeters, faces still only inches apart, they look into each other's eyes for a quiet breath, no words. Shot 5, side-profile close-up: they lean back in and their lips meet again in a second soft closed-mouth kiss, then they rest their foreheads together and both smile shyly, looking down. Soft natural light on their faces, any colored light only in the background. Lips in sharp focus with natural texture. Shallow depth of field, smooth slow motion, emotionally warm, film-like quality. Sound: soft gentle piano and quiet room tone only; no dialogue, no words, no whispering, no laughter.`
  - 네거티브 칸: `extra dialogue, whispering, laughter, kissing sounds, exaggerated lip squish, bouncy or jelly lips, swollen or glossy lips, open mouth, tongue, blurry lips`
  - 거절될 때: 2컷의 `focused on their lips`와 `held still for a few seconds`를 빼고 `held for a moment`로 바꾼다. 그래도 거절되면 `Cinematic romantic shot: the subjects in the image lean in and share a gentle, brief kiss. Start wide, then cut to a soft close-up. They part and smile shyly. Soft natural lighting, shallow depth of field, smooth slow motion, emotionally warm, film-like quality.`
- **손·로고:** 손이 얼굴을 가리는 포즈를 쓰지 않는다(손은 목 뒤·주머니·소품에). 신발·시계·가방·옷에 브랜드 로고 없음.

## 파일 구성 (본보기와 같은 순서·제목)

1. `# {번호} {이름} · 숏드라마 「{제목}」`
2. `>` 설명 줄: `유저(남) 이름: …. 세로 9:16 · 약 N초 · 블록 4개 + 입맞춤 클립. 콘셉트 한 줄. 장소·시간. 참고 이미지 = {번호}_{영문 이름}-character-sheet-2k-v*.png, {번호}_{영문 이름}-user-m-character-sheet-2k-v*.png, {영문 이름}-main.png, {영문 이름}-user-m.png (드라이브 '이미지 프로필 제작'). 작업용 참고(공개 칸에 쓰지 않음).`
3. `## 목소리` — 두 사람 목소리 영어 한 줄씩.
4. `## 콘티` — 블록별 표(컷 번호 · 길이 · 그림 · 대사). 컷은 블록당 3~5개, 손·소품 인서트 컷을 최소 3개 넣는다. 대사를 주고받는 블록에는 **답하는 쪽 클로즈업 컷**(웃는 얼굴)을 표에 따로 적는다.
5. `## 시작 스틸 프롬프트` — `### A`~`### D` 블록마다 `>` 한글 장면 한 줄 + ```text 구조형 프롬프트```. 틀은 본보기와 같다: 첫 문장(세로 9:16 2K, 연인인 성인 두 사람) → 【REFERENCE IMAGES】(시트·프로필로 얼굴, 앞 블록 스틸로 옷·장소를 맞춘다는 문장, A는 닿기 직전 스틸이 있으면 그것을, B~D는 "A 블록 채택 스틸"을 기준으로) → 【CHARACTER — 주인공】 → 【CHARACTER — Boyfriend】 → 【SCENE】 → 【COMPOSITION】 → 【LIGHTING · COLOR · STYLE】 → 【PROHIBITIONS】(본보기 공통 항목 + 외꺼풀이면 `No double eyelids on …`, 유저에 점이 없으면 `No mole on the boyfriend.`, 동물이 있으면 `Only one {동물}.`, 손·로고 문장). C 다음, D 앞에 `### 닿기 직전` 칸(위 「닿기 직전 스틸」).
6. `## 영상 프롬프트` — `### A`~`### D`와 `### 입맞춤 클립`(시작 이미지 = 닿기 직전 스틸, 위 「입맞춤」의 A형·B형·C형을 채운 ```text 칸 세 개 + 네거티브 칸 + 거절될 때 칸 — 001 파일과 같은 모양), 그리고 대사를 주고받는 블록마다 `### {블록}2 클로즈업`(답하는 쪽이 웃으며 대사를 하는 4~5초 클립, 시작 이미지는 그 블록 스틸이고 카메라가 답하는 사람 얼굴로 다가가는 클로즈업). Kling 3.0 pro, 9:16, 10~12초(입맞춤 15초), 소리 켬. 블록 클립의 틀(입맞춤 클립은 위 A·B·C형 틀만): 첫 문장(시작 이미지에서 이어짐, 얼굴·옷·장소 유지, 서두르지 않는 속도) → 【CHARACTERS】(외모 한 줄 + 목소리) → 【ACTION · SOUND · DIALOGUE (in this exact order)】 초 단위 시간표, 대사는 `in Korean: "…"` → 【SOUND】(이 대사만, 천천히·또렷하게, 입 모양 맞춤, 효과음 목록, 음악·내레이션 없음) → 【CAMERA · STYLE】 → 【PROHIBITIONS】.
7. `## 자막` — 시작·끝 시각과 한국어 대사 표(편집 순서 기준 누적 시간).
8. `## 편집 순서` — A → B → C → 입맞춤 클립 → D, 각 쓸 구간과 편집 메모(멈춤·확대 인서트·암전 등). A·B형을 쓰면 입맞춤 클립에 넣은 대사는 D 블록에서 건너뛰고, C형이면 D 블록 대사를 그대로 쓴다고 적는다.
9. `## 생성 후 검수` — 본보기의 체크리스트(손 → 얼굴 표식 → 옷 → 로고·글씨 → 동물 수 → 비율 9:16)를 작품에 맞게.

## 실행 전 점검 (작품마다)

- [ ] 대사가 프롬프트 안에서 철자가 맞다(한 글자씩 다시 읽는다. 예: "줘야죠"를 "줄야죠"로 쓰지 않는다).
- [ ] 한 영상 클립에 말하는 사람이 한 명뿐이다. 주고받는 대사는 클로즈업 클립으로 나뉘어 있고, 말하는 사람이 위치·옷으로 지목돼 있으며, 돌아보는 동작 뒤에 대사가 온다.
- [ ] 목소리 문장이 다섯 개 영상 프롬프트에서 글자까지 같다.
- [ ] 웃음은 배시시 수줍은 미소(`small, shy smile`)이고, 영상 프롬프트에 `burst out laughing`·`genuine laughter`·`hearty`·`doubling over`·`delighted grin`이 없으며, 웃음이 있는 클립의 금지 줄에 `No loud laughter`가 있다.
- [ ] 시작 스틸에 얼굴·귀가 붉어지는 표현이 0건이다(`blush`·`flush`·`ears red`·`red cheeks`·빨개·붉어 검색).
- [ ] 블록 C·D와 시작 스틸에 입맞춤이 없고, 입맞춤은 입맞춤 클립(영상)에만 있다. 입맞춤 클립의 시작 이미지는 닿기 직전 스틸이고, 프롬프트는 규칙의 A·B·C형 틀(작품에 맞는 인서트 포함)이며, A·B형의 대사는 콘티의 입맞춤 바로 다음 대사 한 줄(말하는 사람은 옷으로 지목)뿐이고 C형은 대사가 없다. 입맞춤 스틸 프롬프트를 쓰지 않았다.
- [ ] 주인공 외꺼풀/쌍꺼풀·점·흉터·안경이 프로필과 맞고, 유저 이름이 프롬프트 본문에 없다.
- [ ] `young`, `passionate`, `kissing passionately`, 브랜드 이름이 없다. 침실·노출·손이 얼굴을 가리는 포즈가 없다.
- [ ] 장소·시간이 플롯(닿기 직전 칸/에필로그/이벤트)에서 왔다.
- [ ] `### 닿기 직전` 칸이 시작 스틸의 C 다음에 있고(작품 파일에 있던 것은 글자 그대로 옮기고 작품 파일엔 안내 한 줄만 남김), C 영상 칸에 끝 프레임 = 닿기 직전, D 영상 칸에 입맞춤 끝에서 이어짐, 편집 순서 맨 위에 연결 줄이 있다. 닿기 직전 칸에 `kiss`·`passionate`·붉어짐 표현이 없다.
- [ ] 입맞춤 클립의 인서트가 그 작품만의 소품·동물·버릇(또는 손)이고, 닿기 직전 스틸에 보이는 것이다.
- [ ] 자막 표의 시각이 편집 순서의 누적 길이와 맞다.

## 저장

- 새 파일 `zeta/shortdrama/{번호}_{이름}_숏드라마.md`를 만들고, 닿기 직전 칸을 옮긴 작품 파일만 함께 고친다. `python3 viewer/build.py`로 뷰어를 다시 만들어 같이 커밋한다(충돌이 나면 main을 합치고 다시 빌드).
- 작업 브랜치에 커밋하고(`숏드라마 콘티 추가: 이름, 이름, 이름`) 푸시한 뒤 PR을 만들고 머지한다. 충돌이 나면 main을 합쳐 푼다.
- 머지한 뒤 세 작품 이름·콘티 제목·남은 작품 수를 한 줄로 알린다.
