---
name: "cady-core-execution"
description: "Shared execution rules: authority, blockers, credentials, effects and receipts, recurrence and model choice. Use when: a skill points here, or before an effect, credential use, retry or recovery. Not for: choosing what work to do."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.all"
  version: "1ba582b04e05f5538ad772a769e709541f0f76c3d011f639769b5b70f713422e"
  library: "c524ef7ffada6715"
  function: "core"
---
# Execution guidance

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>"})`

Shared execution rules: authority, blockers, credentials, effects and receipts, recurrence and model choice. Use when: a skill points here, or before an effect, credential use, retry or recovery. Not for: choosing what work to do.
- **Application:** Use this method when complex work, execution design, integrations or recovery need it; reuse it within the task. Combine the shared method with only the relevant use-case guidance and current company/task context. Read missing context that could change the approach; refresh authority and mutable targets before effects. Apply controls proportionately to consequence and uncertainty, not as a checklist for every chat. Save only material decisions, changed facts or continuation state at the existing owner; keep implementation details in the chosen project.
- **Authority:** Advisory method; verify current executor, account, capability and authority before effects. Admin or owner invitations and payments always need the person.
- **Blockers:** A blocker stops progress without being an external risk: a missing or unauthenticated tool, a stale document, an ambiguous specification, a failing check, an empty helper result. Work around it and record the route: the next strongest native path or a script; the reading a careful colleague would take; the cause of a failing check, never its assertion; one new prompt to an empty helper, then one fresh helper of the same class; do only a small remainder yourself, and record any move to a stronger class as an exception. An unauthenticated connection is a blocked capability, not a reason to use another environment or account. Never work around an authorisation wall, a denied permission, a provider challenge or a safety refusal; those stop that channel while the rest of the work finishes. For a product or method defect found during an authorized outcome, record expected versus observed behavior with exact evidence in the existing task or claim and route bounded repair to the owner of that product or method under current authority. Verify the repair, then continue the original operation through its supported owner transition; if none exists, hold an exact actionable handoff. A code fix alone does not complete that outcome. Keep unrelated work moving, and preserve access/provider holds, uncertain-effect reconciliation and review/release gates.

See [Credentials](references/credentials.md).

See [Delivery completion](references/delivery-completion.md).

See [Native orchestration](references/native-orchestration.md).

## Recurrence

- Recurring work: company_scheduling below. Every run of every agent follows `cady-core-run-sequence`. Waiting work records nextAction and a dueDate and relies on the host's next wake; there is no separate wake mechanism.

## Risk first

- Before code, name consequential effects, the company's critical paths and worst failures; derive focused edge-case and security tests, then implement the smallest controls.
- For two emails, journal each logical message separately before dispatch; key by company, operation and message identity. After first success and second timeout, retain the first receipt and reconcile the second with the provider. Never rerun the whole batch or blindly resend an uncertain effect. A local lock alone cannot guarantee exactly-once delivery.
- For effectful integrations, cover relevant failure boundaries: duplicate delivery, crash near provider acceptance, partial success, timeout, rate limit, cancellation, revoked permission and wrong account/tenant. Select tests for changed behavior and plausible consequence; reuse existing evidence where it suffices. Use provider idempotency where supported; otherwise stop ambiguous sends for reconciliation.
- Where untrusted input reaches execution, test relevant source/model manipulation, shell/path/URL injection and secret leakage. Use argument arrays, validated paths/destinations, schema validation, least privilege and redacted receipts. Dry runs must have no external effects; cap calls, tokens, cost, runtime and concurrency.

See [Scheduled model selection](references/scheduled-model-selection.md).

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
