---
name: "cady-core-run-sequence"
description: "Agent run sequence. Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.run_sequence"
  version: "e7abd7be22de94b2ac02"
  library: "eeb0c2f0062592df"
  function: "core"
---
# Agent run sequence

**Point:** One order for every session, so no run acts on stale state, doubles an effect or ends unrecorded.

**Company context:** `context_read({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.run_sequence": "e7abd7be22de94b2ac02@eeb0c2f0062592df"}})`

Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work.

## Bets

- Read current company state and settle unresolved effects before starting anything new. Instead of: Act from the prompt, memory or a previous run's summary, starting with the newest or most interesting task.
- Surface any founder outcome no live work covers before routine work. Instead of: Work the existing queue in order, trusting it reflects what the founder wants.
- One holder claims, scopes and finishes each item; a claim expires so a dead session cannot block it. Instead of: Let any session that sees an item work on it.
- Treat the owner's recorded words as settled: ask only what only they can give, once, as one ready ask; decide the rest and keep working. Instead of: Re-asking, acting on a paraphrase, or stopping to wait whenever unsure.
- Trust a reported result and correct it afterwards, except work a user meets, which completes only once walked. Instead of: Hold every result for owner acceptance before it counts.
- End on a decision or one ready next move, decisions first; a research run's move is held for approval, never an unapproved send, and more research only if it would change the call. Instead of: Stopping at research or a question, or jumping from research to a send.
- Treat a failure of the run's own environment (dead links, stale dependencies, memory or slot pressure, missing test data) as a defect: fix its cause once, sweep for the same fault, continue. Instead of: Retry, work around it for this run only, or call it unrelated to the task and stop.
- External effects use the one approval rule and the one message-sending rule in execution authority; channel skills keep only their route mechanics. Instead of: Let each channel restate approval and sending, or let a local route diverge from the approved review.
- Classify a record by what it is when it is written (relationship type, persona, stage, the unit of work) and let that decide its one home; reuse the record that already covers it. Instead of: Filing it wherever the tool or workflow that made it writes.
- Record each decision with the one or two pieces of evidence that decided it. Instead of: Collecting quotes and figures, or recording the choice with no reason.
- When a fact you need is missing, say so and get it from its owner; if no one holds it, decide on a labelled estimate with its basis; an empty, capped or refused read means unknown, not none. Instead of: Filling it with a plausible value presented as fact, a template marker, or a quote found somewhere else; or stopping at unknown when the call still has to be made.

## Run sequence

**Precedence:** Where guidance disagrees: code and tool results, then the charter, then recorded decisions, then your card and skill, then host files.

- **Applies to:** Every Cady session, every role. Your card and skills say what to work on; this says the order.

### Plan heads

- Read company state: `context_read {"task": "$task"}`
- Reconcile unresolved effects: `work_read {"workId": "$reconcileWorkId"}` (agents)
- Check which open goal this task serves: `work_read {"decisions": {"contextType": "goal", "state": "current"}, "homePage": {"area": "goals", "filter": "active"}}`
- Claim the selected work: `work_write {"do": "claim", "expectedGeneration": "$generation", "expectedRevision": "$revision", "workId": "$workId"}` (agents)
- Check current decisions, then do the work: `work_read {"decisions": {"state": "current"}}`
- Close with the checked outcome: `work_write {"do": "finish", "outcome": "done", "result": "<checked outcome>", "workId": "$workId"}`

### Steps

- 1. Call context_read with your agentId if you are a registered agent (a person's own session omits it), the area you work in and a task sentence. Agents: pass agentId on every Cady call that accepts it. If you are paused or retired (agent.stop, retired state, an AGENT_PAUSED or AGENT_RETIRED refusal), stop: remove or pause your host trigger as the stop says, call agents_change mode confirm_unscheduled and end the run. Before work, record any new or changed outcome the person states in chat through `cady-company-decision-check` step 6.
- 2. Agents: reconcile first. For each reconcileWorkIds item settle unresolved effects with their owner (work_write with workId and reconciled {effectRef, disposition}); an expired claim is no longer held: claim again (step 4) or recover it with work_write {do: "recover", workId, why}. Start no new effect on an item until it is clear.
- 3. Read open goals and current goal decisions (including the person's recorded words), then their live work and brief.doneWhen; follow page and omitted-detail reads. If no open goal covers this task, say so before starting. Agents: check due standing duties from your assignment and hostReview; an empty queue does not cancel them. Claim before controlled work; after claim only the claim holder changes the brief, through checkpoint. Read the goals_and_work section before you create work, act on asks or a goal call, or conclude no_work.
- 4. Agents: claim one item with work_write {do: "claim", workId, expectedRevision, expectedGeneration}. Stop on a live claim conflict. The method follows the work's subject, not the session's area: if the item is bound to another function's method, refile it (work_write with workId, methodId and why). A claim lasts 30 minutes (control.claim.expiresAt); renew it before it expires by claiming again (same call).
- 5. Do the work. Read context_read (agentId, workId) for the skill. Resolve lane overlap before go_live. Finish every step short of a human boundary yourself and checkpoint at natural boundaries. Near the budget (about four-fifths spent or a host warning), stop starting steps and close with result or shortfall. Read the asking section when you would ask, a call is refused or you rely on an assumption. Record each decision per `cady-company-decision-check` step 6 (subject, rationale, alternatives, layer); quote an OPEN pendingConfirmations item back once. decisions.omissions means the list is incomplete.
- 6. Close with one work_write call (fields, output shape, recovery and the walked-story rule: the reporting section). Say saved, sent or done only after the write succeeded and you read it back (an effect: cite provider evidence), otherwise proposed or unverified. Until live, prepare only. Turn each question left in your text into an ask if only the owner can answer it, else decide it and say why; chat points to the ask. Agents (agentId): nobody reads your reply, so your whole final reply is the reply line work_write returns.

## References

- Read [Reporting a run](references/reporting.md) when you close or report a run.
- Read [Goals, asks and work](references/goals-and-work.md) when you create work, or asksFiled, answered asks or a goal call are in your context.
- Read [Asking and refusals](references/asking.md) when you are blocked, a call is refused or a permission is missing.
- Read [Plan path](references/plan-path.md) when the work belongs to a plan.
