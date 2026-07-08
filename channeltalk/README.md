# 채널톡 제출용 플러그인

> AX 인재전쟁 2026 예선 제출 후보: ChannelTalk ALF Knowledge Planner

## 1. 플러그인 개요

이 플러그인은 이커머스 운영자와 CX/CS 담당자가 공개 FAQ, 배송·교환·환불 정책, 상품 안내, 쿠폰/프로모션 정보를 채널톡 ALF용 지식·규칙·테스트 세트로 바꾸도록 돕는 Codex 플러그인입니다.

사용자는 ALF 도입 전 공개 사이트 정보는 갖고 있지만, AI가 안전하게 답해도 되는 범위, 상담원에게 넘겨야 하는 조건, 테스트해야 할 질문을 수작업으로 정리해야 할 때 이 플러그인을 씁니다.

## 2. 공개 근거

| 출처 URL | 발행 주체 | 확인일 | 입증하는 주장 |
| --- | --- | --- | --- |
| `docs/source-video.ko.vtt` | 프라이머/채널코퍼레이션 발표 영상 자막 | 2026-07-08 | 채널톡 트랙은 이커머스 고객사의 상담 문제와 AI 에이전트 활용을 직접 힌트로 제시한다. |
| https://channel.io/kr/talk | ChannelTalk | 2026-07-08 | ALF/AI 상담은 규칙, 구조화된 지식, 실행 가능한 태스크/액션과 연결된다. |
| https://docs.channel.io/help/ko/articles/%EC%A7%80%EC%8B%9D-803f6ac9 | ChannelTalk | 2026-07-08 | ALF가 참조할 지식은 문서, 파일, 웹사이트 자료를 구조화해 관리해야 한다. |
| https://docs.channel.io/help/ko/articles/%EA%B7%9C%EC%B9%99-b43e19a1 | ChannelTalk | 2026-07-08 | ALF 규칙은 상황별 지시문, 필터, 개인화 변수, 상담 처리 액션으로 답변을 제어한다. |
| https://channel.io/kr/blog/articles/crawling-press-9b611f25 | ChannelTalk | 2026-07-08 | URL 입력과 웹 크롤링으로 AI 상담 사전 체험을 제공한다는 공개 자료다. |
| https://channel.io/kr/blog/articles/ai-cs-best-cases-6a7fd39d | ChannelTalk | 2026-07-08 | 반복 문의와 프로모션 상담량 폭증이 CS팀 pain point라는 공식 근거다. |

## 3. 작동 방식

입력:

- 공개 URL 또는 사용자가 붙여넣은 FAQ/정책/상품 설명
- 선택 입력: 배송, 교환/환불, 주문 변경, 상품/사이즈, 쿠폰, 상담원 이관 등 대상 범위

절차:

1. 입력 자료와 출처를 분리해 기록합니다.
2. 문서를 상담 의도별로 나눕니다.
3. 각 의도마다 근거 문장, 답변 규칙, 금지 답변, 상담원 이관 기준을 만듭니다.
4. 환불, 취소, 배송 예정일, 쿠폰 적용처럼 고객 오해가 큰 항목은 `high risk`로 표시합니다.
5. 문서가 부족하면 `missing`, 충돌하면 `conflict`로 표시하고 사람 확인 질문을 만듭니다.
6. 정상 질문, 애매한 질문, 정책 충돌 질문, 이관 질문을 포함한 ALF 테스트 세트를 출력합니다.

출력:

- ALF 지식 맵
- AI 답변 규칙과 금지 답변
- 상담원 이관 기준
- 누락·충돌 정보 체크리스트
- 테스트 질문과 기대 근거

## 4. 폴백과 제한

- 내부 ALF 설정, 고객사의 주문/CRM 데이터, 비공개 정책을 안다고 전제하지 않습니다.
- 공개 출처가 약한 주장은 `확인 필요`로 표시합니다.
- 정책이 충돌하면 한쪽을 선택하지 않고 사람 검토로 넘깁니다.
- 개인정보, API 키, 계정 정보는 입력하지 않습니다.

## 5. 설치·실행 방법

```bash
python tools/make_submission.py channeltalk
```

생성된 `dist/channeltalk/submission.zip` 안의 `src/`가 플러그인 루트입니다. Codex에서 플러그인을 로드한 뒤 다음처럼 호출합니다.

```text
이 이커머스 FAQ와 교환/환불 정책을 채널톡 ALF용 지식 맵, 답변 규칙, 상담원 이관 기준, 테스트 질문으로 바꿔줘.
```

## 6. 검증 방법

제출 전 확인할 항목:

1. `src/.codex-plugin/plugin.json`이 validator를 통과한다.
2. `src/skills/main/SKILL.md`가 ALF 지식 구조화 절차를 담고 있다.
3. `src/references/evidence.md`에 공개 근거와 금지 주장이 정리되어 있다.
4. 정상 입력으로 FAQ/정책 텍스트를 넣으면 지식 맵, 답변 규칙, 테스트 질문이 나온다.
5. 예외 입력으로 충돌하는 환불 정책을 넣으면 `conflict`와 사람 확인 질문을 출력한다.
6. `logs/`에는 AI와 나눈 전체 대화 로그 원본이 포함되어 있다.
