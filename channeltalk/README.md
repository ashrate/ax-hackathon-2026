# 채널톡 ALF 출력물 생성 플러그인

## 심사자 5분 재현 가이드

1. 복붙 입력 프롬프트:

```text
브랜드명: 바잇미
공개 URL:
- https://channel.io/kr/blog/articles/ai-case-biteme-d3e09ab9
- https://m.biteme.co.kr/shop/community/faq_lists
- https://m.biteme.co.kr/shop/service/service_guide
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000050043
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000040999
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000006873

요청:
채널톡 ALF에 넣을 지식 문서, 답변 규칙, 상담원 이관 기준,
배포 전 테스트 질문, 누락 정책 질문을 output/바잇미/ 아래에 만들어줘.
출처가 없거나 문서가 충돌하는 숫자는 단정하지 말고 gaps.md에 남겨줘.
```

2. 예상 출력 폴더: `output/바잇미/`
3. 먼저 볼 핵심 파일 3개: `src/examples/biteme/alf-test-cases.csv`, `src/examples/biteme/gaps.md`, `src/examples/biteme/alf-rules.md`
4. 실패 처리 예시: 접근 실패 URL이 있으면 내용을 추정하지 않고 `gaps.md`의 접근 실패 항목에 URL, 실패 증상, 확인일을 기록한다.
5. 사람이 판단할 지점: 문서 충돌은 ALF 확정 규칙에 넣기 전에 운영자가 최종 우선순위를 확정한다.

## 왜 이 문제, 왜 이 범위인가

채널톡 트랙 힌트 영상은 이커머스 고객사의 상담 문제와 AI 에이전트를 직접 가리킨다. 이 제출물은 API 키나 채널톡·브랜드 내부 데이터 없이 로그인 없이 열람 가능한 공개 자료만 사용하므로 심사자가 같은 URL로 재현할 수 있다. 공개 문서를 구조화하고, 검증 가능한 테스트와 가드레일을 만드는 작업은 Codex 스킬이 가장 잘하는 범위다. 그래서 실제 ALF 관리자 자동 반영이나 주문/환불 처리까지 넓히지 않고, 공개 URL 기반 `사전 설계 산출물` 생성으로 범위를 제한했다.

> AX 인재전쟁 2026 채널톡 트랙 제출 후보: ChannelTalk ALF Knowledge Planner

## 한 문장 요약

이 플러그인은 이커머스 CS 담당자가 브랜드 홈페이지, FAQ, 배송/교환/환불 정책 URL을 주면 채널톡 ALF에 옮겨 넣을 지식 문서, 규칙, 테스트 케이스, 상담원 이관 기준, 누락 질문, 적용 가이드를 폴더 형태로 생성한다.

## MVP 비용·리소스

이 MVP는 API 키와 채널톡·브랜드 내부 데이터 없이, 로그인 없이 열람 가능한 공개 URL만 입력으로 사용한다. 실제 이 repo에서 1인 참가자가 2일 내 바잇미 풀 실행과 알라딘 라이트 실행을 만들고 검증해 구현 가능성을 실증했으며, 심사자는 같은 공개 URL과 README의 절차로 재현할 수 있다. 사람은 `gaps.md`의 미확인 정책, 문서 충돌, 상담원 이관 기준을 최종 승인하고 ALF 반영 여부를 판단한다. 이 리소스 조건에서 이 문제가 최선인 이유는 공개 문서 구조화가 Codex 스킬의 강점과 정확히 겹치기 때문이다. URL 수집, 정책 분류, 지식·규칙·테스트·이관 기준 생성까지 내부 권한 없이도 바로 검증할 수 있다.

## 입력 예시

```text
브랜드명: 바잇미
공개 URL:
- 채널톡 공식 바잇미 사례
- 바잇미 FAQ
- 바잇미 이용안내
- 대표 상품 상세 3개

요청:
채널톡 ALF에 넣을 지식 문서, 답변 규칙, 상담원 이관 기준,
배포 전 테스트 질문, 누락 정책 질문을 만들어줘.
```

## 실행 결과

풀 실행 예시([biteme](src/examples/biteme/)) / 라이트 실행 예시([aladin](src/examples/aladin/)) — 서로 다른 업종에서 동일 워크플로우가 작동함을 확인했다.

| 예시 | 업종 | 실행 깊이 | 산출물 |
| --- | --- | --- | --- |
| [src/examples/biteme/](src/examples/biteme/) | 반려동물 커머스 | 풀 실행 | 지식 문서 8개, 계약 산출 파일 13개, CSV 테스트 질문 41개, 문서 충돌 1건 기록 |
| [src/examples/aladin/](src/examples/aladin/) | 도서/음반/전자책 커머스 | 라이트 실행 | 지식 문서 3개, 규칙 발췌 1개, CSV 테스트 질문 12개, 운영자 확인 항목 6개 기록 |

