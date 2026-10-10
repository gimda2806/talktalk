# 제타 이미지 프롬프트 제작 규칙

주인공 프로필 이미지를 만들 때 쓰는 규칙. 특정 인물을 복제하지 않고 "K-드라마 아이돌급 실사 미감"과 "미모 하한선"을 모든 캐릭터에 공통으로 고정하고, 얼굴 구조·머리·체형·의상만 캐릭터마다 바꾼다.

> 영어 블록은 원본 프롬프트 자료의 원문을 그대로 옮긴 것이다. 한글 설명은 이해를 돕기 위한 것이다. "원문 그대로" 표시가 붙은 영어 블록은 실제 프롬프트에 **영어 원문 그대로** 넣는다. 번역·압축·요약·의역하지 않는다.

## 0. 제타 작업에서의 적용 범위

- 주인공 프로필용 프롬프트: 5절 구성 순서의 1~9번 블록 전체를 적용한다. 캐릭터 시트가 아니라 프로필 한 장이 필요하면 7번(레이아웃 블록)은 쓰지 않고 6-12의 구도 문장 한 줄로 대신한다. 이때 6-1 블록의 첫 문장 `Vertical character design sheet for a Korean live-action short drama, ultra-photorealistic 2K, NOT illustration.`은 `Upper body portrait for a Korean live-action short drama, ultra-photorealistic 2K, NOT illustration.`으로 바꾼다. 시트 문장을 그대로 두면 여러 칸짜리 그림이 나올 수 있다. 6-1의 나머지 문장은 그대로 둔다.
- 유저 대화 프로필용 프롬프트: 남성용과 여성용 두 개를 만든다. 주인공과 같은 블록 구성(6-1, 6-2, 6-3, 얼굴 구조, 의상, 조명, 6-9)을 쓰되 6-3은 각각 MALE/FEMALE을 넣고, 얼굴 구조는 6-10의 유저 공통 얼굴을 쓴다. 얼굴이 보이는 상반신 초상이다. 대화 프로필 설명 칸은 성별 없이 하나만 둔다. (옛 웹툰풍·뒷모습 형식은 더 쓰지 않는다)
- 각 영문 프롬프트 바로 아래에 한글 설명을 한두 문장으로 덧붙인다. (코드블록 밖)
- 조연 프로필용 프롬프트(선택): 서브 남주·라이벌처럼 이벤트와 설정집에 직접 등장하고 대사가 있는 조연에게만 한 장 더 만든다. 제목은 `### 조연 프로필용 (이름 · 역할)`, 주인공과 같은 블록 구성, 푸터 이름은 조연 이름. 6-11 구분 축에서 **주인공과 최소 2개, 되도록 4개 이상** 다르게 하고(같은 화면에 둘이 나올 수 있으니 한눈에 구분돼야 한다), 유저 얼굴(6-10)과도 다르게 한다. 짧은 버전·한글 설명도 같이 둔다. 등록은 `register.py <작품> 조연 <파일>`(파일명 `-sub`). 곽말순·남궁두처럼 한두 줄 스쳐 가는 조연에게는 만들지 않는다.

## 1. 레퍼런스에서 "전체 미감"만 뽑고 개인은 복제하지 않는다

사용자가 선호하는 프롬프트나 이미지를 레퍼런스로 주면 두 그룹으로 나눈다.

**GLOBAL LOOK DNA (모든 캐릭터에 고정)**

- 실사 매체와 2K급 정교함
- 아이돌급 얼굴 골격 기준
- 피부 광채, 쿨/웜 언더톤, 사실적인 질감, 피부 보정의 한계선
- K-아이돌 메이크업의 강도와 정밀도
- 광학적 소프트닝, 렌즈 플레어, 눈의 선명도, 피사계 심도
- 저채도, 저~중간 대비, K-드라마 색보정, 필름 반응
- 공통 금지: 플라스틱 같은 느낌, 번들거리는 피부, 흔한 "AI 얼굴"

GLOBAL LOOK DNA는 성격, 머리색, 의상, 직업, 장면과 관계없이 모든 캐릭터 프롬프트에 원문 그대로 넣는다.

**CHARACTER DESIGN VARIABLES (캐릭터마다 고유)**

- 구체적인 눈 모양, 얼굴 너비, 턱 모양, 광대 높이, 눈썹 모양, 코-입 비율
- 머리색, 헤어스타일, 키, 체형, 보이는 나이, 자세
- 직업, 성격, 기본 표정
- 의상, 신발, 액세서리, 소품
- 특정 배경색 또는 캐릭터 전용 조명 모드

레퍼런스 프롬프트에 전역 미감과 특정 의상이 섞여 있으면 둘을 분리한다. 전역 미감은 유지하고 의상은 그 캐릭터에게만 묶는다. 검은 코트, 수건, 니트, 상의 탈의 같은 레퍼런스 특징을 다른 캐릭터에 적용하지 않는다.

여러 캐릭터를 만들 때는 **얼굴 다양성 매트릭스**를 만들어 캐릭터별로 기록한다: 얼굴 가로세로 비율, 턱 각도, 광대 위치, 눈매 각도와 길이, 눈썹 굵기와 아치, 콧대 길이와 코끝 모양, 입술 두께, 헤어라인, 기본 얼굴 긴장도. 주요 캐릭터들은 같은 GLOBAL LOOK DNA를 공유하면서 최소 4개 지표에서 확실히 달라야 한다. 이 매트릭스는 기획 기록에만 두고 이미지 모델에는 넘기지 않는다.

## 2. 아이돌급 얼굴 기준선과 차별화의 경계

GLOBAL IDOL FACIAL BEAUTY FLOOR는 모든 주연이 공유하는 고정 미모 기준점이다. 얼굴 다양성 매트릭스로 이 높은 미모 범위 안에서만 변화를 준다.

다음 방법으로 캐릭터를 구분하지 않는다: 콧대 낮추기, 콧볼 넓히기, 뭉툭한 코끝, 긴 중안부나 인중, 넓고 두꺼운 턱, 큰 교근(사각턱), 헤어라인 뒤로 밀기, 튀어나온 귀, 깊은 눈썹뼈, 흔한 둥근 얼굴.

전역 미모 기준선은 "작은 얼굴, 오밀조밀하고 조화로운 얼굴 3등분, 절제된 거의-대칭, 정돈된 중안부, 짧은 인중, 탄탄한 하안부, 좁고 높은 콧대, 정밀한 눈꼬리, 정돈된 입술선"이다. 구체적인 눈 모양, 눈썹 모양, 광대 위치, 입술 모양, 얼굴 비율, 기본 긴장도는 캐릭터 변수로 남는다.

레퍼런스 프롬프트에 모순이 있으면(전역은 높은 콧대인데 캐릭터 설명은 낮은 콧대, 전역은 조각 같은 골격인데 캐릭터 설명은 묻힌 광대 등) 더 높은 아이돌급 기준을 우선하고 캐릭터 고유 블록을 다시 쓴다. 생성 실패로 생긴 "하향" 표현을 다음 단계로 전파하지 않는다.

## 3. K-드라마 아이돌 미감과 캐릭터 대비

- 모든 콘텐츠는 고퀄리티 K-드라마 아이돌 제작 기준을 유지한다.
- 흔한 외모, 저예산 드라마 클리셰, 얼굴 바꿔치기를 피한다.
- 직업과 설정은 플롯의 기획 요약을 따른다.
- 여러 캐릭터는 최소 두 가지 대비점(지위/권력, 실루엣/체격, 겉 태도와 속마음, 행동 속도, 감정 표현 방식)을 가진다. 차이는 헤어스타일, 옆모습, 키/체격, 옷, 색상 팔레트로 바로 알아볼 수 있어야 한다.
- 미감을 떨어뜨리거나 메이크업 품질을 낮추거나 "평범한" 엑스트라를 쓰는 방식으로 대비를 만들지 않는다. 같은 기본 얼굴에 머리색이나 옷만 바꾸는 방식도 쓰지 않는다.
- 남성성(강인함, 위험함, 다정함, 젊음)은 거칠어진 이목구비가 아니라 골격, 시선, 눈썹 표정, 연기에서 나온다. 여성성은 과장된 "인플루언서 스타일" 이목구비가 아니라 비율, 눈 모양, 입술 모양, 메이크업, 얼굴 긴장도에서 나온다.

## 4. 제타에서 만드는 이미지

제타에서는 주인공 프로필 1장과 유저 대화 프로필 2장(남성용·여성용), 모두 상반신 초상 세 장만 만든다. 세 장 모두 맨 아래에 배경 위로 `캐릭터 이름 | 생성일시` 글씨(6-13)가 들어간다(유저용은 `이름(U, M)` / `이름(U, F)`). 캐릭터 시트, 스토리보드, 키 프레임, 영상은 만들지 않는다.

## 5. 프롬프트 구성 순서 (엄격히 지킨다)

