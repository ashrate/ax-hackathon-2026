# 채널톡 — 검증 기록

> 이 문서의 사본은 submission.zip의 src/docs/에 포함된다. 문항 ⑤와 README.md 작성의 원천 자료다.

## 1. 테스트 시나리오

| 입력 | 기대 결과 | 실제 결과 | 판정 | 날짜 |
| --- | --- | --- | --- | --- |
| 바잇미 공개 URL 6개와 “ALF 출력 계약대로 만들어줘” | `examples/biteme/` 아래 지식 문서, 규칙, CSV 테스트, 이관 기준, gaps, 적용 가이드가 생성된다. | 계약 산출 파일 13개 생성, 지식 문서 8개, 테스트 질문 41개 생성 | PASS | 2026-07-08 |
| 환불 가능 기간이 상품별로 다르게 적힌 공개 상품 상세 | 공통 정책으로 단정하지 않고 상품별 예외와 운영자 확인 질문을 만든다. | HAX 2일, 케스티/이츠독 7일로 분리하고 `gaps.md`와 `alf-rules.md`에 단정 금지를 기록 | PASS | 2026-07-08 |
| 같은 상품 페이지 안의 제주/도서산간 교환 반품 추가비용 충돌 | conflict로 표시하고 사람이 확인해야 할 질문을 만든다. | HAX 상품 추가비 4,000원/3,000원 충돌을 `gaps.md` 문서 충돌로 기록 | PASS | 2026-07-08 |
| 공개 FAQ 본문이 기본 화면이 아니라 AJAX로 로딩되는 상황 | 로그인 없이 접근 가능한 공개 응답만 사용하고 수집 방법을 남긴다. | `faq_lists_ajax?page=1..4`에서 38개 FAQ를 확인하고 출처 수집 방법에 기록 | PASS | 2026-07-08 |
| 알라딘 공개 FAQ와 공개 AJAX 응답으로 라이트 실행 | 바잇미와 다른 업종에서도 지식 맵, 규칙 발췌, CSV 테스트, gaps가 생성된다. | `examples/aladin/` 아래 지식 문서 3개, 규칙 발췌 1개, 테스트 질문 12개, 운영자 확인 항목 6개 생성 | PASS | 2026-07-08 |
| 인용 URL 전수 curl 점검 | README, docs, src, examples의 인용 URL이 공개 접근 가능한지 확인한다. | 중복 제거 후 53개 URL을 `curl -L --max-time 20`로 확인했고 모두 HTTP 200 응답 | PASS | 2026-07-08 |
| 플러그인 validator | `src/.codex-plugin/plugin.json`과 스킬 구조가 통과한다. | `python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py src` 통과 | PASS | 2026-07-08 |

## 2. 정상 케이스와 예외 케이스

- 정상 케이스: 배송/교환/환불/쿠폰 안내가 충분한 공개 문서를 입력하면 의도별 지식 맵과 테스트 질문이 생성된다.
- 예외 케이스 - 빈 입력: 필요한 입력 형식과 예시를 요청한다.
- 예외 케이스 - 잘못된 입력: 고객 개인정보나 주문번호가 들어오면 제출 로그에 남기지 말라고 안내하고 공개 정책만 사용하게 한다.
- 예외 케이스 - 정보 부족: 확정 답변을 만들지 않고 누락 정보와 사람 확인 질문을 출력한다.
- 예외 케이스 - 문서 충돌: 한쪽을 선택하지 않고 conflict로 표시한다.

## 3. 의심한 것과 확인 방법

- 의심한 것: 공개 자료만으로 ALF 실제 설정을 안다고 표현할 위험이 있다.
  - 확인 방법: `SKILL.md`와 `evidence.md`에서 내부 설정 접근을 전제하는 문장을 제거한다.
  - 결과: 스킬은 내부 설정 자동화가 아니라 ALF 도입 전 준비 산출물 생성으로 범위를 제한했다.
- 의심한 것: 정책 민감 항목을 AI가 단정할 위험이 있다.
  - 확인 방법: 환불, 취소, 배송 예정일, 쿠폰 적용을 high risk로 표시하는 절차를 넣었다.
  - 결과: 사람 확인과 상담원 이관 기준을 기본 출력에 포함했다.

