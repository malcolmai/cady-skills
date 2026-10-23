---
name: "cady-core-run-sequence"
description: "Agent run sequence. Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.run_sequence"
  version: "ddc861d39b3d8ed23cb630e2ed0c5158b5c7dc3e83dfa32a747ae995364bb576"
  library: "c524ef7ffada6715"
  function: "core"
---
# Agent run sequence

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.run_sequence": "ddc861d39b3d8ed23cb630e2ed0c5158b5c7dc3e83dfa32a747ae995364bb576"}})`

Run one ordered piece of company work from reconciliation through result. Use when: the user wants a task carried through to a recorded outcome. Not for: setting up recurring work.

## Run sequence

- **Applies to:** Every Cady session, every role. Your role card (if any) and skills say what to work on; this says the order.
- **Previous run check:** Only when the owner has opted this host in (a current decision with subject host:previous_run_check): on Codex, before step 1, if the newest rollout in ~/.codex/sessions other than this session's ended on a usage limit or auth error, call report_host_event {event: "previous_run", reason: "rate_limit" or "authentication_failed", resetsAt: its resets_at as an ISO time, session: file name} (call_cady_tool if unlisted); never copy its text.

### Steps

- 1. Read get_cady_context with your agentId if you are a registered agent (a person's own session omits it), the area you are working in (for example gtm/outreach or product/context) and a task sentence. Stop if you are paused or retired. Agents: pass agentId on every Cady call that accepts it. The read returns the decisions routed to that area's action classes; read_cady search covers the rest, its method, live work and refs; read any ref with read_cady. Record new decisions with the returned writeAs.appliesTo.
- 2. Agents: reconcile first. For each reconcileWorkIds item: settle unresolved effects with their owner and call transition_company_work action='report_effect_reconciliation'; an expired claim is no longer held: claim again (step 4) or action='recover' with a recoveryNote; a legacy result still pending (OPEN with a result) takes action='accept_result' once, otherwise leave it. Start no new effect on an item until it is clear.
- 3. Agents: choose: resumeWorkIds first, then openWorkIds whose dueDate has passed or is empty, in the order served. Also check due standing duties from your current assignment and hostReview; an empty work queue does not cancel those duties. Reuse the task statement, brief.doneWhen and current context as the working scope; add goal or constraints only when they change the action or acceptance. Create owner work only when needed, and claim before controlled work. A finish line names the deliverable, its size rule and what done is; a sample is labelled one and never meets a request for the deliverable; a budget, time-box or access stop closes as partial (delivered N of T). Reuse the existing done-when lines. After claim, only the claim holder changes the brief through checkpoint, . Do not turn every task into a universal form. Use work tools only for real company work; small fixes and questions need no work item. Ordinary reads, monitoring and preparation do not require a new task by default. An ongoing responsibility stays open between runs. If neither work nor a standing duty is due, go to step 6 with outcome no_work.
- 4. Agents: claim one item: transition_company_work action='claim' (omit attemptId and claimProof; the server fills and reuses them on your connection; a claim on BLOCKED work unblocks it). Stop on a live claim conflict. A claim lasts 30 minutes (control.claim.expiresAt on the work item); renew it with action='renew' before it expires.
- 5. Do the work. Read get_cady_context {agentId, workId: id} for the skill and records. Stay within scope; resolve lane overlap before go_live. Finish every step short of a human boundary yourself and checkpoint at natural boundaries. Near the budget (about four-fifths spent or a host warning), stop starting steps and close with the result or shortfall. Ask only what blocks and what no current record answers; otherwise choose a sensible default and proceed. When a missing owner fact blocks the next step, ask now with submit_company_work_checkpoint {ask} and keep working on the rest. Put every ask you can make now in one packet: who acts, where and what, options with your recommendation, owner minutes. An open hypothesis is the working assumption: treat it as answered, build on it, cite it, and propose a change only with new evidence. decisions.omissions means the list is incomplete; a capped or empty read is not proof of absence. Record a chat approval or correction in the person's exact words (source chat, quote, decidedBy "me", status COMPLETE) and act on it; quote an OPEN one from pendingConfirmations back once. Record each decision once and supersede it to change it. A statement is a one-sentence title; reasons go in rationale and sources in evidenceRefs.
- 6. Last, call report_company_work once; use the reporting section below for its fields, metadata and recovery. For existing work, supply the expectedRevision read with your intent unless the owner binds the request to your valid claim. Establish decisionId/nonce and a stable partKey for every member of each populated part array before the first mutation; retain them and the unchanged payload after a lost response. A corrected payload gets a new report identity. Never refresh a revision just to force stale intent through. Link owner artifacts; never copy their body. Preserve material checkpoints/no-change, partial/blocked status, unresolved effects and follow the close tool's parts and pre-close checks during recovery. Cady reports or accepts under current owner policy; reported done alone proves neither acceptance nor business outcome. Deliver requested result or verify effect; preparation is progress unless requested. Sends need owner receipts. Until live, prepare only. Interactive runs end with asksForYou; report nextRunAt for cadence or runsOn for trigger. When scheduledBy=none, name host setup and raise the owner ask.

## References

- [Refusal codes](references/refusals.md)
- [Reporting a run](references/reporting.md)
