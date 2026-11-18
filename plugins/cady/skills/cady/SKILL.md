---
name: "cady"
description: "Reads the company's context in Cady, then loads the matching skill. Use when the work is a company's sales and outreach, drafting to a person (read the sender's voice pack first), posts, competitors and pricing, tools and integrations, budget, fundraising, filings and hiring, product and engineering work, and company agents. Not for personal tasks or coding with no company context. Requires a Cady account."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "cady.front-door"
  version: "ecbac3211bd2f721befe"
  library: "b214552fcaa8da00"
  function: "core"
---
# Cady

**Point:** Start every run from Cady's state, then load the one installed skill that fits, so no run guesses.

## Start every run

    cady_start {"task": "<your request, verbatim>"}

It returns the state and the exact calls for what is open. A new company, or one with no direction yet, starts at `ops/onboarding` (`cady-company-onboarding`).

| Area | For |
|---|---|
| `gtm/strategy` | ICP, offer, segments, positioning, targets |
| `gtm/prospecting` | lists, enrichment, CRM records |
| `gtm/outreach` | cold and warm mail, follow-ups, replies |
| `gtm/content` | public posts, assets, website copy |
| `sales/deals` | discovery through closing |
| `customer_success/lifecycle` | onboarding through renewal and expansion |
| `fundraise/raise` | raise plan, investors, materials and outreach |
| `product/<productId>/scope` | roadmap, features, product bar |
| `product/<productId>/ui` | pages, layout, components, UI copy |
| `product/<productId>/context` | how context and records are written, served and cleaned up |
| `product/<productId>/engineering` | infrastructure, data model, MCP interface, code |
| `product/<productId>/release` | merge, gates, staging and production |
| `product/<productId>/methods` | shipped methods, agent guidance and evals |
| `ops/agents` | create, schedule, approve and retire agents; what they may do |
| `ops/onboarding` | a new company's first review and goals |
| `ops/legal` | filings, registers, compliance, tax |
| `ops/records` | recording and consolidating decisions, files and work |
| `ops/inbox` | mail triage, commitments, follow-ups and what to record |
| `company/direction` | the company point, bets and company-wide choices |
| `finance/pricing` | plans, prices, limits, Stripe |
| `finance/plan` | the finance plan: cash, burn, runway |

## Load a skill

Load the installed skill by name: the role's `cady-<function>-method`, then the task skill its area names. A skill that is not installed is unavailable: say so and hold company writes.