## 4. 예시 실행 기록

- 브랜드: 바잇미
- 선정 이유: 채널톡 공식 바잇미 사례가 ALF/FAQ로 배송, 교환, 반품, 주문 취소 같은 반복 문의를 줄이는 맥락을 제공한다.
- 입력 URL:
  - https://channel.io/kr/blog/articles/ai-case-biteme-d3e09ab9
  - https://m.biteme.co.kr/shop/community/faq_lists
  - https://m.biteme.co.kr/shop/service/service_guide
  - https://m.biteme.co.kr/shop/product/product_view?product_cd=1000050043
  - https://m.biteme.co.kr/shop/product/product_view?product_cd=1000040999
  - https://m.biteme.co.kr/shop/product/product_view?product_cd=1000006873
- 출력 경로: `examples/biteme/`
- 생성 결과:
  - 계약 산출 파일 13개
  - `alf-knowledge/` 문서 8개
  - `alf-test-cases.csv` 테스트 질문 41개
  - 입력 URL은 `curl -L` 점검에서 접근 실패가 발견되지 않았다.
  - 문서 충돌 1건: HAX 상품 제주/도서산간 교환 반품 추가비용
- 확인한 것:
  - 지식 문서의 출처 URL과 확인일 표기를 자동 스캔과 수동 검수로 확인했다.
  - CSV는 Python `csv.DictReader`로 파싱 가능했다.
  - 테스트 질문 수가 출력 계약의 30개 이상 기준을 넘었다.
  - 고위험 질문은 환불/하자/오배송/주문상태 추정 대신 상담원 확인으로 처리했다.

## 5. 알라딘 라이트 실행 기록

- 브랜드: 알라딘
- 선정 이유: 바잇미가 반려동물 커머스인 반면 알라딘은 도서/음반/전자책 커머스이며, 고객센터 FAQ와 배송/반품/교환 AJAX 응답이 로그인 없이 접근 가능해 다른 업종 일반화 확인에 적합하다.
- 입력 URL:
  - https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx
  - https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=75&UpperId=75
  - https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=76&UpperId=76
  - https://blog.aladin.co.kr/cscenter/1451688
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=209
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=275
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1278
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1284
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=137
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=478
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1272
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1267
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1924
  - https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1600
- 출력 경로: `examples/aladin/`
- 생성 결과:
  - `knowledge-map-summary.md` 1개
  - `alf-knowledge/` 대표 문서 3개
  - `alf-rules.md` 규칙 발췌 1개
  - `alf-test-cases.csv` 테스트 질문 12개
  - `gaps.md` 운영자 확인 항목 6개
- 확인한 것:
  - 공개 FAQ 목록에서 배송/수령일안내와 반품/교환 카테고리를 확인했다.
  - FAQ 상세 답변은 공개 AJAX URL로 수집하고 각 문서 출처에 수집 방법을 남겼다.
  - 전자책, 전자제품류, 중고/판매자직배송 상품은 공통 반품 정책으로 합치지 않고 gaps와 이관 규칙으로 분리했다.

## 6. 아직 부족한 것

- 바잇미 풀 실행과 알라딘 라이트 실행으로 다른 업종 2곳의 재현성은 확인했지만, 알라딘은 제출 보강용 축약 실행이라 전체 30개 이상 테스트 계약까지 확장하지 않았다.
- ChannelTalk ALF의 최신 공개 문서가 바뀌면 `src/references/evidence.md`의 URL 확인일을 갱신해야 한다.
- 실제 고객사 내부 정책 문서는 사용할 수 없으므로 공개 샘플 기반 검증에 머문다.
- 바잇미 내부 주문/CRM/상담 데이터는 사용하지 않았으므로 고객별 주문 상태를 검증하지 못한다.

## 7. 테스트하며 고친 것

