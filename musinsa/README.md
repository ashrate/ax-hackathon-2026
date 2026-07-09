# 무신사 제출용 플러그인

> AX 인재전쟁 2026 예선 제출 후보: MUSINSA Trend & Brand Triage

## 심사자 5분 재현 가이드

① 복붙 입력 프롬프트:

```text
여성 컨템포러리에서 다음 주간 리뷰에 볼 브랜드/협업/입점 후보와
트렌드 신호를 공개 자료 기반 triage 산출물 폴더로 만들어줘.
```

② 예상 출력 폴더: `src/examples/여성-컨템포러리-2026-07-08/`

③ 먼저 볼 핵심 파일 3개(제출 zip 경로):

- `src/examples/여성-컨템포러리-2026-07-08/scout-report.md`
- `src/examples/여성-컨템포러리-2026-07-08/signals-log.csv`
- `src/examples/여성-컨템포러리-2026-07-08/scorecards/MATIN-KIM.md`

④ 실패 처리 예시: 무신사 랭킹·추천·상품 리스트처럼 동적 렌더링으로 본문 자동 확인이 어려운 URL은 핵심 근거로 단정하지 않고 `manual-check-required`로 남긴다.

⑤ 사람이 판단할 지점: MD가 산출물의 근거와 반대 근거를 보고 `신규 검토`, `협업/콘텐츠 확장`, `모니터링`, `제외` 중 최종 4분류 판정을 확정한다.

## 문제 문장

무신사 MD와 브랜드 스카우트가 MD 회의 전에 뉴스룸, 기사, 플랫폼 콘텐츠, 브랜드 공식 사이트, 공개 커뮤니티에 흩어진 브랜드/협업/입점 후보 공개 신호를 감사(audit)해야 하는 일을 Codex가 자동화한다. 결과는 `신규 검토`, `협업/콘텐츠 확장`, `모니터링`, `제외` 4분류 triage와 출처 URL, 확인일, 출처 강도, 반대 근거가 붙은 회의 전 감사 산출물이다.

출제 영상의 힌트인 "고객들이 좋아할 만한 브랜드를 어떻게 찾아낼까"와 "AI로 관심 가져야 할 트렌드를 어떻게 놓치지 않고 찾아낼까"는 여기서 "매주 놓치지 않고 공개 신호를 스크리닝하고 분류한다"로 좁혀 해석한다. 이미 무신사/29CM에 노출된 브랜드가 나오면 실패가 아니라, 신규 검토가 아닌 협업/콘텐츠 확장 후보로 정확히 분기한 결과다.

## 왜 이 문제, 왜 이 범위인가

출제 영상의 브랜드 발굴·트렌드 포착 힌트와 맞추려면 "새 브랜드를 맞힌다"가 아니라 MD가 매주 놓칠 수 있는 공개 신호를 회의 전에 정리하는 문제로 보는 편이 정확하다. 이 범위는 API 키, 크롤링 권한, 무신사 내부 매출·검색·CRM·파트너센터 데이터 없이 공개 자료와 제출 zip 안의 예시 파일만으로 재현된다. 신호 수집, 출처 검증, 반대 근거 병기, 구조화된 산출물 생성은 Codex가 강한 반복 작업이다. 그래서 이 플러그인은 소비자 추천이 아니라 `MD 회의 전 신호 감사 자동화`로 범위를 제한한다.

## 숫자로 본 예시 실행 1회

실측 기준은 `src/examples/여성-컨템포러리-2026-07-08/signals-log.csv`다. `source_url` 고유값 기준 공개 출처 23곳, `related_brand`에서 `category`를 제외한 브랜드 8개, 데이터 행 기준 신호 24건을 확인했다. 각 신호는 출처 URL·확인일을 같은 CSV 형식으로 남기고, 반대 근거와 4분류 판정은 `src/examples/여성-컨템포러리-2026-07-08/scout-report.md`와 `src/examples/여성-컨템포러리-2026-07-08/scorecards/ (브랜드별 8개 md)`에서 같은 후보 단위로 확인한다. **사람(MD)은 최종 화면 확인과 의사결정만 한다.**

## 공식 힌트 영상 근거

- YouTube: https://www.youtube.com/watch?v=OLAWeIuiD5Y
- 핵심 자막: "고객들이 좋아할 만한 브랜드들을 어떻게 찾아낼 수 있을까요?" "AI를 이용해서 무신사가 관심 있어야 할 만한 트렌드를 어떻게 놓치지 않고 찾아낼 수 있을까요?"
- 전체 자막은 제출 zip의 `src/docs/source-video.ko.vtt`에 포함한다.

## 입력 예시

```text
여성 컨템포러리에서 다음 주간 리뷰에 볼 브랜드/협업/입점 후보와
트렌드 신호를 공개 자료 기반 triage 산출물 폴더로 만들어줘.
```

