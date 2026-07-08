# Musinsa Evidence Map

> 공식 힌트 영상 원본: https://www.youtube.com/watch?v=OLAWeIuiD5Y (자막 사본: `docs/source-video.ko.vtt`, 확인일 2026-07-08) — 자막 5등급 근거의 역추적 경로.

## Selected Problem

`MUSINSA Trend & Brand Triage`는 무신사 MD, 브랜드 스카우트, 카테고리/뷰티 담당자, 마케팅·전략 담당자가 공개 자료에 흩어진 브랜드/협업/입점 후보 신호를 매주 스크리닝해 `신규 검토`, `협업/콘텐츠 확장`, `모니터링`, `제외`로 분류하도록 돕는 Codex 플러그인이다.

## Source Weight Scale

| 등급 | 의미 | 사용 규칙 |
| --- | --- | --- |
| 5 | 공식 영상 자막 | 출제 의도와 문제 선정의 최상위 근거다. |
| 4 | 회사 공식 사이트, 뉴스룸, 채용공고, 파트너 문서, 공식 서비스 페이지 | 핵심 주장 근거로 사용할 수 있다. |
| 3 | 기사, 앱마켓 리뷰, 공개 커뮤니티 | 보조 근거로만 사용한다. 핵심 근거는 4~5등급으로 보강한다. |
| 2 | 검색 결과 스니펫, 블로그, 2차 요약 | 후보 탐색용이다. 핵심 근거로 쓰지 않는다. |
| 1 | AI 요약, NotebookLM 답변 | 구조화 보조용이다. 원문으로 역추적되지 않으면 폐기한다. |

## Audited Core Claims

확인일은 모두 2026-07-08이다.

| 핵심 주장 | 등급 | 출처 URL/파일 | 확인일 | 수집 방법 | 판단 |
| --- | --- | --- | --- | --- | --- |
| 출제 영상은 브랜드 발굴과 트렌드 포착을 무신사의 본질 질문으로 제시한다. | 5 | `docs/source-video.ko.vtt` | 2026-07-08 | 로컬 `grep`/`sed`로 00:01:35~00:01:59 구간 확인 | 유지. 최종 문제 선정의 최상위 근거다. |
| 무신사 MD 업무에는 신규 브랜드 발굴, 입점, 트렌드 상품 소싱이 포함된다. | 4 | https://newsroom.musinsa.com/newsroom-menu/2022-0216-01 | 2026-07-08 | 웹 검색 후 본문 접속 | 보강. “MD/스카우트 업무가 실재한다”는 주장의 핵심 근거다. |
| 현행 MD 채용공고도 신규 브랜드 발굴, 고객 인사이트 기반 브랜드 성장/발굴, 트렌드 상품 소싱을 요구한다. | 4 | https://www.musinsacareers.com/ko/o/213276 | 2026-07-08 | 웹 검색 후 본문 접속 | 보강. 2026년 현재 채용 중인 직무기술 근거로 사용한다. |
| 무신사 MD는 브랜드와 고객을 연결하고 매 순간 트렌드를 살피는 역할이다. | 4 | https://newsroom.musinsa.com/newsroom-menu/2022-0216-md-10 | 2026-07-08 | 웹 검색 후 본문 접속 | 보강. 직무의 반복 리서치 성격을 뒷받침한다. |
| 무신사의 사업 구조에는 브랜드 소싱, 국내외 감각적 브랜드 연결, 브랜드 취향 콘텐츠 소개가 포함된다. | 4 | https://corp.musinsa.com/ko/business | 2026-07-08 | 웹 접속 | 보강. 브랜드 발굴이 회사 사업 범위와 맞는다는 근거다. |
| 29CM는 신진 브랜드 발굴에 적극적이고, MD와 에디터가 유망 브랜드를 엄선해 소개한다. | 4 | https://newsroom.musinsa.com/newsroom-menu/2022-0223-03 | 2026-07-08 | 웹 검색 후 본문 접속 | 보강. 무신사 그룹 내 브랜드 발굴·콘텐츠화 사례다. |
| 무신사는 이미 업무와 서비스 개발에 AI를 활용하고 패션 빅데이터 기반 트렌드 분석을 공개했다. | 4 | https://newsroom.musinsa.com/newsroom-menu/2025-1119 | 2026-07-08 | 웹 검색 후 본문 접속 | 유지. 플러그인의 AI 방향성과 맞지만 “이미 일부 자동화 중”이라는 반증 검토에도 사용한다. |
| 무신사는 소비자용 AI 트렌드 큐레이션을 공개했다. | 4 | https://newsroom.musinsa.com/newsroom-menu/2026-0603 | 2026-07-08 | 웹 검색 후 본문 접속 | 신규 반증 근거. 플러그인은 소비자 상품 추천이 아니라 MD용 근거 감사 워크플로우로 제한한다. |
| 무신사 ChatGPT/Kakao 서비스는 소비자에게 상품·스타일을 추천하는 방향이다. | 4 | https://newsroom.musinsa.com/newsroom-menu/2026-0324, https://newsroom.musinsa.com/newsroom-menu/2026-0609-01 | 2026-07-08 | 웹 검색 후 본문 접속 | 반증 보강. 기존 소비자 추천과 제출 플러그인의 차별 범위를 명시한다. |
| 무신사 랭킹·월간 랭킹·추천 페이지는 공개 신호 수집 대상이 될 수 있다. | 4(부분) | https://www.musinsa.com/main/musinsa/ranking, https://www.musinsa.com/ranking/archive, https://www.musinsa.com/main/musinsa/recommend?gf=F | 2026-07-08 | `curl` HTTP 200 확인, 웹 검색 스니펫 확인, `web.open` 제목 확인 | 유지하되 핵심 주장 근거는 아님. 동적 페이지라 본문 추출이 제한되어 실행 입력 후보로만 둔다. |
| 29CM 파트너 문서는 신규 입점 브랜드를 소개하는 수요입점회/일요입점회와 상품 등록·승인 절차를 공개한다. | 4 | https://partner-stage.one.musinsa.com/posts/basic-strategy/36 | 2026-07-08 | 웹 본문 접속 | 보조 보강. 발굴 이후 입점/노출 검토 게이트 근거로만 사용한다. |