- 기존 스킬이 범용 문제 발굴 도우미라 실제 ALF 준비 플러그인으로 보이지 않았다. `SKILL.md`를 회사별 최종 문제, 입력, 절차, 출력물 중심으로 고쳤다.
- 제출 zip에 `docs/research.md`가 들어가지 않기 때문에 `src/references/evidence.md`를 추가해 플러그인 소스 안에도 근거 맵이 남도록 고쳤다.
- 패키징 후 zip 내부에 `src/references/evidence.md`, `src/skills/main/SKILL.md`, `README.md`, `logs/repo/`, `logs/channeltalk/`가 포함되는지 확인했다.
- 새 지침에 따라 `docs/output-spec.md`를 추가하고, 출력 계약을 중심으로 `SKILL.md`와 README를 다시 맞췄다.
- 예시 실행 중 HAX 상품의 추가 교환 반품비용 충돌을 발견해 확정 규칙에 넣지 않고 `gaps.md`와 이관 규칙으로 넘겼다.
- `alf-test-cases.csv`를 Python CSV 파서로 확인해 41개 질문이 정상 파싱되는 것을 확인했다.
- 외부 리뷰 피드백에 따라 알라딘 라이트 실행을 추가하고, README 전면부를 입력/결과/실패 동작/사람 판단 구조로 재배치했다.
- `README.md`, `docs/output-spec.md`, `src/skills/main/SKILL.md`, `docs/engineering.md`, 이 파일의 절대 표현을 검사 방법이 붙은 표현으로 바꿨다.

## 8. 인용 URL curl 점검

- 점검 대상: `README.md`, `docs/`, `src/`, `examples/`의 Markdown/CSV/JSON 인용 URL
- 점검 명령: `curl -L -s -o /dev/null --max-time 20 -w '%{http_code}' <URL>`
- 점검 결과: 중복 제거 53개 URL, HTTP 200 응답 53개, 접근 실패 0개

| URL | HTTP | 판정 |
| --- | --- | --- |
| https://adjh54.tistory.com/755 | 200 | PASS |
| https://apps.apple.com/kr/app/channel-works-for-desktop/id1102655071?l=en-GB&mt=12 | 200 | PASS |
| https://apps.apple.com/us/app/channel-works/id1088828788?see-all=reviews&platform=iphone | 200 | PASS |
| https://apps.shopify.com/channel-talk?locale=ko | 200 | PASS |
| https://aws.amazon.com/ko/blogs/tech/architecture-modernization-journey-of-channel-corporation-with-amazon-dynamodb-part1/ | 200 | PASS |
| https://blog.aladin.co.kr/cscenter/1451688 | 200 | PASS |
| https://channel.io/kr/alf-customer | 200 | PASS |
| https://channel.io/kr/blog/articles/ai-case-biteme-d3e09ab9 | 200 | PASS |
| https://channel.io/kr/blog/articles/ai-cs-best-cases-6a7fd39d | 200 | PASS |
| https://channel.io/kr/blog/articles/alimtalk-7f4003bb | 200 | PASS |
| https://channel.io/kr/blog/articles/channelcon2026-press-21de9c04 | 200 | PASS |
| https://channel.io/kr/blog/articles/crawling-press-9b611f25 | 200 | PASS |
| https://channel.io/kr/blog/articles/guide-self-install-42adf567 | 200 | PASS |
| https://channel.io/kr/blog/articles/notifications-56c7413f | 200 | PASS |
| https://channel.io/kr/blog/articles/renew-channelcorp-ac6d3388 | 200 | PASS |
| https://channel.io/kr/careers | 200 | PASS |
| https://channel.io/kr/talk | 200 | PASS |
| https://developers.channel.io/en/articles/11e97a83 | 200 | PASS |
| https://developers.channel.io/en/articles/3b9fc715 | 200 | PASS |
| https://developers.channel.io/ko/articles/%EC%BD%94%EB%93%9C-%EB%85%B8%EB%93%9C-fdcd71b4 | 200 | PASS |
| https://developers.channel.io/ko/articles/d27c51d1 | 200 | PASS |
| https://docs.channel.io/help/ko/articles/%EA%B7%9C%EC%B9%99-b43e19a1 | 200 | PASS |
| https://docs.channel.io/help/ko/articles/%EB%B0%B0%ED%8F%AC-%EC%84%A4%EC%A0%95-e9dbb764 | 200 | PASS |
| https://docs.channel.io/help/ko/articles/%EC%95%8C%EB%A6%BC%ED%86%A1-9747de9a | 200 | PASS |
| https://docs.channel.io/help/ko/articles/%EC%A7%80%EC%8B%9D-803f6ac9 | 200 | PASS |
| https://docs.channel.io/help/ko/articles/%EC%B1%84%EB%84%90%ED%86%A1-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-1bfa136b | 200 | PASS |
| https://docs.channel.io/help/ko/articles/%ED%83%9C%EC%8A%A4%ED%81%AC-2a16be8b | 200 | PASS |
| https://docs.channel.io/help/ko/articles/ALF%EB%9E%80-d791e043 | 200 | PASS |
| https://docs.channel.io/help/ko/articles/ALF-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0--219af581 | 200 | PASS |
| https://docs.channel.io/help/ko/articles/ALF-%ED%85%8C%EC%8A%A4%ED%8A%B8-bffe077d | 200 | PASS |
| https://docs.channel.io/help/ko/articles/CoS-a8e86305 | 200 | PASS |
| https://m.biteme.co.kr/shop/community/faq_lists | 200 | PASS |
| https://m.biteme.co.kr/shop/product/product_view?product_cd=1000006873 | 200 | PASS |
| https://m.biteme.co.kr/shop/product/product_view?product_cd=1000040999 | 200 | PASS |
| https://m.biteme.co.kr/shop/product/product_view?product_cd=1000050043 | 200 | PASS |
| https://m.biteme.co.kr/shop/service/service_guide | 200 | PASS |
| https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx | 200 | PASS |
| https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=75&UpperId=75 | 200 | PASS |
| https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=76&UpperId=76 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1267 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1272 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1278 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1284 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=137 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1600 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=1924 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=209 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=275 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=478 | 200 | PASS |
| https://www.aladin.co.kr/ucl/cs_center/ajax/wfaq_ajax.aspx?faqid=856 | 200 | PASS |
| https://www.oopy.io/ko/guides/plugins/channeltalk | 200 | PASS |
| https://www.youtube.com/watch?v=5iRf37Z8Wd4 | 200 | PASS |
| https://zdnet.co.kr/view/?no=20241217160629 | 200 | PASS |

