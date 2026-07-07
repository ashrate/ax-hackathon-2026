# AX 인재전쟁 2026 — 예선 제출 monorepo

'AX 인재전쟁 2026' 해커톤 예선 제출물을 관리하는 저장소입니다.

- **예선 마감: 2026-07-10**
- 기업별 실제 문제를 해결하는 Codex 플러그인을 만들어, **기업마다 별도의 `submission.zip`** 으로 제출합니다.

## Repo 구조

```
ax인재전쟁/
├── .claude/settings.json        # Claude Code 로그 훅 (공식 도구 — 수정 금지)
├── .codex/hooks.json            # Codex 로그 훅 (공식 도구 — 수정 금지)
├── tools/
│   ├── save_log.py              # 훅이 호출하는 로그 저장 스크립트 (공식 도구 — 수정 금지)
│   └── make_submission.py       # submission.zip 패키징 스크립트
├── logs/                        # 이 repo에서 진행한 AI 세션 로그 (자동 저장)
├── channeltalk/                 # 채널톡 트랙
│   ├── src/
│   │   ├── .codex-plugin/plugin.json
│   │   └── skills/main/SKILL.md
│   ├── README.md
│   └── logs/                    # 채널톡 작업 전용 로그 (필요 시)
├── musinsa/                     # 무신사 트랙 (동일 구조)
└── kakaopay-securities/         # 카카오페이증권 트랙 (동일 구조)
```

## 제출 규칙 (기업별 별도 제출)

기업마다 아래 형식의 `submission.zip` 을 각각 만들어 제출합니다.

```
submission.zip
├── src/                          # 플러그인 루트 전체 (.codex-plugin/plugin.json 필수)
│   ├── .codex-plugin/plugin.json
│   └── skills/<이름>/SKILL.md
├── README.md
└── logs/                         # AI 대화 로그 원본 (md/txt/json/jsonl)
```

## 로그 규정 (중요)

- 로그는 **원본 그대로** 제출해야 합니다. **편집·발췌 시 실격**됩니다.
- 로그는 그대로 제출되므로 **AI 채팅에 API 키 등 비밀정보를 절대 입력하지 마세요.**
- 로그 훅(`.claude/settings.json`, `.codex/hooks.json`)이 세션 로그를
  `logs/claude-code/`, `logs/codex/` 에 자동 저장합니다.
- 훅은 **새로 시작하는** Claude Code / Codex 세션부터 적용됩니다.
  이 저장소 루트에서 새 세션을 시작해 작업하세요.

## 패키징

```bash
python tools/make_submission.py channeltalk
python tools/make_submission.py musinsa
python tools/make_submission.py kakaopay-securities
```

결과물은 `dist/<slug>/submission.zip` 에 생성됩니다.
(`<slug>/src/.codex-plugin/plugin.json` 이 없으면 에러로 종료하고,
logs 가 비어 있으면 경고를 출력하되 패키징은 진행합니다.)
