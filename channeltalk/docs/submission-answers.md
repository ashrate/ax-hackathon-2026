# 채널톡 트랙 제출 답변

글자수는 각 답변 본문 기준이며 공백을 포함해 계산했다.

## 문항 ①

`ChannelTalk ALF Knowledge Planner`는 브랜드의 공개 FAQ와 정책 URL을 읽어 채널톡 ALF에 옮길 지식 문서, 응답 규칙, 상담원 이관 기준, 테스트 질문, 누락 질문을 생성하는 Codex 플러그인입니다. 이커머스 CS/CX 담당자, 쇼핑몰 운영자, AX 컨설턴트가 프로모션·신상품·배송 이슈로 반복 문의가 늘었지만 개발자나 내부 데이터 없이 ALF 도입 초안을 준비해야 할 때 사용합니다. 사용자는 홈페이지, FAQ, 상품 상세, 고객센터 문서처럼 사람이 읽기 위한 정보가 흩어져 있어 AI가 안전하게 답할 구조화 지식과 금지/이관 규칙으로 바꾸는 데서 막힙니다. 바잇미뿐 아니라 도서/음반/전자책 커머스인 알라딘 라이트 실행에서도 같은 흐름으로 지식·규칙·테스트·gaps가 생성되어 업종 일반성을 확인했습니다. (417자)

## 문항 ②

이 문제를 선택한 이유는 채널톡 트랙의 핵심 힌트가 이커머스 상담 문제와 AI 에이전트였고, 공식 제품 문서가 ALF 성공 조건을 규칙, 구조화된 지식, 실행 가능한 태스크로 설명하기 때문입니다[1]. 채널톡은 URL 입력만으로 홈페이지 자료를 수집해 AI 상담 환경을 사전 체험하는 기능을 냈으므로[2], 공개 사이트 정보를 ALF 준비물로 바꾸는 흐름은 제품 방향과 맞습니다. 실제 막힘은 운영자 쪽에 있습니다. FAQ와 정책은 사람이 읽는 문서라 ALF가 참조할 지식 구조[3]와 상황별 규칙[4]으로 나뉘어 있지 않고, 반복 문의와 프로모션 상담량 폭증으로 CS팀이 중요한 상담을 놓치는 상황[5]에서 테스트 질문과 이관 기준까지 동시에 만들어야 합니다. 그래서 API 키나 내부 고객 데이터 없이도 공개 URL 기반으로 재현 가능한 이 문제를 골랐습니다. (427자)

문항 ② 출처 URL:

- [1] https://channel.io/kr/talk
- [2] https://channel.io/kr/blog/articles/crawling-press-9b611f25
- [3] https://docs.channel.io/help/ko/articles/%EC%A7%80%EC%8B%9D-803f6ac9
- [4] https://docs.channel.io/help/ko/articles/%EA%B7%9C%EC%B9%99-b43e19a1
- [5] https://channel.io/kr/blog/articles/ai-cs-best-cases-6a7fd39d

## 문항 ③

플러그인은 브랜드명과 공개 URL을 받으면 입력을 출처 단위로 기록하고 FAQ, 배송, 교환/반품/환불, 주문/회원, 쿠폰, 상품별 정책으로 분류합니다. 로그인 없이 읽을 수 있는 공개 본문과 AJAX 응답만 수집하고, 각 카테고리에 대해 ALF 지식 문서, 규칙, 이관 기준, CSV 테스트 질문, gaps, 적용 가이드를 만듭니다. 지식은 고객에게 답해도 되는 확정 문장, 답변 시 주의, 상담원 확인 필요, 출처 URL/확인일로 나눕니다. 판단 기준은 공식·공개 출처 우선, 출처 없는 정책 단정 금지, 상품별 예외 분리, 내부 주문/CRM 데이터 추정 금지입니다. URL 접근에 실패하면 재시도 후 `gaps.md`에 URL·증상·확인일을 남기고 내용을 추정하지 않습니다. 문서에 없는 정책은 `미확인`으로 표시하고 규칙에는 답변 금지나 상담원 연결을 둡니다. 문서끼리 충돌하면 한쪽을 고르지 않고 충돌 문장과 운영자 확인 질문을 남깁니다. 환불, 결제 취소, 상품 하자, 개인정보처럼 고위험 주제는 ALF가 확정 답변하지 않고 추가 확인 질문 또는 상담원 이관으로 처리합니다. (551자)

