# 제타 이미지 프롬프트 제작 규칙

주인공 프로필 이미지를 만들 때 쓰는 규칙. 특정 인물을 복제하지 않고 "K-드라마 아이돌급 실사 미감"과 "미모 하한선"을 모든 캐릭터에 공통으로 고정하고, 얼굴 구조·머리·체형·의상만 캐릭터마다 바꾼다.

> 한글 설명은 이해를 돕기 위한 것이다. "원문 그대로" 표시가 붙은 영어 블록은 실제 프롬프트에 **영어 원문 그대로** 넣는다. 번역·압축·요약·의역하지 않는다.

## 0. 제타 작업에서의 적용 범위

- 주인공 프로필용 프롬프트: 아래 2~9번 규칙 전체를 적용한다. 캐릭터 시트가 아니라 프로필 한 장이 필요하면 7번(레이아웃 블록)은 쓰지 않고 `upper body portrait` 한 줄로 대신한다. 시트가 필요하면 7번을 쓴다.
- 유저 대화 프로필용 프롬프트: 성별이 드러나지 않는 뒷모습·옆모습이므로 미모 블록과 성별 블록(2~4번)은 쓰지 않는다. 기존 형식(`gender-neutral`, `face not shown`)을 유지한다.
- 각 영문 프롬프트 바로 아래에 한글 설명을 한두 문장으로 덧붙인다. (코드블록 밖)
- 이전 방식(`Korean webtoon style, semi-realistic manhwa illustration ...`)은 만화풍을 원할 때만 쓴다.

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
- 직업과 설정은 사용자 입력을 따르고, 입력이 너무 모호할 때만 짧은 선택지 3개를 제안한다.
- 여러 캐릭터는 최소 두 가지 대비점(지위/권력, 실루엣/체격, 겉 태도와 속마음, 행동 속도, 감정 표현 방식)을 가진다. 차이는 헤어스타일, 옆모습, 키/체격, 옷, 색상 팔레트로 바로 알아볼 수 있어야 한다.
- 미감을 떨어뜨리거나 메이크업 품질을 낮추거나 "평범한" 엑스트라를 쓰는 방식으로 대비를 만들지 않는다. 같은 기본 얼굴에 머리색이나 옷만 바꾸는 방식도 쓰지 않는다.
- 남성성(강인함, 위험함, 다정함, 젊음)은 거칠어진 이목구비가 아니라 골격, 시선, 눈썹 표정, 연기에서 나온다. 여성성은 과장된 "인플루언서 스타일" 이목구비가 아니라 비율, 눈 모양, 입술 모양, 메이크업, 얼굴 긴장도에서 나온다.

## 4. 이미지 생성 워크플로

- 캐릭터 콘셉트 아트와 장면 설정에는 GPT Image 2를 쓴다. 안정된 에셋이 없으면 먼저 TextToImage로 후보를 만들고, 캐릭터·장면·스타일 레퍼런스가 있으면 ImageToImage를 우선한다. (정체성과 공간 일관성 유지)
- 제작 전에는 주연별 콘셉트 아트, 주요 장면별 설정 또는 공간 레퍼런스, 연속성 기록만 만든다. 스토리보드, 키 프레임, 시작/끝 프레임은 만들지 않는다.
- 캐릭터 콘셉트 시트에는 인물 사진, 정면, 3/4 측면, 좌우 측면, 전신, 뒷모습, 눈 디테일, 입술 디테일, 표정 3종이 들어가며, 모든 칸이 같은 얼굴·머리·체형·옷·나이를 유지한다. 각 캐릭터는 별도의 key_element로 등록하고 합치지 않는다.
- 미감 품질이 떨어지면 캐릭터나 장면 생성 단계로 되돌아간다. 영상 모델로 부족한 비주얼을 덮지 않는다. 정체성이 흔들리면 기준점과 레퍼런스 연결을 강화하고 오류를 다음 단계로 넘기지 않는다.

## 5. 프롬프트 구성 순서 (엄격히 지킨다)

1. GLOBAL K-DRAMA IDOL LOOK BLOCK (원문 그대로)
2. GLOBAL IDOL FACIAL BEAUTY FLOOR (원문 그대로)
3. GENDER BEAUTY AMPLIFIER 하나 (원문 그대로)
4. 현재 캐릭터의 독립적인 FACE GEOMETRY BLOCK
5. ARCHETYPE ADAPTER 또는 커스텀 성격 디자인
6. HAIR / BODY / WARDROBE VARIABLES
7. GLOBAL CHARACTER SHEET LAYOUT BLOCK (원문 그대로, 시트일 때만)
8. LIGHTING MODE 하나
9. GLOBAL NEGATIVE BLOCK (원문 그대로)