1. GLOBAL K-DRAMA IDOL LOOK BLOCK (원문 그대로)
2. GLOBAL IDOL FACIAL BEAUTY FLOOR (원문 그대로)
3. GENDER BEAUTY AMPLIFIER 하나 (원문 그대로)
4. 현재 캐릭터의 독립적인 FACE GEOMETRY BLOCK
5. ARCHETYPE ADAPTER 또는 커스텀 성격 디자인
6. HAIR / BODY / WARDROBE VARIABLES
7. 구도 문장 한 줄 (6-12에서 프레임·앵글·시선·자세를 골라 쓴다. 시트 레이아웃 블록은 제타에서 쓰지 않는다)
8. LIGHTING MODE 하나
9. GLOBAL NEGATIVE BLOCK (원문 그대로)
10. BOTTOM IDENTIFICATION FOOTER (6-13, 세 장 모두. 배경 위에 이름과 생성일시 글씨만, 띠 없음. 유저용은 이름 뒤에 `(U, M)`/`(U, F)`)

블록을 더 짧은 프롬프트로 요약하지 않는다. GLOBAL LOOK, GLOBAL BEAUTY FLOOR, 선택한 GENDER AMPLIFIER, GLOBAL NEGATIVE는 최종 출력에 끊김 없이 완전한 텍스트로 들어가야 한다. 단 하나의 예외가 6-14의 '짧은 버전'이다. 긴 프롬프트를 받지 못하는 도구를 위해 긴 버전 옆에 따로 두는 칸이며, 긴 버전 자체를 줄이는 것이 아니다. 레퍼런스 이미지는 정체성만 고정하며 전역 스타일 용어를 대체할 수 없다.

## 6. 블록 원문

### 6-1. GLOBAL K-DRAMA IDOL LOOK BLOCK (모든 캐릭터, 원문 그대로)

한글 설명: (프로필 한 장일 때는 첫 문장을 0절의 예외대로 '상반신 초상'으로 바꾼다) 한국 실사 숏드라마용 세로 캐릭터 시트, 초실사 2K, 일러스트 아님. 아이돌급 입체 골격과 정제된 얼굴 면, 높고 곧은 콧대, 또렷한 쌍꺼풀. 젊고 생기 있는 아이돌 에너지. 하얗고 고른 쿨톤 백자 피부에 가벼운 소프트터치 보정(모공 질감은 유지, 물광·유분·글래스 스킨 없음). 또렷한 K-아이돌 그루밍과 눈 화장. 모든 인물 칸에 시네마틱 소프트 포커스. 저채도, 저~중간 대비, 부드러운 하이라이트, 은은한 필름 그레인.

```text
Vertical character design sheet for a Korean live-action short drama, ultra-photorealistic 2K, NOT illustration. Premium live-action K-drama character photography with idol-grade visual impact. Highly sculpted three-dimensional bone structure, refined elegant facial planes, a clean defined jawline, a prominent high straight nose bridge, deep naturally defined double eyelids, precise and harmonious face geometry. Youthful Korean idol energy — fresh-faced, polished and camera-ready, never juvenile, never ordinary, never a generic passerby. Skin: extremely fair, bright, radiant, and even-toned — luminously cool white porcelain complexion, zero dullness, zero sallowness, zero redness, zero shadow pooling across any facial zone. Moderate retouching: light skin smoothing applied with a cinematic glamour soft-touch finish — visibly smoother than raw skin yet retaining real pore texture, subtle micro-skin grain, and natural skin surface detail; NOT plastic, NOT wax-figure, NOT over-erased. Luminosity comes from even brightness and whiteness of the skin tone. Non-oily, no dewy wet-look sheen, no glass-skin gloss, no concentrated specular highlights. Makeup — defined polished K-idol grooming: fuller precisely groomed brows with a clean controlled shape, defined eye makeup with visible soft eyeliner tracing the upper and subtle lower lash line, enhanced eye contour depth, naturally refined lashes, more visible tinted lip color with a clean finish and no wet gloss, brightening skin-tint finish. Polished and complete K-idol grooming, visibly more refined than minimal natural grooming but NOT heavy influencer or theatrical makeup. Cinematic soft focus applied across all portrait panels: gentle lens diffusion, filmic bokeh glow around subject edges, soft halation, optical glamour softness that preserves facial structure, skin micro-detail and eye sharpness — NOT blurry, NOT out of focus; controlled soft-focus quality as seen in high-end Korean drama cinematography. Color response: clean Korean drama cinematic texture, low saturation, low-to-mid contrast, luminous skin separation, soft highlight roll-off, gentle shadow detail, subtle filmic grain, no harsh digital sharpening and no cheap short-drama filter.
```

### 6-2. GLOBAL IDOL FACIAL BEAUTY FLOOR (모든 캐릭터, 원문 그대로)

6-1 바로 뒤에 놓는다. 한글 설명: 최상급 한국 아이돌 주연 비주얼. 작은 얼굴, 조화로운 얼굴 3등분, 짧은 인중, 탄탄한 하안부, 좁고 높은 콧대, 선명한 눈꼬리, 다듬어진 입술 윤곽. 이목구비 배치는 정밀하고 균형 잡혔으며 거칠거나 평범하지 않다.

```text
Exceptionally refined top-tier Korean idol lead visual, with a small face and compact harmonious facial thirds, controlled near-symmetry, narrow clean facial width, dimensional yet delicate midface structure, a short neat philtrum, a compact tapered lower face, a precise narrow high nose bridge, a refined narrow nose base with delicate nostrils, long clean eye openings with crisp inner and outer eye corners, a clean under-eye plane, and a polished lip contour. Feature placement is exceptionally precise, balanced and camera-perfect. Every facial feature remains delicate, sculpted and high-definition; never coarse, bulky, ordinary, average-looking or generic.
```

이 미모 하한선은 정교함과 비율의 품질만 규정한다. 구체적인 얼굴형, 눈 모양, 눈썹 모양, 입술 모양, 성격은 고정하지 않는다. 모든 캐릭터 차별화는 이 범위 안에서 이루어진다.

### 6-3. GENDER BEAUTY AMPLIFIER (정확히 하나만, 원문 그대로)

성인 남성은 MALE을, 성인 여성은 FEMALE을 고른다. 둘을 같이 쓰지 않고 "male/female beauty" 같은 한 구절로 줄이지 않는다.

**MALE K-IDOL BEAUTY AMPLIFIER**

한글 설명: 최상급 한국 남성 아이돌 겸 주연 배우급 얼굴 정교함. 어깨 대비 작은 머리, 깔끔한 이마-눈썹 연결, 길고 정밀한 눈선, 좁고 높은 코, 오밀조밀한 입-턱, 교근 볼륨 없이 갸름해지는 남성적 턱. 남성미는 뼈의 긴장감, 시선, 자세, 어깨선에서 나온다.

```text
For an adult male character: exceptionally beautiful top-tier Korean male idol and leading-actor facial refinement, youthful adult freshness, a small head-to-shoulder ratio, a clean forehead-to-brow transition, an elegant brow-to-eye relationship, a long precise eye line, a tall narrow refined nose, a compact mouth-to-chin area, and a clean tapered masculine jaw without bulky masseter volume. Masculinity comes from bone tension, gaze, posture and shoulder line — never from coarse features, a heavy lower face or reduced facial harmony.
```

**FEMALE K-DRAMA LEAD BEAUTY AMPLIFIER**

한글 설명: 최상급 한국 아이돌 여배우 겸 주연급 얼굴 정교함. 작고 우아한 얼굴, 깔끔한 이마-눈썹 연결, 아몬드형·여우형·부드러운 고양이형 눈매, 섬세하고 높고 좁은 코, 오밀조밀한 하안부, 깔끔한 입술 윤곽, 계란형·하트형·부드러운 V라인 턱. 여성미는 정밀한 비율, 절제된 표정, K-드라마 메이크업에서 나온다.

```text
For an adult female character: exceptionally beautiful top-tier Korean idol-actress and leading-woman facial refinement, a small elegant face, a clean forehead-to-brow transition, long luminous almond, fox or soft cat-eye geometry with crisp corners, a delicate high narrow nose, a compact refined lower face, a sculpted clean lip contour, and an elegant tapered oval, heart-shaped or soft V-line jaw. Femininity comes from precise proportion, controlled expression and polished K-drama makeup — never from influencer-style feature enlargement, an overfilled face or generic AI-beauty symmetry.
```

### 6-4. FACE GEOMETRY BLOCK (캐릭터마다, 독립적이고 긍정형)

각 캐릭터마다 현재 캐릭터만 묘사하는 영어 긍정형 문장으로 다음 10가지를 모두 쓴다.

1. 얼굴 가로세로 비율
2. 턱 각도
3. 광대 위치
4. 눈 길이와 방향
5. 쌍꺼풀 구조 (6-11의 눈꺼풀 축에서 고른 것과 같아야 한다)
6. 눈썹 굵기와 방향
7. 콧대와 코끝 구조
8. 입술 모양
9. 헤어라인
10. 기본 얼굴 긴장도