## 9. 답변 초안

### 문항 ⑤ 어떻게 검증했나요? (800자 제한)

검증은 세 층으로 잡았습니다. 첫째, 구조 검증으로 `src/.codex-plugin/plugin.json`과 `skills/main/SKILL.md`가 validator를 통과하는지 확인합니다. 둘째, 정상 입력으로 이커머스 FAQ와 배송·교환·환불 정책 텍스트를 넣어 상담 의도별 지식 맵, 답변 규칙, 금지 답변, 상담원 이관 기준, 테스트 질문이 나오는지 봅니다. 셋째, 예외 입력으로 환불 기간이 서로 다른 두 문장을 넣어 한쪽을 추정하지 않고 conflict와 사람 확인 질문을 내는지 확인합니다. 의심한 점은 AI가 내부 ALF 설정을 아는 것처럼 말하거나 정책을 단정하는 것이었고, 이를 막기 위해 공개 문서 기반 준비 산출물로 범위를 줄이고 high risk, missing, conflict 표시를 넣었습니다. 아직 실제 고객사 내부 정책으로는 검증하지 못했고 공개 샘플 기반이라는 한계가 있습니다.

## Claim Audit (2026-07-08)

인용 URL의 생존 여부가 아니라 **링크 본문이 실제로 주장을 뒷받침하는지**를 정밀 대조했다. 각 출처를 WebFetch로 열고, 핵심 구절은 `curl -sL <URL> | grep`으로 원문 HTML에서 재확인해 WebFetch 요약 모델의 환각 가능성을 제거했다. 자막 5등급 주장은 `docs/source-video.ko.vtt` 로컬 파일에서 발언 구절을 직접 확인했고, README 산출 수치는 `examples/` 로컬 파일을 `find`/`csv` 카운트로 대조했다.

