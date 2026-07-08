# 카카오페이증권 제출용 플러그인

> AX 인재전쟁 2026 예선 제출 후보: KakaoPay Securities Risk Review Copilot

이 플러그인은 답변 생성기가 아니라 **위험 문구 제거 + 공식 근거 정리 + 에스컬레이션 판단 보조** 워크플로우입니다. 모든 `response-draft.md`는 상담사 또는 컴플라이언스 담당자가 검토 후 사용하는 답변 초안이며, 고객 발송·보상 판단·자문 이관의 마지막 게이트는 항상 사람입니다.

## 입력 예시

```text
고객 문의: "아침에 앱이 안 열려서 주문을 못 했어요. 보상해 주나요?"
맥락: 2026-07-08 오전, 앱 접속 지연 주장, 주문장애·보상 문의 가능성
요청: output/case-1 산출물로 만들어줘.
```

## 실행 결과

- [case-1 소수점 주문 검토용 초안](examples/case-1/response-draft.md): 소수점매매 체결 구조와 최신 공지 확인, 손실·추천 단정 제거.
- [case-2 장애·보상 검토용 초안](examples/case-2/response-draft.md): 보상 단정 제거, 주문장애 기준 확인과 증빙·비상주문 여부 확인으로 이관.
- [case-3 투자 판단 검토용 초안](examples/case-3/response-draft.md): 매도·보유 추천 제거, 의사결정 체크리스트와 등록 투자자문업자 확인 안내.

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

## 상담사가 줄이는 반복 작업

| 상담사가 수동으로 하던 일 | 플러그인이 대신 정리하는 부분 | 사람이 남기는 판단 |
| --- | --- | --- |
| 공지·FAQ·기준을 여러 탭에서 교차 확인 | 케이스 유형별 공식 근거 URL과 확인일을 산출물에 묶음 | 해당 근거가 최신 운영 기준과 일치하는지 승인 |
| 추천·보상·원금 보장처럼 보일 수 있는 표현 자기 검열 | `compliance-report.md`에서 위험 표현을 플래그하고 보수적 문장으로 제안 | 실제 발송 문구 채택 여부 결정 |
| 장애·보상·자문 요구의 이관 기준 정리 | `escalation.md`에 이관 조건, 이관처, 근거를 표로 정리 | 보상 접수, 고객센터 확인, 자문 이관 실행 |

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

상세 스키마와 품질 기준은 `docs/output-spec.md`에 있습니다.

## 사용하는 사람과 상황

사용자는 카카오페이증권 상담사, VOC 담당자, 상담 QA 또는 컴플라이언스 검토자입니다. 고객이 "소수점 주문이 왜 바로 체결되지 않나요?", "앱이 안 열려 주문을 못 했는데 보상되나요?", "지금 이 주식을 팔아야 하나요?"처럼 불안과 판단 요청이 섞인 문의를 남기면, 담당자는 투자 추천이나 보상 단정으로 보이지 않게 답해야 합니다. 이 플러그인은 그 상황에서 위험 문구를 제거하고 공식 근거와 이관 판단을 정리한 검토용 산출물을 만듭니다.

## 공개 근거

| 출처 URL | 발행 주체 | 확인일 | 쓰는 곳 |
| --- | --- | --- | --- |
| `docs/source-video.ko.vtt` | 프라이머/카카오페이증권 발표 영상 자막 | 2026-07-08 | 초보 투자자의 매수·매도 불안과 납득 가능한 과정 설계가 문제 힌트임을 확인 |
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
examples/
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

생성된 `dist/kakaopay-securities/submission.zip` 안의 `src/`가 플러그인 루트입니다. Codex에서 플러그인을 로드한 뒤 다음처럼 호출합니다.

```text
고객 문의: "아침에 앱이 안 열려서 주문을 못 했어요. 보상해 주나요?"
위 문의를 output/case-1 산출물로 만들어줘.
```

## 검증 방법

```bash
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py src
```

검증 기준:

1. `src/.codex-plugin/plugin.json`이 validator를 통과합니다.
2. `src/skills/main/SKILL.md`가 계약된 5개 출력물을 종착점으로 삼습니다.
3. `examples/case-1..3`에 모든 계약 파일이 존재합니다.
4. 소수점 주문 케이스는 FAQ·공지 근거와 손실 단정 금지를 포함합니다.
5. 장애·보상 케이스는 주문장애 기준 절차와 보상 단정 금지를 포함합니다.
6. 투자 판단 케이스는 특정 종목 매수·매도 추천 없이 체크리스트와 등록 투자자문업자 안내로 전환합니다.
7. 모든 검토용 초안은 사람 검토가 마지막 게이트라는 문구를 포함합니다.