- 6-2의 미모 하한선을 지킨다. 작은 얼굴, 조화로운 얼굴 3등분, 짧은 인중, 탄탄한 하안부, 좁고 높은 콧대와 정제된 콧구멍, 선명한 눈꼬리를 유지한다. 얼굴형과 이목구비의 관계는 바꿀 수 있지만 미모 등급은 낮출 수 없다.
- 쓰지 않는 표현: 낮거나 덜 두드러진 콧대, 넓은 코 밑동, 뭉툭하거나 둥근 코끝, 낮고 묻힌 광대, 넓고 무거운 턱, 큰 교근, 긴 중안부, 긴 인중, 뒤로 밀린 관자놀이 헤어라인, 튀어나온 귀, 거친 눈썹뼈, 얇고 납작한 입술, 흔한 둥근 얼굴. 사용자가 명시적으로 지정한 경우에만 허용하며, 그때도 미모 하한선과 어떻게 양립하는지 설명한다.
- 캐릭터 간 비교는 금지한다. `character A`, `character B`, `other character`, `different from`, `less than`, `more than`, `softer than`, `sharper than`을 포함하지 않는다. 그룹 전체의 다양성은 얼굴 다양성 매트릭스에서 먼저 기획하고, 각 캐릭터는 독립적인 긍정형 기준점으로 옮겨 쓴다.

**선택 가능한 고미모 얼굴 방향** (정체성 디자인의 출발점이며 GLOBAL BEAUTY FLOOR를 덮어쓰지 않는다)

- **날카로운 고양이상 (Angular feline):** 작고 좁고 긴 얼굴, 오밀조밀한 얼굴 3등분, 깔끔하게 갸름한 턱, 높고 선명한 광대, 길고 날카롭게 올라간 눈, 좁고 높은 콧대, 정제된 입술 윤곽
- **정제된 부드러운 남성형 (Refined soft masculine):** 작은 계란형 또는 부드러운 V자 얼굴, 오밀조밀한 하안부, 부드럽지만 높고 선명한 광대, 밝고 긴 복숭아꽃 눈 또는 아몬드 눈, 좁고 높고 곧은 코, 깔끔한 입술
- **우아한 계란형 (Elegant oval):** 길쭉하지만 중안부가 오밀조밀한 작은 계란형, 균형 잡힌 높은 광대, 차분하고 긴 아몬드 눈, 부드럽고 깔끔한 눈썹, 좁고 높은 콧대, 탄탄한 하안부
- **매혹적인 위험형 (Glamorous dangerous):** 작고 좁은 정제된 얼굴형, 높은 광대, 길고 좁고 날카로운 눈매, 명확한 코-입 관계, 정밀한 입술산, 통제된 얼굴 긴장감
- **상쾌한 스포티형 (Fresh athletic):** 어깨너비와 비례를 이루는 작은 얼굴, 깔끔하지만 거칠지 않은 턱, 시원하게 트인 긴 눈썹과 눈 부위, 좁고 높은 콧뼈, 오밀조밀한 하안부, 건강한 얼굴 긴장감

### 6-5. ARCHETYPE ADAPTERS (선택 사항)

고정된 캐릭터가 아니라 성격과 스타일링 방향이다. 하나를 고르거나, 두 개를 섞거나, 새로 만든다. 어떤 유형이든 GLOBAL 블록은 온전히 쓴다. 새 유형은 얼굴 기하, 형태, 몸짓 언어, 머리, 의상의 5개 층으로 설계한다.

| 유형 | 연기 기본값 | 형태 | 스타일링 제안 | 추천 얼굴 방향 |
| --- | --- | --- | --- | --- |
| A. 차갑고 절제된 | 차분하고 꿰뚫어 보며 감정은 턱과 시선에 억눌림 | 세로로 깔끔한 실루엣, 선명한 어깨선, 절제된 자세 | 어두운 테일러링, 구조적인 코트, 미니멀한 터틀넥, 쿨 그레이·블랙 레이어링 | 날카로운 고양이상, 우아한 계란형 |
| B. 능청스러운 연하 | 느긋하고 무심하며 입꼬리가 웃음을 참음 | 열린 어깨와 목, 살짝 기운 무게중심, 여유로운 움직임 | 정제된 라운지웨어, 부드러운 니트, 심플한 셔츠, 밝은 캐주얼 테일러링 | 정제된 부드러운 남성형 |
| C. 다정한 엘리트 | 다정하고 믿음직하며 감정은 시선이 멈추는 순간에 숨음 | 균형 잡히고 곧으며 공격적이지 않은 자세 | 고품질 셔츠, 니트 카디건, 전문직 복장, 밝은 트렌치코트, 깔끔한 중성색 | 우아한 계란형 |
| D. 위험한 미인 | 조용하고 자신감 있으며 진짜 의도를 알기 어려움 | 좁고 긴 윤곽, 정밀한 자세, 강한 시선 장악 | 몸에 맞는 어두운 패션, 실크 셔츠, 젖은 듯하거나 정돈된 머리 | 매혹적인 위험형, 날카로운 고양이상 |
| E. 햇살 스포티 | 직설적이고 밝으며 반응이 빠르지만 연기 절제는 유지 | 넓은 어깨와 등, 안정적인 무게중심, 열린 자세 | 프리미엄 애슬레저, 야구 점퍼, 트레이닝복, 티셔츠와 테일러드 바지 | 상쾌한 스포티형 |

스타일링 제안은 예시일 뿐이며 직업과 스토리에 따라 바꾼다.

### 6-6. HAIR / BODY / WARDROBE VARIABLES (완전 가변)

현재 캐릭터가 정하며 이전 캐릭터에게서 물려받지 않는다.

- 머리색과 스타일 (6-11의 구분 축에서 고른다)
- 키, 어깨너비, 근육량, 머리-몸 비율, 자세
- 직업, 사회적 지위, 생활 방식
- 의상 스타일, 색, 레이어링, 소재, 신발, 액세서리, 노출 수준
- 캐릭터 고유 표정과 소품 (6-11의 '직업이 보이게 하는 세 가지'를 포함한다)

의상의 공통 품질 요건 (원문 그대로):

```text
Premium contemporary Korean drama wardrobe styling, intentional silhouette, refined fit, believable high-quality material, clean construction, role-appropriate layering and restrained color coordination. The wardrobe must express the character's identity and situation without reducing the idol-grade visual finish.
```

사용자가 의상을 명시하면 그대로 따르고, 아니면 캐릭터 정체성에 따라 디자인한다. 앞 작품의 의상을 그대로 물려주지 않는다.

### 6-7. (삭제) 시트 레이아웃 블록

제타에서는 캐릭터 시트를 만들지 않으므로 레이아웃 블록을 쓰지 않는다. 이 자리에는 6-12의 구도 문장 한 줄을 넣는다.

### 6-8. LIGHTING MODES (하나 선택)

조명 모드는 환경과 분위기만 바꾸고 피부, 메이크업, 얼굴 정교함은 바꾸지 않는다.

**쿨 뉴트럴 스튜디오 (Cool-neutral studio)**

```text
Neutral cool-gray photography studio or minimal clean interior, soft diffused frontal key light with sculpted gentle side shadow, shallow depth of field, cool-neutral low saturation and low-to-mid contrast. Skin remains luminous cool white with no dull patches.
```

**웜 화이트 아파트 (Warm-white apartment)**

```text
Soft blurred warm-white and beige minimalist interior, soft diffuse frontal key light, gentle sculpted side shadow, shallow depth of field, low saturation and low-to-mid contrast. Environment may be warm beige; skin must remain cool porcelain-white, never warm yellow.
```

**균형 잡힌 고급 실내 (Balanced upscale interior)**

```text
Premium neutral Korean interior with warm practical lights and controlled cool shadow fill, soft frontal key, restrained halation, low saturation and low-to-mid contrast. No harsh orange-teal split.
```

### 6-9. GLOBAL NEGATIVE BLOCK (모든 캐릭터, 원문 그대로)

특정 의상, 머리색, 체형을 금지하는 블록이 아니다. 다른 캐릭터 간 같은 얼굴 재사용을 금지한다.

세 장 모두 하단 이름·생성일시 글씨(6-13)를 넣으므로 맨 앞의 `NO text, NO watermark, NO UI overlay,`를 아래 문장으로 바꾼다. `NO text`를 그대로 두면 모델이 하단의 이름·날짜까지 지워 버린다.

```text
NO UNINTENTIONAL TEXT, NO WATERMARK, NO UI OVERLAY. EXCEPTION: The bottom cinematic character-identification footer is intentional and MUST contain the exact specified character name and date/time.
```

```text
Negative constraints: NO text, NO watermark, NO UI overlay, NO different identity across panels, NO same-face reuse across different characters, NO plastic high-gloss skin, NO over-smoothed wax-figure skin, NO generic passerby features, NO cheap short-drama casting, NO exaggerated facial expressions, NO screaming, NO wide-open mouth, NO unintended hair color change, NO costume drift within the same sheet, NO body-type drift within the same sheet, NO age drift, NO blurry or unsharp panels outside the controlled soft-focus intent, NO dewy glass-skin sheen, NO oily shine or highlight pooling, NO wet-look skin surface, NO dull or sallow patches anywhere on the face, NO heavy blur that erases skin texture detail, NO heavy influencer or theatrical makeup, NO long midface, NO long philtrum, NO wide nose base, NO bulbous or rounded nose tip, NO broad heavy jaw, NO bulky masseter, NO protruding ears, NO coarse brow ridge, NO receded temple hairline, NO tired hollow eyes, NO generic actor casting face, NO average commercial-model face, NO coarse or bulky facial feature, NO wrong limb count, NO merged identities.
```

### 6-10. USER PROFILE FACE (유저 대화 프로필용 공통 얼굴 구조)

