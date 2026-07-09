# ChannelTalk Evidence Map

> 공식 힌트 영상 원본: https://www.youtube.com/watch?v=5iRf37Z8Wd4 (자막 사본: `src/docs/source-video.ko.vtt`, 확인일 2026-07-08) — 자막 5등급 근거의 역추적 경로.

## Selected Problem

채널톡 트랙의 제출 플러그인은 이커머스 운영자, CX/CS 담당자, 채널톡 AX 컨설턴트가 공개 FAQ, 배송/교환/환불 정책, 상품/프로모션 페이지를 ALF 도입 전 `지식`, `규칙`, `상담원 이관 기준`, `테스트 질문`으로 구조화하도록 돕는다.

## Evidence Weight Rule

| 등급 | 자료 유형 | 이 파일에서의 사용 |
| --- | --- | --- |
| 5 | 대회 영상 자막 | 트랙 의도와 평가 관점의 최우선 근거 |
| 4 | 채널톡 공식 사이트, 뉴스룸, 도움말, 개발자 문서 | 핵심 주장과 플러그인 판단 기준의 주 근거 |
| 3 | 기사, 공개 리뷰, 커뮤니티, 산업 자료 | 실제 pain point 보조 근거. 단독 핵심 근거로 쓰지 않음 |
| 2 | 검색 결과, 개인 블로그, 2차 요약 | 후보 탐색용. 제출 근거로 쓰지 않음 |
| 1 | AI 요약 | 누락 확인용. 원문 역추적이 안 되면 폐기 |

## Core Claim Audit

| ID | 핵심 주장 | 등급 | 출처 URL/위치 | 확인일 | 수집 방법 | 판정 |
| --- | --- | --- | --- | --- | --- | --- |
| CT-01 | 채널톡 트랙은 이커머스 고객사의 상담 문제와 AI 에이전트 활용을 직접 힌트로 준다. | 5 | `src/docs/source-video.ko.vtt` | 2026-07-08 | 로컬 자막 `rg "이커머스|AI|에이전트|상담"` 검색 | 유지 |
| CT-02 | 채널톡 AI 상담사가 제대로 답하려면 규칙, 구조화된 지식, 실행 가능한 태스크/액션이 필요하다. | 4 | https://channel.io/kr/talk | 2026-07-08 | 웹 검색 후 `web.open`, `curl -L` 200 확인 | 승격: 기존 `channel.io/us/talk`보다 제출용 한국어 공식 페이지가 직접적 |
| CT-03 | ALF의 지식은 문서, 파일, 웹사이트 자료를 모아 관리하는 공간이며, 구조화된 지식은 RAG 답변 품질을 높인다. | 4 | https://docs.channel.io/help/ko/articles/%EC%A7%80%EC%8B%9D-803f6ac9 | 2026-07-08 | 공식 도움말 검색, `web.open`, `curl -L` 200 확인 | 신규 보강 |
| CT-04 | ALF 규칙은 상황별 지시문이며 필터, 개인화 변수, 상담 처리 액션, 미리보기를 통해 동작을 제어한다. | 4 | https://docs.channel.io/help/ko/articles/%EA%B7%9C%EC%B9%99-b43e19a1 | 2026-07-08 | 공식 도움말 검색, `web.open`, `curl -L` 200 확인 | 신규 보강 |
| CT-05 | ALF 테스트는 배포 전 고객 시나리오와 평가 기준으로 답변 품질을 반복 검증하는 공식 기능이다. | 4 | https://docs.channel.io/help/ko/articles/ALF-%ED%85%8C%EC%8A%A4%ED%8A%B8-bffe077d | 2026-07-08 | 공식 도움말 검색, `web.open`, `curl -L` 200 확인 | 신규 보강 |
| CT-06 | ALF 오답변, 지식 미참조, 환각성 표현은 지식 추가/수정, 규칙 수정, 제한 규칙으로 다루는 문제다. | 4 | https://docs.channel.io/help/ko/articles/ALF-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0--219af581 | 2026-07-08 | 공식 도움말 검색, `web.open` 확인 | 신규 보강 |
| CT-07 | 채널톡은 URL 입력과 웹 크롤링으로 AI 상담 환경을 사전 체험하는 기능을 공식 출시했다. | 4 | https://channel.io/kr/blog/articles/crawling-press-9b611f25 | 2026-07-08 | 공식 뉴스룸 검색, `web.open`, `curl -L` 200 확인 | 유지/핵심화 |
| CT-08 | 반복 문의와 프로모션 시 상담량 폭증은 채널톡이 AI 상담 리포트의 주요 독자로 직접 제시한 pain point다. | 4 | https://channel.io/kr/blog/articles/ai-cs-best-cases-6a7fd39d | 2026-07-08 | 공식 블로그 검색, `web.open`, `curl -L` 200 확인 | 승격: 보조 기사 대신 공식 pain point로 사용 |
| CT-09 | 이커머스 반복 문의 예시는 배송지 변경, 주문 취소, 사이즈 문의 등으로 공개 기사에서 확인된다. | 3 | https://zdnet.co.kr/view/?no=20241217160629 | 2026-07-08 | 웹 검색, `web.open` 확인 | 강등: 문항 2 핵심 근거에서 제외하고 보조 근거로만 사용 |
| CT-10 | 채널톡에는 이미 AI 상담 시뮬레이션, ALF 테스트, CoS 같은 보조 기능이 있어 동일 기능 제공 여부를 반증으로 검토해야 한다. | 4 | https://channel.io/kr/blog/articles/crawling-press-9b611f25, https://docs.channel.io/help/ko/articles/ALF-%ED%85%8C%EC%8A%A4%ED%8A%B8-bffe077d, https://docs.channel.io/help/ko/articles/CoS-a8e86305 | 2026-07-08 | 공식 자료 검색, `web.open`, `curl -L` 200 확인 | 반증 항목으로 유지 |
| CT-11 | 실제 업무 처리 자동화는 태스크/코드 노드/외부 API와 연결될 수 있으나, 이 플러그인은 API 키나 내부 데이터 없이 설계 초안만 만든다. | 4 | https://docs.channel.io/help/ko/articles/%ED%83%9C%EC%8A%A4%ED%81%AC-2a16be8b, https://developers.channel.io/ko/articles/%EC%BD%94%EB%93%9C-%EB%85%B8%EB%93%9C-fdcd71b4 | 2026-07-08 | 공식 도움말/개발자 문서 검색, `web.open`, `curl -L` 200 확인 | 범위 제한 근거로 유지 |