## Before/After

| Before | After |
| --- | --- |
| FAQ/상품상세/정책을 사람이 복사해 지식·규칙·테스트로 수작업 분해했다. 문서 충돌은 사고가 난 뒤에야 발견되기 쉬웠다. | 공개 URL 입력 → 지식 문서 8개·테스트 41개·충돌 1건 사전 발견·`gaps.md` 자동 생성. 전부 `src/examples/biteme/` 안에서 확인 가능한 실측치다. |

## 정보 부족/실패 시 동작

- URL이 막히면 내용을 추정하지 않고 `gaps.md`의 접근 실패 항목에 URL, 실패 증상, 확인일을 적는다.
- 공개 FAQ가 동적 로딩이면 로그인 없이 접근 가능한 AJAX 응답만 수집하고 수집 방법을 출처에 남긴다.
- 정책이 빠져 있으면 `미확인`으로 표시하고, ALF 규칙에는 단정 답변 금지 또는 상담원 이관 조건을 연결한다.
- 문서끼리 충돌하면 한쪽을 선택하지 않고 `gaps.md`에 충돌 문장과 운영자 확인 질문을 남긴다.

## 사람이 최종 판단하는 지점

- 충돌 정책의 우선순위 확정.
- 상품군별 예외 정책과 상담원 이관 기준 승인.
- 환불, 하자 판정, 개인정보, 고객별 주문 상태처럼 내부 확인이 필요한 항목 처리.
- 공개 문서 업데이트 주기와 ALF 지식 갱신 담당자 지정.

## 수동 작업과 플러그인 대체 범위

| CS 담당자가 수동으로 하던 작업 | 플러그인이 대신하는 부분 | 사람이 남겨야 하는 판단 |
| --- | --- | --- |
| FAQ, 이용안내, 상품 상세를 열어 상담 의도별로 복사 | 공개 URL을 배송, 주문, 교환/반품/환불, 쿠폰, 이관 의도로 분류 | 공개되지 않은 내부 정책 제공 여부 |
| ALF 지식 문서 폴더 구조 설계 | `alf-knowledge/` 카테고리와 대표 문서 초안 생성 | 실제 운영 폴더명과 배포 범위 승인 |
| 답변 금지 규칙과 예외 조건 정리 | `alf-rules.md`에 금지 답변, 고위험 주제, 이관 조건 작성 | 충돌 정책의 최종 우선순위 확정 |
| 배포 전 테스트 질문 작성 | `alf-test-cases.csv`에 정상/예외/이관 질문 생성 | 내부 주문 데이터가 필요한 테스트 추가 |
| 애매한 정책을 메모로 남김 | `gaps.md`에 미확인 정책, 문서 충돌, 운영자 확인 질문 기록 | 확인 답변을 받아 ALF 지식에 반영 |

## 무엇이 나오나요?

사용자가 브랜드명과 공개 URL 목록을 주면 `output/<브랜드명>/` 아래에 다음 파일을 만든다.

```text
output/<브랜드명>/
  alf-knowledge/
    <지식 카테고리>/
      <문서명>.md
  alf-rules.md
  alf-test-cases.csv
  alf-escalation.md
  gaps.md
  APPLY-GUIDE.md
```

- `alf-knowledge/`: ALF 지식 관리 화면에 폴더째 옮길 수 있는 구조화 문서. 각 문서 하단에 출처 URL과 확인일을 둔다.
- `alf-rules.md`: 채널톡 규칙 입력창에 복사할 상황별 지시문. 기본 톤, 금지 답변, 정책별 규칙, 고위험 주제 처리를 포함한다.
- `alf-test-cases.csv`: ALF 배포 전 테스트 질문 30개 이상. 컬럼은 `질문,의도분류,기대답변요지,근거URL,오답위험도`다.
- `alf-escalation.md`: 상담원 이관 기준. 트리거 조건, 제외 조건, 이관 문구를 포함한다.
- `gaps.md`: 공개 사이트에 없거나 모호한 정책, 접근 실패 URL, 문서 충돌, 운영자 확인 질문.
- `APPLY-GUIDE.md`: 산출물을 채널톡 관리자 화면에 적용하고 테스트하는 단계별 가이드.

출력 계약의 상세 스키마와 품질 기준은 `src/docs/output-spec.md`에 있다.

## 예시 실행

실제 공개 자료로 실행한 풀 예시는 `src/examples/biteme/`, 라이트 예시는 `src/examples/aladin/`에 있다.

입력으로 사용한 공개 URL:

- https://channel.io/kr/blog/articles/ai-case-biteme-d3e09ab9
- https://m.biteme.co.kr/shop/community/faq_lists
- https://m.biteme.co.kr/shop/service/service_guide
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000050043
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000040999
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000006873

예시 결과:

