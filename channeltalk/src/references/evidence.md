# ChannelTalk Evidence Map

## Selected Problem

ChannelTalk track focuses on ecommerce operators and CX teams that need to turn public FAQ, shipping, exchange, refund, product, and promotion pages into ALF-ready knowledge, rules, escalation criteria, and test questions before launching AI customer support.

## Video Intent Weight

- Source: `docs/source-video.ko.vtt` in the repository workspace.
- Weight: highest source priority.
- Key intent captured from the transcript: ChannelTalk wants to solve ecommerce customer-support problems with AI agents, and the submission should show how AI performs work while a human makes defensible judgments.

## Primary User

- Ecommerce CX/CS owner
- ChannelTalk implementation consultant
- Small ecommerce operator preparing ALF or AI customer-support workflows

## Core Public Sources

| Priority | URL | Claim Supported |
| --- | --- | --- |
| 1 | https://channel.io/us/talk | ChannelTalk positions AI support around knowledge, rules, customer support automation, and human handoff. |
| 1 | https://channel.io/kr | ChannelTalk's product direction centers on customer communication and AI-powered support. |
| 1 | https://channel.io/kr/blog/articles/crawling-press-9b611f25 | ChannelTalk publicly describes URL-based website crawling for AI customer-support previews. |
| 2 | https://zdnet.co.kr/view/?no=20241217160629 | Public interview/article evidence that ecommerce support includes repetitive inquiries such as delivery, cancellation, and size questions. |
| 2 | https://channel.io/kr/blog/articles/ai-cs-best-cases-6a7fd39d | Public examples of AI customer-support use cases and operational benefits. |
| 3 | https://aws.amazon.com/ko/blogs/tech/architecture-modernization-journey-of-channel-corporation-with-amazon-dynamodb-part1/ | Public background on Channel Corporation's mission around customer-company communication. |

## Plugin Scope

Inputs:

- Public ecommerce site URL or pasted FAQ/policy/product text
- Optional target scope, such as shipping, exchange/refund, size, coupon, order change, or escalation

Outputs:

- ALF knowledge map
- AI response rules
- escalation and human-handoff criteria
- test questions with expected evidence
- missing-information checklist
- 5-question submission draft updates when requested

## Judgment Rules

- Prefer official company or merchant text over secondary summaries.
- Mark claims as `verified`, `weak`, or `missing`.
- Treat policy-sensitive topics such as refund, cancellation, delivery date, and coupons as high-risk.
- If a page conflicts with another page, surface the conflict and require human review instead of choosing silently.
- If source text is too thin, output a missing-information checklist rather than inventing policy.

## Do Not Claim

- Do not claim access to ChannelTalk internal ALF configuration.
- Do not claim a merchant's private order, CRM, or customer data.
- Do not promise fully automated policy decisions.
- Do not use unverified numbers as proof of business impact.
