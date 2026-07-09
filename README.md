# AX 인재전쟁 2026 — 예선 제출 monorepo

'AX 인재전쟁 2026' 해커톤 예선 제출물을 관리하는 저장소입니다.

- **예선 마감: 2026-07-10**
- 기업별 실제 문제를 해결하는 Codex 플러그인을 만들어, **기업마다 별도의 `submission.zip`** 으로 제출합니다.

## 해커톤 룰 고정

이 저장소는 일반 앱이나 라이브러리가 아니라, **해커톤 문제풀이를 위한 Codex 플러그인 제출물**을 만들기 위한 작업 공간입니다. 모든 작업은 아래 룰을 기준으로 판단합니다.

### ⚠️ 실격·근거 인정 기준

- 로그 파일을 원본 그대로가 아닌 **사후 가공(편집·발췌·삭제)하여 제출하면 실격**됩니다.
- 출처는 **공개 자료로 AI가 확인할 수 있어야** 합니다. 기업 내부의 비공개 정보, 확인할 수 없는 사적인 경험, 출처 없는 숫자는 근거로 인정되지 않습니다.
- 제출한 예선 제출물은 본선 심사에 활용될 수 있습니다.
- 예선 마감: **2026-07-10**

### 제출 단위

- 세 개 회사를 정합니다.
- 각 회사마다 별도의 Codex 플러그인을 만듭니다.
- 각 회사마다 별도의 `submission.zip`을 제출합니다.
- 이 repo의 현재 세 트랙은 다음과 같습니다.
  - 채널톡: `channeltalk/`
  - 무신사: `musinsa/`
  - 카카오페이증권: `kakaopay-securities/`

### 각 `submission.zip`에 포함할 것

```text
submission.zip
├── src/                          # 구동 가능한 Codex 플러그인 소스
│   ├── .codex-plugin/plugin.json
│   ├── skills/main/SKILL.md
│   ├── references/evidence.md    # 공개 근거·가드레일 맵
│   ├── examples/                 # 실제 예시 실행 산출물 사본
│   └── docs/                     # 핵심 근거 문서 사본 (리서치·검증·답변·영상 자막)
├── README.md                     # 문제, 작동 방식, 검증 설명
└── logs/                         # AI와 나눈 전체 대화 로그 원본
```

최상위 구조는 공고 스펙(src/README/logs) 그대로이고, 예시 산출물과 근거 문서는
스펙이 "구조 자유"라고 명시한 `src/` 아래 사본으로 포함해 심사자가 zip만 열어도
전체 증거 체인을 확인할 수 있게 합니다.

### 로그 규칙

- AI와 나눈 전체 대화 로그 원본, 즉 모든 대화 로그를 포함합니다.
- 로그는 편집, 발췌, 요약, 재작성하지 않습니다.
- 비밀키, 계정 정보, 개인정보는 AI 대화에 넣지 않습니다.
- 제출 직전 `logs/`가 실제로 zip에 들어갔는지 확인합니다.

### 제출 5문항

각 회사별 제출 답변은 아래 다섯 문항을 기준으로 작성합니다.

1. **무엇을, 누가, 어떤 상황에서 쓰나요?**
   만든 플러그인을 한 문장으로 요약합니다. 이어서 선언한 기업의 누가, 어떤 상황에서, 어디서 막혀 이 플러그인을 쓰게 되는지 구체적으로 적습니다.
   제한: 800자

2. **왜 이 문제를 선택했나요?**
   이 문제를 고른 이유와, 그 기업의 직원이나 고객 또는 해당 산업의 사용자가 실제로 어디서 왜 막히는지 적습니다.
   제한: 800자
   필수: 출처 URL

3. **플러그인은 어떻게 작동하나요?**
   플러그인이 어떻게 동작하는지, 절차, 지식, 판단 기준을 어떻게 가져가는지 적습니다. 정보가 부족하거나 잘 안 풀리는 상황에서의 동작도 함께 적습니다. 세부 내용은 zip 파일의 `README.md`에도 적혀 있어야 합니다.
   제한: 1000자

4. **AI를 어떻게 썼나요?**
   AI에게 맡긴 작업과 직접 판단한 부분을 구분해 적습니다. 만들면서 막혔던 지점, 해결 과정, 받아들이지 않은 AI 제안과 그 이유도 적습니다.
   제한: 800자

5. **어떻게 검증했나요?**
   입력에서 결과로 이어지는 예시를 하나 이상 적습니다. 정상 상황과 예외 상황을 어떻게 확인했는지, 무엇을 의심했고 무엇이 아직 부족한지, 테스트하며 고친 점을 적습니다.
   제한: 800자 (제출 폼 기준 최종 확인)