## Downgraded Or Discarded Evidence

| 근거 | 처리 | 이유 |
| --- | --- | --- |
| App Store/Google Play 리뷰 | 보조 3등급으로 강등 | 고객 불만·앱 포지셔닝 보조에는 유효하지만 MD/브랜드 발굴 문제의 핵심 근거가 아니다. |
| Reddit/Blind 공개 글 | 보조 3등급 이하로 격리 | 글로벌 CS·배송 후보 검토에는 도움되지만 최종 문제의 핵심 근거로 쓰지 않는다. |
| `www.musinsacareers.com/ko/o/219295`, `/225987`, `/217964` 등 일부 채용공고 검색 결과 | 핵심 근거에서 제외 | 검색 결과에는 유용한 문구가 보였으나 이번 접속에서 안정적으로 본문을 확보하지 못했다. 접근 안정성이 확인된 `/ko/o/213276`과 뉴스룸 MD 채용 기사로 대체했다. |
| NotebookLM/AI 요약 | 폐기 또는 구조화 보조만 허용 | 원문 URL이나 자막으로 역추적되지 않으면 제출 근거로 쓰지 않는다. |

## Plugin Scope

Inputs:

- 카테고리, 고객군, 트렌드 질문, seed brand
- 선택 입력: 무신사 랭킹·월간 랭킹·추천, 뉴스룸, 파트너 문서, 앱 리뷰, 공개 커뮤니티, 검색 결과 URL

Outputs:

- `output/<category-slug>-<YYYY-MM-DD>/scout-report.md`
- `output/<category-slug>-<YYYY-MM-DD>/scorecards/<brand>.md`
- `output/<category-slug>-<YYYY-MM-DD>/signals-log.csv`
- `output/<category-slug>-<YYYY-MM-DD>/watchlist.md`

Output contract rules:

- `scout-report.md`에는 후보 브랜드 5~10개 요약표와 이번 주 트렌드 신호 3~5개가 있어야 한다.
- `scorecards/<brand>.md`에는 개요, 신호와 근거, 고객 반응 신호, 리스크/반대 근거, 입점 적합성, 다음 액션이 있어야 한다.
- `signals-log.csv` 헤더는 `date,signal,source_url,source_strength,related_brand,note` 순서를 지킨다.
- `watchlist.md`에는 모니터링/제외 후보, 이유, 필요한 추가 근거, 다음 확인 시점을 남긴다.
- 출처 강도 3 이하 단독 근거는 `가설`로 표시한다.
- 동적 페이지는 `manual-check-required`로 두고 사용자가 화면으로 확인할 입력 후보로 안내한다.

## Example Run Evidence Scope

2026-07-08 실제 예시 실행:

- 카테고리: 여성 컨템포러리
- 산출물 경로: `examples/여성-컨템포러리-2026-07-08/`
- 후보 브랜드 수: 8개
- 신호 수: 24개
- 후보 브랜드: MATIN KIM, THE BARNNET, FOETO, SIYAZU, LE17SEPTEMBRE, RECTO, TREEMINGBIRD, HAAG
- triage 결과: `협업/콘텐츠 확장` 3개, `모니터링` 5개

