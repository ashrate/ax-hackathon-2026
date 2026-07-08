# 무신사 — 검증 기록

> 이 파일은 submission.zip에는 포함되지 않는 작업 기록이며, 문항 ⑤와 README.md 작성의 원천 자료다.

## 1. 테스트 시나리오

| 입력 | 기대 결과 | 실제 결과 | 판정 | 날짜 |
| --- | --- | --- | --- | --- |
| “여성 컨템포러리에서 다음 주간 리뷰에 볼 브랜드 후보와 트렌드 신호를 공개 자료 기반 산출물 폴더로 만들어줘” | `scout-report.md`, `signals-log.csv`, `watchlist.md`, 브랜드별 `scorecards/*.md`가 나온다. | `examples/여성-컨템포러리-2026-07-08/`에 후보 8개, 신호 24개, 스코어카드 8개를 생성했다. | PASS | 2026-07-08 |
| 출처 강도 3 이하 단독 근거만 있는 후보 브랜드 | `가설` 또는 `모니터링`으로 표시하고 추가 확인 출처와 모니터링 쿼리를 제안한다. | `watchlist.md`에서 LOW CLASSIC, ENZO BLUES, FOR YOUR EYES ONLY를 `가설`로 두고 추가 공식/플랫폼 근거를 요구했다. | PASS | 2026-07-08 |
| 로그인 전용 또는 동적 렌더링 페이지 | unavailable 또는 manual-check-required로 표시하고 핵심 근거에서 제외한다. | 무신사 랭킹과 동적 상품/콘텐츠 페이지는 `manual-check-required`로 기록하고 화면 확인 액션을 남겼다. | PASS | 2026-07-08 |
| 플러그인 validator | `src/.codex-plugin/plugin.json`과 스킬 구조가 통과한다. | 원본 `src`와 zip에서 추출한 `src` 모두 validator 통과 | PASS | 2026-07-08 |

## 2. 정상 케이스와 예외 케이스

- 정상 케이스: 카테고리와 공개 URL을 입력하면 후보별 출처, 확인일, 지지 근거, 반대 근거, 점수, 다음 액션이 나온다.
- 예외 케이스 - 빈 입력: 카테고리, 고객군, seed brand, 공개 URL 중 최소 하나를 요청한다.
- 예외 케이스 - 잘못된 입력: 내부 매출·검색·CRM 데이터가 있다고 가정하지 않고 공개 자료만 요구한다.
- 예외 케이스 - 정보 부족: 후보를 확정하지 않고 모니터링 후보로 낮춘다.
- 예외 케이스 - 출처 접근 제한: unavailable로 기록하고 대체 공개 출처를 제안한다.

## 3. 의심한 것과 확인 방법

- 의심한 것: 브랜드 후보를 추천처럼 단정할 위험이 있다.
  - 확인 방법: `SKILL.md`에서 “검토할 후보 가설”로 표현하게 했다.
  - 결과: scorecard는 입점 추천이 아니라 MD가 검토할 가설로 제한된다.
- 의심한 것: 일회성 리포트로 끝날 위험이 있다.
  - 확인 방법: 출력에 monitoring query와 다음 액션을 포함했다.
  - 결과: 매주 같은 형식으로 반복 실행할 수 있는 구조가 됐다.

## 4. 아직 부족한 것

- 실제 무신사 랭킹/아카이브 URL과 외부 공개 자료를 함께 넣어 후보 점수의 안정성을 봐야 한다.
- SNS/API 없이 공개 자료만 쓰기 때문에 빠른 바이럴 신호 포착력은 제한될 수 있다.
- 무신사 내부 데이터가 없으므로 실제 매출성과 연결 검증은 할 수 없다.

## 5. 테스트하며 고친 것

- 기존 최종 후보였던 파트너 운영 QA는 영상 힌트와 간접적으로 연결됐다. 최종 스킬을 브랜드/트렌드 공개 신호 triage 중심으로 바꿨다.
- 제출 zip에 `docs/research.md`가 들어가지 않기 때문에 `src/references/evidence.md`를 추가해 플러그인 소스 안에도 근거 맵이 남도록 고쳤다.
- 패키징 후 zip 내부에 `src/references/evidence.md`, `src/skills/main/SKILL.md`, `README.md`, `logs/repo/`, `logs/musinsa/`가 포함되는지 확인했다.
- 참가자 새 지침에 맞춰 결과물을 먼저 정의하도록 `docs/output-spec.md`를 추가했다.
- 실제 예시 실행 중 공개 반응이 약한 후보를 무리하게 추천하지 않고 `watchlist.md`와 `모니터링` 상태로 낮췄다.
- 동적 페이지의 자동 추출 숫자를 쓰지 않고 `manual-check-required`로 남기도록 `SKILL.md`와 예시 산출물을 수정했다.

## 6. 실제 예시 실행 기록