블록을 더 짧은 프롬프트로 요약하지 않는다. GLOBAL LOOK, GLOBAL BEAUTY FLOOR, 선택한 GENDER AMPLIFIER, GLOBAL NEGATIVE는 최종 출력에 끊김 없이 완전한 텍스트로 들어가야 한다. 레퍼런스 이미지는 정체성만 고정하며 전역 스타일 용어를 대체할 수 없다.

## 6. 블록 원문

### 6-1. GLOBAL K-DRAMA IDOL LOOK BLOCK (모든 캐릭터, 원문 그대로)

한글 설명: 한국 실사 숏드라마용 세로 캐릭터 시트, 초실사 2K, 일러스트 아님. 아이돌급 입체 골격과 정제된 얼굴 면, 높고 곧은 콧대, 또렷한 쌍꺼풀. 젊고 생기 있는 아이돌 에너지. 하얗고 고른 쿨톤 백자 피부에 가벼운 소프트터치 보정(모공 질감은 유지, 물광·유분·글래스 스킨 없음). 또렷한 K-아이돌 그루밍과 눈 화장. 모든 인물 칸에 시네마틱 소프트 포커스. 저채도, 저~중간 대비, 부드러운 하이라이트, 은은한 필름 그레인.

```text
Vertical character design sheet for a Korean live-action short drama, hyper-realistic 2K, not illustration. Premium live-action K-drama character photography with idol-grade visual impact. Highly sculpted three-dimensional bone structure, refined and elegant facial planes, clean and defined jawline, noticeably high and straight nose bridge, deep naturally defined double eyelids, precise and harmonious facial geometry.

Young Korean idol energy: a lively, polished, camera-ready face. Never childish, never ordinary, never a generic passerby.

Skin: extremely fair, bright, luminous and even in tone. Softly glowing cool-toned porcelain skin. Zero dullness, zero yellowing, zero redness. Zero shadow pooling on any part of the face.

Moderate retouching: light skin smoothing with a cinematic glamour soft-touch finish. Visibly smoother than raw skin, while keeping real pore texture, fine skin grain and natural surface detail. Not plastic, not waxy, not erased. The glow comes from even skin-tone brightness and fairness. No oiliness, no dewy wet look, no glass-skin sheen, no concentrated specular highlights.

Makeup: clearly groomed K-idol finish. Cleanly shaped, full, tidy eyebrows. Defined eye makeup with soft eyeliner following the upper lash line and a subtle lower lash line. Enhanced eye contour depth, naturally tidy lashes. A more visible tinted lip color with a clean, non-wet finish. A brightening skin-tint finish. Visibly more refined than minimal natural grooming, but not heavy influencer makeup or stage makeup.

Cinematic soft focus on every portrait panel: soft lens diffusion, film-like bokeh glow on subject edges, gentle halation. Optical glamour softness that protects facial structure, fine skin detail and eye clarity. Not blurry or out of focus, but the controlled soft-focus quality seen in high-end Korean drama cinematography.

Color response: clean Korean drama cinematic texture, low saturation, low-to-medium contrast, luminous skin separation, soft highlight roll-off, soft shadow detail, subtle film grain. No harsh digital sharpening, no cheap short-drama filter.
```

### 6-2. GLOBAL IDOL FACIAL BEAUTY FLOOR (모든 캐릭터, 원문 그대로)

6-1 바로 뒤에 놓는다. 한글 설명: 최상급 한국 아이돌 주연 비주얼. 작은 얼굴, 조화로운 얼굴 3등분, 짧은 인중, 탄탄한 하안부, 좁고 높은 콧대, 선명한 눈꼬리, 다듬어진 입술 윤곽. 이목구비 배치는 정밀하고 균형 잡혔으며 거칠거나 평범하지 않다.

```text
Exceptionally refined top-tier Korean idol lead visual. Small face with compact, harmonious facial thirds, restrained near-symmetry, narrow and clean face width, dimensional yet delicate midface structure, short and tidy philtrum, a compact lower face that tapers cleanly, a precise narrow high nose bridge, a refined narrow nasal base with delicate nostrils, long clean eye shapes with defined inner and outer corners, a clean under-eye plane, and a tidy lip contour.

Feature placement is exceptionally precise, balanced and camera-perfect. Every feature stays delicate, sculpted and high-definition. Never coarse, bulky, plain, average-looking or generic.
```

이 미모 하한선은 정교함과 비율의 품질만 규정한다. 구체적인 얼굴형, 눈 모양, 눈썹 모양, 입술 모양, 성격은 고정하지 않는다. 모든 캐릭터 차별화는 이 범위 안에서 이루어진다.

### 6-3. GENDER BEAUTY AMPLIFIER (정확히 하나만, 원문 그대로)

성인 남성은 MALE을, 성인 여성은 FEMALE을 고른다. 둘을 같이 쓰지 않고 "male/female beauty" 같은 한 구절로 줄이지 않는다.

