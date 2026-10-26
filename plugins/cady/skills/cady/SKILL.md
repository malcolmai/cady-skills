---
name: "cady"
description: "Reads the company's context in Cady, then loads the matching skill. Use when the work is a company's sales and outreach, drafting to a person (read the sender's voice pack first), posts, competitors and pricing, tools and integrations, budget, fundraising, filings and hiring, product and engineering work, and company agents. Not for personal tasks or coding with no company context. Requires a Cady account."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "cady.front-door"
  version: "5b3f58da932139b252f0"
  library: "83b4e016aaf66612"
  function: "core"
---
# Cady

Reads the company's context in Cady, then loads the matching skill. Use when the work is a company's sales and outreach, drafting to a person (read the sender's voice pack first), posts, competitors and pricing, tools and integrations, budget, fundraising, filings and hiring, product and engineering work, and company agents. Not for personal tasks or coding with no company context.

## Start every run

    get_cady_context({"area": "<area>", "task": "<what you are about to do, in one sentence>"})

Add "agentId" when you run as a registered Cady agent, "workId" to resume a work item, and
"knownMethods" {cady-id: version} (up to 8) for the skills you hold, so Cady returns company
content without re-sending their text. Product areas take the id from get_company_product in place of <productId>.
Then follow cady-core-run-sequence. A new company, or one with no direction yet, starts at `ops/onboarding` (`cady-company-review`).

| Area | For |
|---|---|
| `gtm/strategy` | ICP, offer, segments, positioning, targets |
| `gtm/prospecting` | lists, enrichment, CRM records |
| `gtm/outreach` | cold and warm mail, follow-ups, replies |
| `gtm/content` | public posts, assets, website copy |
| `product/<productId>/scope` | roadmap, features, product bar |
| `product/<productId>/ui` | pages, layout, components, UI copy |
| `product/<productId>/context` | how context and records are written, served and cleaned up |
| `product/<productId>/engineering` | infrastructure, data model, MCP interface, code |
| `product/<productId>/release` | merge, gates, staging and production |
| `product/<productId>/methods` | methods and agent behaviour the product ships: skills, role cards, run sequence, guidance placement and cues, evals |
| `ops/agents` | create, schedule, approve and retire agents; what they may do |
| `ops/onboarding` | a new company's first review: understand its evidence and functions, install guidance, propose first goals |
| `ops/legal` | filings, registers, compliance, tax |
| `ops/records` | recording and consolidating decisions, files and work |
| `ops/inbox` | mail triage, commitments, follow-ups and what to record |
| `finance/pricing` | plans, prices, limits, Stripe |
| `finance/plan` | the finance plan: cash, burn, runway |

## Add or change an agent

Read `list_company_agents` first (through `read_cady_tool` where your host does not list it). If an agent already owns the outcome, reuse or update it instead of creating a second one. To create, bind or schedule one, load `cady-company-manage-agents`; its worked recipe for a go-to-market agent is [`references/agent-recipe-gtm.md`](references/agent-recipe-gtm.md).

## Load a skill

Invoke the installed skill by name; `cady-core-skill-index` (also `INDEX.md`) lists them. Where the library sits beside this skill, read `library/<name>/SKILL.md`. Otherwise fetch the skill and its linked references from the source below. If no route works, say the method is unavailable and hold company writes.

    Library source: https://raw.githubusercontent.com/malcolmai/cady-skills/83b4e016aaf66612/

A fork changes that line to its own raw URL and branch.
