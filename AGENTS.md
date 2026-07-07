# AGENTS.md

이 저장소에서 작업하는 에이전트는 `AX 인재전쟁 2026` 해커톤 제출물을 만드는 중이라는 점을 우선 기억한다. 목표는 일반 앱 개발이 아니라, **세 개 회사 각각의 실제 문제를 공개 자료로 입증하고 이를 해결하는 Codex 플러그인을 제출 가능한 형태로 만드는 것**이다.

## 핵심 목표

- 세 개 회사 각각에 대해 별도 Codex 플러그인을 준비한다.
  - 채널톡: `channeltalk/`
  - 무신사: `musinsa/`
  - 카카오페이증권: `kakaopay-securities/`
- 각 회사는 별도 `submission.zip`으로 제출한다.
- 각 `submission.zip`에는 플러그인 소스, 회사별 README, AI 대화 로그 원본, 즉 모든 대화 로그가 포함되어야 한다.

## 대회 제출 룰

각 회사별 제출 답변은 아래 5문항을 따른다.

1. **무엇을, 누가, 어떤 상황에서 쓰나요?**
   플러그인을 한 문장으로 요약하고, 선언한 기업의 누가 어떤 상황에서 어디서 막혀 이 플러그인을 쓰게 되는지 구체적으로 적는다. 제한은 800자다.

2. **왜 이 문제를 선택했나요?**
   문제를 고른 이유와 그 기업의 직원, 고객 또는 산업 사용자가 실제로 어디서 왜 막히는지 적는다. 제한은 800자이며 출처 URL이 필요하다.

3. **플러그인은 어떻게 작동하나요?**
   플러그인의 절차, 지식, 판단 기준, 정보가 부족하거나 잘 안 풀리는 상황에서의 동작을 적는다. 제한은 1000자다. 세부 내용은 zip 파일의 README.md에도 있어야 한다.

4. **AI를 어떻게 썼나요?**
   AI에게 맡긴 작업과 직접 판단한 부분을 구분한다. 막혔던 지점, 해결 과정, 받아들이지 않은 AI 제안과 이유를 적는다. 제한은 800자다.

5. **어떻게 검증했나요?**
   입력에서 결과로 이어지는 예시를 하나 이상 적는다. 정상 상황과 예외 상황 확인, 의심한 점, 아직 부족한 점, 테스트하며 고친 점을 적는다.

## 작업 원칙

- 문제는 반드시 공개 자료로 입증한다.
- 비공개 정보, 출처 없는 숫자, 추측성 기업 내부 사정은 사실처럼 쓰지 않는다.
- 플러그인은 문제 설명서가 아니라 Codex가 반복 실행할 수 있는 문제 해결 워크플로우여야 한다.
- `README.md`, `SKILL.md`, 5문항 답변은 같은 문제와 같은 작동 방식을 설명해야 한다.
- 회사별 README에는 문항 3의 세부 작동 방식이 들어가야 한다.
- AI 대화 로그는 원본 그대로 제출해야 한다. 모든 대화 로그를 포함하고, 편집, 발췌, 요약, 재작성하지 않는다.
- API 키, 계정 정보, 개인정보는 대화와 로그에 남기지 않는다.

## 검증 체크리스트

제출 전 각 트랙에 대해 아래를 확인한다.

```bash
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py channeltalk/src
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py musinsa/src
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py kakaopay-securities/src

python tools/make_submission.py channeltalk
python tools/make_submission.py musinsa
python tools/make_submission.py kakaopay-securities
```

확인할 결과:

- 각 `src/.codex-plugin/plugin.json`이 validator를 통과한다.
- 각 `src/skills/main/SKILL.md`가 실제 수행 절차를 담고 있다.
- 각 회사별 `README.md`에 문제, 공개 근거, 작동 방식, 검증 방식이 들어 있다.
- `logs/`에 전체 대화 로그 원본이 포함되어 있다.
- 생성된 zip을 풀었을 때 `src/`, `README.md`, `logs/` 구조가 유지된다.