선택 입력으로 카테고리, 고객군, seed brand, 공개 URL, 제외할 브랜드, 우선 평가 관점(입점, 협업, 라이브, 글로벌, 콘텐츠)을 줄 수 있다.

## 실행 결과

실제 예시는 `src/examples/여성-컨템포러리-2026-07-08/`에 있다.

- 공개 출처: 23곳(`signals-log.csv`의 `source_url` 고유값)
- 후보 브랜드: 8개
- 수집 신호: 24개
- triage 결과: `협업/콘텐츠 확장` 3개, `모니터링` 5개
- 생성 파일: `scout-report.md`, `signals-log.csv`, `watchlist.md`, `scorecards/` 브랜드별 md 8개

이 결과는 "신규 브랜드 8개를 찾았다"가 아니다. MATIN KIM, THE BARNNET, FOETO처럼 이미 공식 협업·노출·성과가 강한 브랜드는 신규 검토가 아니라 협업/콘텐츠 확장으로 분류했고, SIYAZU, LE17SEPTEMBRE, RECTO, TREEMINGBIRD, HAAG처럼 공개 고객 반응 또는 최근성 확인이 부족한 후보는 모니터링으로 낮췄다.

## 정보 부족/실패 시 동작

- curl 기준 403, 로그인 전용, 동적 렌더링으로 본문 확인이 어려운 URL은 핵심 근거에서 제외하거나 `manual-check-required`로 남긴다.
- 출처 강도 3 이하 보조 기사만 있는 주장은 `가설`로 낮추고 공식/플랫폼/브랜드 공식 출처를 추가 요구한다.
- 이미 무신사/29CM에 노출된 브랜드는 "신규 발굴"로 포장하지 않고 협업, 라이브, 단독 상품, 글로벌, 콘텐츠 확장 후보로 분기한다.
- 공개 고객 반응이 부족한 브랜드는 `모니터링`으로 두고 다음 확인 날짜와 필요한 화면 확인 항목을 남긴다.

## 사람이 최종 판단하는 지점

플러그인은 후보를 입점 확정이나 성과 예측으로 단정하지 않는다. MD가 최종 판단해야 하는 지점은 다음이다.

- 무신사/29CM 동적 화면의 랭킹, 리뷰, 좋아요, 품절, 가격대 확인
- 이미 노출된 브랜드의 다음 목적 선택: 단독 상품, 라이브, 글로벌, 콘텐츠, 제외
- 내부 매출, 검색량, CRM, 파트너센터 데이터와 공개 신호의 충돌 여부
- 브랜드 미팅, 공급 안정성, 반품/재고 리스크 같은 비공개 운영 판단

## 이번 실행 1회가 대체한 반복 확인

이번 예시 실행 1회는 `src/examples/여성-컨템포러리-2026-07-08/signals-log.csv`와 `src/examples/여성-컨템포러리-2026-07-08/scorecards/ (브랜드별 8개 md)` 기준으로 공개 출처 23곳을 탐색하고, 브랜드 8개와 신호 24건을 교차 확인하며, 각 판단에 출처 URL·확인일·출처 강도·반대 근거를 남겼다. 4분류 판정 초안은 `src/examples/여성-컨템포러리-2026-07-08/scout-report.md`, `src/examples/여성-컨템포러리-2026-07-08/signals-log.csv`, `src/examples/여성-컨템포러리-2026-07-08/watchlist.md`, `src/examples/여성-컨템포러리-2026-07-08/scorecards/ (브랜드별 8개 md)`로 제출 zip 안에서 검증할 수 있다. **사람(MD)은 최종 화면 확인과 의사결정만 한다.**

| 수동으로 하는 일 | 이번 예시에서 반복되는 확인 | 플러그인이 대신 산출하는 것 |
| --- | --- | --- |
| 후보별 공개 근거 모으기 | 공개 URL 23곳 확인 | `signals-log.csv` 24개 신호와 출처 강도 |
| 브랜드와 신호 교차 확인 | 브랜드 8개 × 신호 24건 연결 | 브랜드별 `scorecards/` 브랜드별 md 8개 |
| 이미 알려진 브랜드와 신규 검토 후보 구분 | 무신사/29CM 노출·협업 이력 확인 | 4분류 triage 상태와 반대 근거 |
| 브랜드별 고객 반응 확인 | 고객 반응, 플랫폼 큐레이션, 공개 성과 여부 확인 | `scorecards/*.md`의 고객 반응 신호와 `확인 필요` 표시 |
| 약한 출처 걸러내기 | 기사 403, 동적 페이지, 단일 보조 기사 여부 확인 | `가설`, `manual-check-required`, `모니터링` 처리 |
| 다음 회의 액션 정리 | 후보마다 MD/콘텐츠/스카우트 담당 액션 작성 | `scout-report.md`와 `watchlist.md`의 다음 액션 |

## 공개 근거

