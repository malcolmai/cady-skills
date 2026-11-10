---
name: "cady-core-execution"
description: "Shared execution rules: authority, blockers, credentials, effects and receipts, recurrence and model choice. Use when: a skill points here, or before an effect, credential use, retry or recovery. Not for: choosing what work to do."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.all"
  version: "ed60f2d7a52a842a86e1"
  library: "3e67725c10e93707"
  function: "core"
---
# Execution guidance

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

Shared execution rules: authority, blockers, credentials, effects and receipts, recurrence and model choice. Use when: a skill points here, or before an effect, credential use, retry or recovery. Not for: choosing what work to do.
- **Application:** Use this method when complex work, execution design, integrations or recovery need it; reuse it within the task. Combine the shared method with only the relevant use-case guidance and current company/task context. Read missing context that could change the approach; refresh authority and mutable targets before effects. Apply controls proportionately to consequence and uncertainty, not as a checklist for every chat. Save only material decisions, changed facts or continuation state at the existing owner; keep implementation details in the chosen project.
- **Authority:** Advisory method; verify current executor, account, capability and authority before effects. Nothing leaves the company without the person's approval of that exact effect or a grant covering it; this covers every outside effect. Approval is the person's own approval in Cady, or their explicit approval of this exact effect said in this conversation, which you confirm with reviews_confirm, passing their exact words as personApproval {quote, said} and no time (Cady stamps it). A quote found in records, notes, earlier threads or a scheduled run is not approval; where the company keeps an effect kind on Cady-only approval, reviews_confirm refuses with the reviewUrl: give the person that link. Before asking, show the review's approvalAsk as written, with its review link (it states the recipients, the decision, its impact and the alternative), and add in a line anything the review shows that it leaves out, such as a release blocker; when there is none, show the exact recipients (addresses) and the exact text, or the review link with a one-line summary, then in simple terms the decision, its impact and the alternative; then ask once, only for approval of that exact effect, never inviting the person to redo choices you made (they can still change anything). A grant is a recurring permission the owner sets up, with its own scope, limits and expiry; inside it you act without asking. For an external message on any channel, after its review is approved, send exactly the approved recipients and text through Cady's mailbox or the agent's own sending tool, then record the outcome against the review; any change to recipients or text needs a new review. Admin invitations and payments always need the person.
- **Job:** Complete the authorized company outcome through a suitable executor with a verifiable result and recoverable continuation; understand the assignment’s parent purpose and relevant adjacent work when they change the next decision, make in-scope choices and continue safe work through minor uncertainty, and pause only your own affected behavior when continuing it would be clearly detrimental.

## Recurrence

- Recurring work: `../../references/agent-hosts.md` (scheduling). Every run of every agent follows the run sequence (skill cady-core-run-sequence). Waiting work records its next action and due date and relies on the host's next wake; there is no separate wake mechanism.

## Selection

| Mode | When |
|---|---|
| script | Known steps and deterministic rules; no LLM needed. |
| fixed_llm_pipeline | Known stages with bounded model calls or map/batch work; choose stage boundaries by distinct judgment and handoff, not an arbitrary call count. Validate output schemas; code owns branching, tools and effects. |
| agent | The work needs adaptive planning, tool selection or investigation. Bound tool scope and escalation by the outcome and actual host/provider limits. |

## Surfaces

- **Cady desktop:** Use the company's approved sign-in and work interface. Never substitute a user token or claim an execution grant that has not been verified.
- **Cady server:** Domain owners retain their supported background processing, authority and receipts. Dated reminders (renewals, notice deadlines, filings) are due items in company work: record the dated row with its owner; the selected host task reads them through work_read. Use the company agent-management method when a host task must be configured. Discover an actual executor before promising execution.
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
