# KakaoPay Securities Evidence Map

## Selected Problem

KakaoPay Securities track focuses on novice investors who ask whether they should buy or sell, and on support agents who need to respond without giving investment recommendations. The plugin decomposes anxiety into purpose, time horizon, risk tolerance, order-structure understanding, official-source checks, and next safe actions.

## Video Intent Weight

- Source: `docs/source-video.ko.vtt` in the repository workspace.
- Weight: highest source priority.
- Key intent captured from the transcript: the company is interested in helping novice investors with buy/sell anxiety and values a logical process that helps users understand and feel reassured, not a mathematically perfect answer.

## Primary User

- Novice investor using KakaoPay Securities
- Customer support agent handling investment anxiety or transaction-structure questions
- Product or CX operator reviewing whether an answer stays within official guidance

## Core Public Sources

| Priority | URL | Claim Supported |
| --- | --- | --- |
| 1 | `docs/source-video.ko.vtt` | Official problem hint around beginner investor buy/sell anxiety and support process design. |
| 1 | https://kakaopaysec.com/ | Public positioning around accessible investment experience. |
| 1 | https://support.kakaopay.com/web/faq-list/CUSTOMER_CENTER_FAQ_STOCK?device=m&qna=CUSTOMER_CENTER_FAQ_DECIMAL_POINT_TRADING | Official FAQ evidence for fractional trading questions. |
| 1 | https://www.kakaopaysec.com/customer/notice/dynamicBoardPageDetail.do?id=6807 | Official notice evidence that order rules and trading details can change. |
| 1 | https://www.fsc.go.kr/po010101/76239 | Financial regulator guidance on explanation duties and consumer understanding. |
| 2 | https://eiec.kdi.re.kr/policy/materialView.do?datecount=&num=220522 | Public regulator-linked material warning that fractional trading structures differ by securities firm. |
| 2 | https://support.kakaopay.com/web/phone-cs-notice | Public support-channel context. |

## Plugin Scope

Inputs:

- Customer question, support draft, or pasted concern about buy/sell anxiety
- Optional transaction context such as fractional trading, order correction, dividend, settlement, notice, or FAQ URL

Outputs:

- non-advisory issue decomposition
- clarification questions
- official-source checklist
- customer-facing answer draft
- prohibited-expression review
- escalation path when official evidence is insufficient

## Judgment Rules

- Never recommend a specific stock, price, timing, or buy/sell action.
- Separate emotional reassurance from factual explanation.
- Use official KakaoPay Securities, KakaoPay support, regulator, and public notice sources first.
- Mark outdated or unverifiable claims as requiring official re-check.
- If the input asks for a recommendation, redirect to a decision checklist and risk questions.

## Do Not Claim

- Do not provide investment advice, profit promises, target prices, or buy/sell recommendations.
- Do not interpret private account data.
- Do not state compensation, execution, or regulatory conclusions without official source support.
- Do not imply that the plugin replaces licensed financial professionals or official customer support.
