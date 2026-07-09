# 카카오페이증권 제출용 플러그인

> AX 인재전쟁 2026 예선 제출 후보: KakaoPay Securities Risk Review Copilot

이 플러그인은 답변 생성기가 아니라 **위험 문구 제거 + 공식 근거 정리 + 에스컬레이션 판단 보조** 워크플로우입니다. 모든 `response-draft.md`는 상담사 또는 컴플라이언스 담당자가 검토 후 사용하는 답변 초안이며, 고객 발송·보상 판단·자문 이관의 마지막 게이트는 항상 사람입니다.

## 심사자 5분 재현 가이드

1. 복붙 가능한 입력 프롬프트(case-1 문의 예시):

```text
고객 문의: "소수점 주문을 넣었는데 왜 바로 체결이 안 되나요? 손해 보는 것 아닌가요?"
맥락: 해외주식 소수점 주문, 체결 지연과 손실 불안, 투자 추천·장애 여부는 불명확
요청: output/case-1 산출물로 만들어줘.
```

2. 예상 출력 폴더: `output/case-1/`이며, 동일 계약은 `output/case-N/` 형식으로 반복됩니다.
3. 먼저 볼 핵심 파일 3개(zip 경로): [src/examples/case-3/response-draft.md](src/examples/case-3/response-draft.md), [src/examples/case-3/compliance-report.md](src/examples/case-3/compliance-report.md), [src/examples/case-1/checklist.md](src/examples/case-1/checklist.md).
4. 실패 처리 예시: "앱이 이상해서 손해 봤어요"처럼 모호한 문의는 보상 여부를 말하기 전에 발생 시각, 채널, 오류 화면, 비상주문 시도 여부를 확인 질문으로 먼저 냅니다.
5. 사람이 판단할 지점: 상담사 또는 컴플라이언스 담당자가 실제 고객 상황과 회사 응대 기준을 확인해 발송 승인 게이트를 통과시킵니다.

## 상담사가 줄이는 반복 작업

실측 근거는 예시 케이스마다 계약된 5종 파일(`response-draft.md`, `checklist.md`, `compliance-report.md`, `escalation.md`, `case-log.csv`)이 있고, 규제·공식 근거를 verbatim 인용으로 남긴다는 점입니다. 시간 절감 수치는 창작하지 않았습니다.

| 상담사가 줄이는 반복 작업 | 대신 확인하는 출력 파일 | 실제로 줄어드는 손작업 |
| --- | --- | --- |
| FAQ·공지·금투협·금융위 근거 교차 탐색 | `response-draft.md`, `compliance-report.md` | 케이스별 공식 URL, 확인일, 원문 인용을 한 번에 대조 |
| 추천성 표현 자기 검열 | `compliance-report.md` | 종목·가격·타이밍 추천처럼 보이는 문장을 플래그하고 보수적 표현으로 수정 |
| 보상 단정 표현 제거 | `response-draft.md`, `compliance-report.md` | 보상 가능·확정처럼 읽히는 표현을 확인 절차와 증빙 요청으로 전환 |
| 이관 문구 작성 | `escalation.md` | 장애·보상 접수, 고객센터 확인, 투자자문 이관 문구와 조건을 표로 정리 |

## 왜 이 문제, 왜 이 범위인가

공식 영상 힌트는 초보 투자자가 매수·매도와 손실 가능성 앞에서 불안해하고 상담 지원 AI가 그 불안을 낮춰야 한다는 방향과 맞닿아 있습니다. 내부 API나 고객 데이터 없이 공식 공개 자료(FAQ·공지·금융위·금투협 기준)만으로 재현되므로 zip 심사와 repo 검증 모두에 맞습니다. 문장 점검, 근거 정리, 위험 플래그는 Codex가 빠르게 반복 품질을 낼 수 있는 작업입니다. 규제 리스크는 고객 답변 자동화가 아니라 상담사·컴플라이언스가 검토하는 초안 포지션으로 통제하므로 이 범위가 최선입니다.

## MVP 비용·리소스