한글 설명: 유저 이미지(남성용·여성용)에 공통으로 쓰는 얼굴 구조. 주인공의 얼굴 구조(6-4)는 이 얼굴과 다르게 쓴다(같은 그림체, 다른 얼굴). 작고 부드러운 계란형, 긴 아몬드 눈, 좁고 높은 코, 차분하고 밝은 표정. 성별 블록(6-3)과 머리 모양만 남녀를 다르게 하고 이 얼굴 구조는 그대로 쓴다. 작품별로 바뀌는 것은 Character design의 자세·장소·옷차림(·소품)과, 여성용은 아래 "헤어스타일 축"의 머리다.

```text
Face geometry: a small soft oval face with a balanced height-to-width ratio, a gently tapered clean jawline ending in a neat softly defined chin, cheekbones set moderately high with a smooth contour, long clear almond eyes with a level outer corner and crisp inner and outer corners, a soft double eyelid fold, softly straight dark brows with a gentle length, a narrow high straight nose bridge with a delicate tip, softly full lips with a clean contour and a naturally relaxed resting line, a smooth forehead with a neat natural hairline and a light side-swept fringe, and a calm baseline expression with a bright attentive composure.
```

**유저 여성용 헤어스타일 축 (작품마다 다르게)**

유저 얼굴 구조는 공통이지만 머리까지 같으면 모든 작품의 여성 유저가 "어깨 길이 흑갈색 머리" 한 사람으로 보인다(2026-10-09까지 70편이 그랬다). 여성은 머리 손질이 다양하므로 머리를 그 작품 유저의 개성으로 쓴다. 남성용도 같은 뜻으로 길이·가르마·결을 조금씩 바꿀 수 있지만 필수는 아니다.

- Character design의 머리 구절을 아래 표에서 골라 쓰고, **직전 5편의 여성용과 다른 스타일**을 고른다. 색은 8절대로 검정·흑갈색·짙은 갈색·짙은 애쉬 브라운 안에서만. 단, 유저가 아이돌·연습생·신인 가수·모델·배우·댄서처럼 **스타일링이 직업인 역할**이면 남성용·여성용 모두 6-11 "머리색 변주" 표의 색을 쓸 수 있다. 남녀 같은 색 한 가지로 가볍게(주인공보다 한 단계 얌전한 톤), 주인공과는 다른 색으로, 한글 설명과 짧은 버전에도 반영한다. 회사원·학생·손님 같은 일반 역할은 그대로.
- 그 작품에서 유저가 하는 일·장면에 맞춘다. 운동·주방·현장·병원은 묶거나 올린 머리, 사무·카페·도서관·연인은 푼 머리나 반묶음, 학교·학원은 단정한 쪽. 액세서리(집게핀·리본·헤어밴드·머리꽂이)는 하나까지.
- 얼굴 구조(6-10 Face geometry)는 바꾸지 않는다. 머리만 바꾼다. 짧은 버전과 한글 설명 줄도 같이 고친다.

| 스타일 | 영문 구절 (Character design에 그대로) |
| --- | --- |
| 긴 생머리 | long straight black hair falling past the shoulders |
| 긴 웨이브 | long softly waved dark brown hair parted at the side |
| 낮은 포니테일 | dark brown-black hair gathered in a low ponytail with a few loose strands at the temples |
| 높은 포니테일 | black hair pulled into a high sleek ponytail |
| 집게핀 번 | dark brown hair twisted up into a loose low bun held with a claw clip |
| 반묶음 | half-up dark brown-black hair with the top section tied back and the rest loose over the shoulders |
| 단발 보브 | a chin-length black bob with a soft inward curl |
| 옆 땋기 | a single loose side braid of dark brown hair resting over one shoulder |
| 앞머리 긴 머리 | long dark brown-black hair with a full straight fringe |
| 리본 낮은 묶음 | dark ash-brown hair tied low at the nape with a thin ribbon |
| 헤어밴드 | long straight dark brown hair held back with a slim fabric headband |
| 숏컷 | a short textured pixie cut of black hair |
| 웨이브 단발 | a shoulder-grazing dark brown lob with loose waves |
| 올림머리 | black hair pinned up in a neat twist with a wooden hair stick |

### 6-11. VISIBLE DIFFERENTIATORS (눈에 보이는 구분 축, 주인공마다 필수)

**직업이 외모와 분위기에 남기는 것 (구분 축을 고르기 전에 먼저 정한다)**

직업은 옷과 소품이 아니라 얼굴 나이, 몸, 피부, 표정에 먼저 남는다. 6-1·6-3 블록이 모든 인물을 "젊고 앳된 아이돌"로 밀기 때문에, 그대로 두면 호텔 대표도 원장도 20대 초반 얼굴로 나온다. 주인공마다 아래 여섯 가지를 직업에서 먼저 뽑고, 그 결과로 구분 축의 값을 정한다.

아래 표는 **기본값**이지 의무가 아니다. 일부러 비트는 것은 캐릭터의 매력(겉과 속의 간극)이 된다. 단정한 도예가, 날티 나는데 알고 보니 스타트업 대표, 운동선수 같은 사서처럼 직업과 어긋나는 인상은 환영한다. 다만 **우연이 아니라 결정**이어야 한다. 비틀었으면 검수 결과에 "반전: 손질 흐트러짐(스타트업 대표)"처럼 적고, 그 어긋남이 플롯의 겉과 속 설계와 이어지게 한다. 여섯 가지 중 **나이 인상만은 비틀지 않는다.** 설정 나이가 30대면 얼굴도 30대로 읽혀야 하고, 책임 있는 자리의 인물이 앳되게 나오면 실패다.

| 항목 | 직업에 따라 달라지는 것 | 예 |
| --- | --- | --- |
| 나이 인상 | 대표·원장·교수·셰프·팀장처럼 책임이 있는 자리는 성숙한 어른 얼굴, 아르바이트·신인·조수는 앳되게. 설정 나이와 얼굴 나이가 맞아야 한다 | 33세 호텔 대표는 "30대 중반으로 또렷이 읽히는 얼굴", 24세 신인 가수는 "20대 초반" |
| 손질 정도 | 규정이 있는 직업은 정갈(올백·매끈한 면도·다림질), 창작·현장 직업은 자연스럽게 흐트러짐 | 은행원·승무원: 정갈 / 보컬 트레이너·도예가: 손으로 쓸어 넘긴 머리 |
| 체격·자세 | 앉아서 일하면 마르고 곧은 선, 몸 쓰는 직업은 어깨·팔이 탄탄하고 손목이 굵음 | 정비사·택배 기사·구조대원: 탄탄한 어깨 / 사서·편집자: 마르고 긴 선 |
| 피부·혈색 | 실내 직업은 창백하고 고름, 야외·현장 직업은 밝게 그을리고 혈색이 있음 | 사서·은행원: 쿨 포슬린 / 정비사·수영 강사: 밝게 그을린 톤 |
| 표정 기본값 | 서비스직은 입꼬리가 올라간 채 멈춤, 전문직은 침착한 무표정, 교사·훈련사는 눈이 먼저 웃음, 대표는 시선이 무거움 | 은행원: 절제된 미소 / 대표: 무게 있는 시선 / 트레이너: 평가하는 눈 |
| 머리 규정 | 제복·규정 직업은 귀를 드러낸 짧은 머리, 예술·자영업은 길이와 스타일이 자유 | 승무원·은행원: 귀 드러남 / 웹툰 작가·셰프: 묶거나 흐트러짐 |

- **나이 인상이 성숙 쪽이면 6-1·6-3의 "앳됨" 구절을 바꿔 쓴다.** 6-1의 `Youthful Korean idol energy — fresh-faced, polished and camera-ready, never juvenile, never ordinary, never a generic passerby.` → `Mature Korean idol-actor presence — a settled adult face, polished and camera-ready, never boyish, never juvenile, never ordinary, never a generic passerby.` 6-3 MALE의 `youthful adult freshness` → `settled adult maturity`. Character design 첫 문장에 얼굴 나이를 직접 쓴다. 예: `reads clearly as a man in his mid-thirties with a settled adult face`.
- 피부·혈색이 야외 쪽이면 6-1의 `luminously cool white porcelain complexion` → `lightly sun-kissed complexion with healthy warmth`로 바꾼다(6-11의 피부 톤 세 번째 선택지).
- 체격이 몸 쓰는 직업이면 Character design에 `athletic build with solid shoulders and strong forearms`처럼 분명히 쓴다. 6-3의 작은 두상·마른 어깨선 묘사가 이를 덮지 않게 한다.
- 검수 결과의 이미지 항목에 "직업 인상: 나이/손질/체격/피부/표정/머리" 여섯 칸을 적고, 기본값과 다르게 비튼 칸은 "(반전)"을 붙인다. 같은 직업군끼리도 이 여섯 칸이 겹치지 않게 한다.

6-4의 얼굴 방향은 형용사 차이라서 이미지 생성기가 거의 구분하지 못한다. 57편을 만들어 보니 모든 주인공이 "검은 머리, 또렷한 쌍꺼풀, 작은 계란형 얼굴, 쿨 포슬린 피부"로 수렴해 같은 얼굴이 나왔다. 그래서 생성기가 실제로 다르게 그리는 **구분 축**을 따로 둔다.

