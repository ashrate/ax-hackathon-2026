# 무신사 제출용 플러그인

> AX 인재전쟁 2026 예선 제출 후보: MUSINSA Trend & Brand Scout

## 1. 플러그인 개요

이 플러그인은 무신사 MD, 브랜드 스카우트, 카테고리/뷰티, 마케팅·전략 담당자가 공개 자료에서 고객이 좋아할 브랜드와 놓치지 말아야 할 트렌드 신호를 반복 발굴하도록 돕는 Codex 플러그인입니다.

사용자는 주간 트렌드 리뷰나 신규 브랜드 검토를 준비할 때 무신사 랭킹, 뉴스룸, 앱 리뷰, 공개 커뮤니티, 검색 결과에 흩어진 신호를 모아야 하지만 출처 강도와 우선순위를 수동으로 판단하기 어렵습니다.

## 2. 공개 근거

| 출처 URL | 발행 주체 | 확인일 | 입증하는 주장 |
| --- | --- | --- | --- |
| `docs/source-video.ko.vtt` | 프라이머/무신사 발표 영상 자막 | 2026-07-08 | 무신사는 고객이 좋아할 브랜드와 관심 트렌드를 AI로 놓치지 않는 방법을 핵심 질문으로 제시한다. |
| https://newsroom.musinsa.com/newsroom-menu/2021-0930-03 | Musinsa Newsroom | 2026-07-08 | 무신사의 플랫폼 정체성과 브랜드 발견 맥락을 보강한다. |
| https://newsroom.musinsa.com/newsroom-menu/2026-0324 | Musinsa Newsroom | 2026-07-08 | AI 기반 대화형 패션 커머스와 추천 방향을 보여준다. |
| https://www.musinsa.com/main/musinsa/ranking | Musinsa | 2026-07-08 | 무신사 안에서 공개적으로 볼 수 있는 고객 관심 신호다. |
| https://www.musinsa.com/ranking/archive | Musinsa | 2026-07-08 | 기간별 랭킹 변화로 트렌드 이동을 관찰할 수 있다. |
| https://play.google.com/store/apps/details?hl=ko&id=com.musinsa.store | Google Play/Musinsa | 2026-07-08 | 개인화 추천, 트렌드 지표, 리뷰 등 고객 탐색 기능의 공개 설명이다. |

## 3. 작동 방식

입력:

- 카테고리, 고객군, 트렌드 질문, seed brand 중 하나 이상
- 선택 입력: 무신사 랭킹/아카이브, 뉴스룸, 앱 리뷰, 공개 커뮤니티, 검색 결과 URL

절차:

1. 입력 질문을 브랜드 발굴, 트렌드 감지, 카테고리 비교, 후보 모니터링으로 분류합니다.
2. 출처를 무신사 내부 공개 신호, 외부 시장 신호, 고객 반응, 보조 기사/검색으로 구분합니다.
3. 후보 브랜드나 트렌드마다 supporting evidence와 opposing evidence를 함께 남깁니다.
4. 출처 강도, 반복 관찰 가능성, 고객 반응 신호, 무신사 카테고리 적합성, 다음 액션 가능성을 점수화합니다.
5. 로그인 전용 자료, 출처 불명 자료, 단일 바이럴 노이즈는 `weak` 또는 `unavailable`로 표시합니다.
6. 결과는 입점 추천이 아니라 사람이 검토할 후보 가설로 표현합니다.

출력:

- 트렌드 신호 ledger
- 브랜드 후보 scorecard
- 지지 근거와 반대 근거
- 확인일과 출처 강도
- 다음 액션과 모니터링 쿼리

## 4. 폴백과 제한

- 무신사 내부 매출, 검색, CRM, 파트너 데이터 접근을 전제하지 않습니다.
- 공개 출처가 한 곳뿐이면 후보를 확정하지 않고 `weak`로 표시합니다.
- 로그인 전용 SNS나 비공개 자료는 핵심 근거에서 제외합니다.
- 브랜드 후보를 객관적 정답이나 입점 추천으로 단정하지 않습니다.

## 5. 설치·실행 방법

```bash
python tools/make_submission.py musinsa
```

생성된 `dist/musinsa/submission.zip` 안의 `src/`가 플러그인 루트입니다. Codex에서 플러그인을 로드한 뒤 다음처럼 호출합니다.

```text
여성 캐주얼과 뷰티 카테고리에서 무신사가 다음 주간 리뷰에 볼 브랜드 후보와 트렌드 신호를 공개 자료 기반 scorecard로 정리해줘.
```

## 6. 검증 방법

제출 전 확인할 항목:

1. `src/.codex-plugin/plugin.json`이 validator를 통과한다.
2. `src/skills/main/SKILL.md`가 브랜드/트렌드 발굴 절차를 담고 있다.
3. `src/references/evidence.md`에 공개 근거와 금지 주장이 정리되어 있다.
4. 정상 입력으로 카테고리와 공개 URL을 넣으면 후보 scorecard와 supporting/opposing evidence가 나온다.
5. 예외 입력으로 단일 커뮤니티 글이나 로그인 전용 링크를 넣으면 `weak` 또는 `unavailable`로 표시한다.
6. `logs/`에는 AI와 나눈 전체 대화 로그 원본이 포함되어 있다.
