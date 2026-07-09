# 알라딘 라이트 실행 지식 맵 요약

확인일: 2026-07-08
수집 방법: `curl -L`로 공개 고객센터/FAQ/AJAX 응답 확인

## 선정 이유

알라딘은 도서, 음반, 전자책, 중고 상품을 다루는 이커머스다. 바잇미의 반려동물 커머스와 업종이 다르고, 고객센터 FAQ와 반품/교환/배송 관련 공개 응답이 로그인 없이 접근 가능해 같은 ALF 지식·규칙·테스트 워크플로우의 일반화 확인 대상으로 적합하다.

## 입력 URL

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

## 생성 구조

```text
examples/aladin/
  knowledge-map-summary.md
  alf-knowledge/
    01-brand-and-scope/
      source-scope.md
    03-shipping/
      shipping-and-pickup.md
    04-exchange-return-refund/
      return-exchange.md
  alf-rules.md
  alf-test-cases.csv
  gaps.md
```

## 대표 지식 문서

| 문서 | 상담 의도 | 핵심 근거 |
| --- | --- | --- |
| `alf-knowledge/01-brand-and-scope/source-scope.md` | 적용 범위, 고객센터 운영시간, 공개 수집 범위 | 고객센터 FAQ 목록과 고객센터 운영시간 영역 |
| `alf-knowledge/03-shipping/shipping-and-pickup.md` | 배송 예정일, 편의점 픽업, 예약상품 포함 주문, 출고 지연 | 배송/수령일 FAQ 목록과 공개 AJAX 응답 |
| `alf-knowledge/04-exchange-return-refund/return-exchange.md` | 반품 가능 기간, 반품 신청, 지정택배 방문, 하자 교환, 반품 불가 조건 | 반품/교환 FAQ 목록과 공개 AJAX 응답 |

## 라이트 실행 결과

- 지식 문서 3개
- 규칙 발췌 1개
- 테스트 질문 12개
- 운영자 확인 항목 6개
- 공개 URL 접근 점검: `docs/verification.md`의 URL 점검표에 기록

## 출처

- 출처 URL: https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx
- 출처 URL: https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=75&UpperId=75
- 출처 URL: https://www.aladin.co.kr/cs_center/wcs_faq_list.aspx?CategoryId=76&UpperId=76
- 출처 URL: https://blog.aladin.co.kr/cscenter/1451688
- 확인일: 2026-07-08
