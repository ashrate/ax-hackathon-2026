# 카카오페이증권 — 검증 기록

> 이 파일은 submission.zip에는 포함되지 않는 작업 기록이며, 문항 ⑤와 README.md 작성의 원천 자료다.

## 1. 출력 계약 검증

확정 출력 계약:

```text
output/case-<번호>/
  response-draft.md
  checklist.md
  compliance-report.md
  escalation.md
  case-log.csv
```

예시 실행은 `examples/case-1`, `examples/case-2`, `examples/case-3`에 같은 파일명으로 생성했다.

## 2. 검증 명령

| 항목 | 명령 | 결과 | 날짜 |
| --- | --- | --- | --- |
| 플러그인 validator | `python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py src` | PASS | 2026-07-08 |
| 스킬 파일 validator | `PYTHONUTF8=1 python C:/Users/kimdo/.codex/skills/.system/skill-creator/scripts/quick_validate.py src/skills/main` | PASS | 2026-07-08 |
| 예시 산출물 트리 | `find examples -maxdepth 2 -type f | sort` | 3개 케이스, 15개 계약 파일 확인 | 2026-07-08 |
| 케이스 원장 헤더 | `rg "^날짜,문의유형,위험플래그,사용근거URL,처리결과$" examples/case-*/case-log.csv` | 3개 CSV 헤더 확인 | 2026-07-08 |

## 3. 3케이스 실행 기록

| 케이스 | 입력 | 기대 결과 | 실제 결과 | 판정 | 날짜 |
| --- | --- | --- | --- | --- | --- |
| case-1 | "소수점 주문을 넣었는데 왜 바로 체결이 안 되나요? 손해 보는 것 아닌가요?" | 소수점매매 체결 구조를 공식 FAQ·공지로 설명하고, 손실 단정과 투자 추천을 피한다. | `examples/case-1`에 5개 파일 생성. 답변 초안은 실시간 체결과 다를 수 있음을 설명하고, 손실·보상 단정을 하지 않음. | PASS | 2026-07-08 |
| case-2 | "아침에 앱이 안 열려서 주문을 못 했어요. 보상해 주나요?" | 보상 가능 여부를 단정하지 않고 주문장애 기준, 증빙, 비상주문 시도, 신청기한 확인으로 이관한다. | `examples/case-2`에 5개 파일 생성. 이관 판단은 주문장애·보상 기준 확인 담당으로 라우팅. | PASS | 2026-07-08 |
| case-3 | "지금 이 주식 팔아야 할까요? 더 떨어질까 봐 무서워요." | 특정 종목 매도 추천 없이 목적·기간·손실 감내도 체크리스트와 등록 투자자문업자 안내로 전환한다. | `examples/case-3`에 5개 파일 생성. 컴플라이언스 보고서가 고객 원문의 추천성 요청을 플래그하고 답변 초안에서 제거. | PASS | 2026-07-08 |

## 4. 산출물 존재 확인

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

## 5. 정상 상황과 예외 상황

- 정상 상황: 소수점 주문 문의는 검토용 답변 초안, 확인 질문, 공식 FAQ·공지 근거, 금지 표현 QA, 이관 기준을 함께 생성한다.
- 예외 상황 - 장애·보상: 앱 접속 불가와 보상 요구가 들어오면 보상을 단정하지 않고 주문장애 기준 확인 절차로 넘긴다.
- 예외 상황 - 투자 추천 요구: 특정 종목을 팔아야 하는지 묻는 입력은 추천을 거절하고 의사결정 체크리스트와 등록 투자자문업자 안내로 바꾼다.
- 예외 상황 - 공식 근거 부족: 답을 단정하지 않고 "공식 확인 필요"로 표시한다.
- 예외 상황 - 개인정보 포함: 산출물과 원장에 계좌번호, 주문번호 전체값, 전화번호를 옮기지 않고 인증된 고객센터 채널로 안내한다.

## 6. 의심한 점과 확인 방법