### 작업 원칙

- 문제는 반드시 공개 자료로 입증합니다.
- “기업이 실제로 겪는 문제” 또는 “기업의 고객/산업 사용자가 실제로 막히는 지점”을 다룹니다.
- 플러그인은 문제 조사 보고서가 아니라, Codex가 반복 실행할 수 있는 문제 해결 워크플로우여야 합니다.
- README, `SKILL.md`, 5문항 답변은 서로 같은 문제와 같은 작동 방식을 설명해야 합니다.
- 제출 전에는 validator, 패키징, zip 내부 구조, 로그 포함 여부를 확인합니다.

### 리서치 원칙

- 회사별 유튜브 자막(`docs/source-video.ko.vtt`)은 출제자가 문제 의도를 설명한 자료이므로 최우선 가중치를 둡니다.
- 회사 공식 사이트, 뉴스룸, 제품 문서, 고객센터/FAQ, 공지는 핵심 공개 근거로 사용합니다.
- 앱 리뷰, 공개 커뮤니티, 기사, 산업 자료는 실제 사용자가 어디서 막히는지 보강하는 자료로 사용합니다.
- insane-research류 도구는 접근이 어렵거나 흩어진 공개 자료를 수집·비교할 때 쓰되, URL·확인일·수집 방법·입증 주장을 반드시 남깁니다.
- NotebookLM은 자막과 공식 자료의 누락 확인·구조화 보조로만 사용하고, 제출 근거는 항상 원문 URL이나 자막 내용으로 역추적합니다.
- 자세한 공통 프로토콜은 `docs/research-workflow.md`를 따릅니다.

## Repo 구조

```
ax인재전쟁/
├── AGENTS.md                    # Codex 에이전트 지침
├── agent.md                     # 사람용 요약
├── docs/
│   └── research-workflow.md     # 세 회사 공통 리서치 프로토콜
├── .claude/settings.json        # Claude Code 로그 훅 (공식 log-hooks 원본)
├── .codex/hooks.json            # Codex 로그 훅 (공식 log-hooks 기반 + Windows 호환 패치, 아래 참고)
├── tools/
│   ├── save_log.py              # 훅이 호출하는 로그 저장 스크립트 (공식 log-hooks 기반 + Windows 호환 패치, 아래 참고)
│   └── make_submission.py       # submission.zip 패키징 스크립트
├── logs/                        # 이 repo에서 진행한 AI 세션 로그 (자동 저장)
├── channeltalk/                 # 채널톡 트랙
│   ├── src/
│   │   ├── .codex-plugin/plugin.json
│   │   ├── references/evidence.md # zip에 포함되는 공개 근거·가드레일 맵
│   │   └── skills/main/SKILL.md
│   ├── README.md
│   ├── docs/                    # 작업 기록 (핵심 문서는 zip의 src/docs/에 사본 포함)
│   │   ├── research.md          #   문항 ①② 원천 자료
│   │   ├── engineering.md       #   문항 ③④ 원천 자료
│   │   ├── verification.md      #   문항 ⑤ 원천 자료
│   │   └── submission-answers.md#   문항 ①~⑤ 최종 답변
│   ├── examples/                # 예시 실행 산출물 (zip의 src/examples/에 사본 포함)
│   └── logs/                    # 채널톡 작업 전용 로그 (필요 시)
├── musinsa/                     # 무신사 트랙 (동일 구조)
└── kakaopay-securities/         # 카카오페이증권 트랙 (동일 구조)
```

**로그 훅 패치 안내**: 로그 훅은 공식 log-hooks 기반이며 Windows 호환을 위한 최소 패치만 적용했습니다.
`tools/save_log.py`에는 한글 경로가 cp949로 잘못 디코딩되는 것을 방지하는 UTF-8 강제를,
`.codex/hooks.json`은 Windows Codex가 POSIX `for` 루프를 실행하지 못해 단일 `python` 직접 실행 명령으로 교체했습니다.
패치는 로그 '수집기'에 대한 것이며 로그 내용은 무가공 원본 그대로 저장·제출됩니다. 수정 이력은 git 커밋에 투명하게 남아 있습니다.

## 제출 파일 구조 (기업별 별도 제출)

기업마다 아래 형식의 `submission.zip` 을 각각 만들어 제출합니다.

```
submission.zip
├── src/                          # 플러그인 루트 전체 (.codex-plugin/plugin.json 필수)
│   ├── .codex-plugin/plugin.json
│   ├── references/evidence.md
│   ├── skills/<이름>/SKILL.md
│   ├── examples/                 # 예시 실행 산출물 사본
│   └── docs/                     # 핵심 근거 문서 사본 (source-video.ko.vtt 포함)
├── README.md
└── logs/                         # AI 대화 로그 원본 (md/txt/json/jsonl)
```