API 키·내부 데이터·고객 계정 없이 공식 공개 자료(FAQ·공지·감독당국 문서)만으로 1인 2일 내 구현과 실증이 가능하며, 심사자는 제출 zip의 `src/` 자료와 예시 케이스만으로 같은 흐름을 재현할 수 있습니다.

## 입력 예시

```text
고객 문의: "소수점 주문을 넣었는데 왜 바로 체결이 안 되나요? 손해 보는 것 아닌가요?"
맥락: 해외주식 소수점 주문, 체결 지연과 손실 불안, 투자 추천·장애 여부는 불명확
요청: output/case-1 산출물로 만들어줘.
```

## 실행 결과

- [case-1 소수점 주문 검토용 초안](src/examples/case-1/response-draft.md): 소수점매매 체결 구조와 최신 공지 확인, 손실·추천 단정 제거.
- [case-2 장애·보상 검토용 초안](src/examples/case-2/response-draft.md): 보상 단정 제거, 주문장애 기준 확인과 증빙·비상주문 여부 확인으로 이관.
- [case-3 투자 판단 검토용 초안](src/examples/case-3/response-draft.md): 매도·보유 추천 제거, 의사결정 체크리스트와 등록 투자자문업자 확인 안내.

각 케이스는 `response-draft.md`, `checklist.md`, `compliance-report.md`, `escalation.md`, `case-log.csv` 5개 파일로 끝납니다.

## 정보 부족/실패 시 동작

- 공식 FAQ·공지·규제 근거가 없으면 결론을 내리지 않고 `공식 확인 필요`로 표시합니다.
- 장애인지 단순 접속 지연인지 불명확하면 보상 여부를 말하지 않고 발생 시각, 채널, 오류 화면, 비상주문 시도 여부를 확인합니다.
- 투자 판단 요청이면 종목·가격·시점 답변을 거절하고 목적, 기간, 손실 감내도, 객관 정보 확인 질문으로 전환합니다.
- 고객 계좌나 주문 내역이 필요하면 공개 산출물에 세부값을 쓰지 않고 인증된 고객센터 채널 확인으로 안내합니다.

## 사람이 최종 판단하는 지점

| 최종 판단 | 사람이 확인할 내용 | 플러그인이 대신하는 반복 작업 |
| --- | --- | --- |
| 발송 승인 | 답변 초안이 실제 고객 상황과 회사 응대 기준에 맞는지 확인 | 금지 표현 제거, 공식 URL 각주 정리, 최신 공지 확인 필요 표시 |
| 보상 판단 | 주문장애 기준 충족, 증빙, 비상주문 시도, 신청기한 등 내부 절차 확인 | 보상 단정 문구 제거, 주문장애 기준·공지·고객센터 경로 교차 확인 |
| 자문 이관 | 고객 요구가 일반 정보인지 1:1 투자자문인지 판단 | 특정 종목·가격·타이밍 추천성 표현 플래그, 등록 투자자문업자 확인 안내 근거 정리 |

## 무엇이 나오는가

상담사 또는 VOC 담당자가 고객 문의 텍스트와 시간대·채널 같은 맥락을 붙여넣으면, 플러그인은 `output/case-<번호>/` 아래에 바로 검토 가능한 5개 파일을 생성합니다.

```text
output/case-<번호>/
  response-draft.md
  checklist.md
  compliance-report.md
  escalation.md
  case-log.csv
```

- `response-draft.md`: 상담사 또는 컴플라이언스 담당자가 검토 후 사용하는 답변 초안입니다. 공식 근거 URL 각주와 투자·보상·최신성 유의 문구를 포함합니다.
- `checklist.md`: 답변 전 고객에게 물어볼 확인 질문과 다음 행동 단계입니다.
- `compliance-report.md`: 종목·가격·타이밍 추천성 표현, 보상 단정, 원금·수익 보장 표현을 검사하고 수정안을 냅니다.
- `escalation.md`: 장애·보상 문의, 투자자문 요구, 공식 근거 부족 케이스를 어디로 넘길지 판단합니다.
- `case-log.csv`: 날짜, 문의유형, 위험플래그, 사용근거URL, 처리결과를 누적하는 원장 스냅샷입니다.

