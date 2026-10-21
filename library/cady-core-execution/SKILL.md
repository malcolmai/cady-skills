---
name: "cady-core-execution"
description: "Shared execution rules: authority, blockers, credentials, effects and receipts, recurrence and model choice. Use when: a skill points here, or before an effect, credential use, retry or recovery. Not for: choosing what work to do."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.all"
  version: "2a43002125ba3124dd87a28cab9607591f961035683552e1030e2d204768a36b"
  library: "8fdc1a430e92c8e2"
  function: "core"
---
# Execution guidance

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>"})`

Shared execution rules: authority, blockers, credentials, effects and receipts, recurrence and model choice. Use when: a skill points here, or before an effect, credential use, retry or recovery. Not for: choosing what work to do.
- **Application:** Use this method when complex work, execution design, integrations or recovery need it; reuse it within the task. Combine the shared method with only the relevant use-case guidance and current company/task context. Read missing context that could change the approach; refresh authority and mutable targets before effects. Apply controls proportionately to consequence and uncertainty, not as a checklist for every chat. Save only material decisions, changed facts or continuation state at the existing owner; keep implementation details in the chosen project.
- **Authority:** Advisory method; verify current executor, account, capability and authority before effects. Admin or owner invitations and payments always need the person.
- **Blockers:** A blocker stops progress without being an external risk: a missing or unauthenticated tool, a stale document, an ambiguous specification, a failing check, an empty helper result. Work around it and record the route: the next strongest native path or a script; the reading a careful colleague would take; the cause of a failing check, never its assertion; one new prompt to an empty helper, then one fresh helper of the same class; do only a small remainder yourself, and record any move to a stronger class as an exception. An unauthenticated connection is a blocked capability, not a reason to use another environment or account. Never work around an authorisation wall, a denied permission, a provider challenge or a safety refusal; those stop that channel while the rest of the work finishes. For a product or method defect found during an authorized outcome, record expected versus observed behavior with exact evidence in the existing task or claim and route bounded repair to the owner of that product or method under current authority. Verify the repair, then continue the original operation through its supported owner transition; if none exists, hold an exact actionable handoff. A code fix alone does not complete that outcome. Keep unrelated work moving, and preserve access/provider holds, uncertain-effect reconciliation and review/release gates.

## Credentials

- Use supported provider authentication (host connector, OAuth, scoped API key or service identity); redirect OAuth retains PKCE/state and endpoint/audience-bound token protections. For explicitly authorized free private setup, generate or download credentials only through supported flows and transiently handle them only as needed before direct write to a qualified secret store and custody readback; never print or persist plaintext in chat, logs, source, arguments, prompts or company workspace. If qualified custody/readback is unavailable, hold only the credential-dependent step. Keep GUI native-user, CLI MCP and provider grants separate; use supported refresh/revocation and reconcile uncertain effects before retrying after reauthentication.
- Provider credentials for effects Cady governs (email, LinkedIn and other outbound communication, provider writes) never reach the host agent: Cady holds API and OAuth credentials server-side, and Cady's own signed local executor (the cady CLI) holds device credentials in the OS keychain. Never request, read, store or script those credentials, and never write a script that sends with them; pass execution ticket ids to the executor instead. For tools you run yourself, keep Keychain on macOS. Repeated access prompts need locked-vault/access-control/signing diagnosis, not plaintext fallback or blanket access. CLI keyring access may be attributed to its Python interpreter; stable signed packaging is a separate qualification requirement.
- Ask once. Gather every account to connect or provision, key to create (console link, exact steps, scope names and where the owner stores it, never its value) and agent or plan to review into one setup session: record each with record_company_work_setup (call_cady_tool; a BLOCKED Projects item whose boundary, of the kind that fits, carries the setup step), so Cady shows the owner one ordered packet of about 30 minutes. Listing an item grants nothing; each approval, access grant and spend keeps its own route. After the owner's session, do not come back mid-run for a credential or connection: record a newly found need as another such ask for the next packet and keep preparing.
- **Decision standard:** Direction and existing grants govern action; reversible work in scope needs no ask. Use get_company_direction for accepted choices. For a choice that belongs in direction, update it with update_company_direction and a one-line summary (the owner is notified and can edit or revert); a bet enters direction only from the owner's own words, otherwise record it as a hypothesis with its recommendation, alternatives and source refs. For a blocked action, record the missing choice and next action in a BLOCKED Projects work item through submit_company_work_checkpoint; cite that item from get_company_work in the chat close. An ask without a held item is not asked. Record the answer in its owner before resuming. Keep independent authorized work moving; silence never approves an external or irreversible effect.

See [Delivery completion](references/delivery-completion.md).
## Recurrence

- Recurring work: company_scheduling below. Every run of every agent follows `cady-core-run-sequence`. Waiting work records nextAction and a dueDate and relies on the host's next wake; there is no separate wake mechanism.

See [Risk first](references/risk-first.md).
## Surfaces

- **Cady desktop:** Use the company's approved sign-in and work interface. Never substitute a user token or claim an execution grant that has not been verified.
- **Cady server:** Domain owners retain their supported background processing, authority and receipts. Dated reminders (renewals, notice deadlines, filings) are due items in company work: record the dated row with its owner; the selected host task reads them through get_company_work. Use the company agent-management method when a host task must be configured. Discover an actual executor before promising execution.
- **Local host:** The selected ChatGPT, Codex, Claude or equivalent host manages its execution permissions. Verify actual tools, persistence and scheduler before promising unattended work; Cady still enforces company authority. Prefer CLI JSON/file inputs for scripted Cady calls when available, MCP for agent discovery; both use the same owner contracts.
