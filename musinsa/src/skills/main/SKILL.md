---
name: main
description: "Use when preparing a Musinsa AX Talent War submission: finding public evidence, defining a real company or customer problem, designing a Codex plugin solution, drafting the 5 required answers, or validating the package."
---

# Musinsa AX Problem Solver

## 목적

무신사 또는 무신사 고객이 겪는 실제 문제를 공개 자료로 입증하고, 그 문제를 해결하는 Codex 플러그인 제출물로 구체화한다.

## 발동 조건

다음 요청에서 사용한다.

- 무신사 트랙의 문제 후보, 공개 근거, 고객 pain point, 운영 자동화 아이디어를 찾을 때
- 무신사 관련 Codex 플러그인의 작동 방식, 스킬 지침, README, 5문항 답변을 작성할 때
- 제출 전 `submission.zip`의 구조, 로그 포함 여부, 검증 절차를 점검할 때

## 수행 단계

1. 사용자가 이미 선택한 문제가 있으면 그 문제를 기준으로 진행한다. 문제가 없으면 공개 자료를 조사해 문제 후보 3개를 제안하고, 각 후보마다 근거 URL과 해결 가능성을 함께 제시한다.
2. 모든 사실 주장은 공개 출처로만 뒷받침한다. 출처마다 URL, 발행 주체, 발행일 또는 확인일, 해당 출처가 입증하는 주장을 기록한다.
3. 문제 정의는 `누가`, `어떤 상황에서`, `무엇 때문에`, `어떤 손실이나 비효율을 겪는지`가 드러나게 쓴다.
4. 플러그인 설계는 트리거 문구, 입력 자료, Codex가 수행할 단계, 생성 산출물, 사람이 검토해야 할 지점을 포함한다.
5. 구현 또는 문서 작성 시 `.codex-plugin/plugin.json`, `skills/main/SKILL.md`, `README.md`, `logs/` 포함 여부를 함께 점검한다.
6. 5문항 답변은 문제 선택 이유, 공개 근거, 작동 방식, AI 활용 방식, 검증 방법이 서로 모순되지 않게 작성한다.
7. 제출 전 패키징 명령과 검증 명령을 실행해 재현 가능한 결과를 확인한다.

## 출력 형식

기본 출력은 다음 순서를 따른다.

- 문제 정의 한 문단
- 공개 근거 표
- 플러그인 작동 흐름
- 구현 또는 문서 변경 목록
- 검증 명령과 기대 결과
- 5문항 답변 초안 또는 수정안

## 주의사항

- 비공개 정보, 추측성 수치, 출처 없는 기업 내부 사정을 사실처럼 쓰지 않는다.
- 공개 출처가 약한 문제는 과감히 후보에서 제외한다.
- API 키, 계정 정보, 개인정보는 대화와 로그에 남기지 않는다.
- 로그 제출 조건 때문에 대화 내용을 임의로 편집하거나 요약본만 제출하라고 안내하지 않는다.