| 주장 | 출처 | 지지 구절 인용(원문) | 판정 | 조치 |
| --- | --- | --- | --- | --- |
| CT-01(5): 트랙이 이커머스 고객사 상담 문제와 AI 에이전트 활용을 직접 힌트로 제시 | `docs/source-video.ko.vtt` (01:28~01:36) | "저희 이커머스 고객사의 상담 문제를 풀고 있어요" / "커머스가 가진 많은 문제들을 AI로 에이전트를 만들고 있거든요" | 지지 | 유지 |
| CT-02 / 문항2#1: ALF 성공 조건 = 규칙·구조화된 지식·실행 가능한 태스크/액션 | https://channel.io/kr/talk | "구조화된 지식, 직접 실행 가능한 태스크" / "구조화된 지식 체계(RAG)를 구축하여 AI가…답변하게 합니다" / "기업이 정의한 룰을 기준으로 그 안에서만 동작합니다" | 지지 | 유지 (curl 원문 재확인) |
| CT-03 / 문항2#3: 지식 = 문서·파일·웹사이트 자료를 모아 관리, 구조화가 RAG 품질↑ | https://docs.channel.io/help/ko/articles/지식-803f6ac9 | "지식은 고객 ALF가 참조할 수 있도록 문서, 파일, 웹사이트 등 다양한 자료를 모아 관리하는 공간입니다" / "지식이 잘 정리되어 있을수록 RAG 품질이 향상되며" | 지지 | 유지 (curl 원문 재확인) |
| CT-04 / 문항2#4: 규칙 = 상황별 지시문 + 필터·개인화 변수·액션·미리보기 제어 | https://docs.channel.io/help/ko/articles/규칙-b43e19a1 | "규칙은 ALF가…미리 작성하는 지시문(프롬프트) 입니다" / "필터 설정을 통해…" / "개인화 변수를 포함할 수 있어요" / "상담 처리 액션을 수행" / "미리보기를 통해…테스트" | 지지 | 유지 (필터·미리보기 구절 curl 재확인) |
| CT-05: ALF 테스트 = 배포 전 시나리오·평가 기준으로 답변 품질 반복 검증 | https://docs.channel.io/help/ko/articles/ALF-테스트-bffe077d | "배포 전에 문제를 미리 발견할 수 있어" / "설정해 둔 평가 기준에 따라 통과/실패를 자동으로 판정해요" | 지지 | 유지 |
| CT-06: ALF 오답변·지식 미참조·환각을 지식 추가/수정·규칙 수정·제한 규칙으로 처리 | https://docs.channel.io/help/ko/articles/ALF-문제-해결--219af581 | "① 오답변할 때 → 참조한 지식 수정 + 지식 추가" / "② 모를 때 → 지식 추가" / "③ 원하는대로 동작하지 않을 때 → 규칙 수정" / "④ 말을 지어낼 때 → 제한 규칙 추가" | 지지 | 유지 |
| CT-07 / 문항2#2: URL 입력·웹 크롤링으로 AI 상담 환경 사전 체험을 공식 출시 | https://channel.io/kr/blog/articles/crawling-press-9b611f25 | "‘AI 상담 시뮬레이션’ 기능 출시" / "URL 입력만으로 AI 상담 환경" (2026-05-27 발행) | 지지 | 유지 (curl 원문 재확인) |
| CT-08 / 문항2#5: 반복 문의·프로모션 상담량 폭증이 CS팀 pain point | https://channel.io/kr/blog/articles/ai-cs-best-cases-6a7fd39d | "단순 반복 문의 때문에 중요한 상담이나 영업 기회를 놓치고 있는 CS팀" / "프로모션 시 폭발하는 상담량" | 지지 | 유지 (curl 원문 재확인) |
| CT-10: AI 상담 시뮬레이션·ALF 테스트·CoS 등 보조 기능이 이미 존재(반증 검토 대상) | crawling-press + ALF-테스트 + CoS-a8e86305 | 시뮬레이션·ALF 테스트 상동 확인, CoS = "채널톡의 AI 비서 기능" | 지지 | 반증표 CoS 설명 문구만 조정(아래 행) |
| CT-11: 실제 업무 자동화가 태스크/코드 노드/외부 API와 연결될 수 있음 | https://docs.channel.io/help/ko/articles/태스크-2a16be8b | "코드 단계는…JavaScript 형태의 코드를 직접 실행하여…실제 처리(조회, 갱신)를 수행" / "함수 단계는 외부 서비스와의 API 통신" | 지지 | 유지 |
| 반증표 CoS 설명: "CoS는 상담 데이터 분석, ALF 개선 제안, 태스크 설계까지 도울 예정" | https://docs.channel.io/help/ko/articles/CoS-a8e86305 | 페이지 원문: "비즈니스 데이터를 분석하고, 인사이트를 찾아 전략 설계부터 리포트 생성까지 도와주는 채널톡의 AI 비서 기능" (원문에 "ALF 개선 제안"·"태스크 설계" 문구 없음, curl에서 "태스크" 매칭 0건) | 부분지지 | `evidence.md` 반증표 문구를 원문(데이터 분석·인사이트·전략 설계·리포트 생성 AI 비서)에 맞게 수정 |
| README 공개 근거: 바잇미가 배송·교환·반품·주문 취소 반복 문의를 FAQ/ALF로 처리한 사례 | https://channel.io/kr/blog/articles/ai-case-biteme-d3e09ab9 | "저희에 들어오는 문의의 80%는 배송, 교환, 반품, 취소 등…" / "80%를 자동화하는" | 지지 | 유지 (curl 원문 재확인) |
| README biteme 수치: 지식 문서 8·계약 파일 13·CSV 41·문서 충돌 1 | 로컬 `examples/biteme/` | `find` 결과 md 8, 파일 13, CSV 데이터행 41, `gaps.md` 문서 충돌 1행(HAX 제주/도서산간 4,000원 vs 3,000원) | 지지 | 유지 |
| README aladin 수치: 지식 문서 3·규칙 발췌 1·CSV 12·운영자 확인 6 | 로컬 `examples/aladin/` | `find` 결과 md 3, `alf-rules.md` 1, CSV 데이터행 12, `gaps.md` 미확인 정책 4 + 운영자 확인 질문 2 = 6 | 지지 | 유지 |