- 실행 날짜: 2026-07-08
- 카테고리: 여성 컨템포러리
- 출력 경로: `examples/여성-컨템포러리-2026-07-08/`
- 생성 파일:
  - `scout-report.md`
  - `signals-log.csv`
  - `watchlist.md`
  - `scorecards/MATIN-KIM.md`
  - `scorecards/THE-BARNNET.md`
  - `scorecards/FOETO.md`
  - `scorecards/SIYAZU.md`
  - `scorecards/LE17SEPTEMBRE.md`
  - `scorecards/RECTO.md`
  - `scorecards/TREEMINGBIRD.md`
  - `scorecards/HAAG.md`
- 후보 브랜드 수: 8개
- 신호 수: 24개
- 정상 상황 확인: 공개 URL과 확인일이 붙은 후보 요약표, 트렌드 신호, 브랜드별 상세 카드가 생성됐다.
- 예외 상황 확인: 신호 부족 후보는 `watchlist.md`로 내렸고, 동적 페이지는 `manual-check-required`로 처리했다.
- 아직 부족한 점: 무신사/29CM 동적 화면의 랭킹, 리뷰, 좋아요, 품절 여부는 사용자가 실제 화면으로 확인해야 한다.
- validator 결과: `python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py src` 통과.
- 산출물 스키마 확인: `signals-log.csv` 헤더 일치, 스코어카드 8개 모두 필수 섹션 포함, `scout-report.md` 필수 섹션 포함.

## 7. URL 접근성 전수 점검

- 점검 날짜: 2026-07-08
- 점검 명령: `curl -L -o /dev/null -s -w "%{http_code}"`
- 점검 범위: `README.md`, `docs/research.md`, `src/references/evidence.md`, `examples/**`
- 1차 점검 결과: 실패 6개. Fashionbiz 3개, Apparelnews 2개, Teamblind 1개가 curl 기준 403이었다.
- 조치 후 재점검 결과: 대상 범위 고유 URL 53개, 실패 0개.

| URL | 1차 상태 | 조치 | 조치 후 상태 |
| --- | --- | --- | --- |
| https://fashionbiz.co.kr/article/222002 | 403 | THE BARNNET 라이브 반응 근거를 29CM 공식 라이브 페이지와 KTNews 접근 가능 기사로 교체했다. | 교체 URL 200 |
| https://fashionbiz.co.kr/article/223560 | 403 | SIYAZU 잡화/워크웨어 확장 주장을 핵심 근거에서 제외하고 공식 스토어·29CM 페이지 기반 모니터링으로 낮췄다. | 대상 인용 제거 |
| https://fashionbiz.co.kr/article/225539 | 403 | LE17SEPTEMBRE 2026 S/S 보조 기사 근거를 공식 글로벌 사이트와 29CM 콘텐츠로 교체했다. | 교체 URL 200 |
| https://www.apparelnews.co.kr/news/news_view/?idx=223492 | 403 | SIYAZU 2026 스프링 보조 기사 근거를 공식 스토어·29CM 페이지로 교체했다. | 교체 URL 200 |
| https://www.apparelnews.co.kr/news/news_view/?cat=CAT100&idx=216123 | 403 | TREEMINGBIRD 반응 근거를 29CM/무신사 브랜드 페이지와 Fashion Insight 접근 가능 기사로 교체하고 상태를 모니터링으로 낮췄다. | 교체 URL 200 |
| https://www.teamblind.com/kr/post/%EC%9C%BC-%EB%AC%B4%EC%8B%A0%EC%82%AC-%EA%B5%90%ED%99%98-%EC%A7%9C%EC%A6%9D%EB%82%98%EB%84%A4%E3%85%A0%E3%85%A0-Ch3YJ72j | 403 | 최종 문제와 무관한 탈락 후보 보조 근거였으므로 research 후보 목록과 사용자 피드백 근거에서 제외했다. | 대상 인용 제거 |

## 8. 답변 초안

### 문항 ⑤ 어떻게 검증했나요? (800자 제한)

검증은 정상 입력과 예외 입력을 나눠 설계했습니다. 정상 입력은 “여성 컨템포러리에서 다음 주간 리뷰에 볼 브랜드/협업/입점 후보를 공개 자료 기반으로 triage해줘”라는 질문입니다. 기대 결과는 `signals-log.csv`, 브랜드별 scorecard, `scout-report.md`, `watchlist.md`이며, 실제 예시는 후보 8개를 `협업/콘텐츠 확장` 3개와 `모니터링` 5개로 분류했습니다. 예외 입력은 403 기사 URL, 동적 렌더링 페이지, 단일 보조 기사 근거입니다. 이 경우 후보를 확정하지 않고 `manual-check-required`, `가설`, `모니터링`으로 낮춰야 합니다. 의심한 점은 이미 알려진 브랜드를 신규 발굴처럼 포장하는 것이었고, 이를 막기 위해 이미 노출된 브랜드를 확장 후보로 분기했습니다. 아직 내부 매출·검색 데이터로 성과를 검증하지 못하는 한계가 있습니다.