| 축 | 선택지 |
| --- | --- |
| 머리색 | 검정 / 흑갈색 / 짙은 갈색 / 짙은 애쉬 브라운 (밝은 갈색·금발은 쓰지 않는다, 8절) · 아이돌·예술·스타일 직업군만 아래 "머리색 변주" 표의 염색·탈색 색을 쓸 수 있다 |
| 머리 길이 | 옆을 짧게 친 투블럭 / 귀를 덮는 중간 길이 / 목에 닿는 장발 |
| 머리 스타일 | 앞머리를 내림 / 이마를 드러낸 올백·업스타일 / 가르마(2:8, 5:5) / 자연 곱슬·파마 |
| 눈꺼풀 | 또렷한 쌍꺼풀 / 속쌍꺼풀(hooded inner double eyelid) / 홑꺼풀(long clean monolid eyes) |
| 눈꼬리 | 올라감 / 수평 / 내려감 |
| 얼굴형 | 계란형 / 깔끔하게 각진 턱(clean angular jaw) / 긴 얼굴 / 부드럽게 둥근 턱 |
| 표식 | 안경(테 종류까지) / 눈 밑·입가의 작은 점 / 보조개 / 눈썹 끝의 작은 흉터 / 옅은 주근깨 / 타투(선택, 아래 "타투 표식" 조건대로) / 귀 피어싱(선택, 아래 "피어싱 표식" 조건대로) (수염은 턱수염·콧수염·stubble 모두 쓰지 않는다) |
| 피부 톤 | 쿨 포슬린(cool white porcelain) / 밝은 웜 아이보리(luminous warm ivory) / 밝게 그을린 톤(lightly sun-kissed with healthy warmth, 야외·현장 직업) |
| 체격 | 마르고 긴 / 어깨 넓고 탄탄한 / 중간 |
| 직업 표식 | 아래 "직업이 보이게 하는 세 가지" |

**규칙**
1. 주인공은 **직전 5편의 주인공 각각과 최소 2개 축**이 다르다. 머리 한 축만 다른 것은 "같은 얼굴에 머리만 바꾼 것"이라 인정하지 않는다(3절).
2. 표식 축은 작품마다 하나 이상 넣는다. 점·보조개·안경·작은 흉터처럼 작은 표식이 얼굴을 기억하게 만든다. 수염은 어떤 형태로도 쓰지 않는다.
3. 눈꺼풀·피부 톤·나이 인상을 기본값 외로 고르면 6-1·6-3 블록의 해당 구절만 아래처럼 바꿔 쓴다. 그 밖의 문장은 그대로 둔다.
   - `deep naturally defined double eyelids` → `clean hooded inner double eyelids` 또는 `long clean monolid eyes with crisp corners`
   - `luminously cool white porcelain complexion` → `luminously warm ivory complexion` 또는 `lightly sun-kissed complexion with healthy warmth`
   - `Youthful Korean idol energy — fresh-faced, polished and camera-ready, never juvenile,` → `Mature Korean idol-actor presence — a settled adult face, polished and camera-ready, never boyish, never juvenile,` (6-3 MALE의 `youthful adult freshness` → `settled adult maturity`)
   - 조명 블록 끝의 `skin must remain cool porcelain-white, never warm yellow`도 피부 톤에 맞게 `skin remains luminous warm ivory, never sallow`로 바꾼다.
4. 고른 축을 검수 결과의 이미지 항목에 적는다. 예: "직업 인상: 성숙한 30대 중반/자연스러운 손질/마르고 곧음/실내 밝은 톤/평가하는 눈/자유 · 구분 축: 짙은 애쉬 브라운 중간 길이 쓸어 넘김 / 속쌍꺼풀 / 각진 턱 / 눈 밑 점 / 웜 아이보리". 다음 작품은 이 기록과 대조한다.

**머리색 변주 (아이돌·예술·스타일 직업군 한정)**

회사원·교사·의사처럼 규정이 있는 직업은 8절대로 검정~짙은 애쉬 브라운 안에서만 고른다. 하지만 아이돌·가수·댄서·배우·헤어 디자이너·패션 디자이너·DJ·뮤지컬 배우처럼 **머리 스타일링이 직업의 일부인 캐릭터**는 염색·탈색이 오히려 그 사람답다. 이 직업군에는 아래 표의 색을 쓸 수 있고, 같은 직업군이 여러 편이면 색이 겹치지 않게 돌린다. 조건은 세 가지다.

- 플롯 어딘가(캐릭터 설명의 외모 줄, 인트로, 이벤트 하나)에 그 머리색이 한 번은 보인다. "컴백 무대용으로 탈색했다", "이번 배역 때문에 염색했다"처럼 이유가 한 구절 붙으면 대화 소재도 된다.
- 밝은 색(밀크 브라운·애쉬 베이지·실버)은 서구 얼굴로 흐르기 쉽다. 6-1·6-3의 Korean idol 구절을 그대로 두고, `bleached … toned for the comeback stage`, `with the dark regrowth just showing at the roots`처럼 **염색한 머리라는 것**이 드러나는 구절을 붙인다. `light brown`이라고만 쓰지 않는다.
- 이미 이미지를 만든 작품(`zeta/generated/manifest.json`)에 넣으면 6-15 변경 메모와 재생성 확인이 따라온다. 바꿀 가치가 있을 때만 바꾼다.

| 색 | 영문 구절 (Character design의 머리 구절 앞에) | 어울리는 직업 |
| --- | --- | --- |
| 라벤더 애쉬 그레이 | bleached lavender-ash gray hair toned for the comeback stage, with the dark regrowth just showing at the roots | 아이돌(컴백 시즌) |
| 밀크티 애쉬 베이지 | milk-tea light ash-beige brown hair, freshly bleached and toned for the comeback | 신인 아이돌, 댄서 |
| 플래티넘 실버 | platinum silver-gray bleached hair | 패션·디자이너, 모델 |
| 블루블랙 | deep blue-black hair with a cool navy sheen, dyed for the current drama role | 배우, 뮤지컬 배우 |
| 와인 버건디 브라운 | wine-toned dark burgundy brown hair | 싱어송라이터, 밴드 |
| 애쉬 카키 | matte ash-khaki hair with an olive undertone | 헤어 디자이너(기술 자랑), 아티스트 |
| 부분 탈색 | black hair with a few bleached ash-gray streaks through the top | 안무가, 댄서, DJ |
| 핑크 베이지 | soft pink-beige toned hair | 아이돌(여름 컴백), 뷰티 |
| 애쉬 민트 | ash-mint toned hair, muted and cool | 아이돌(콘셉트 앨범) |
| 코랄 오렌지 | bright coral-orange dyed hair, clearly a stage color | 아이돌(컴백 티저), 메인댄서 |
| 레드 | vivid cherry-red dyed hair for the comeback concept | 아이돌(강한 콘셉트) |
| 퍼플 | muted grape-purple toned hair | 아이돌(콘셉트 앨범) |
| 일렉트릭 블루 | electric blue dyed hair with a subtle wolf cut | 아이돌(퍼포먼스 포지션) |

**아이돌 헤어 레퍼런스 (스트레이 키즈·보이넥스트도어 계열)**

아이돌 캐릭터의 머리를 고를 때 두 그룹의 "방향"을 참고한다. 실제 멤버 이름·그룹 이름은 프롬프트에 절대 쓰지 않고(초상권·동일 얼굴 위험), 색·길이·손질 방식만 옮겨 담는다. 아래는 공개된 활동 사진에서 반복되는 경향을 정리한 것이지 특정 시점의 정확한 색이 아니다.

| 계열 | 느낌 | 색 | 길이·손질 | 어울리는 캐릭터 |
| --- | --- | --- | --- | --- |
| 스트레이 키즈 계열 | 컴백마다 색이 확 바뀌는 "무대용 머리". 강한 색을 자신 있게 쓴다 | 플래티넘·핑크·코랄 오렌지·레드·퍼플·일렉트릭 블루, 비활동기엔 흑발로 복귀 | 무대는 젤·왁스로 올백, 행사는 가운데 가르마 커튼 앞머리에 부드러운 웨이브. 한쪽을 짧게 친 실험적 컷, 살짝 울프컷 | 메인댄서·센터·퍼포먼스 포지션, 데뷔 몇 년 차의 자신감 있는 주인공 |
| 보이넥스트도어 계열 | 꾸미지 않은 듯한 "옆집 소년" 머리. 색보다 질감과 흐트러짐으로 개성 | 자연 흑발·자연 갈색·밀크 브라운, 탈색해도 애쉬 베이지 정도의 한 단계 얌전한 톤 | 눈썹을 덮는 흐트러진 앞머리, 자연 곱슬·히피펌, 레이어드 울프컷·짧은 멀렛, 후드티·모자와 어울리는 부스스한 결 | 신인·연습생·연하 아이돌, 유저가 아이돌일 때(6-10의 "한 단계 얌전한 톤") |

머리 모양 구절(Character design의 머리 구절에 색과 함께 쓴다):

