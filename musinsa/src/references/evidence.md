# Musinsa Evidence Map

## Selected Problem

Musinsa track focuses on MDs, brand scouts, category owners, beauty/fashion strategists, and marketers who need to continuously discover customer-loved brands and trend signals from public sources without turning the work into a one-off manual report.

## Video Intent Weight

- Source: `docs/source-video.ko.vtt` in the repository workspace.
- Weight: highest source priority.
- Key intent captured from the transcript: Musinsa asks how it can stay ahead in fashion and beauty, how it can find brands customers will like, and how AI can help it avoid missing trends it should care about.

## Primary User

- Musinsa MD
- Brand scout
- Category or beauty strategy operator
- Marketing or platform strategy team member preparing weekly trend review

## Core Public Sources

| Priority | URL | Claim Supported |
| --- | --- | --- |
| 1 | `docs/source-video.ko.vtt` | Official problem hint prioritizing brand discovery and trend sensing. |
| 1 | https://newsroom.musinsa.com/newsroom-menu/2021-0930-03 | Musinsa's platform identity around brands and customer discovery. |
| 1 | https://newsroom.musinsa.com/newsroom-menu/2026-0324 | Public direction toward AI-assisted conversational fashion commerce and recommendation. |
| 2 | https://newsroom.musinsa.com/newsroom-menu/2025-1119 | Public evidence around Musinsa's brand/content/platform activity. |
| 2 | https://www.musinsa.com/main/musinsa/ranking | Public ranking signal for current customer interest inside Musinsa. |
| 2 | https://www.musinsa.com/ranking/archive | Public archive signal for trend movement over time. |
| 3 | https://play.google.com/store/apps/details?hl=ko&id=com.musinsa.store | Public app positioning around recommendation, trend indicators, and reviews. |

## Plugin Scope

Inputs:

- Category, demographic, trend question, or seed brand
- Optional public URLs from Musinsa ranking, newsroom, reviews, community posts, or search results

Outputs:

- trend-signal ledger
- brand-candidate scorecard
- supporting and opposing evidence list
- confidence level and source-strength labels
- next action for MD or brand scout
- monitoring query list for later runs

## Judgment Rules

- Video intent outranks generic ecommerce operations problems.
- Public source strength matters more than model confidence.
- Separate `already visible in Musinsa` signals from `external emerging` signals.
- A candidate brand is not "recommended"; it is a research hypothesis that needs human review.
- If a source is blocked, login-only, or noisy, mark it as unavailable or weak instead of using it as a core claim.

## Do Not Claim

- Do not claim access to Musinsa internal sales, search, CRM, or partner data.
- Do not rank brands as objectively best.
- Do not scrape private social accounts or login-only pages.
- Do not treat viral noise as a verified trend without public corroboration.
