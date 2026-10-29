---
name: "cady-core-execution"
description: "Shared execution rules: authority, blockers, credentials, effects and receipts, recurrence and model choice. Use when: a skill points here, or before an effect, credential use, retry or recovery. Not for: choosing what work to do."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.all"
  version: "38a8a7bc1a5d2055b86c"
  library: "010d8211a6a994a9"
  function: "core"
---
# Execution guidance

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>"})`

Shared execution rules: authority, blockers, credentials, effects and receipts, recurrence and model choice. Use when: a skill points here, or before an effect, credential use, retry or recovery. Not for: choosing what work to do.
- **Application:** Use this method when complex work, execution design, integrations or recovery need it; reuse it within the task. Combine the shared method with only the relevant use-case guidance and current company/task context. Read missing context that could change the approach; refresh authority and mutable targets before effects. Apply controls proportionately to consequence and uncertainty, not as a checklist for every chat. Save only material decisions, changed facts or continuation state at the existing owner; keep implementation details in the chosen project.
- **Authority:** Advisory method; verify current executor, account, capability and authority before effects. Admin invitations and payments always need the person.
- **Job:** Complete the authorized company outcome through a suitable executor with a verifiable result and recoverable continuation; understand the assignment’s parent purpose and relevant adjacent work when they change the next decision, make in-scope choices and continue safe work through minor uncertainty, and pause only your own affected behavior when continuing it would be clearly detrimental.

## Recurrence

- Recurring work: `cady-company-manage-agents` (reference scheduling). Every run of every agent follows the run sequence (skill cady-core-run-sequence). Waiting work records nextAction and a dueDate and relies on the host's next wake; there is no separate wake mechanism.

## Selection

| Mode | When |
|---|---|
| script | Known steps and deterministic rules; no LLM needed. |
| fixed_llm_pipeline | Known stages with bounded model calls or map/batch work; choose stage boundaries by distinct judgment and handoff, not an arbitrary call count. Validate output schemas; code owns branching, tools and effects. |
| agent | The work needs adaptive planning, tool selection or investigation. Bound tool scope and escalation by the outcome and actual host/provider limits. |

## Surfaces

- **Cady desktop:** Use the company's approved sign-in and work interface. Never substitute a user token or claim an execution grant that has not been verified.
- **Cady server:** Domain owners retain their supported background processing, authority and receipts. Dated reminders (renewals, notice deadlines, filings) are due items in company work: record the dated row with its owner; the selected host task reads them through get_company_work. Use the company agent-management method when a host task must be configured. Discover an actual executor before promising execution.
- **Local host:** The selected ChatGPT, Codex, Claude or equivalent host manages its execution permissions. Verify actual tools, persistence and scheduler before promising unattended work; Cady still enforces company authority. Prefer CLI JSON/file inputs for scripted Cady calls when available, MCP for agent discovery; both use the same owner contracts.

## References

- Read [Blockers](references/blockers.md) when something stops you: a missing tool, a stale document, an ambiguous spec, a failing check.
- Read [Credentials](references/credentials.md) when an effect, retry or recovery needs a credential, token or secret.
- Read [Decision standard](references/decision-standard.md) when you are unsure whether a choice needs an ask or is yours to make.
- Read [Delivery completion](references/delivery-completion.md) when you are about to call work done or deliver it and need the completion and acceptance checks.
- Read [Native orchestration](references/native-orchestration.md) when you split work across helpers or hosts, hand off, cancel or resume and need the orchestration rules.
- Read [Quality check](references/quality-check.md) when you are about to hand off, report or take an effect.
- Read [Risk first](references/risk-first.md) when an action carries external risk.
- Read [Scheduled model selection](references/scheduled-model-selection.md) when you set up or change a scheduled run, or must choose a model, effort or budget for work.
