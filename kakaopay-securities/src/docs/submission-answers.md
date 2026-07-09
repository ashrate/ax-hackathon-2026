# 제출 폼 최종 답변

> 글자수는 각 답변 끝의 `(N자)` 표기를 제외하고 공백 포함으로 계산했습니다.

## 문항 ①

### 최종 답변

이 플러그인은 상담사와 컴플라이언스 담당자가 고객 문의를 검토할 때 쓰는 검토용 초안 생성, 위험 문구 검사, 이관 판단 보조 워크플로우입니다. 초보 투자자가 “지금 사야 하나요”, “팔아야 손해를 줄이나요”, “소수점 주문이 왜 바로 체결되지 않나요”, “장애 때 보상되나요”처럼 매수·매도 판단, 체결 지연, 보상 기대를 한꺼번에 묻는 상황에서 사용합니다. 고객은 손실 불안과 거래 구조 이해 부족 때문에 다음 행동을 정하기 어렵고, 상담사는 특정 종목·가격·시점 추천이나 보상 확정처럼 들리지 않게 공식 근거를 붙여 안내해야 해서 막힙니다. 그래서 문의를 쪼개 확인 질문, 공식 출처, 금지 표현 수정안, 상담·컴플라이언스 이관 여부를 정리하며, 최종 판단은 사람이 합니다. (380자)

### 사용 출처 URL

- https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING
- https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807
- https://www.kakaopaysec.com/portal/cstmnotice-obstc/dynamicPage.do
- https://www.fsc.go.kr/po010101/76239
- https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=1193&seq=149

## 문항 ②

### 최종 답변

대회 영상은 초보 투자자가 매수·매도 때 “손해 보지 않았나”, “어떻게 해야 하나”, “도움을 받을 수 있나”를 불안해하고, 상담사를 돕는 AI 시스템이 필요하다는 힌트를 주었습니다. 카카오페이증권 공식 페이지도 경험이 부족하거나 자산 규모가 적은 사용자가 소액으로 투자에 접근하도록 돕는다고 설명합니다[1]. 카카오 공식 서비스 소개는 주가 등락에 따라 마음이 흔들리고 어떤 주식을 사야 할지 모르는 고민을 직접 다룹니다[2]. KDI에 게시된 금융감독원·한국은행 금융이해력 조사는 20대 등 취약 부문의 금융행위 역량 보강 필요성을 보여줍니다[4]. 금융위의 설명의무 자료는 정보열위 소비자가 거래결과에 책임질 수 있도록 필요한 정보를 이해 가능한 방식으로 제공해야 한다고 봅니다[3]. 제 역량과 리소스 안에서는 API·내부 데이터 없이 공개 근거를 읽고 문장 위험을 줄이는 Codex형 작업이라 가장 빠르게 검증할 수 있습니다. 그래서 추천이 아니라 공식 근거, 확인 질문, 쉬운 설명, 사람 검토로 불안을 낮추는 문제를 선택했습니다. (528자)

### 사용 출처 URL

- [1] https://kakaopaysec.com/
- [2] https://www.kakaocorp.com/page/detail/10417
- [3] https://www.fsc.go.kr/po010101/76239
- [4] https://eiec.kdi.re.kr/policy/materialView.do?num=266065

## 문항 ③

### 최종 답변

작동은 README와 같이 5단계로 고정했습니다. 먼저 고객 문의를 소수점 주문·체결 지연, 앱 접속 장애·보상, 투자 판단 요청, 일반 거래 구조, 상담 초안 QA로 분류합니다. 다음으로 불안을 체결 지연, 손실 가능성, 보상 기대, 매도·보유 판단, 주문 방식 이해 부족으로 분해합니다. 이후 카카오페이증권 FAQ·공지, 주문장애 기준, 금융위·금투협 자료를 공식 근거로 매칭하고, 확인 가능한 사실과 판단할 수 없는 영역을 분리합니다. 결과는 `response-draft.md`, `checklist.md`, `compliance-report.md`, `escalation.md`, `case-log.csv` 5종으로 출력합니다. 마지막으로 종목·가격·타이밍 추천, 보상 단정, 원금·수익 보장, 불확실한 단정, 개인정보 요구가 남았는지 자체 검사합니다. 정보가 부족하거나 문의가 모호하면 답변보다 확인 질문을 먼저 만들고, 공식 근거가 없으면 “공식 확인 필요”로 표시해 담당 부서나 고객센터 확인으로 이관합니다. 모든 초안은 상담사 또는 컴플라이언스 담당자의 사람 검토가 마지막 게이트입니다. (560자)

### 사용 출처 URL

- https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING
- https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807
- https://www.kakaopaysec.com/portal/cstmnotice-obstc/dynamicPage.do
- https://www.fsc.go.kr/po010101/76239
- https://www.fsc.go.kr/edu/news/83077?curPage=11&srchCtgry=&srchKey=&srchText=
- https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=1193&seq=149
- https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=437&seq=150

