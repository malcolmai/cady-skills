---
name: "cady"
description: "Reads the company's context in Cady, then loads the matching skill. Use when the work is a company's sales and outreach, drafting to a person (read the sender's voice pack first), posts, competitors and pricing, tools and integrations, budget, fundraising, filings and hiring, product and engineering work, and company agents. Not for personal tasks or coding with no company context. Requires a Cady account."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "cady.front-door"
  version: "adbdd935b381036175ea"
  library: "92b470f2d8d6c53e"
  function: "core"
---
# Cady

Reads the company's context in Cady, then loads the matching skill. Use when the work is a company's sales and outreach, drafting to a person (read the sender's voice pack first), posts, competitors and pricing, tools and integrations, budget, fundraising, filings and hiring, product and engineering work, and company agents. Not for personal tasks or coding with no company context.

## Start every run

    context_read({"area": "<area>", "task": "<what you are about to do, in one sentence>"})

Add "agentId" for a registered agent, "workId" to resume work, and
"knownMethods" {cady-id: version} (up to 32) for held skills, so Cady returns company
content without repeating their text. Product areas use the id from get_company_product for <productId>.
Then follow cady-core-run-sequence. A new company, or one with no direction yet, starts at `ops/onboarding` (`cady-company-review`).

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
| `finance/pricing` | plans, prices, limits, Stripe |
| `finance/plan` | the finance plan: cash, burn, runway |

## Add or change an agent

Read `agents_read` first (through `read_cady_tool` where your host does not list it). Reuse or update an agent that already owns the outcome. To create, bind or schedule one, load `cady-company-manage-agents`; its channel execution agent brief is [`references/execution-agent-brief.md`](references/execution-agent-brief.md).

## Load a skill

Try: the installed skill by name (`cady-core-skill-index`); local `skills/<name>/SKILL.md` in its Claude Code group plugin, or `library/<name>/SKILL.md` beside this skill (Cady reply paths mean either place); `records_read {refs:["<cady-id>"]}`, e.g. `records_read {refs:["skill.gtm.reply"]}`, returns method text; finally fetch the skill and its linked references from the source below (pinned Library URL). If no route works, say the method is unavailable and hold company writes.

    Library source: https://raw.githubusercontent.com/malcolmai/cady-skills/92b470f2d8d6c53e/

A fork changes that line to its own raw URL and branch.