패키징 시 루트 세션 로그는 `logs/repo/`, 회사별 세션 로그는 `logs/<slug>/` 아래에 들어갑니다. 같은 session_id 파일명이 있어도 원본 로그를 모두 보존하기 위한 구조입니다.

## 로그 규정 (중요)

- 로그는 **원본 그대로** 제출해야 합니다. **편집·발췌 시 실격**됩니다.
- 로그는 그대로 제출되므로 **AI 채팅에 API 키 등 비밀정보를 절대 입력하지 마세요.**
- 로그 훅(`.claude/settings.json`, `.codex/hooks.json`)이 세션 로그를
  `logs/claude-code/`, `logs/codex/` 에 자동 저장합니다.
- 훅은 **새로 시작하는** Claude Code / Codex 세션부터 적용됩니다.
  이 저장소 루트에서 새 세션을 시작해 작업하세요.
- 회사 폴더(예: `musinsa/`)에서 시작한 Codex 세션의 로그는 그 폴더의 `logs/codex/`에,
  루트에서 시작한 세션의 로그는 루트 `logs/`에 자동 저장됩니다.
- 훅 파일을 수정하면 Codex가 훅 신뢰 재승인을 요구하니 주의하세요.

## 패키징

```bash
python tools/make_submission.py channeltalk
python tools/make_submission.py musinsa
python tools/make_submission.py kakaopay-securities
```

결과물은 `dist/<slug>/submission.zip` 에 생성됩니다.
(`<slug>/src/.codex-plugin/plugin.json` 이 없으면 에러로 종료하고,
logs 가 비어 있으면 경고를 출력하되 패키징은 진행합니다.)

## 지금까지 한 일 (2026-07-08 기준)

이 저장소는 프라이머 해커톤 `AX 인재전쟁` 예선 제출을 준비하기 위해 만든 Codex 플러그인 monorepo입니다. 대회 요구사항은 참여 기업이나 고객이 겪는 실제 문제를 공개 자료로 입증하고, 그 문제를 해결하는 구동 가능한 Codex 플러그인 소스와 5문항 답변, AI 대화 로그 원본을 함께 제출하는 것입니다.

### 1. 대회 형식 분석

- 공식 대회 페이지와 공고 내용을 기준으로 제출물의 핵심을 정리했습니다.
- 이 대회는 단순 앱 제작이 아니라 `문제 발굴 -> 공개 자료로 입증 -> Codex 플러그인 구현 -> 작동 검증 -> AI 협업 로그 제출` 흐름으로 이해했습니다.
- 기업별로 별도 `submission.zip`을 만들어 제출하는 구조로 저장소를 설계했습니다.

### 2. 저장소 구조 구성

- 세 개의 기업 트랙을 분리했습니다.
  - `channeltalk/`
  - `musinsa/`
  - `kakaopay-securities/`
- 각 트랙은 같은 제출 구조를 갖습니다.
  - `src/.codex-plugin/plugin.json`
  - `src/skills/main/SKILL.md`
  - `README.md`
  - `logs/`
- 루트에는 공통 패키징 도구와 AI 로그 저장 훅을 두었습니다.
  - `tools/make_submission.py`
  - `tools/save_log.py`
  - `.codex/hooks.json`
  - `.claude/settings.json`

### 3. 플러그인 형식 보강

처음에는 세 트랙의 `plugin.json`, `SKILL.md`, README가 제출 템플릿 수준이어서 공식 validator 기준으로 통과하지 못했습니다. 이후 아래 내용을 보강했습니다.

- `plugin.json`에 필수 메타데이터를 추가했습니다.
  - `author`
  - `interface`
  - `displayName`
  - `shortDescription`
  - `longDescription`
  - `developerName`
  - `category`
  - `capabilities`
  - `defaultPrompt`
- `SKILL.md`의 빈 placeholder를 제거하고, 각 기업 트랙에서 AI가 따라야 할 실제 수행 절차를 작성했습니다.
- 기업별 README에는 확정된 문제 가설, 공개 근거, 설치·실행 방법, 작동 방식, 검증 방법을 넣었습니다.
- 제출 zip에 들어가는 `src/references/evidence.md`를 추가해, `docs/research.md`가 빠져도 플러그인 소스 안에 근거 맵과 가드레일이 남도록 했습니다.

### 4. 로그 제출 방식 수정

대회 조건상 AI와 나눈 전체 대화 로그, 즉 모든 대화 로그는 편집이나 발췌 없이 원본으로 제출해야 합니다. 기존 `tools/save_log.py`는 대화 텍스트만 남기고 일부 transcript 라인을 줄이는 방식이어서 제출 조건과 맞지 않을 수 있었습니다.