| 모양 | 영문 구절 |
| --- | --- |
| 커튼 앞머리 웨이브 | center-parted curtain fringe with soft waves, fluffy and camera-ready |
| 무대용 올백 | hair slicked back from the forehead with gel for the stage, a few strands falling loose |
| 레이어드 울프컷 | a layered wolf cut, shaggy on top and tapering at the nape |
| 짧은 멀렛 | a short mullet with the nape left slightly longer |
| 흐트러진 앞머리 | messy eyebrow-length fringe, brushed down and slightly tousled |
| 히피펌 | loose hippie-perm curls with a soft natural volume |
| 한쪽 짧은 실험 컷 | an asymmetric cut with one side cropped shorter |
| 반묶음 장발 | hair grown past the jaw with the top half tied back |
| 눈썹 드러낸 쉼표 앞머리 | a comma-shaped fringe parted to one side, brows showing |
| 투블럭 다운펌 | a neat two-block cut with the top pressed down in a soft down-perm |
| 부분 탈색 가닥 | with a few bleached strands framing the face |
| 헤어핀·실핀 | fringe pinned back with two small black bobby pins |
| 비니·캡 | under a loose black beanie / a black cap worn backwards with the fringe out |
| 땀에 눌린 연습 머리 | hair slightly damp and pressed flat at the temples from rehearsal |
| 질감 | fluffy and airy (행사·화보) / matte and textured (무대) / wet-look gelled (강한 콘셉트) |

스타일링까지 캐릭터에 맞춘다. 색 하나만 바꾸는 것은 6-11 3절의 "같은 얼굴에 머리만 바꾼 것"이다. 같은 작품 안에서도 주인공은 무대용(올백·젤·강한 색), 유저는 연습실용(흐트러진 앞머리·땀·비니)처럼 **장면에 맞는 손질**로 나누면 두 사람이 한 그룹의 다른 멤버처럼 읽힌다.

6-11의 "직전 5편과 2축 이상 다름" 규칙은 아이돌 캐릭터에도 그대로 적용된다. 같은 소속사·같은 그룹 설정의 작품(예: 소담 엔터테인먼트 시리즈)은 서로 다른 계열을 쓰면 한 그룹처럼 보여서 좋다.

**피어싱 표식 (선택, 성격을 말해 줄 때만)**

귀 피어싱은 얼굴 가까이에 있어 작아도 기억에 남고, 타투처럼 "본인이 고른 것"이라 성격을 말해 준다. 쓰는 방향은 두 가지다.

- **날티형**: 능청스러운 연하, 위험한 미인, 밴드·가수·아이돌·타투이스트·바텐더처럼 자유로운 직업. 가는 은색 링 두 개, 헬릭스(귀 윗연골) 스터드, 이어커프처럼 **두 개 이상**을 한쪽 귀에 몰아 단다. 손질이 흐트러진 머리·열린 옷깃과 같이 쓰면 "날것"이 된다.
- **반전형**: 단정하게 차려입는 **자유 직장**의 캐릭터에게 **아주 작은 것 하나**(한쪽 귓불의 작은 은색 스터드, 귀 뒤에 가려지는 헬릭스 한 점). 광고 대행사·IT 회사·스타트업·디자인 에이전시·출판사·방송국 PD처럼 복장 규정이 없는 사무직이 대상이다. 다림질한 셔츠·올백 머리와 대비되어 "의외의 매력"이 되고, 기획 요약의 반전 한 줄·겉과 속의 간극과 이어지면 가장 좋다. **원장·교사·의사·간호사·한의사·공무원·은행원·제복 직업에는 반전형도 절대 넣지 않는다**(직업 신뢰감이 먼저다).

| 항목 | 조건 |
| --- | --- |
| 종류·영문 | 가는 은색 링 `a thin silver hoop in the left earlobe` / 작은 스터드 `a tiny silver stud in the right earlobe` / 헬릭스 `a small silver helix stud on the upper cartilage of the left ear` / 이어커프 `a slim silver ear cuff on the left ear` / 더블 링 `two thin silver hoops stacked in the left earlobe` / 체인 드롭(아이돌 무대) `a short silver chain-drop earring in one ear` |
| 개수 | 날티형은 한쪽 귀에 2~3개, 반전형은 전체 1개. 양쪽 귀에 똑같이 달지 않는다(한쪽이 더 기억에 남는다) |
| 재질 | 은색만. 금색·보석·큰 장식은 쓰지 않는다(아이돌급 얼굴 기준선과 저채도 색감을 흐린다) |
| 직업 | 날티형: 미용·패션·음악·아이돌·바텐더·타투이스트 등 자유 직업. 반전형: 광고·IT·스타트업·디자인·출판·방송처럼 복장 규정 없는 사무직만. 원장·교사·의사·간호사·공무원·은행원·제복·조리 직업은 어느 쪽도 쓰지 않는다(자국도 쓰지 않는다) |
| 머리와의 관계 | 피어싱이 보이려면 그쪽 귀가 드러나야 한다. 귀를 덮는 머리면 `with the hair tucked behind the left ear` 같은 구절을 붙이거나 짧은 머리 쪽 귀에 단다 |
| 사연 | 플롯 어딘가(캐릭터 설명 외모 줄, 설정집, 상황 예시 한 줄)에 한 번은 보인다. 반전형은 "왜 이 사람이?"가 대화 소재가 된다(예: 학생 때 뚫고 하나만 남겼다) |
| 기존 작품 | 이미 이미지를 만든 작품에 넣으면 6-15 변경 메모와 재생성 확인이 따라온다. 재생성이 어차피 예정된 작품(배지가 이미 뜬 것)에 먼저 넣는다 |

**타투 표식 (선택, 캐릭터에 어울릴 때만)**

타투는 표식 중 유일하게 "본인이 고른 것"이라 성격까지 말해 주지만, 없어도 된다. 그 캐릭터의 매력 요소(겉과 속의 간극, 버릇, 설렘 스위치)와 이어질 때만 넣고, 구분 축을 채우려고 아무에게나 넣지 않는다. 넣을 때의 조건:

| 항목 | 조건 |
| --- | --- |
| 무늬 | 글자 없는 작은 선 그림만. 가는 한 줄 산등성이·파도선·별자리 점선·식물 줄기·조리개 날·음표 같은 것. 글자·숫자·레터링은 쓰지 않는다(6-9의 "의도하지 않은 글자 금지"와 충돌해 도구가 엉뚱한 글자를 만든다) |
| 자리 | 상반신 초상에 보이는 곳만: 손목 안쪽 / 손가락 옆면 / 팔뚝 안쪽(소매를 걷는 직업) / 목 옆·귀 뒤 / 쇄골. 등·허벅지처럼 안 보이는 자리는 표식이 못 된다 |
| 크기 | 얼굴 가까이(목·귀 뒤)는 손가락 한 마디, 팔뚝은 손바닥 길이까지. 아이돌급 얼굴 기준선을 가리지 않는다 |
| 직업 | 제복·규정 직업(역무원·승무원·은행원·교사·의사)은 소매에 가려지는 자리에 아주 작게, 또는 쓰지 않는다. 예술·자영업·운동·현장 직업은 자유 |
| 사연 | 플롯 어딘가(캐릭터 설명 둘째 줄, 설정집, 이벤트 하나)에 그 타투가 왜 거기 있는지 한 줄은 있어야 한다. 그림에만 있고 글에 없는 타투는 쓰지 않는다 |
| 기존 작품 | 이미 이미지를 만든 작품(`zeta/generated/manifest.json`)에는 넣지 않는다. 넣으면 6-15 변경 메모와 재생성이 필요하다 |

프롬프트에는 Face geometry나 Character design 안에 `a small single-line ○○ tattoo on the inside of the left forearm (distinguishing mark, no lettering)`처럼 자리·무늬·글자 없음을 한 구절로 쓴다.

**직업이 보이게 하는 세 가지 (6-6과 함께, 주인공마다 필수)**

얼굴만 아이돌이고 배경에 소품 하나 놓인 사진은 어느 직업으로도 보인다. 직업은 세 겹으로 넣는다.
1. **입은 것**: 그 직업만의 복장 한 가지. 명찰·조끼·앞치마·작업복·사원증 끈·가운처럼 입거나 걸친 것.
2. **손이 하는 것**: 직업 도구를 손에 쥐고 **그 도구를 쓰는 동작** 중에 찍힌 자세. 들고만 있지 않는다. 예: 보컬 트레이너는 한 손을 들어 음을 짚어 주는 동작, 정비사는 장갑을 벗는 중, 사서는 날짜 도장을 면지에 찍는 중, 은행원은 번호표 뒷면에 볼펜을 대는 중.
3. **몸에 남은 흔적**: 직업이 몸에 남긴 것 하나. 손등의 기름 자국, 굳은살, 분필 가루, 안경 자국, 햇볕에 탄 목, 소매의 밀가루, 귀에 꽂은 연필.
배경은 그 직업의 일터로 흐릿하게 두되, 세 가지 중 둘 이상이 배경 없이도 읽혀야 한다.

### 6-12. COMPOSITION (구도, 주인공마다 필수)

5절 7번이 `Upper body portrait, three-quarter angle, (표정)` 한 줄로 고정돼 있어 모든 주인공이 같은 프레임, 같은 앵글, 같은 시선으로 나왔다. 7번 자리에는 아래 네 축을 고른 **구도 문장**을 쓴다.