예시 실행에서 사용한 주요 공개 근거:

| 주장 | 등급 | 출처 URL | 확인일 | 판단 |
| --- | --- | --- | --- | --- |
| MATIN KIM은 무신사와 일본 총판 파트너십 및 오프라인 성과가 공개되어 있다. | 4 | https://newsroom.musinsa.com/newsroom-menu/2024-1112, https://newsroom.musinsa.com/newsroom-menu/2025-0428 | 2026-07-08 | 신규 입점보다 글로벌/콘텐츠 확장 사례로 사용한다. |
| 29CM는 신진 여성 디자이너 브랜드의 성장과 FOETO 성과를 공식 뉴스룸에 공개했다. | 4 | https://newsroom.musinsa.com/newsroom-menu/2025-0326-29cm | 2026-07-08 | 수요입점회/스토리텔링 기반 검증 모델 근거로 사용한다. |
| THE BARNNET은 공식 Summer 2026 전개, 29CM 단독 콘텐츠, 29LIVE 편성이 확인된다. | 3/4 | https://the-barnnet.com/, https://www.29cm.co.kr/content/29edition/2026/02/thebarnnet, https://content.29cm.co.kr/29live/2025/11/thebarnnet, https://www.ktnews.com/news/articleView.html?idxno=142676 | 2026-07-08 | 협업/콘텐츠 확장 후보로 사용한다. |
| SIYAZU는 공식 사이트와 29CM 브랜드 페이지에서 미니멀 여성복 포지션이 확인된다. | 4 | https://en.siyazu.co.kr/, https://shop.29cm.co.kr/brand/10005 | 2026-07-08 | 고객 반응 수치 부족으로 모니터링에 둔다. |
| LE17SEPTEMBRE는 공식 브랜드 페이지, 공식 컬렉션 페이지, 29CM 단독 콘텐츠가 확인된다. | 4 | https://le17septembre.com/about.html, https://en.le17septembre.com/, https://content.29cm.co.kr/brand-event/2026/06/01/2nd | 2026-07-08 | 정량 반응 확인 전까지 모니터링에 둔다. |
| RECTO는 공식 브랜드 철학과 2026 SS 보조 기사 신호가 있다. | 3/4 | https://recto.co/about.html, https://www.ktnews.com/news/articleView.html?idxno=144475 | 2026-07-08 | 고객 반응 부족으로 가설/모니터링에 둔다. |
| TREEMINGBIRD는 29CM/무신사 브랜드 페이지와 접근 가능한 보조 기사상 반응 신호가 있다. | 3/4 | https://shop.29cm.co.kr/brand/40284, https://www.musinsa.com/brand/treemingbird/contents, https://www.fi.co.kr/main/view.asp?idx=82565 | 2026-07-08 | 보조 기사 수치의 공식 재확인이 필요해 모니터링에 둔다. |
| HAAG는 29CM 브랜드 페이지와 여름 콘텐츠가 확인된다. | 4 | https://shop.29cm.co.kr/brand/19972, https://www.29cm.co.kr/content/special/2026/06/haag | 2026-07-08 | 고객 반응 수치 부족으로 모니터링에 둔다. |

## Judgment Rules

- 영상 자막 5등급 근거가 일반 커머스 운영 문제보다 우선한다.
- 핵심 근거는 4~5등급이어야 한다. 3등급 이하는 보조 신호로만 둔다.
- `already visible in Musinsa` 신호와 `external emerging` 신호를 분리한다. 이미 노출된 브랜드는 신규 발굴이 아니라 `협업/콘텐츠 확장`으로 분기한다.
- 후보 브랜드는 입점 추천이 아니라 사람이 검토할 리서치 가설이다.
- 소비자용 AI 추천·트렌드 큐레이션과 중복되지 않도록, 결과물은 MD용 출처 감사·반대 근거·다음 액션 스코어카드로 제한한다.
- 동적 페이지, 로그인 전용, 출처 불명, 단일 바이럴 노이즈는 unavailable 또는 weak로 기록하고 핵심 근거에서 제외한다.

## Do Not Claim

- 무신사 내부 매출, 검색, CRM, 파트너 데이터에 접근한다고 말하지 않는다.
- 브랜드를 객관적으로 “최고”라고 순위화하지 않는다.
- 비공개 SNS 계정이나 로그인 전용 페이지를 수집한다고 말하지 않는다.
- 공개 반증 없이 유행 예측을 확정하지 않는다.
