# 카카오페이증권 제출용 플러그인

> AX 인재전쟁 2026 예선 제출 후보: KakaoPay Securities Response Copilot

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

- `response-draft.md`: 고객에게 그대로 보낼 수 있는 쉬운 답변 문안입니다. 공식 근거 URL 각주와 투자·보상·최신성 유의 문구를 포함합니다.
- `checklist.md`: 답변 전 고객에게 물어볼 확인 질문과 다음 행동 단계입니다.
- `compliance-report.md`: 종목·가격·타이밍 추천성 표현, 보상 단정, 원금·수익 보장 표현을 검사하고 수정안을 냅니다.
- `escalation.md`: 장애·보상 문의, 투자자문 요구, 공식 근거 부족 케이스를 어디로 넘길지 판단합니다.
- `case-log.csv`: 날짜, 문의유형, 위험플래그, 사용근거URL, 처리결과를 누적하는 원장 스냅샷입니다.

상세 스키마와 품질 기준은 `docs/output-spec.md`에 있습니다.

## 사용하는 사람과 상황

사용자는 카카오페이증권 상담사 또는 VOC 담당자입니다. 고객이 "소수점 주문이 왜 바로 체결되지 않나요?", "앱이 안 열려 주문을 못 했는데 보상되나요?", "지금 이 주식을 팔아야 하나요?"처럼 불안과 판단 요청이 섞인 문의를 남기면, 담당자는 투자 추천이나 보상 단정으로 보이지 않게 답해야 합니다. 이 플러그인은 그 상황에서 고객 답변 초안과 내부 확인·이관 문서를 한 번에 만듭니다.

## 공개 근거

| 출처 URL | 발행 주체 | 확인일 | 쓰는 곳 |
| --- | --- | --- | --- |
| `docs/source-video.ko.vtt` | 프라이머/카카오페이증권 발표 영상 자막 | 2026-07-08 | 초보 투자자의 매수·매도 불안과 납득 가능한 과정 설계가 문제 힌트임을 확인 |
| https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING | 카카오페이 고객센터 | 2026-07-08 | 소수점매매가 실시간 체결과 다를 수 있음을 안내하는 근거 |
| https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807 | 카카오페이증권 | 2026-07-08 | 해외주식 소수점 거래설명서와 유의사항이 개정될 수 있음을 확인 |
| https://kakaopaysec.com/portal/cstmnotice-obstc/dynamicPage.do | 카카오페이증권 | 2026-07-08 | 주문장애 정의, 비상주문, 보상 기준, 보상 제외 기준 |
| https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=7011 | 카카오페이증권 | 2026-07-08 | 앱 접속 및 서비스 지연 공지 사례 |
| https://support.kakaopay.com/web/phone-cs-notice | 카카오페이 고객센터 | 2026-07-08 | 고객센터 상담 채널 안내 |
| https://www.fsc.go.kr/edu/news/83077?curPage=11&srchCtgry=&srchKey=&srchText= | 금융위원회 | 2026-07-08 | 1:1 투자자문은 등록 투자자문업자 영역, 원금·고수익 보장 주의, 금융감독원 신고 안내 |
| https://www.fsc.go.kr/po010101/76239 | 금융위원회 | 2026-07-08 | 쉬운 설명과 중요 정보 중심 안내 필요성 |
| https://law.kofia.or.kr/service/law/lawFullScreen.do?1787=&historySeq=1787&seq=149 | 금융투자협회 | 2026-07-08 | 투자권유를 원하지 않는 투자자에게 객관 정보만 제공해야 한다는 기준 |
| https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=437&seq=150 | 금융투자협회 | 2026-07-08 | 불확실한 사항에 대한 단정적 판단 금지와 설명·위험고지 기준 |
| https://www.fss.or.kr/ | 금융감독원 | 2026-07-08 | 제도권 금융회사 조회와 민원·불법금융신고 경로 안내 |

## 작동 방식

1. 문의를 소수점 주문·체결 지연, 앱 접속 장애·보상, 투자 판단 요청, 일반 거래 구조, 상담 초안 QA로 분류합니다.
2. 고객의 불안을 체결 지연, 손실 가능성, 보상 가능성, 매도·보유 판단, 주문 방식 이해 부족으로 분해합니다.
3. `src/references/evidence.md`의 공식 근거 맵에서 FAQ, 공지, 주문장애 기준, 금융위·금감원·금투협 자료를 연결합니다.
4. 공식 근거로 확인 가능한 사실과 확인 불가능한 판단을 분리합니다.
5. 계약된 5개 파일을 생성합니다.
6. 마지막에 추천성 표현, 보상 단정, 원금·수익 보장 표현, 불확실한 단정, 개인정보 요구가 남아 있는지 자체 검사합니다.

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
6. 투자 판단 케이스는 특정 종목 매수·매도 추천 없이 체크리스트와 등록 투자자문업자 안내로 답합니다.