| 출처 URL | 발행 주체 | 확인일 | 입증하는 주장 |
| --- | --- | --- | --- |
| https://www.youtube.com/watch?v=OLAWeIuiD5Y | 프라이머/무신사 발표 영상 | 2026-07-08 | 무신사 트랙의 공식 힌트 영상 원본이다. |
| `src/docs/source-video.ko.vtt` | 프라이머/무신사 발표 영상 자막 사본 | 2026-07-08 | 무신사는 고객이 좋아할 브랜드와 관심 트렌드를 AI로 놓치지 않는 방법을 핵심 질문으로 제시한다. |
| https://newsroom.musinsa.com/newsroom-menu/2022-0216-01 | Musinsa Newsroom | 2026-07-08 | 무신사 MD 업무에는 신규 브랜드 발굴, 입점, 트렌드 상품 소싱이 포함된다. |
| https://www.musinsacareers.com/ko/o/213276 | Musinsa Careers | 2026-07-08 | 현행 MD 직무도 신규 브랜드 발굴, 고객 인사이트, 트렌드 상품 소싱을 요구한다. |
| https://newsroom.musinsa.com/newsroom-menu/2025-1119 | Musinsa Newsroom | 2026-07-08 | 무신사는 AI를 업무와 서비스 개발에 활용하고 패션 빅데이터 기반 트렌드 분석을 공개했다. |
| https://newsroom.musinsa.com/newsroom-menu/2026-0603 | Musinsa Newsroom | 2026-07-08 | 소비자용 AI 트렌드 큐레이션이 이미 있어, 이 플러그인은 MD용 근거 감사·후보 triage 워크플로우로 좁혀야 한다. |
| https://newsroom.musinsa.com/newsroom-menu/2025-0326-29cm | Musinsa Newsroom | 2026-07-08 | 29CM의 큐레이션과 스토리텔링이 신진 여성 브랜드 성장의 공개 사례가 된다. |

## 작동 방식

1. 사용자가 준 카테고리와 날짜로 출력 폴더를 먼저 정의한다.
2. 공개 자료에서 브랜드, 협업, 콘텐츠, 입점 후보 신호를 수집한다.
3. 각 신호에 URL, 확인일, 출처 강도, curl 접근 상태를 붙인다.
4. 브랜드별 supporting evidence와 opposing evidence를 같이 기록한다.
5. `신규 검토`, `협업/콘텐츠 확장`, `모니터링`, `제외` 중 하나로 triage한다.
6. 신호 부족 후보는 `watchlist.md`로 내리고, 출처 강도 3 이하 단독 근거는 `가설`로 표시한다.
7. 최종적으로 `signals-log.csv`, `scorecards/*.md`, `scout-report.md`, `watchlist.md`를 생성한다.

동적 페이지 처리:

- 무신사 랭킹, 아카이브, 추천, 상품 리스트처럼 동적 렌더링이 강한 페이지는 자동 추출 결과를 핵심 근거로 단정하지 않는다.
- 대신 사용자가 화면으로 랭킹 위치, 리뷰, 좋아요, 가격대, 품절 여부를 확인할 입력 후보로 안내하고 `manual-check-required`를 남긴다.

## 제출 zip 구조

제출 zip 안의 `src/`가 플러그인 루트다. 공개 검증에 필요한 예시 산출물과 핵심 문서는 `src/` 아래 사본으로 포함한다.

```text
submission.zip
  README.md
  src/.codex-plugin/plugin.json
  src/skills/main/SKILL.md
  src/references/evidence.md
  src/docs/submission-answers.md
  src/docs/research.md
  src/docs/verification.md
  src/docs/source-video.ko.vtt
  src/docs/output-spec.md
  src/examples/여성-컨템포러리-2026-07-08/scout-report.md
  src/examples/여성-컨템포러리-2026-07-08/signals-log.csv
  src/examples/여성-컨템포러리-2026-07-08/watchlist.md
  src/examples/여성-컨템포러리-2026-07-08/scorecards/ (브랜드별 8개 md)
```

Codex에서 `src/` 플러그인을 로드한 뒤 입력 예시처럼 호출한다.

## 검증 방법

제출 전 확인할 항목:

1. `src/.codex-plugin/plugin.json`이 validator를 통과한다.
2. `src/skills/main/SKILL.md`가 4분류 triage와 출력 계약을 종착점으로 삼는다.
3. 정상 입력 예시가 `src/examples/여성-컨템포러리-2026-07-08/`에 생성되어 있다.
4. `scout-report.md`, `signals-log.csv`, `watchlist.md`, `scorecards/*.md` 구조가 유지된다.
5. 신호 부족 후보와 출처 강도 3 이하 단독 근거가 `가설` 또는 `모니터링`으로 처리된다.
6. `src/docs/source-video.ko.vtt`와 `src/docs/output-spec.md`가 포함되어, 영상 힌트와 출력 계약을 zip 내부에서 확인할 수 있다.
7. `logs/`에는 AI와 나눈 전체 대화 로그 원본이 포함되어 있다.