- 지식 문서 8개
- 계약 산출 파일 총 13개
- CSV 테스트 질문 41개
- 입력 URL은 `curl -L` 점검에서 접근 실패가 발견되지 않았다.
- 확인된 문서 충돌 1건: HAX 상품의 제주/도서산간 교환 반품 추가비용

알라딘 라이트 실행 입력으로 사용한 공개 URL:

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

알라딘 라이트 예시 결과:

- 지식 문서 3개
- 규칙 발췌 1개
- CSV 테스트 질문 12개
- 운영자 확인 항목 6개
- 선택 URL은 `curl -L` 점검에서 HTTP 200 응답을 확인했다.

## 공개 근거

공식 힌트 영상 원본은 https://www.youtube.com/watch?v=5iRf37Z8Wd4 이다. 핵심 자막은 "저희 이커머스 고객사의 상담 문제를 풀고 있어요.", "커머스가 가진 많은 문제들을 AI로 에이전트를 만들고 있거든요."로, 이 문제 선택이 이커머스 상담과 AI 에이전트 방향을 직접 겨냥한다는 근거다. 전체 자막은 제출 zip의 `src/docs/source-video.ko.vtt`에 포함된다.

| 출처 URL | 발행 주체 | 확인일 | 입증하는 주장 |
| --- | --- | --- | --- |
| https://www.youtube.com/watch?v=5iRf37Z8Wd4 / `src/docs/source-video.ko.vtt` | 프라이머/채널코퍼레이션 발표 영상 자막 | 2026-07-08 | 채널톡 트랙은 이커머스 고객사의 상담 문제와 AI 에이전트 활용을 직접 힌트로 제시한다. |
| https://channel.io/kr/talk | ChannelTalk | 2026-07-08 | ALF/AI 상담은 규칙, 구조화된 지식, 실행 가능한 태스크/액션과 연결된다. |
| https://docs.channel.io/help/ko/articles/%EC%A7%80%EC%8B%9D-803f6ac9 | ChannelTalk | 2026-07-08 | ALF가 참조할 지식은 문서, 파일, 웹사이트 자료를 구조화해 관리해야 한다. |
| https://docs.channel.io/help/ko/articles/%EA%B7%9C%EC%B9%99-b43e19a1 | ChannelTalk | 2026-07-08 | ALF 규칙은 상황별 지시문, 필터, 개인화 변수, 상담 처리 액션으로 답변을 제어한다. |
| https://docs.channel.io/help/ko/articles/ALF-%ED%85%8C%EC%8A%A4%ED%8A%B8-bffe077d | ChannelTalk | 2026-07-08 | ALF는 배포 전 시나리오와 평가 기준으로 테스트해야 한다. |
| https://channel.io/kr/blog/articles/crawling-press-9b611f25 | ChannelTalk | 2026-07-08 | URL 입력과 웹 크롤링으로 AI 상담 사전 체험을 제공한다는 공개 자료다. |
| https://channel.io/kr/blog/articles/ai-case-biteme-d3e09ab9 | ChannelTalk | 2026-07-08 | 바잇미가 배송, 교환, 반품, 주문 취소 같은 반복 문의를 FAQ/ALF로 처리한 공식 사례다. |

## 작동 방식

1. 브랜드명과 공개 URL 목록을 입력받는다.
2. URL을 FAQ, 배송, 교환/반품/환불, 주문/회원, 쿠폰/적립금, 상품별 정책으로 분류한다.
3. 로그인 없이 읽을 수 있는 공개 문서와 공개 AJAX 응답만 수집한다.
4. 상담 의도별로 확정 지식, 금지 답변, 이관 기준, 테스트 질문을 만든다.
5. 접근 실패, 미확인 정책, 문서 충돌은 `gaps.md`에 남기고 ALF 규칙에서는 단정 답변을 금지한다.
6. 자체 품질 점검으로 지식 문서의 출처 URL/확인일 표기, CSV 파싱 가능 여부, 테스트 질문 수, 고위험 주제 이관 처리를 자동 스캔과 수동 검수로 확인한다.

## 제한

- 채널톡 내부 설정이나 브랜드 내부 주문/CRM 데이터에 접근한다고 주장하지 않는다.
- API 키 없이 설계되며 실제 주문 취소, 환불, 쿠폰 발급을 자동 처리하지 않는다.
- 공개 문서에 없는 정책은 `미확인`으로 표시하고 상담원 확인으로 넘긴다.

## 검증

Codex 공식 plugin-creator 스킬에 포함된 `validate_plugin.py`로 검증했으며 통과 기록은 `src/docs/verification.md`에 있다. 심사 환경에서는 로컬 마켓플레이스 등록(`codex plugin marketplace add`) 후 설치로 구동을 확인할 수 있다. 절차는 `src/docs/verification.md`의 실구동 테스트를 참조한다.

예시 실행 검증도 `src/docs/verification.md`에 기록했다.