## Downgraded Or Non-Core Sources

| 출처 | 등급 | 처리 | 이유 |
| --- | --- | --- | --- |
| https://zdnet.co.kr/view/?no=20241217160629 | 3 | 보조 근거 | 이커머스 반복 문의 예시는 유용하지만 기사이므로 공식 자료를 핵심으로 둔다. |
| https://apps.shopify.com/channel-talk?locale=ko | 3 | 보조 근거 | 리뷰는 편향 가능성이 있어 반복 문의 자동화 가치의 정성 단서로만 사용한다. |
| App Store 리뷰 URL들 | 3 | 비핵심 후보 근거 | 알림/데스크톱 품질 후보에는 유용하나 최종 ALF 지식·규칙 문제와 직접성이 약하다. |
| https://www.oopy.io/ko/guides/plugins/channeltalk | 2 | 후보 탐색 근거 | 설치 이슈 후보에만 사용하고 제출 핵심 근거에서 제외한다. |
| https://adjh54.tistory.com/755 | 2 | 후보 탐색 근거 | 개인 블로그라 설치 후보 탐색용으로만 사용한다. |
| AI/NotebookLM 요약 | 1 | 미사용 | 원문 URL로 역추적한 내용만 남긴다. |

## Final Source URL Candidates For Form Question 2

| URL | 등급 | 접근 확인 | 문항 2에서 쓰는 이유 |
| --- | --- | --- | --- |
| https://channel.io/kr/talk | 4 | 2026-07-08 `curl -L` 200, `web.open` 성공 | ALF 성공 조건이 규칙, 구조화된 지식, 태스크/액션이라는 공식 제품 근거 |
| https://channel.io/kr/blog/articles/crawling-press-9b611f25 | 4 | 2026-07-08 `curl -L` 200, `web.open` 성공 | URL/웹 크롤링으로 AI 상담 환경을 구성한다는 공식 방향 |
| https://docs.channel.io/help/ko/articles/%EC%A7%80%EC%8B%9D-803f6ac9 | 4 | 2026-07-08 `curl -L` 200, `web.open` 성공 | ALF가 참조할 지식의 형태와 구조화 필요성 |
| https://docs.channel.io/help/ko/articles/%EA%B7%9C%EC%B9%99-b43e19a1 | 4 | 2026-07-08 `curl -L` 200, `web.open` 성공 | ALF 답변을 상황별 지시문과 필터로 제어해야 한다는 근거 |
| https://channel.io/kr/blog/articles/ai-cs-best-cases-6a7fd39d | 4 | 2026-07-08 `curl -L` 200, `web.open` 성공 | 반복 문의와 프로모션 상담량 폭증이 실제 CS팀 pain point라는 공식 근거 |

## Counterevidence And Response