- 의심한 점: 출력이 여전히 설명서처럼 보일 수 있다.
  - 확인 방법: `docs/output-spec.md`에 파일별 스키마와 품질 기준을 만들고, `examples/case-*`에 실제 파일을 생성했다.
  - 결과: 각 케이스가 5개 파일로 끝난다.
- 의심한 점: case-2에서 보상 가능성을 암시할 수 있다.
  - 확인 방법: 카카오페이증권 주문장애 기준의 장애 정의, 비상주문, 보상 조건, 제외 기준을 근거로 라우팅했다.
  - 결과: 답변 초안은 "보상 여부는 공식 접수 후 기준 충족 여부 확인"으로만 쓴다.
- 의심한 점: case-3이 투자자문처럼 보일 수 있다.
  - 확인 방법: 금융위원회 투자자문 안내와 금융투자협회 기준을 근거로 매도·보유 판단을 제거했다.
  - 결과: 답변은 체크리스트와 등록 투자자문업자 안내로 전환된다.

## 7. 테스트하며 고친 것

- 기존 `SKILL.md`는 질문 유형 분류와 체크리스트를 출력하는 설명형 구조였다. 모든 실행이 계약 파일 생성으로 끝나도록 고쳤다.
- README를 문제 설명 중심에서 "무엇이 나오는가" 중심으로 바꿨다.
- `case-log.csv`는 각 케이스 폴더에 현재 케이스까지의 원장 스냅샷을 두는 방식으로 명문화했다.
- 소수점 FAQ는 일반 웹 fetch에서 본문이 비어 보였으나 `curl` 원문에서 FAQ 데이터가 확인되어 공식 URL을 유지했다.

## 8. 아직 부족한 것

- 실제 카카오페이증권 내부 상담 매뉴얼과 장애 접수 시스템은 접근할 수 없어 공개 자료 기반 프로토타입으로 제한된다.
- 제출 직전 FAQ, 공지, 주문장애 기준 URL의 최신성을 다시 확인해야 한다.
- 운영형 플러그인이 되려면 `output/case-<번호>/` 번호 부여와 중앙 원장 누적을 자동화하는 스크립트가 추가될 수 있다.

## 9. 인용 URL curl 점검 결과

점검 명령은 각 URL에 대해 `curl -L -o /dev/null -s -w "%{http_code}"` 형식으로 실행했다. 최초 점검은 고유 URL 33개 중 실패 1개였고, 실패 URL은 구체 페이지로 교체했다. 교체 후 현재 인용 URL 33개는 모두 `200`이다.

| URL | 상태 | 조치 |
| --- | --- | --- |
| https://apps.apple.com/kr/app/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%8E%98%EC%9D%B4/id1464496236 | 200 | 유지 |
| https://career.rememberapp.co.kr/job/posting/293435 | 200 | 유지 |
| https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=220522 | 200 | 유지 |
| https://eiec.kdi.re.kr/policy/materialView.do?num=266065 | 200 | 유지 |
| https://kakaopaysec.com/ | 200 | 유지 |
| https://kakaopaysec.com/downloadFile.do?id=8275 | 200 | 유지, 반증·보조 근거 |
| https://kakaopaysec.com/downloadFile.do?id=8276 | 200 | 유지, 반증·보조 근거 |
| https://kakaopaysec.com/portal/cstmnotice-obstc/dynamicPage.do | 200 | 유지 |
| https://law.kofia.or.kr/service/law/lawFullScreen.do?1787=&historySeq=1787&seq=149 | 200 | Claim Audit(아래)에서 lawFullScreenContent.do?historySeq=1193&seq=149로 교체 — 200이지만 JS 뷰어라 본문 미노출 |
| https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=1193&seq=149 | 200 | 유지 |
| https://law.kofia.or.kr/service/law/lawFullScreenContent.do?historySeq=437&seq=150 | 200 | 유지 |
| https://play.google.com/store/apps/details?hl=ko&id=com.kakaopay.app | 200 | 유지 |
| https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING | 200 | 유지 |
| https://support.kakaopay.com/web/phone-cs-notice | 200 | 유지 |
| https://v.daum.net/v/20260602131103925 | 200 | 유지 |
| https://www.dailian.co.kr/news/view/1557754 | 200 | 유지 |
| https://www.etnews.com/20200206000277 | 200 | 유지 |
| https://www.fsc.go.kr/edu/news/83077?curPage=11&srchCtgry=&srchKey=&srchText= | 200 | 유지 |
| https://www.fsc.go.kr/no010101/81575 | 200 | 유지 |
| https://www.fsc.go.kr/po010101/76239 | 200 | 유지 |
| https://www.kakaocorp.com/page/detail/10417 | 200 | 유지 |
| https://www.kakaopaysec.com/business/retail/dynamicPage.do | 200 | 유지 |
| https://www.kakaopaysec.com/company/about/dynamicPage.do | 200 | 유지 |
| https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807 | 200 | 유지 |
| https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=7011 | 200 | 유지 |
| https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=7314 | 200 | 유지 |
| https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=7315 | 200 | 유지 |
| https://www.kakaopaysec.com/portal/cstmnotice-obstc/dynamicPage.do | 200 | 유지 |
| https://www.kakaopaysec.com/portal/process/dynamicPage.do | 200 | 유지 |
| https://www.kofia.or.kr/wpge/m_168/sub04070102.do | 200 | 신규 채택: FSS 루트 URL 대체 |
| https://www.yna.co.kr/view/AKR20221214052400002 | 200 | 유지 |
| https://www.yna.co.kr/view/AKR20260624032600008 | 200 | 유지 |
| https://www.youtube.com/watch?v=aBuoojGjyf4 | 200 | 유지 |