- 감사한 주장: 14 (문항2 후보 5 + Core Claim Audit 4~5등급 10 중 중복 제외, CoS 반증 문구 1, README 수치·사실 3)
- 지지 13 / 부분지지 1 / 불지지 0 / 보류 0
- 부분지지 1건: 반증표의 CoS 설명이 실제 도움말 원문과 달라 문구를 원문 범위로 축소 조정함(아래 evidence.md 반영).

## 실구동 테스트 (2026-07-09)

### 설치 방법

- 확인 명령: `codex plugin --help`, `codex plugin add --help`, `codex plugin marketplace add --help`, `codex plugin marketplace list --help`, `codex plugin remove --help`.
- 공식 문서 기준의 repo 스코프 `.agents/plugins/marketplace.json`은 이 작업의 수정 허용 범위 밖이므로 만들지 않았다.
- 대신 허용 범위 안인 `channeltalk/output/live-test/marketplace/`에 로컬 마켓플레이스를 만들고, 그 아래 `plugins/channeltalk-plugin/`에 `src` 사본을 둔 뒤 `source.path`를 `./plugins/channeltalk-plugin`으로 지정했다.
- `codex plugin marketplace add <repo>/channeltalk/output/live-test/marketplace --json` 결과 `ax-live-channeltalk` 등록 성공.
- `codex plugin add channeltalk-plugin@ax-live-channeltalk --json` 결과 설치 성공. 설치 경로는 사용자 Codex 캐시(`~/.codex/plugins/cache/ax-live-channeltalk/...`)였다.
- 참고: 처음에는 `source.path`를 `./../../../src`로 두었으나 `codex plugin list --marketplace ax-live-channeltalk --available --json`에서 available이 비어 있었다. 로컬 marketplace root 밖의 경로는 이 CLI에서 발견되지 않아, 테스트용 사본을 marketplace root 아래에 두는 방식으로 재시도했다.