| 축 | 선택지 |
| --- | --- |
| 프레임 | 가슴 위(chest-up) / 허리 위(waist-up) / 손과 소품이 보이는 반신(half-body with hands in frame) / 얼굴 클로즈업(tight close-up from the shoulders) |
| 앵글 | 정면 반측면(three-quarter) / 옆얼굴에서 돌아보는(profile turning toward the camera) / 살짝 위에서 내려다보는(slight high angle) / 살짝 아래에서 올려다보는(slight low angle) / 어깨 너머(over-the-shoulder, 얼굴은 카메라 쪽) |
| 시선 | 카메라를 봄 / 손에 든 일을 봄 / 화면 밖 옆을 봄 / 아래를 봄 |
| 자세 | 서 있음 / 앉아 있음 / 무언가에 기대어 있음 / 동작 중(걷다 멈춤, 돌아보는 중, 손을 뻗는 중) |

**규칙**
1. 직전 5편과 프레임·앵글·시선·자세 중 **2개 이상**을 다르게 고른다.
2. 프로필 이미지이므로 얼굴은 늘 4분의 3 이상 보여야 한다. 뒷모습, 완전한 옆얼굴, 손이나 소품으로 얼굴을 가리는 구도는 쓰지 않는다.
3. 구도는 직업 표식(6-11)의 '손이 하는 것'과 이어진다. 손에 든 일을 보는 시선이면 그 일이 프레임 안에 있어야 한다.
4. 조명 모드(6-8)도 직전 5편과 같은 것만 반복하지 않는다. 창가 측광(window side light), 역광 테두리(soft rim backlight), 무대·부스의 국소광(single practical light)처럼 직업 공간에서 나오는 빛을 고를 수 있다.
5. 구도 문장 예: `Waist-up portrait seen from a slight high angle, seated at the booth desk and turned toward the camera, eyes lowered to the script in hand, a faint closed-lip smile.` 고른 축을 검수 결과에 "구도: 허리 위/살짝 위에서/손을 봄/앉음" 형식으로 적는다.

### 6-13. BOTTOM IDENTIFICATION FOOTER (세 장 모두, 이름·생성일시를 채워서 원문 그대로)

주인공 프로필과 유저 대화 프로필 세 장 모두 맨 아래에 `캐릭터 이름 | 생성일시` 글씨를 넣는다. 영화 포스터 아래에 제목과 개봉일이 한 줄로 찍히는 것과 같은 방식인데, 띠나 상자를 깔지 않고 배경이 그대로 이어지는 위에 글씨만 올린다. 블록은 프롬프트의 맨 끝(6-9 뒤)에 붙이고, `{{이름}}`과 `{{생성일시}}` 두 자리만 채운다. 생성일시는 `YYYY.MM.DD HH:MM`(24시간)이며 이미지를 실제로 만드는 그 순간의 시각이다. 작품 파일에는 `{{생성일시}}` 자리표시를 그대로 두고, 뷰어의 복사 버튼이 누르는 순간의 기기 시각으로 바꿔 넣는다. 파일에서 직접 복사해 쓸 때는 손으로 지금 시각을 적는다. `26.10.09`처럼 연도를 줄이지 않는다. 블록은 "~을 추가하라"가 아니라 "이미지 맨 아래에 ~글씨가 있다"처럼 그림을 설명하는 말투로 쓴다. "추가하라"고 쓰면 일부 이미지 도구가 기존 사진을 고치는 편집 요청으로 알아듣고 원본 이미지를 먼저 올리라고 되묻는다. 유저 대화 프로필은 이름 자리에 `홍마루(U, M)`(남성용) / `홍마루(U, F)`(여성용)처럼 주인공 이름 뒤에 유저 표시를 붙여 어느 작품의 유저 이미지인지 알 수 있게 한다.

```text
BOTTOM IDENTIFICATION FOOTER (this is part of the newly generated image itself, NOT an edit of an existing image; no source image is needed): the very bottom edge of the image carries a clean cinematic character-identification caption. There is NO band, NO box, NO bar and NO solid background behind the text: the scene continues uninterrupted to the bottom edge, and only the typography is placed over it, with at most a very soft, barely visible darkening of the lowest 8–10% of the frame and a faint soft shadow under the letters so they stay legible. It should feel like a premium Korean drama character profile title card, not a UI overlay and not a watermark. The caption shows the following information in one horizontal line: {{이름}} | {{생성일시}} — the character name "{{이름}}" appears larger and more prominent, using elegant refined Korean typography in warm ivory-white; a thin vertical separator line sits between the character name and the date/time; the date and time appear smaller than the character name, using refined serif-style typography in soft ivory-white. Layout reference: the character name is positioned slightly left of center, followed by a thin vertical divider, then the date and time, with the character name approximately 1.5–1.8× larger than the date/time text, generous horizontal spacing and a sophisticated Korean editorial title-card aesthetic similar to a premium K-drama character introduction. Typography must be clean, elegant, cinematic, highly legible, vertically centered within the bottom margin, horizontally balanced and professionally typeset. The caption is visually subtle and premium and does not cover the character's body or face. The caption must be firmly anchored to the very bottom edge of the image. IMPORTANT: The ONLY intentional text in the image is the character identification caption. Do NOT add any other text, letters, captions, logos, signs, labels, watermark, random typography, or illegible text anywhere else in the image.
```

### 6-14. 짧은 버전 (긴 프롬프트를 못 받는 도구용, 세 장 모두 긴 버전 옆에 따로 둔다)

긴 버전은 영문 8,000~9,000자쯤 된다. 일부 이미지 도구는 이 길이를 받으면 이유를 말하지 않고 결과만 비운다(송예찬으로 확인: 긴 버전은 실패, 약 2,000자 축약판은 성공). 그래서 주인공 프로필과 유저 대화 프로필 세 장 모두 긴 버전 바로 아래에 `· 짧은 버전` 칸을 하나 더 둔다. 짧은 버전은 긴 버전에서 캐릭터 고유 부분만 남긴 것이다.

- 남기는 것: 첫 문장(실사 K-드라마 초상, 어른 얼굴 인상), 피부 톤 한 줄, `Face geometry: … Character design: … Wardrobe: … Props: … 구도 문장`(캐릭터 고유 부분 전부), 조명 문장, 짧은 네거티브 한 줄, 6-13 하단 글씨(짧은 문장형, 이름과 `{{생성일시}}`는 그대로).
- 빼는 것: 6-1 전역 룩, 6-2 미모 기준선, 6-3 증폭 블록, 6-9 긴 네거티브 원문. 이 네 가지는 긴 버전에만 있다.
- 길이: 영문 2,000~3,400자. 긴 버전을 고치면 짧은 버전도 같은 캐릭터 고유 부분으로 다시 만든다.
- 쓰는 순서: 먼저 긴 버전으로 시도하고, 도구가 결과를 비우거나 길이 제한을 말하면 짧은 버전을 쓴다. 짧은 버전은 긴 버전의 대체가 아니라 비상용이다.
- 만드는 법: 작업 스크립트로 긴 버전에서 위 조각을 잘라 붙인다. 손으로 요약하지 않는다.

```text
Upper body portrait for a Korean live-action short drama, photorealistic, not illustration, premium K-drama character photography with idol-grade visual finish. {{어른 얼굴 인상 한 문장}} Skin: {{피부 톤}}. Face geometry: {{긴 버전의 Face geometry … 구도 문장까지 그대로}} Lighting: {{긴 버전의 조명 문장}} Negative: no unintentional text, no watermark, no UI overlay (the bottom name caption is the only intentional text), no plastic or wax-figure skin, no generic or coarse features, no exaggerated expression, no extra limbs, no merged identities.
The very bottom edge of the image carries a clean cinematic character-identification caption, with no band or box behind it: the scene continues to the bottom edge and only the typography sits over it. One horizontal line: {{이름}} | {{생성일시}} — the name "{{이름}}" larger in elegant Korean serif typography in warm ivory-white, a thin vertical divider, then the date and time smaller in soft ivory-white serif, anchored to the bottom margin and not covering the face or body.
```

### 6-15. 프롬프트를 고칠 때의 변경 메모 (이미지를 이미 만든 작품이 있다)

이미지 프롬프트 세 장 중 하나라도 고치면(재설계, 문구 교체, 일괄 치환 모두) `zeta/image-prompt-changelog.md`에 날짜·작품·바뀐 프롬프트·바뀐 내용·이미지 유무·처리를 한 줄 적는다. 이미 만든 이미지는 `zeta/generated/manifest.json`에 등록돼 있고 등록 당시의 프롬프트 지문(`prompt_sha`)을 갖고 있어서, 프롬프트가 바뀌면 `python3 zeta/generated/register.py --check`와 뷰어 갤러리가 "프롬프트 바뀜 · 재생성 확인"이라고 알려 준다. 짧은 버전(6-14)만 새로 만드는 것은 긴 버전이 안 바뀌므로 메모만 남기고 재생성은 필요 없다. 이미지를 다시 만들었으면 `register.py`로 다시 등록해 지문을 갱신한다.

파일 끝 `## 사람이 고친 곳`에 적힌 이미지 프롬프트 칸은 사람이 뷰어에서 직접 고친 것이다. 이 문서의 어떤 규칙보다 우선하므로 재설계·일괄 치환 때 되돌리지 않는다. 바꿔야 한다고 보이면 사용자에게 먼저 묻는다.