교체 전 실패 URL:

| URL | 상태 | 조치 |
| --- | --- | --- |
| FSS 루트 URL(교체 전) | 000 | 핵심 근거에서 제거. 금융투자협회 제도권 금융투자회사 조회 페이지와 금융위 구체 페이지로 대체 |

## 10. 문항 ⑤ 초안

검증은 실제 대표 문의 3개를 플러그인 절차대로 실행해 `examples/case-1..3`에 계약된 5개 파일이 모두 생성되는지 확인했습니다. case-1은 "소수점 주문이 왜 바로 체결되지 않나요?"에 대해 공식 FAQ·공지 근거로 체결 구조를 설명하고 손실 단정을 피했습니다. case-2는 "앱이 안 열려 주문을 못 했는데 보상되나요?"에 대해 보상을 단정하지 않고 주문장애 기준, 증빙, 비상주문 시도, 신청기한 확인으로 이관했습니다. case-3은 "지금 이 주식 팔아야 하나요?"에 대해 매도 추천을 하지 않고 목적, 기간, 손실 감내도 체크리스트와 등록 투자자문업자 안내로 전환했습니다. 의심한 점은 투자 추천·보상 단정 오해였고, 컴플라이언스 보고서에서 금지 표현을 별도로 플래그하도록 고쳤습니다. 내부 상담 매뉴얼 검증은 아직 못 했습니다.

## Claim Audit (2026-07-08)

제출 전 정밀 대조 감사. 각 출처를 `curl -sL`로 열어 원문에서 주장을 뒷받침하는 구절을 직접 확인했다(WebFetch 요약은 교차검증용으로만 사용). 판정 기준: 지지 = 원문이 주장을 그대로 뒷받침 / 부분지지 = 주장은 맞으나 링크·문구 조정 필요 / 불지지 = 교체·삭제 / 보류 = 도구 한계로 본문 자동 확인 불가.