### 실행 시나리오와 입력

- 실행 명령: `codex exec --ephemeral -C channeltalk -s workspace-write -o output/live-test/channeltalk-codex-last-message.md -`
- 입력: 브랜드명 `live-test-mini-faq`, 사용자 제공 공개 FAQ 텍스트 4문장(배송 2~3영업일, 단순 변심 교환/반품 7일 이내, 사용 흔적/포장 훼손 제한, 주문 취소 시 쿠폰 복구 조건).
- 지시: 설치된 `channeltalk-plugin:main` 스킬을 사용하고 `output/live-test/channeltalk-mini-faq/` 아래에만 ALF 지식 구조 초안을 생성.

### 생성된 출력 파일

- `output/live-test/channeltalk-mini-faq/alf-knowledge/01-brand-and-scope/scope.md`
- `output/live-test/channeltalk-mini-faq/alf-knowledge/03-shipping/shipping.md`
- `output/live-test/channeltalk-mini-faq/alf-knowledge/04-exchange-return-refund/exchange-return.md`
- `output/live-test/channeltalk-mini-faq/alf-knowledge/05-coupons-points/coupon-cancel.md`
- `output/live-test/channeltalk-mini-faq/alf-rules.md`
- `output/live-test/channeltalk-mini-faq/alf-test-cases.csv`
- `output/live-test/channeltalk-mini-faq/alf-escalation.md`
- `output/live-test/channeltalk-mini-faq/gaps.md`
- `output/live-test/channeltalk-mini-faq/APPLY-GUIDE.md`

### 확인 결과

- `codex exec` 출력에서 `channeltalk-plugin:main` 스킬을 사용했다고 보고했다.
- 계약 파일 구조가 생성됐다. `alf-knowledge/**/*.md` 4개, 필수 상위 파일 5개가 존재한다.
- `alf-test-cases.csv`는 데이터 30행으로 파싱됐고, 오답위험도 값은 `낮음/중간/높음` 범위 안이었다.
- 원문 URL이 없었으므로 출처는 `N/A - 사용자 제공 공개 FAQ 텍스트`로 분리됐고, `gaps.md`에 원문 FAQ URL 확인 질문이 남았다.

### 검증하지 못한 것과 제약

- 대화형 `/plugins` 설치 UI와 Space 토글은 헤드리스 환경이라 검증하지 못했다. CLI `codex plugin marketplace add`, `codex plugin add`, fresh `codex exec`로 대체 검증했다.
- `-o output/live-test/channeltalk-codex-last-message.md`는 상대 경로 해석 문제로 마지막 메시지 파일 저장에 실패했다. 다만 `codex exec` 표준 출력에 최종 보고와 생성 파일 목록이 남았고, 실제 파일 생성과 CSV 검증은 별도 명령으로 확인했다.
- 실제 채널톡 관리자 화면에 지식/규칙을 업로드하거나 ALF 테스트 UI를 실행하지는 않았다.

### 전역 상태 복구

- 실행 후 `codex plugin remove channeltalk-plugin@ax-live-channeltalk --json` 및 `codex plugin marketplace remove ax-live-channeltalk --json` 실행.
- 최종 확인에서 `codex plugin list --json`과 `codex plugin marketplace list --json`에 `channeltalk-plugin` 및 `ax-live-channeltalk`가 남아 있지 않았다.
- `~/.codex/config.toml` SHA-256은 테스트 전후 동일했다: `6f8f473a8ce0cdda196e32fe5512f1ceb6ad575cea781729f2fc4e4ab2f1f52c`.

### 테스트 환경 제약 주석

- 위 실구동 테스트에서 확인된 CLI 환경 제약은 `-o output/live-test/channeltalk-codex-last-message.md` 상대 경로 해석으로 last message 파일 저장이 1회 실패한 기록이다.
- 이 불안정은 최종 메시지 저장/프로세스 종료 래퍼에 한정된 것이며, 플러그인 산출물 자체는 모두 정상 생성되어 파일 단위로 별도 검증했다(생성 파일 목록·계약 일치 여부는 위 기록 참조).