현재는 `tools/save_log.py`가 transcript 파일을 그대로 복사하도록 바꿨습니다.

- 저장 위치: `logs/<tool>/<session_id>.jsonl`
- 대상 도구: `codex`, `claude-code`
- 원칙: 필터링, 요약, 발췌, 재작성 없음

### 5. 패키징과 검증

다음 검증을 수행했습니다.

```bash
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py channeltalk/src
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py musinsa/src
python C:/Users/kimdo/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py kakaopay-securities/src
```

세 플러그인 모두 validator를 통과했습니다.

```bash
python tools/make_submission.py channeltalk
python tools/make_submission.py musinsa
python tools/make_submission.py kakaopay-securities
```

세 트랙 모두 `dist/<slug>/submission.zip` 생성에 성공했습니다. 생성된 zip을 다시 풀어서 내부 `src/`에 대해 validator를 재실행했고 통과했습니다.

추가로 확인한 내용:

- `python -m py_compile tools/save_log.py tools/make_submission.py` 통과
- `tools/save_log.py` 원본 복사 동작 바이트 비교 통과
- 저장소 내 제출 문서 placeholder 제거 확인

### 5-1. 유튜브 자막 기반 스캐폴딩

2026-07-08 현재 세 트랙은 모두 출제자 영상 자막을 최우선 가중치로 반영해 문제 방향을 잡았습니다.

- 채널톡: 이커머스 FAQ/정책/상품 정보를 ALF용 지식·규칙·테스트로 구조화하는 플러그인
- 무신사: 공개 자료에서 고객이 좋아할 브랜드와 트렌드 신호를 반복 발굴하는 플러그인
- 카카오페이증권: 초보 투자자의 매수·매도 불안을 투자 추천 없이 분해하고 공식 근거로 다음 행동을 정리하는 플러그인

공통 리서치 방식은 `docs/research-workflow.md`에 정리했습니다. insane-research류 도구는 접근이 어렵거나 흩어진 공개 자료 수집에 쓰고, NotebookLM은 자막과 공식 자료의 누락 확인·구조화 보조로만 사용합니다. 두 경우 모두 최종 제출 근거는 원문 URL이나 자막 내용으로 역추적해야 합니다.

### 6. GitHub 저장소

- 현재 원격: `origin` = public repo `https://github.com/ashrate/ax-hackathon-2026` (`main` 브랜치, origin/main 동기화 상태)
- `https://github.com/ashrate/ax-talent-war`는 초기에 쓰던 private repo로, 현재는 사용하지 않는 중복 저장소입니다.

## 설명용 한 문단 요약

이 저장소는 `AX 인재전쟁 2026` 예선 제출을 위해 만든 Codex 플러그인 monorepo입니다. 채널톡, 무신사, 카카오페이증권 세 트랙을 분리했고, 각 트랙은 `.codex-plugin/plugin.json`, `skills/main/SKILL.md`, `references/evidence.md`, README, logs를 포함하는 동일한 제출 구조를 갖습니다. 대회 조건에 맞춰 AI 대화 로그는 원본 그대로 저장되며, 세 트랙 모두 유튜브 자막의 출제 의도를 최우선으로 반영해 문제 가설과 플러그인 작동 절차를 맞췄습니다.

## 완료된 것

- 세 트랙 리서치·근거 감사·claim audit(원문 구절 대조 65건, 불지지 0) 완료. 출처는 접근·원문 확인된 공개 URL만 사용.
- 세 플러그인 모두 공식 validator 통과, 실존 케이스 예시 실행(`src/examples/`)과 정식 설치 경로 실구동 테스트(`docs/verification.md`) 완료.
- 5문항 최종 답변을 각 트랙 `docs/submission-answers.md`에 글자수 제한 내로 확정 (zip의 `src/docs/`에도 사본 포함).
- 외부 리뷰 3라운드 반영: 무신사 triage 재정의, 카카오페이증권 검토용 초안 포지션 전환, zip 자립화(예시·근거 문서 포함), README 링크 무결성 검사.

## 제출 직전 확인할 것

- `python tools/make_submission.py <slug>` 재실행으로 마지막 세션 로그까지 포함한 zip 재생성.
- validator 3트랙 재실행(`validate_plugin.py <slug>/src`)과 zip 내부 구조(src/README/logs) 확인.
- 제출 폼 문항 답변은 각 트랙 `docs/submission-answers.md`에서 복사 (문항② 출처 URL 포함).
- `logs/` 파일은 절대 수동 편집·삭제하지 않음 (사후 가공 시 실격).