| 주장 | 출처 | 지지 구절(원문 인용, 짧게) | 판정 | 조치 |
| --- | --- | --- | --- | --- |
| (자막5) 출제자가 초보 투자자의 매수·매도 불안·손해 여부·도움 니즈를 직접 문제로 제시 | `docs/source-video.ko.vtt` 00:01:03-01:22 | "초보 투자자들이 매수 매도를 할 때 내가 손해 보지 않았다라든지 … 어떻게 도움을 받을 수 있을까에 대한 니즈가 있다 … 문제를 냈습니다" | 지지 | 유지 |
| (자막5) 평가 관점은 수학적 최적점보다 사용자가 납득·안심해 다음 행동하게 하는 과정 설계 | `docs/source-video.ko.vtt` 00:01:32-01:50 | "수학적인 최적점을 찾는다라는 문제라기보다도 … 납득해서 안심하고 그다음을 실행할 수 있게끔 정보를 충분히 주는지 … 제일 중요할 것 같고요" | 지지 | 유지 |
| 카카오페이증권은 경험·자산이 적은 사용자도 소액 투자하게 하는 접근성을 공식 포지션으로 둠 | kakaopaysec.com 홈 | "경험이 부족한 사용자들도 소액으로 다양한 금융 상품에 쉽게 접근할 수 있도록 … 새로운 투자 문화를 만들어 갑니다" | 지지 | 유지 |
| 카카오 서비스 소개도 주가 변동 감정 동요와 "어떤 주식 사야 할지" 고민을 직접 언급 | kakaocorp.com/page/detail/10417 | "주가가 오르락 내리락 / 내 마음도 같이 오르락 내리락" · "어떤 주식 사야 할지 모르겠다고?" | 지지 | 유지 |
| 금융이해력은 일부 계층에서 취약, 특히 20대 청년층이 금융행위 중심으로 낮음 | KDI 266065(원 발표 금감원·한국은행 공동) | "20대·70대, 저소득, 고졸 미만 등의 금융이해력이 취약한 가운데 특히 20대 청년층의 점수가 금융행위를 중심으로 상대적으로 낮게 나타남" | 지지 | 유지. UA 헤더 없으면 봇 차단(113B "정상적인 접근이 아닙니다") — 확인은 UA 지정 curl 사용 |
| 설명의무는 정보열위 소비자가 스스로 거래결과에 책임지도록 정보를 제공하게 하는 영업규제 | FSC 76239 「설명의무의 합리적 이행을 위한 가이드라인」 | "정보열위에 있는" 소비자 보호 취지 + 문서 제목이 설명의무 가이드라인 | 지지 | 유지 |
| 설명서·스크립트가 전문용어 중심이면 소비자 이해보다 판매자 편의에 치중될 수 있다는 금융위 지적 | FSC 76239 | "설명내용이 전반적으로 업계 전문용어로 구성" … "소비자 이해보다는 판매업자 편의에 치중" | 지지 | 유지(원문은 "판매업자") |
| (case-1 초안) 소수점매매는 실시간 거래가 어렵고 10분 단위로 모아 재배분 | support.kakaopay.com 소수점 FAQ | "실시간 거래는 어려워요. 10분 단위로 사용자의 주문을 모아 5분 뒤 체결분을 고객 계좌로 재배분하는 방식으로 거래를 지원해요" | 지지 | 유지 |
| (case-1 초안) 해외 소수점 거래설명서는 개정될 수 있어 최신 공지 확인 필요 | kakaopaysec 공지 6807 | "『… 소수점 거래설명서』개정 안내 … 개정하오니, 거래에 참고하시기 바랍니다"(거래설명서_2025_006호(25.09.29).pdf) | 지지 | 유지 |
| (case-2 초안·규제) 주문장애는 시스템 장애로 어떤 방법으로도 주문 불가 시로 제한, 비상주문·증빙·신청기한 조건 | kakaopaysec 주문장애 보상기준 | "'주문장애'라 함은 … 주문관련 시스템 장애로 … 어떠한 방법으로도 주문이 불가능한 경우" · "비상주문 시도를 하지 않은 경우 보상대상에서 제외될 수 있습니다" | 지지 | 유지 |
| (case-2 초안) 앱 접속·서비스 지연 공지 실재 | kakaopaysec 공지 7011 | "접속 및 서비스 지연 현상 안내 … 접속이 정상적으로 되지 않는 지연 현상이 있었고, 현재는 정상화되었습니다" | 지지 | 유지 |
| 문의 채널은 평일 08:00-18:00 안내 | support.kakaopay.com 전화상담 안내 | "평일 08:00~18:00 증권계좌, 펀드, 주식 문의"(일반 문의는 09:00~18:00) | 지지 | 유지 |
| (규제·case-1/3) 표준투자권유준칙: 투자권유 불원 투자자에겐 권유 행위 금지, 객관적 정보만 제공 | 금투협 표준투자권유준칙 | "임직원등은 투자권유를 희망하지 않는 투자자에 대하여는 투자권유에 해당하는 행위를 하여서는 아니 되며, 투자자가 원하는 객관적인 정보만을 제공하여야 한다" | 부분지지(링크 조정) | 인용 URL을 lawFullScreen.do(JS 뷰어, 본문 빈값) → lawFullScreenContent.do?historySeq=1193&seq=149(원문 노출)로 교체. evidence.md·README.md·case-1 compliance·case-3 draft/escalation/case-log 6곳 반영 |
| (규제·case-1/2/3) 표준내부통제기준: 불확실 사항을 확실하다고 오인하게 하는 내용 금지 | 금투협 표준내부통제기준 4.1.3.4 | "불확실한 사항에 대하여 단정적 판단을 제공하거나 확실하다고 오인하게 할 소지가 있는 내용을 알리는 행위"(부당권유 금지) | 지지 | 유지(URL lawFullScreenContent.do 형식으로 이미 정확) |
| (규제·case-3) 금융위: 1:1 투자자문은 정식 등록 투자자문업자만 가능, 원금·고수익 보장 주의, 유사투자자문 피해 신고 경로 | FSC 83077(유사투자자문 자본시장법 시행 보도) | "1:1 투자자문은 금융위원회에 정식 등록된 투자자문업자만 가능하다" · "원금이나 고수익 … 현혹되지 않도록 주의" · "금융감독원 홈페이지(fss.or.kr) > 민원・신고 > 불법금융신고센터 > 유사투자자문 피해 신고" | 지지 | 유지 |
| (규제·case-1/2) 손실보전·이익보장 문구 및 원금·고수익 보장 광고 주의 | FSC 83077 | "손실보전, 이익보장 등의 문구 또는 금융회사로 오인할 수 있는 표시 또는 광고 등을 할 수 없으므로" | 지지 | 유지(손실보전·이익보장 문구 실제 포함 확인) |
| 금융위: 개별투자자문은 등록 투자자문업자만, 원금·수익 보장·손실보전 약정은 불법 | FSC 81575 | "등록된 투자자문업자만 가능한 업무입니다" · "원금이나 고수익 보장 광고에 속지마세요" · "손실보전", "이익보장 약속 및 허위" | 지지 | 유지 |
| 금투협 투자자지원센터는 제도권 금융투자회사 조회·불법 금융투자업 신고 안내 제공 | kofia.or.kr sub04070102 | "제도권 금융투자회사 조회" · "불법 금융투자업 신고센터" | 지지 | 유지 |
| 카카오페이증권에 시세 감지 주문·주식 모으기 등 투자 보조 기능이 이미 존재 | kakaopaysec.com 홈(+PDF 8276) | 홈 원문 "시세 감지 주문" · "모으기" 확인. 종목추천서비스 설명서는 PDF(8276)로 generic fetch 실패 | 부분지지 | 유지. 반증·보조 근거로만 사용, 종목추천 PDF 본문은 도구 한계로 보류 처리(evidence.md 기존 caveat 유지) |

감사 요약: 감사 19건 = 지지 17, 부분지지 2(표준투자권유준칙 링크 조정, 시세감지 홈+PDF 일부 보류), 불지지 0, 보류 0(종목추천 PDF 본문 1건은 부분지지 내 도구 한계 보류). 규제 인용(표준투자권유준칙·표준내부통제기준·투자자문 유의사항·주문장애 보상기준)은 4건 모두 원문 조항 수준에서 정확. 유일한 조치는 표준투자권유준칙 인용 URL을 원문이 노출되는 콘텐츠 엔드포인트로 교체(evidence.md, README.md, case-1/compliance-report.md, case-3/response-draft.md·escalation.md·case-log.csv 6개 파일). 가드레일(추천·보상 단정 금지) 문구는 변경 없이 유지.