상세 스키마와 품질 기준은 `src/docs/output-spec.md`에 있습니다.

## 사용하는 사람과 상황

사용자는 카카오페이증권 상담사, VOC 담당자, 상담 QA 또는 컴플라이언스 검토자입니다. 고객이 "소수점 주문이 왜 바로 체결되지 않나요?", "앱이 안 열려 주문을 못 했는데 보상되나요?", "지금 이 주식을 팔아야 하나요?"처럼 불안과 판단 요청이 섞인 문의를 남기면, 담당자는 투자 추천이나 보상 단정으로 보이지 않게 답해야 합니다. 이 플러그인은 그 상황에서 위험 문구를 제거하고 공식 근거와 이관 판단을 정리한 검토용 산출물을 만듭니다.

## 공식 힌트 영상

- 원본: https://www.youtube.com/watch?v=aBuoojGjyf4
- 핵심 자막: "초보 투자자들이 매수 매도를 할 때 내가 손해 보지 않았다라든지", "어떻게 도움을 받을 수 있을까"라는 니즈가 문제 힌트입니다.
- 핵심 자막: 평가는 "납득해서 안심하고 그다음을 실행할 수 있게끔 정보를 충분히 주는지"를 본다는 관점입니다.
- 전체 자막은 제출 zip의 `src/docs/source-video.ko.vtt`에 포함했습니다.

## 공개 근거

| 출처 URL | 발행 주체 | 확인일 | 쓰는 곳 |
| --- | --- | --- | --- |
| https://www.youtube.com/watch?v=aBuoojGjyf4 (`src/docs/source-video.ko.vtt` 자막 사본) | 프라이머/카카오페이증권 발표 영상 | 2026-07-08 | 초보 투자자의 매수·매도 불안과 납득 가능한 과정 설계가 문제 힌트임을 확인 |
| https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING | 카카오페이 고객센터 | 2026-07-08 | 소수점매매가 실시간 체결과 다를 수 있음을 안내하는 근거 |
| https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807 | 카카오페이증권 | 2026-07-08 | 해외주식 소수점 거래설명서와 유의사항이 개정될 수 있음을 확인 |
| https://kakaopaysec.com/portal/cstmnotice-obstc/dynamicPage.do | 카카오페이증권 | 2026-07-08 | 주문장애 정의, 비상주문, 보상 기준, 보상 제외 기준 |
| https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=7011 | 카카오페이증권 | 2026-07-08 | 앱 접속 및 서비스 지연 공지 사례 |
| https://support.kakaopay.com/web/phone-cs-notice | 카카오페이 고객센터 | 2026-07-08 | 고객센터 상담 채널 안내 |
| https://www.fsc.go.kr/edu/news/83077?curPage=11&srchCtgry=&srchKey=&srchText= | 금융위원회 | 2026-07-08 | 투자자문 이용 전 등록 여부 확인, 원금·고수익 보장 주의, 피해 신고 안내 |
| https://www.fsc.go.kr/no010101/81575 | 금융위원회 | 2026-07-08 | 1:1 개별투자자문, 원금·수익 보장, 손실보전 약정 금지 근거 |
| https://www.fsc.go.kr/po010101/76239 | 금융위원회 | 2026-07-08 | 쉬운 설명과 중요 정보 중심 안내 필요성 |
| https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=1193&seq=149 | 금융투자협회 | 2026-07-08 | 투자권유를 원하지 않는 투자자에게 객관 정보만 제공해야 한다는 기준 |
| https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=437&seq=150 | 금융투자협회 | 2026-07-08 | 불확실한 사항에 대한 단정적 판단 금지와 설명·위험고지 기준 |
| https://www.kofia.or.kr/wpge/m_168/sub04070102.do | 금융투자협회 | 2026-07-08 | 제도권 금융투자회사 조회와 불법 금융투자업체 주의 안내 |

## 작동 방식

