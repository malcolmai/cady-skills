---
name: "cady-core-run-sequence"
description: "Agent run sequence. Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.run_sequence"
  version: "fd124e972e9b0a8eb310"
  library: "9774417a3b8911e8"
  function: "core"
---
# Agent run sequence

**Point:** One order for every session, so no run acts on stale state, doubles an effect or ends unrecorded.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work.

## Bets

- Read current company state and settle unresolved effects before starting anything new. Instead of: Act from the prompt, memory or a previous run's summary, starting with the newest or most interesting task.
- Surface any founder outcome no live work covers before routine work. Instead of: Work the existing queue in order, trusting it reflects what the founder wants.
- Work the item without claiming it; read related agents' work (same node, parent or child), build on what they finished, and never wait for them. Instead of: Claiming before work, or stopping and waiting while another agent is on the item.
- Treat the owner's recorded words as settled: ask only what only they can give, once, as one ready ask; decide the rest and keep working. Instead of: Re-asking, acting on a paraphrase, or stopping to wait whenever unsure.
- Trust a reported result and correct it afterwards, except work a user meets, which completes only once walked. Instead of: Hold every result for owner acceptance before it counts.
- End on a decision or one ready next move, decisions first; a research run's move is held for approval, never an unapproved send, and more research only if it would change the call. Instead of: Stopping at research or a question, or jumping from research to a send.
- Treat a failure of the run's own environment (dead links, stale dependencies, memory or slot pressure, missing test data) as a defect: fix its cause once, sweep for the same fault, continue. Instead of: Retry, work around it for this run only, or call it unrelated to the task and stop.
- External effects use the one approval rule and the one message-sending rule in execution authority; channel skills keep only their route mechanics. Instead of: Let each channel restate approval and sending, or let a local route diverge from the approved review.
- Classify a record by what it is when it is written (relationship type, persona, stage, the unit of work) and let that decide its one home; reuse the record that already covers it. Instead of: Filing it wherever the tool or workflow that made it writes.
- Record each decision with the one or two pieces of evidence that decided it. Instead of: Collecting quotes and figures, or recording the choice with no reason.
- When a fact you need is missing, say so and get it from its owner; if no one holds it, decide on a labelled estimate with its basis; an empty, capped or refused read means unknown, not none. Instead of: Presenting a guess, placeholder or borrowed quote as fact; stopping at unknown when you must decide; calling a record missing before trying each identifier you have (email, domain or company, name).

## Run sequence

**Precedence:** Where guidance disagrees: code and tool results, then recorded decisions, then your card and skill, then host files.

- **Applies to:** Every Cady session, every role. Your card and skills say what to work on; this says the order.

### Plan heads

- Read company state: `cady_read {"search": "$task"}`
- Reconcile unresolved effects: `work_read {"id": "$reconcileWorkId"}` (agents)
- Check which open goal this task serves: `work_read {"where": {"kind": "goal"}}`
- Start the selected work: `work_set {"id": "$workId", "status": "working"}` (agents)
- Check current decisions, then do the work: `cady_read {"kinds": ["decision"], "search": "$task"}`
- Close with the checked outcome: `work_set {"id": "$workId", "result": "<checked outcome>", "status": "done"}`

### Steps

- 1. Start with cady_start {task: your request, verbatim; agentId if you have one}: the item it names, and the point and bets that govern it (no task: the node's goals and work). Then act on its `do`; read more only for something it names and the task needs (a registered agent reads its work item, cady_read work:<workId>). Agents: pass agentId on every Cady call that accepts it. If you are paused or retired (agent.stop, retired state, an AGENT_PAUSED or AGENT_RETIRED refusal), stop: remove or pause your host trigger as the stop says, call agents_set host {action: removed} and end the run. Before work, record any new or changed outcome the person states in chat through `cady-company-decision-check` step 6.
- 2. Agents: reconcile first. For each reconcileWorkIds item settle unresolved effects with their owner (work_set {id, effects: {reconciled: {effectRef, disposition}}}). Start no new effect on an item until it is clear.
- 3. Read open goals when cady_start named no item (cady_start without a task lists the node's goals first), then their live work and brief.doneWhen; follow page and omitted-detail reads. If no open goal covers this task, say so before starting. Agents: check due standing duties from your assignment and hostReview; an empty queue does not cancel them. Read the goals_and_work section before you create work, act on asks or a goal call, or conclude no_work.
- 4. Agents: start one item with work_set {id, status: working}. Related agents are those working now on the same node, its parent or a child; cady_start and work_read name them. Read their work, build on a finished result instead of redoing it, and never wait for them. The method follows the work's subject, not the session's area: if the item is bound to another function's method, refile it (work_set {id, path, note}: the method comes from the node's path).
- 5. Do the work. Read cady_read work:<workId> and the skill ref its method names (skill.<id>). Resolve lane overlap before go_live. Finish every step short of a human boundary yourself and checkpoint at natural boundaries. Near the budget (about four-fifths spent or a host warning), stop starting steps and close with result or shortfall. Read the asking section when you would ask, a call is refused or you rely on an assumption. Record each decision per `cady-company-decision-check` step 6 (a strategy item as a point or a bet with its basis, through decisions_set; a narrow call in the work result); quote an OPEN pendingConfirmations item back once. decisions.omissions means the list is incomplete.
- 6. Close with one work_set call (fields, output shape, recovery and the walked-story rule: the reporting section). Say saved, sent or done only after the write succeeded and you read it back (an effect: cite provider evidence), otherwise proposed or unverified. Until live, prepare only. Turn each question left in your text into an ask if only the owner can answer it, else decide it and say why; chat points to the ask. Agents (agentId): nobody reads your reply, so your whole final reply is the reply line work_set returns.

## References

- Read [Reporting a run](references/reporting.md) when you close or report a run.
- Read [Goals, asks and work](references/goals-and-work.md) when you create work, or asksFiled, answered asks or a goal call are in your context.
- Read [Asking and refusals](references/asking.md) when you are blocked, a call is refused or a permission is missing.
- Read [Plan path](references/plan-path.md) when the work belongs to a plan.