**MALE K-IDOL BEAUTY AMPLIFIER**

한글 설명: 최상급 한국 남성 아이돌 겸 주연 배우급 얼굴 정교함. 어깨 대비 작은 머리, 깔끔한 이마-눈썹 연결, 길고 정밀한 눈선, 좁고 높은 코, 오밀조밀한 입-턱, 교근 볼륨 없이 갸름해지는 남성적 턱. 남성미는 뼈의 긴장감, 시선, 자세, 어깨선에서 나온다.

```text
For adult male characters: exceptionally beautiful, top-tier Korean male idol and lead-actor level facial refinement. The freshness of a young adult, a small head in proportion to the shoulders, a clean forehead-to-brow connection, an elegant brow-to-eye relationship, long and precise eye lines, a tall, narrow, refined nose, a compact mouth-and-chin area, and a masculine jaw that tapers cleanly without large masseter volume.

Masculinity comes from bone tension, gaze, posture and shoulder line. It does not come from coarse features, a heavy lower face, or a loss of facial harmony.
```

**FEMALE K-DRAMA LEAD BEAUTY AMPLIFIER**

한글 설명: 최상급 한국 아이돌 여배우 겸 주연급 얼굴 정교함. 작고 우아한 얼굴, 깔끔한 이마-눈썹 연결, 아몬드형·여우형·부드러운 고양이형 눈매, 섬세하고 높고 좁은 코, 오밀조밀한 하안부, 깔끔한 입술 윤곽, 계란형·하트형·부드러운 V라인 턱. 여성미는 정밀한 비율, 절제된 표정, K-드라마 메이크업에서 나온다.

```text
For adult female characters: exceptionally beautiful, top-tier Korean idol-actress and female-lead level facial refinement. A small, elegant face, a clean forehead-to-brow connection, long luminous almond, fox or soft cat-shaped eyes with defined outer corners, a delicate, high, narrow nose, a compact refined lower face, a sculpted clean lip contour, and an elegantly tapering oval, heart-shaped or soft V-line jaw.

Femininity comes from precise proportion, restrained expression and polished K-drama makeup. It does not come from influencer-style feature enlargement, an overfilled face, or generic AI-beauty symmetry.
```

### 6-4. FACE GEOMETRY BLOCK (캐릭터마다, 독립적이고 긍정형)

각 캐릭터마다 현재 캐릭터만 묘사하는 영어 긍정형 문장으로 다음 10가지를 모두 쓴다.

1. 얼굴 가로세로 비율
2. 턱 각도
3. 광대 위치
4. 눈 길이와 방향
5. 쌍꺼풀 구조
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

- 머리색과 스타일
- 키, 어깨너비, 근육량, 머리-몸 비율, 자세
- 직업, 사회적 지위, 생활 방식
- 의상 스타일, 색, 레이어링, 소재, 신발, 액세서리, 노출 수준
- 캐릭터 고유 표정과 소품

의상의 공통 품질 요건 (원문 그대로):

```text
Premium contemporary Korean drama costume styling, intentional silhouette, refined fit, believable high-quality fabrics, clean structure, role-appropriate layering and a restrained color palette. The costume must express the character's identity and situation without lowering idol-grade visual polish.
```

사용자가 의상을 명시하면 그대로 따르고, 아니면 캐릭터 정체성에 따라 디자인한다. 과거 의상(검은 오버코트, 터틀넥, 크림 니트, 회색 라운지웨어, 흰 수건 등)을 기본값으로 쓰지 않는다.

### 6-7. GLOBAL CHARACTER SHEET LAYOUT BLOCK (시트일 때만, 원문 그대로)

한글 설명: 3:4 세로 캐릭터 디자인 시트 한 장. 모든 칸은 같은 얼굴·헤어·나이·체격·의상. 큰 대표 인물 사진이 위쪽 절반을 차지한다.

```text
Layout: one 3:4 vertical character design sheet, not a 16:9 landscape grid. Every panel shows exactly the same face, hairstyle, adult age, build and the outfit chosen for the current character.

Include:
1. one large 3/4-angle signature emotional portrait with high detail and cinematic soft-focus bokeh glow
2. front half-body
3. 3/4 side half-body
4. full-body front standing view
5. left profile
6. right profile
7. full-body back view
8. eye detail close-up
9. lip detail close-up
10. three restrained emotion samples

The large signature portrait must occupy the upper half. Keep the full-body and detail panels clean, balanced and easy to read.
```

사용자가 명시적으로 가로를 요청할 때만 비율을 바꾼다.

### 6-8. LIGHTING MODES (하나 선택)

조명 모드는 환경과 분위기만 바꾸고 피부, 메이크업, 얼굴 정교함은 바꾸지 않는다.

**쿨 뉴트럴 스튜디오 (Cool-neutral studio)**