1. 문의를 소수점 주문·체결 지연, 앱 접속 장애·보상, 투자 판단 요청, 일반 거래 구조, 상담 초안 QA로 분류합니다.
2. 고객의 불안을 체결 지연, 손실 가능성, 보상 가능성, 매도·보유 판단, 주문 방식 이해 부족으로 분해합니다.
3. `src/references/evidence.md`의 공식 근거 맵에서 FAQ, 공지, 주문장애 기준, 금융위·금감원·금투협 자료를 연결합니다.
4. 공식 근거로 확인 가능한 사실과 확인 불가능한 판단을 분리합니다.
5. 계약된 5개 파일을 생성합니다.
6. 마지막에 추천성 표현, 보상 단정, 원금·수익 보장 표현, 불확실한 단정, 개인정보 요구가 남아 있는지 자체 검사합니다.
7. 상담사 또는 컴플라이언스 담당자의 최종 검토 전에는 고객 발송, 보상 확정, 투자자문 결론으로 쓰지 않습니다.

정보가 부족하면 고객 답변을 단정하지 않고 확인 질문을 우선합니다. 공식 근거가 없는 주제는 "공식 확인 필요"로 표시하고 상담사 또는 담당 부서 확인으로 넘깁니다.

## 예시 실행

```text
src/examples/
  case-1/
    response-draft.md
    checklist.md
    compliance-report.md
    escalation.md
    case-log.csv
  case-2/
    response-draft.md
    checklist.md
    compliance-report.md
    escalation.md
    case-log.csv
  case-3/
    response-draft.md
    checklist.md
    compliance-report.md
    escalation.md
    case-log.csv
```

- case-1: "소수점 주문을 넣었는데 왜 바로 체결이 안 되나요? 손해 보는 것 아닌가요?" → 소수점매매 체결 구조를 설명하고 손실·장애 단정을 피합니다.
- case-2: "아침에 앱이 안 열려서 주문을 못 했어요. 보상해 주나요?" → 보상 단정을 금지하고 주문장애 기준 확인 절차로 이관합니다.
- case-3: "지금 이 주식 팔아야 할까요? 더 떨어질까 봐 무서워요." → 매도 추천 없이 목적·기간·손실 감내도 체크리스트와 등록 투자자문업자 안내로 전환합니다.

## 설치·실행 방법

제출 zip 생성:

```bash
python tools/make_submission.py kakaopay-securities
```

생성된 `dist/kakaopay-securities/submission.zip` 안의 `src/`가 플러그인 루트입니다. `src/`에는 실행 스킬, 근거 맵, 예시 산출물, 핵심 docs 사본이 함께 들어가며, 전체 영상 자막은 `src/docs/source-video.ko.vtt`에서 확인할 수 있습니다.

```text
src/.codex-plugin/plugin.json
src/skills/main/SKILL.md
src/references/evidence.md
src/docs/source-video.ko.vtt
src/docs/output-spec.md
src/docs/submission-answers.md
src/docs/research.md
src/docs/verification.md
src/examples/case-1/
src/examples/case-2/
src/examples/case-3/
```

Codex에서 플러그인을 로드한 뒤 다음처럼 호출합니다.

```text
고객 문의: "소수점 주문을 넣었는데 왜 바로 체결이 안 되나요? 손해 보는 것 아닌가요?"
위 문의를 output/case-1 산출물로 만들어줘.
```

## 검증 방법

```bash
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py src
```

검증 기준:

1. `src/.codex-plugin/plugin.json`이 validator를 통과합니다.
2. `src/skills/main/SKILL.md`가 계약된 5개 출력물을 종착점으로 삼습니다.
3. `src/examples/case-1/ · src/examples/case-2/ · src/examples/case-3/`에 모든 계약 파일이 존재합니다.
4. 소수점 주문 케이스는 FAQ·공지 근거와 손실 단정 금지를 포함합니다.
5. 장애·보상 케이스는 주문장애 기준 절차와 보상 단정 금지를 포함합니다.
6. 투자 판단 케이스는 특정 종목 매수·매도 추천 없이 체크리스트와 등록 투자자문업자 안내로 전환합니다.
7. 모든 검토용 초안은 사람 검토가 마지막 게이트라는 문구를 포함합니다.
