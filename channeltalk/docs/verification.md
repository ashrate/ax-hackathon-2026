# 채널톡 — 검증 기록

> 이 파일은 submission.zip에는 포함되지 않는 작업 기록이며, 문항 ⑤와 README.md 작성의 원천 자료다.

## 1. 테스트 시나리오

| 입력 | 기대 결과 | 실제 결과 | 판정 | 날짜 |
| --- | --- | --- | --- | --- |
| 바잇미 공개 URL 6개와 “ALF 출력 계약대로 만들어줘” | `examples/biteme/` 아래 지식 문서, 규칙, CSV 테스트, 이관 기준, gaps, 적용 가이드가 생성된다. | 계약 산출 파일 13개 생성, 지식 문서 8개, 테스트 질문 41개 생성 | PASS | 2026-07-08 |
| 환불 가능 기간이 상품별로 다르게 적힌 공개 상품 상세 | 공통 정책으로 단정하지 않고 상품별 예외와 운영자 확인 질문을 만든다. | HAX 2일, 케스티/이츠독 7일로 분리하고 `gaps.md`와 `alf-rules.md`에 단정 금지를 기록 | PASS | 2026-07-08 |
| 같은 상품 페이지 안의 제주/도서산간 교환 반품 추가비용 충돌 | conflict로 표시하고 사람이 확인해야 할 질문을 만든다. | HAX 상품 추가비 4,000원/3,000원 충돌을 `gaps.md` 문서 충돌로 기록 | PASS | 2026-07-08 |
| 공개 FAQ 본문이 기본 화면이 아니라 AJAX로 로딩되는 상황 | 로그인 없이 접근 가능한 공개 응답만 사용하고 수집 방법을 남긴다. | `faq_lists_ajax?page=1..4`에서 38개 FAQ를 확인하고 출처 수집 방법에 기록 | PASS | 2026-07-08 |
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
  - 접근 실패 URL 0건
  - 문서 충돌 1건: HAX 상품 제주/도서산간 교환 반품 추가비용
- 확인한 것:
  - 모든 지식 문서에 출처 URL과 확인일이 있다.
  - CSV는 Python `csv.DictReader`로 파싱 가능했다.
  - 테스트 질문 수가 출력 계약의 30개 이상 기준을 넘었다.
  - 고위험 질문은 환불/하자/오배송/주문상태 추정 대신 상담원 확인으로 처리했다.

## 5. 아직 부족한 것

- 실제 이커머스 사이트 URL 2~3개로 추가 실행해 산출물 품질을 비교해야 한다.
- ChannelTalk ALF의 최신 공개 문서가 바뀌면 `src/references/evidence.md`의 URL 확인일을 갱신해야 한다.
- 실제 고객사 내부 정책 문서는 사용할 수 없으므로 공개 샘플 기반 검증에 머문다.
- 바잇미 내부 주문/CRM/상담 데이터는 사용하지 않았으므로 고객별 주문 상태를 검증하지 못한다.

## 6. 테스트하며 고친 것

- 기존 스킬이 범용 문제 발굴 도우미라 실제 ALF 준비 플러그인으로 보이지 않았다. `SKILL.md`를 회사별 최종 문제, 입력, 절차, 출력물 중심으로 고쳤다.
- 제출 zip에 `docs/research.md`가 들어가지 않기 때문에 `src/references/evidence.md`를 추가해 플러그인 소스 안에도 근거 맵이 남도록 고쳤다.
- 패키징 후 zip 내부에 `src/references/evidence.md`, `src/skills/main/SKILL.md`, `README.md`, `logs/repo/`, `logs/channeltalk/`가 포함되는지 확인했다.
- 새 지침에 따라 `docs/output-spec.md`를 추가하고, 출력 계약을 중심으로 `SKILL.md`와 README를 다시 맞췄다.
- 예시 실행 중 HAX 상품의 추가 교환 반품비용 충돌을 발견해 확정 규칙에 넣지 않고 `gaps.md`와 이관 규칙으로 넘겼다.
- `alf-test-cases.csv`를 Python CSV 파서로 확인해 41개 질문이 정상 파싱되는 것을 확인했다.

## 7. 답변 초안

### 문항 ⑤ 어떻게 검증했나요? (800자 제한)

검증은 세 층으로 잡았습니다. 첫째, 구조 검증으로 `src/.codex-plugin/plugin.json`과 `skills/main/SKILL.md`가 validator를 통과하는지 확인합니다. 둘째, 정상 입력으로 이커머스 FAQ와 배송·교환·환불 정책 텍스트를 넣어 상담 의도별 지식 맵, 답변 규칙, 금지 답변, 상담원 이관 기준, 테스트 질문이 나오는지 봅니다. 셋째, 예외 입력으로 환불 기간이 서로 다른 두 문장을 넣어 한쪽을 추정하지 않고 conflict와 사람 확인 질문을 내는지 확인합니다. 의심한 점은 AI가 내부 ALF 설정을 아는 것처럼 말하거나 정책을 단정하는 것이었고, 이를 막기 위해 공개 문서 기반 준비 산출물로 범위를 줄이고 high risk, missing, conflict 표시를 넣었습니다. 아직 실제 고객사 내부 정책으로는 검증하지 못했고 공개 샘플 기반이라는 한계가 있습니다.