```text
A neutral cool-gray photo studio or a minimal clean interior. Softly diffused frontal key light with gently sculpting side shadows, shallow depth of field, cool-neutral low saturation and low-to-medium contrast. Skin stays a luminous cool white with no dull patches.
```

**웜 화이트 아파트 (Warm-white apartment)**

```text
A softly blurred minimal interior in warm white and beige. Softly diffused frontal key light, gently sculpted side shadows, shallow depth of field, low saturation and low-to-medium contrast. The environment may be warm beige, but the skin must stay cool porcelain white and never turn warm yellow.
```

**균형 잡힌 고급 실내 (Balanced upscale interior)**

```text
A premium neutral Korean interior with warm room lighting and controlled cool shadow fill. Soft frontal key, restrained halation, low saturation and low-to-medium contrast. No harsh orange-teal split.
```

### 6-9. GLOBAL NEGATIVE BLOCK (모든 캐릭터, 원문 그대로)

특정 의상, 머리색, 체형을 금지하는 블록이 아니다. 같은 시트 안의 변화와, 다른 캐릭터 간 같은 얼굴 재사용만 금지한다.

```text
Avoid:
- On-screen elements: no text, no watermark, no UI overlay.
- Identity: no different identity per panel, no reuse of the same face across different characters, no merged identities.
- Skin: no plastic high-gloss skin, no over-smoothed waxy skin, no dewy glass-skin sheen, no oily shine or highlight pooling, no wet-looking skin surface, no dull or yellowish patches anywhere on the face.
- Casting feel: no generic passerby features, no cheap short-drama casting, no generic actor-casting face, no ordinary advertising-model face.
- Expression: no exaggerated expressions, no shouting, no wide-open mouth, no tired hollow eyes.
- Variation within a sheet: no unintended hair color change, no outfit change within the same sheet, no body type change within the same sheet, no age change.
- Focus: no blurry or unsharp panels outside the intended controlled soft focus, no heavy blur that erases skin texture detail.
- Makeup: no heavy influencer makeup or stage makeup.
- Features: no long midface, no long philtrum, no wide nasal base, no bulbous or round nose tip, no wide heavy jaw, no large masseters, no protruding ears, no coarse brow bone, no recessed temple hairline, no coarse or bulky features.
- Anatomy: no wrong number of limbs.
```

## 7. GLOBAL LITERAL GATE (생성 전 필수 검사)

이미지 도구를 호출하기 전에 아래를 모두 확인한다. 하나라도 실패하면 프롬프트를 다시 만든다.

- [ ] 6-1 블록이 첫 단어부터 Color response 마지막 문장까지 누락·번역·축약·동의어 없이 연속적이고 완전하다.
- [ ] 6-2 블록이 "Exceptionally refined top-tier Korean idol lead visual"부터 "average-looking or generic"까지 연속적이고 완전하다.
- [ ] 성인 남성은 MALE을, 성인 여성은 FEMALE을 연속적이고 완전하게 포함하며 둘 다 포함하지 않는다.
- [ ] FACE GEOMETRY가 10가지 항목을 모두 다루고, 모두 현재 캐릭터에 대한 긍정형 독립 묘사다.
- [ ] FACE GEOMETRY에 캐릭터 간 비교어나 미모 하향 금지 표현이 없고, `high nose bridge`, `compact facial thirds`, `delicate sculpted features` 같은 전역 기준점과 충돌하지 않는다.
- [ ] 머리, 체형, 의상이 과거 프리셋이 아닌 현재 캐릭터에서 나온다.
- [ ] 여러 캐릭터를 만들었다면 얼굴 다양성 매트릭스가 최소 4개 항목에서 다르다. (매트릭스의 비교 문장은 이미지 프롬프트에 넣지 않는다.)
- [ ] 시트를 만든다면 6-7 레이아웃 블록과 6-9 네거티브 블록이 완전히 포함되어 있다. (프로필 한 장이라도 6-9는 포함한다.)
- [ ] 영문 프롬프트 바로 아래에 한글 설명이 한두 문장으로 붙어 있다.

## 8. 막힐 때 점검할 것

- 눈동자가 푸른색·청록색으로 나오면 `dark brown eyes`만으로는 부족하다. 눈 모양(쌍꺼풀 구조, 눈매 방향)을 FACE GEOMETRY에서 구체적으로 쓴다.
- 머리색을 `light brown`으로 쓰면 서구 이미지가 섞이기 쉽다. 검은빛 도는 갈색이나 검은색 계열로 쓴다.
- `shallow depth of field`, `85mm`, `film-like` 같은 화보 문구만 더하면 보정된 모델 컷이 된다. 소프트 포커스와 색 반응은 6-1 블록으로 통제한다.
- 번들거림이 남으면 6-1의 피부 단락과 6-9의 Skin 항목이 빠지지 않았는지 확인한다.
