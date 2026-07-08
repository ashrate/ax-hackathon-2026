# 채널톡 ALF 출력물 생성 플러그인

> AX 인재전쟁 2026 채널톡 트랙 제출 후보: ChannelTalk ALF Knowledge Planner

## 한 문장 요약

이 플러그인은 이커머스 CS 담당자가 브랜드 홈페이지, FAQ, 배송/교환/환불 정책 URL을 주면 채널톡 ALF에 옮겨 넣을 지식 문서, 규칙, 테스트 케이스, 상담원 이관 기준, 누락 질문, 적용 가이드를 폴더 형태로 생성한다.

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

출력 계약의 상세 스키마와 품질 기준은 `docs/output-spec.md`에 있다.

## 예시 실행

실제 공개 자료로 실행한 예시는 `examples/biteme/`에 있다.

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
- 접근 실패 URL 0건
- 확인된 문서 충돌 1건: HAX 상품의 제주/도서산간 교환 반품 추가비용

## 공개 근거

| 출처 URL | 발행 주체 | 확인일 | 입증하는 주장 |
| --- | --- | --- | --- |
| `docs/source-video.ko.vtt` | 프라이머/채널코퍼레이션 발표 영상 자막 | 2026-07-08 | 채널톡 트랙은 이커머스 고객사의 상담 문제와 AI 에이전트 활용을 직접 힌트로 제시한다. |
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
6. 자체 품질 점검으로 출처 없는 주장 0건, CSV 파싱 가능, 테스트 질문 30개 이상을 확인한다.

## 제한

- 채널톡 내부 설정이나 브랜드 내부 주문/CRM 데이터에 접근한다고 주장하지 않는다.
- API 키 없이 설계되며 실제 주문 취소, 환불, 쿠폰 발급을 자동 처리하지 않는다.
- 공개 문서에 없는 정책은 `미확인`으로 표시하고 상담원 확인으로 넘긴다.

## 검증

```bash
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py src
```

예시 실행 검증은 `docs/verification.md`에 기록했다.
