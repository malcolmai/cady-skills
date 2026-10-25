---
name: "cady-core-run-sequence"
description: "Agent run sequence. Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.run_sequence"
  version: "ba6e909bba6b430548fb"
  library: "c5c24622655bf77f"
  function: "core"
---
# Agent run sequence

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.run_sequence": "ba6e909bba6b430548fb@c5c24622655bf77f"}})`

Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work.

## Run sequence

- **Applies to:** Every Cady session, every role. Your role card (if any) and skills say what to work on; this says the order.
- **Precedence:** Where guidance disagrees: code and tool results, then the charter, then recorded decisions, then your card and skill, then host files.

### Steps

- 1. Read get_cady_context with your agentId if you are a registered agent (a person's own session omits it), the area you are working in (for example gtm/outreach or product/context) and a task sentence. Stop if you are paused or retired. Agents: pass agentId on every Cady call that accepts it. The read returns the decisions routed to that area's action classes; read_cady search covers the rest, its method, live work and refs; read any ref with read_cady. Record new decisions with the returned writeAs.appliesTo.
- 2. Agents: reconcile first. For each reconcileWorkIds item: settle unresolved effects with their owner and call transition_company_work action='report_effect_reconciliation'; an expired claim is no longer held: claim again (step 4) or action='recover' with a recoveryNote. Start no new effect on an item until it is clear.
- 3. Agents: choose: resumeWorkIds first, then openWorkIds whose dueDate has passed or is empty, in the order served. Also read the asks you filed that were answered since your last run (agent context lists them) and act on the answers, and check due standing duties from your current assignment and hostReview; an empty work queue does not cancel those duties. Reuse the task statement, brief.doneWhen and current context as the working scope; add goal or constraints only when they change the action or acceptance. Create owner work only when needed, and claim before controlled work. Use work tools only for real company work; small fixes and questions need no work item. A finish line names the deliverable, its size rule and what done is; a sample is labelled one and never meets a request for the deliverable; a budget, time-box or access stop closes as partial (delivered N of T). After claim, only the claim holder changes the brief through checkpoint. An ongoing responsibility stays open between runs. When a goal's callReasons or measureDue name a call, record a reading first (submit_company_work_checkpoint measure), then the goal call. If neither work nor a standing duty is due, go to step 6 with outcome no_work.
- 4. Agents: claim one item: transition_company_work action='claim' (omit attemptId and claimProof; the server fills and reuses them on your connection; a claim on BLOCKED work unblocks it). Stop on a live claim conflict. A claim lasts 30 minutes (control.claim.expiresAt on the work item); renew it with action='renew' before it expires.
- 5. Do the work. Read get_cady_context {agentId, workId: id} for the skill and records. Stay within scope; resolve lane overlap before go_live. Finish every step short of a human boundary yourself and checkpoint at natural boundaries. Near the budget (about four-fifths spent or a host warning), stop starting steps and close with the result or shortfall. Ask only what blocks and what no current record answers; otherwise choose a sensible default and proceed. When a missing owner fact blocks the next step, ask now with submit_company_work_checkpoint {ask} and keep working on the rest. Put every ask you can make now in one packet: who acts, where and what, options with your recommendation, owner minutes. Access the owner must grant is an ask (kind access or setup); a wait on a third party is a nextAction, not an ask. An open hypothesis is the working assumption: treat it as answered, build on it, cite it, and propose a change only with new evidence. decisions.omissions means the list is incomplete; a capped or empty read is not proof of absence. Record decisions per cady-company-decision-check step 6; quote an OPEN pendingConfirmations item back once.
- 6. Last, close. Two records: a run (agents only, every slot, even no_work) and a work item (anyone, only for an outcome someone would track). Everyone: a reported result is taken as complete and corrected afterwards if wrong (supersede or reopen), not held for acceptance. Deliver the requested result or verify the effect; preparation is progress unless requested. Until live, prepare only. Link owner artifacts; never copy their body. Agents: close with one report_company_work call (fields, metadata and recovery: the reporting section below). Interactive runs end with asksForYou; report nextRunAt for cadence or runsOn for trigger. When scheduledBy=none, name host setup and raise the owner ask. Agents (agentId): nobody reads your reply, so your whole final reply is the reply line report_company_work returns, nothing before or after it; notify a person only on failure or an owner action.

## References

- [Reporting a run](references/reporting.md)