### 6-16. 장면 스틸 (드라마 속 한 장면, 선택)

프로필 세 장과 별개로, 이벤트 한 장면이나 연작 카메오 장면을 "드라마 스틸 한 장"으로 뽑을 때 쓰는 틀. 2026-10-07까지 유저 프로필에 쓰던 옛 6-10 스틸 블록(뒤쪽 옆모습, 얼굴 미노출)을 장면용으로 되살린 것이다. 등록(`register.py`)이나 6-15 변경 메모 대상이 아니고, 작품 파일 끝 `## 10. 장면 스틸` 또는 `zeta-series.md`에 둔다.

**구성 순서 (긴 버전과 짧은 버전을 프로필처럼 둘 다 둔다. 긴 버전은 1번 헤더 자리에 6-1·6-2·6-3 블록 원문을 그대로 넣고, 짧은 버전은 아래 1번의 한 문장 헤더를 쓴다. 2026-10-09 확인: 사용자의 이미지 도구가 10,000자대 긴 버전도 읽는다)**

1. 스틸 헤더 — 긴 버전: `Vertical character design sheet…`를 `Ultra-photorealistic 2K live-action Korean drama still, NOT illustration.`로 바꾼 6-1 블록 + 6-2 + 인물 성별에 맞는 6-3(두 사람이 같은 성별이면 한 번만). 짧은 버전 (원문 그대로): `Ultra-photorealistic 2K live-action Korean drama still, NOT illustration. Premium live-action K-drama photography with idol-grade visual finish; skin even-toned with real pore texture and no dewy gloss; cinematic soft focus that keeps facial structure and eye sharpness; clean Korean drama cinematic texture, low saturation, low-to-mid contrast, subtle filmic grain.`
2. 장면 한 문장: 장소·시간대·빛·날씨·분위기. 작품의 핵심 장치가 보이면 넣는다(필름 통, 예약표, 보리차 컵).
3. 등장 인물마다 한 덩어리: `LEFT/RIGHT/CENTER, 이름:` + 그 작품 주인공 프롬프트의 `Face geometry: …`와 `Character design: …`(머리·몸·몸의 흔적)과 `Wardrobe: …`를 **그대로 복사** + 이 장면에서의 자세·동작·시선·표정 한 문장. 두 명 이상이면 맨 앞에 `Two established characters, faces kept distinct.`를 쓰고 좌우를 반드시 지정한다.
4. 유저가 나오는 장면: 유저 얼굴은 보이지 않게 한다(대화 프로필 얼굴이 남녀 공용이라 장면에서 성별을 고정하면 안 된다). 옛 블록 구절을 그대로 쓴다: `A young adult seen from behind and slightly from the side, gender-neutral, face not shown, (자세와 자리), (옷차림)`.
5. 구도 한 문장: 6-12의 축(프레임·앵글·시선·자세)에서 고른다. 두 명이면 `two-shot`, 둘 다 얼굴이 선명해야 하면 `both faces sharp`.
6. 네거티브 (원문 그대로): `Negative: no unintentional text, no watermark, no UI overlay, no merged or swapped faces, no extra person, no plastic or wax-figure skin, no exaggerated expression, no extra limbs, no illustration or webtoon style.`
7. 푸터: 6-14 짧은 버전의 푸터 문장을 그대로 쓰되 이름 자리에 `이름 · 이름` 또는 `이름 · 장면 제목`을 넣는다. 예: `백서율 · 노찬영 | {{생성일시}}`.

**규칙**
- 얼굴 블록은 반드시 그 작품의 현재 주인공 프롬프트에서 복사한다(머리색·표식·피어싱이 바뀌면 스틸도 다시 복사). 새로 쓰지 않는다.
- 의상은 장면의 시간·장소에 맞지 않으면 그 장면에 맞게 바꿔 쓴다(무대 재킷을 입고 연습실에 있지 않게). 얼굴 구조·머리·몸의 흔적·표식·액세서리는 그대로 둔다. 동작 문장에는 옷을 다시 쓰지 않는다(의상 문장과 충돌하지 않게).
- 장면은 플롯에 있는 장면만 쓴다(이벤트, 상황 예시, 에필로그, 연작 설정집의 카메오 줄). 플롯에 없는 사건을 스틸로 먼저 만들지 않는다.
- 두 주인공이 한 장에 나오면 얼굴이 섞이기 쉽다. 결과에서 얼굴이 흐트러지면 한 명을 뒷모습·옆모습으로 돌리거나 한 명씩 두 장으로 나눈다.
- 유저가 나오는 장면 스틸은 공개 칸에 쓰지 않는다(플랫폼 규칙상 유저 이미지는 대화 프로필뿐). 작업용 참고 이미지로만 둔다.

## 7. GLOBAL LITERAL GATE (생성 전 필수 검사)

이미지 도구를 호출하기 전에 아래를 모두 확인한다. 하나라도 실패하면 프롬프트를 다시 만든다.

- [ ] 6-1 블록이 첫 단어부터 Color response 마지막 문장까지 누락·번역·축약·동의어 없이 연속적이고 완전하다. (예외: 프로필 한 장이면 0절대로 첫 문장만 `Upper body portrait for …`로 바꾼다. 6-11에서 눈꺼풀·피부 톤·나이 인상을 달리 고르면 그 구절만 6-11의 표현으로 바꾼다.)
- [ ] 직업에서 뽑은 여섯 가지 인상(나이·손질·체격·피부·표정·머리)을 정했고(기본값 또는 의도한 반전), 반전은 검수 결과에 표시했으며, 얼굴 나이는 설정 나이에 맞게 Character design에 직접 썼다.
- [ ] 6-2 블록이 "Exceptionally refined top-tier Korean idol lead visual"부터 "average-looking or generic"까지 연속적이고 완전하다.
- [ ] 성인 남성은 MALE을, 성인 여성은 FEMALE을 연속적이고 완전하게 포함하며 둘 다 포함하지 않는다.
- [ ] FACE GEOMETRY가 10가지 항목을 모두 다루고, 모두 현재 캐릭터에 대한 긍정형 독립 묘사다.
- [ ] FACE GEOMETRY에 캐릭터 간 비교어나 미모 하향 금지 표현이 없고, `high nose bridge`, `compact facial thirds`, `delicate sculpted features` 같은 전역 기준점과 충돌하지 않는다.
- [ ] 머리, 체형, 의상이 과거 프리셋이 아닌 현재 캐릭터에서 나온다.
- [ ] 주인공이 6-11 구분 축에서 직전 5편의 주인공 각각과 최소 2개 축이 다르고, 표식 축이 하나 이상 있으며, 고른 축을 검수 결과에 적었다. (비교 문장은 이미지 프롬프트에 넣지 않는다.)
- [ ] 직업이 보이게 하는 세 가지(입은 것, 손이 도구를 쓰는 동작, 몸에 남은 흔적)가 프롬프트에 모두 있다.
- [ ] 구도(6-12)가 직전 5편과 프레임·앵글·시선·자세 중 2개 이상 다르고, 얼굴이 4분의 3 이상 보이며, 고른 축을 검수 결과에 적었다.
- [ ] 주인공의 얼굴 구조가 6-10 유저 공통 얼굴과 다르다. 주인공과 유저는 그림체(6-1·6-2 블록)는 같지만 얼굴은 다른 사람이어야 한다.
- [ ] 6-9 네거티브 블록이 완전히 포함되어 있고, 세 장 모두 맨 앞 세 항목이 `NO UNINTENTIONAL TEXT … EXCEPTION: …` 문장으로 바뀌어 있다.
- [ ] 세 장 모두 맨 끝에 6-13 하단 이름·생성일시 블록이 있고, 이름과 생성일시(`YYYY.MM.DD HH:MM`)가 채워져 있다. 유저용은 이름이 `이름(U, M)` / `이름(U, F)`다.
- [ ] 유저 대화 프로필용이 남성용·여성용 두 개이고, 각각 MALE/FEMALE 블록 원문과 6-10 얼굴 구조를 포함한다.
- [ ] 영문 프롬프트 바로 아래에 한글 설명이 한두 문장으로 붙어 있다.

## 8. 막힐 때 점검할 것

- 눈동자가 푸른색·청록색으로 나오면 `dark brown eyes`만으로는 부족하다. 눈 모양(쌍꺼풀 구조, 눈매 방향)을 FACE GEOMETRY에서 구체적으로 쓴다.
- 머리색을 `light brown`으로 쓰면 서구 이미지가 섞이기 쉽다. 검은빛 도는 갈색, 짙은 애쉬 브라운, 검은색 계열로 쓴다. 아이돌·예술 직업군의 염색·탈색은 예외인데, 그때도 6-11 "머리색 변주"대로 염색한 머리라는 구절(탈색·뿌리·컴백용)을 붙여 자연 머리색으로 읽히지 않게 한다.
- `shallow depth of field`, `85mm`, `film-like` 같은 화보 문구만 더하면 보정된 모델 컷이 된다. 소프트 포커스와 색 반응은 6-1 블록으로 통제한다.
- 번들거림이 남으면 6-1의 피부 단락과 6-9의 Skin 항목이 빠지지 않았는지 확인한다.