| 약화 정보 | 등급 | 출처 | 대응 논리 |
| --- | --- | --- | --- |
| 채널톡은 URL 기반 AI 상담 시뮬레이션을 이미 제공한다. | 4 | https://channel.io/kr/blog/articles/crawling-press-9b611f25 | 본 플러그인은 시뮬레이션을 대체하지 않고, 로그인 전/외부 감사 단계에서 공개 문서를 지식 폴더, 규칙, 이관 기준, 테스트 케이스, 누락 질문으로 정리하는 준비 산출물을 만든다. |
| ALF 테스트는 제품 안에서 공식 제공된다. | 4 | https://docs.channel.io/help/ko/articles/ALF-%ED%85%8C%EC%8A%A4%ED%8A%B8-bffe077d | 본 플러그인은 ALF 테스트에 넣기 전 고객 시나리오와 평가 기준 초안을 생성한다. 실제 제품 테스트 실행을 대신한다고 주장하지 않는다. |
| CoS는 상담·비즈니스 데이터를 분석해 인사이트, 전략 설계, 리포트 생성을 돕는 채널톡 AI 비서 기능으로 공개되어 있다. | 4 | https://docs.channel.io/help/ko/articles/CoS-a8e86305 | CoS는 채널 안의 데이터와 설정을 다루는 제품 기능이다. 제출 플러그인은 공개 URL/붙여넣은 정책만으로 심사자가 재현 가능한 Codex 워크플로우를 제공한다. |

## Plugin Scope

Inputs:

- 공개 이커머스 사이트 URL 또는 사용자가 붙여넣은 FAQ/정책/상품 설명
- 선택 입력: 배송, 교환/환불, 사이즈, 쿠폰, 주문 변경, 상담원 이관 등 대상 범위

Outputs:

- `output/<브랜드명>/alf-knowledge/`: ALF 지식 관리 화면에 옮길 수 있는 카테고리별 문서
- `output/<브랜드명>/alf-rules.md`: 채널톡 규칙 입력창에 복사할 상황별 지시문
- `output/<브랜드명>/alf-test-cases.csv`: 질문, 의도분류, 기대답변요지, 근거URL, 오답위험도 컬럼을 가진 테스트 질문 30개 이상
- `output/<브랜드명>/alf-escalation.md`: 상담원 이관 기준과 이관 문구
- `output/<브랜드명>/gaps.md`: 접근 실패, 미확인 정책, 문서 충돌, 운영자 확인 질문
- `output/<브랜드명>/APPLY-GUIDE.md`: 채널톡 관리자 화면 적용 순서
- 요청 시 5문항 제출 답변 초안

## Example Runs

| 예시 | 업종 | 실행 깊이 | 공개 근거 | 확인일 | 사용 |
| --- | --- | --- | --- | --- | --- |
| `examples/biteme/` | 반려동물 커머스 | 풀 실행 | https://channel.io/kr/blog/articles/ai-case-biteme-d3e09ab9, https://m.biteme.co.kr/shop/community/faq_lists, https://m.biteme.co.kr/shop/service/service_guide | 2026-07-08 | 공식 바잇미 사례와 공개 FAQ/정책으로 전체 출력 계약을 검증한 예시 |
| `examples/aladin/` | 도서/음반/전자책 커머스 | 라이트 실행 | https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx, https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=75&UpperId=75, https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=76&UpperId=76 | 2026-07-08 | 다른 업종의 공개 FAQ와 공개 AJAX 응답에서도 같은 지식·규칙·테스트·gaps 워크플로우가 작동함을 확인한 축약 예시 |

## Judgment Rules

- 영상 자막(5)과 채널톡 공식 자료(4)를 우선한다.
- 기사/리뷰/개인 블로그는 핵심 주장 단독 근거로 쓰지 않는다.
- 환불, 취소, 배송 예정일, 쿠폰 적용처럼 정책 민감도가 높은 항목은 `high risk`로 표시한다.
- 출처가 없는 정책은 `missing`, 문서끼리 충돌하는 정책은 `conflict`로 표시하고 사람 검토로 넘긴다.
- 실제 채널톡 계정, ALF 내부 설정, 고객사 주문/CRM 데이터 접근을 전제하지 않는다.

## Do Not Claim

- 채널톡 내부 ALF 설정에 접근한다고 주장하지 않는다.
- 고객사의 비공개 주문, CRM, 고객 데이터를 안다고 주장하지 않는다.
- 실제 주문 취소, 환불, 쿠폰 발급 같은 업무를 API 없이 자동 처리한다고 쓰지 않는다.
- 출처 없는 숫자를 비즈니스 임팩트 근거로 쓰지 않는다.