## 문항 ④

### 최종 답변

AI에는 영상 자막, 카카오페이증권 FAQ·공지, 금융위·금투협 자료를 요약해 근거 맵을 만들고, 문의 유형별 출력 파일 스키마와 예시 케이스 초안을 생성하게 했습니다. 직접 판단한 것은 문제의 중심과 책임 경계입니다. 처음에는 소수점 거래 FAQ 플러그인이 근거가 강해 보였지만, 영상 정합을 최우선으로 재평가해 초보 투자자의 매수·매도 불안을 중심 문제로 바꾸고 소수점 거래는 하위 모듈로 흡수했습니다. 또 답변 생성기처럼 보인다는 피드백을 반영해 발송 문안이 아니라 상담사·컴플라이언스 담당자가 검토 후 사용하는 초안으로 전환했습니다. 막힌 지점은 카카오페이 고객센터 FAQ가 일반 fetch에서 빈 본문처럼 보인 점이었고, curl로 Next.js `qnaList` 원문을 확인해 해결했습니다. 받아들이지 않은 AI 제안은 종목 분석, 매매 타이밍 보조, 보상 가능성 추정입니다. 투자권유와 보상 단정 오해가 커서 공식 근거와 확인 절차 중심으로 제한했습니다. (485자)

### 사용 출처 URL

- https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING
- https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807
- https://www.fsc.go.kr/po010101/76239
- https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=1193&seq=149

## 문항 ⑤

### 최종 답변

검증은 실제 입력을 넣어 산출물이 만들어지는지 확인했습니다. case-1에는 “소수점 주문을 넣었는데 왜 바로 체결이 안 되나요? 손해 보는 것 아닌가요?”를 넣었고, 결과로 검토용 초안, 체크리스트, 컴플라이언스 점검, 이관 판단, 케이스 원장 5종이 생성되었습니다. live-test의 `kakaopay-case1-live`도 같은 5종 파일을 만들었고, 초안은 체결 시점·가격·손익·보상 여부를 단정하지 않았습니다. 정상 케이스는 소수점 체결 지연 안내였고, 예외 케이스는 case-3의 “지금 이 주식 팔아야 할까요?”였습니다. case-3은 매도 추천을 거절하고 목적, 기간, 손실 감내도, 등록 투자자문업자 확인 안내로 전환했습니다. 의심한 점은 규제 인용 정확성이어서 표준투자권유준칙·표준내부통제기준·금융위 자료·주문장애 기준을 원문 조항 단위로 대조했습니다. 부족한 점은 내부 상담 매뉴얼과 실제 주문 원장을 검증하지 못한 것입니다. 고친 점은 JS 뷰어 URL을 원문 노출 콘텐츠 URL로 교체하고, FAQ 빈 본문은 curl 원문 확인으로 보완한 것입니다. (545자)

### 사용 출처 URL

- https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING
- https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807
- https://www.fsc.go.kr/edu/news/83077?curPage=11&srchCtgry=&srchKey=&srchText=
- https://www.fsc.go.kr/no010101/81575
- https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=1193&seq=149
- https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=437&seq=150
- https://www.kofia.or.kr/wpge/m_168/sub04070102.do

## 글자수 요약

| 문항 | 제한 | 글자수 |
| --- | ---: | ---: |
| ① | 800자 이내 | 380자 |
| ② | 800자 이내 | 528자 |
| ③ | 1000자 이내 | 560자 |
| ④ | 800자 이내 | 485자 |
| ⑤ | 800자 이내 | 545자 |

## 전체 사용 출처 URL 목록

- https://kakaopaysec.com/
- https://www.kakaocorp.com/page/detail/10417
- https://www.fsc.go.kr/po010101/76239
- https://eiec.kdi.re.kr/policy/materialView.do?num=266065
- https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING
- https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807
- https://www.kakaopaysec.com/portal/cstmnotice-obstc/dynamicPage.do
- https://www.fsc.go.kr/edu/news/83077?curPage=11&srchCtgry=&srchKey=&srchText=
- https://www.fsc.go.kr/no010101/81575
- https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=1193&seq=149
- https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=437&seq=150
- https://www.kofia.or.kr/wpge/m_168/sub04070102.do

## 내부 근거 파일

- `docs/research.md`
- `docs/output-spec.md`
- `README.md`
- `docs/verification.md`
- `docs/engineering.md`
- `examples/case-1`
- `examples/case-2`
- `examples/case-3`
- `output/live-test/kakaopay-case1-live`

## README 수정 여부

- 수정하지 않음. README는 문항 ③의 작동 절차, 정보 부족 시 동작, 사람 검토 게이트와 이미 일치합니다.