## 문항 ④

AI에는 역할을 나눠 맡겼습니다. Claude는 오케스트레이션·검수 역할로 최종 문제가 채널톡 트랙과 맞는지, README 전면부가 판단 감소 효과를 보이는지 점검했고, Codex는 유튜브 자막·공식 문서 리서치, URL 접근성 확인, 스킬/README/출력 계약 구현, 바잇미·알라딘 산출물 생성, claim audit을 수행했습니다. 직접 판단한 것은 후보 선택과 범위 제한입니다. 설치 QA, 리뷰 VOC, ALF 준비 중 영상의 “이커머스 상담 문제”와 AI 에이전트 방향에 가장 가까운 ALF 지식·규칙·테스트 구조화를 선택했습니다. 막힌 지점은 채널톡이 이미 AI 상담 시뮬레이션과 ALF 테스트를 제공한다는 반증, 공개 자료만으로 내부 ALF 설정을 알 수 없다는 점이었습니다. 해결은 제품 기능 대체가 아니라 공개 URL 기반 사전 설계 산출물로 범위를 좁히는 것이었습니다. 받아들이지 않은 제안은 공개 리뷰 VOC 티켓화, 실제 관리자 화면 자동 반영, 주문·환불 자동 처리, 알라딘 30문항 풀 확장입니다. 각각 고객사 상담 문제와 직접성이 약하거나 API 키·내부 데이터·시간이 필요해 제외했습니다. (570자)

## 문항 ⑤

검증은 실제 입력에서 산출물이 생기는지부터 확인했습니다. 바잇미는 공식 사례, FAQ, 이용안내, 상품 상세 URL을 넣어 `examples/biteme/`에 지식 문서 8개, 계약 산출 파일 13개, `alf-test-cases.csv` 41문항, `gaps.md`, 적용 가이드를 만들었습니다. 정상 케이스는 FAQ/AJAX 38개와 정책 문서를 배송·교환·환불·쿠폰 의도로 분류하고 CSV가 파싱되는지 확인했습니다. 예외 케이스는 HAX 상품의 제주/도서산간 교환·반품 추가비가 4,000원과 3,000원으로 충돌한 사례를 확정 규칙에서 빼고 `gaps.md`와 상담원 확인으로 넘긴 것입니다. 의심한 점은 출처 환각이어서 문항② 후보 5개와 README 수치를 curl·원문 대조·로컬 카운트로 다시 확인했습니다. 추가로 `output/live-test`에서는 설치한 플러그인을 fresh `codex exec`로 호출해 사용자 제공 FAQ 4문장만으로 필수 파일과 30행 CSV가 생성되는지 확인했습니다. 테스트하며 CoS 설명처럼 원문과 어긋난 claim audit 1건을 축소 조정했고, 보조 기사·리뷰는 핵심 근거에서 내렸습니다. 아직 실제 고객사 내부 정책, 주문/CRM 데이터, 채널톡 관리자 화면 업로드는 검증하지 못했습니다. (641자)

## 사용 출처 URL 목록

- https://channel.io/kr/talk
- https://channel.io/kr/blog/articles/crawling-press-9b611f25
- https://docs.channel.io/help/ko/articles/%EC%A7%80%EC%8B%9D-803f6ac9
- https://docs.channel.io/help/ko/articles/%EA%B7%9C%EC%B9%99-b43e19a1
- https://channel.io/kr/blog/articles/ai-cs-best-cases-6a7fd39d
- https://channel.io/kr/blog/articles/ai-case-biteme-d3e09ab9
- https://m.biteme.co.kr/shop/community/faq_lists
- https://m.biteme.co.kr/shop/service/service_guide
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000050043
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000040999
- https://m.biteme.co.kr/shop/product/product_view?product_cd=1000006873
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
