# AGENTS.md

이 저장소에서 작업하는 에이전트는 `AX 인재전쟁 2026` 해커톤 제출물을 만드는 중이라는 점을 우선 기억한다. 목표는 일반 앱 개발이 아니라, **세 개 회사 각각의 실제 문제를 공개 자료로 입증하고 이를 해결하는 Codex 플러그인을 제출 가능한 형태로 만드는 것**이다.

## 핵심 목표

- 예선 마감은 **2026-07-10**이다.
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
   입력에서 결과로 이어지는 예시를 하나 이상 적는다. 정상 상황과 예외 상황 확인, 의심한 점, 아직 부족한 점, 테스트하며 고친 점을 적는다. 제한은 800자다(제출 폼 기준 최종 확인).

## 작업 원칙

- 문제는 반드시 공개 자료로 입증한다.
- 비공개 정보, 출처 없는 숫자, 추측성 기업 내부 사정은 사실처럼 쓰지 않는다.
- 플러그인은 문제 설명서가 아니라 Codex가 반복 실행할 수 있는 문제 해결 워크플로우여야 한다.
- `README.md`, `SKILL.md`, 5문항 답변은 같은 문제와 같은 작동 방식을 설명해야 한다.
- 회사별 README에는 문항 3의 세부 작동 방식이 들어가야 한다.
- AI 대화 로그는 원본 그대로 제출해야 한다. 모든 대화 로그를 포함하고, 편집, 발췌, 요약, 재작성하지 않는다.
- 로그 파일을 원본 그대로가 아닌 사후 가공(편집·발췌·삭제)하여 제출하면 실격이다.
- 출처는 공개 자료로 AI가 확인할 수 있어야 한다. 기업 내부의 비공개 정보, 확인할 수 없는 사적인 경험, 출처 없는 숫자는 근거로 인정되지 않는다.
- 로그 훅이 세션 로그를 자동 저장하므로 `logs/` 안의 파일을 만들거나 수정·삭제하지 않는다.
- API 키, 계정 정보, 개인정보는 대화와 로그에 남기지 않는다.

## 작업 기록(docs/)

- 루트 `docs/research-workflow.md`는 세 회사 공통 리서치 프로토콜이다.
- 각 트랙의 `docs/source-video.ko.vtt`는 출제 의도가 담긴 최우선 자료로 본다.
- 각 트랙의 `docs/research.md`(문항 ①②), `docs/engineering.md`(문항 ③④), `docs/verification.md`(문항 ⑤)에 진행하며 기록한다.
- 각 트랙의 `src/references/evidence.md`는 submission.zip 안에 들어가는 공개 근거·가드레일 맵이다. `docs/research.md`만 갱신하고 `src/references/evidence.md`를 방치하지 않는다.
- 특히 AI에게 맡긴 작업, 직접 판단한 부분, 받아들이지 않은 AI 제안과 그 이유는 그때그때 기록한다. 나중에는 복원할 수 없다.

## 리서치 방식

- 영상 자막, 회사 공식 자료, 고객센터/FAQ/공지, 공개 리뷰·커뮤니티·기사 순으로 근거 강도를 둔다.
- insane-research류 도구를 쓸 때는 URL, 확인일, 수집 방법, 입증 주장, 접근 실패 여부를 기록한다.
- NotebookLM은 누락 확인과 구조화 보조로만 쓰고, 답변 내용은 반드시 원문 URL 또는 자막으로 역추적한다.
- 공개 출처가 약하거나 원문으로 확인되지 않는 주장은 5문항 답변과 README에 넣지 않는다.

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
