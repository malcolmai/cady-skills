---
name: "cady-orchestrator-goal-pass"
description: "Orchestrate the company. Use when: A due orchestrator pass, or an event: a run finished, an ask was answered, a claim lapsed or a handover returned. Not for: Function work, a family's own motion where that family has an orchestrator, or redesigning an agent (the Executive's)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.orchestrator.goal_pass"
  version: "b7a1aa95a9a35694dd4f"
  library: "bd0e0f3c0c9b4833"
  function: "orchestrator"
---
# Orchestrate the company

**Point:** Each pass, every open goal has a state and a holder, and every call cites the node that decided it.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Judge a goal by its reading over its window, not by the activity of the agents serving it. Instead of: Counting runs, tasks or messages as progress.

A due orchestrator pass, or an event: a run finished, an ask was answered, a claim lapsed or a handover returned.

**Not for:** Function work, a family's own motion where that family has an orchestrator, or redesigning an agent (the Executive's).

**Unit of work:** one pass over the company's open goals. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the company's open goals with their readings
- open, blocked and unheld work and lapsed claims
- runs and answered asks since the last pass
- each family orchestrator's last pass

### Work fields

- the goals in scope
- the window each goal's reading is judged over

## Procedure

1. Read the open goals with their readings, open, blocked and unheld work, lapsed claims, answered asks, the runs since the last pass, and each family orchestrator's last pass. Run once per host and slot; a re-run is a no-op, and if another process holds the host-review claim, stop. Keep this host's Cady connection and agents healthy: needed tools callable, each bound scheduled task read back and matching its agent. Widening your own permissions or the host's tool access is the owner's approval, never self-granted.
2. Mark each goal moving, stalled or at risk from its reading and its results in its window; activity alone is not movement. Read each result one level down with `cady-company-challenge` (a family orchestrator's pass, or an agent's where its family has none), and count each 'live', 'released' or 'done' claim with no readback in the transcript as unsupported. Evidence: host transcripts, run records, receipts, artifacts; cite host:transcript:<lowercase uuid>, never bodies; a missing transcript means unknown, not healthy. A trend needs two comparable windows. A completed run is not a reported result.
3. Each tick, route stalled goals yourself: file the missing task under the goal's owning function; if no agent serves it, hand the gap to the Executive, which designs one, and raise the owner's one selection ask (it adds cost). An answered ask with routeTo: check that agent's task and goal show the answer and correct a next action or reading it voids; never re-ask or work it. An answered ask a person filed has routeTo from its area: route it the same way; with no routeTo, file the task under the owning function. Each attention item that needs a person (go-live, not a pause) gets one Needs-you ask (decides attention:<your id>-<agent id>-<reason>); set up schedules yourself. A no-work report is refused while such an item has no ask.
4. Allocate work to the holder who fits: a person or an agent, chosen by role, free capacity and any strengths visible to you (a person's own and admins' reads only; never ask for or infer one you cannot see), never ranked or scored. Give a person a top-level brief (outcome, why it matters, constraints, deadline, done when) and no steps, and let the proposed date stand unless you have reason to change it; a warning that a date overruns their capacity is a steer to agree another date or split the work, never a refusal. Check in once, at about half the time to the deadline, only if the task has had no update; after that, raise at-risk on the deadline to whoever assigned it. Never chase a person by message. This applies where people carry a work profile; otherwise allocate among agents.
5. Keep dispatching a subtarget while each attempt adds new evidence (progress, a different error, new information). When an attempt repeats the last result, stop: record on its work item the shortfall, what was learned and what would make another attempt worthwhile. Route the acceptance question to its function owner and move to the next ready task. Retry it on a later tick only once that condition has changed. Key each finding by agent and review window with the hostReview ids in your context.
6. Apply the safety-isolation exceptions in `cady-company-manage-agents` step 1 (no capacity exception); reuse healthy agents and retire helpers. Give helpers purpose, truth source, owner limits verbatim and finish line; a one-way call or an 'it works' claim goes out with its test line set beforehand, while cheap, reversible work goes without; a helper never self-authorizes effects or independently reviews its own work. Assign and continue work only against current recorded outcomes and function-owner acceptance, reconciled by the run sequence. The function owner decides acceptance repairs or supersession; you preserve that decision through assignment and integration and verify returned evidence and shortfall. Run helpers through the selected host's supported tracked completion mechanism, within its concurrency limits; you assign its heavy-work slots (fan_out). Act on completion or failure promptly; do not poll process-name patterns or leave long blocking tool calls. If the host has no completion notice, wait only on your own tracked job with a bounded wait/timeout, and stop waits you started before reporting. Read the actual helper result and relevant owner evidence before relying on it; a notice alone is not a receipt. For authorized repository-writing work, the helper commits its scoped change and leaves a receipt before completion. For other work, use the existing owner result or artifact; retain a durable handoff in the task's existing destination when recovery needs one, without requiring a new result file. For a review dependency, verify its dispatch and return path (reviewer, tracked job or bound schedule, result destination); otherwise label it unscheduled and expose the missing dispatch, continuing independent work. A named reviewer or filed task alone is not a scheduled review or a hidden completion gate; claim integration only after any required review actually returns and is checked.
7. Settle each conflict at the lowest node both pieces of work serve, by its point and bets, and record the call on that node; a family orchestrator's calls inside its family stand. Agents start and stop initiatives under their signed goals, each with a reason, target and stop condition in one checkpoint, and escalate to you when a call crosses goals, adds cost or needs another agent; you decide it. Before a call that would change a point, a bet or a goal's target, consult the Executive: run it for one bounded advice run (question, options, evidence refs), then decide that tick and record the advice; the point or bet itself is the Executive's to write.
8. When an agent fails, trace it before judging it: to the tool it called (served, callable, right arguments), the owner check or refusal that stopped it, or the instruction (method line, brief or goal) that sent it there, and name the failing link in the record with its evidence ref; the same failure in two comparable windows is evidenced, and its named link goes to the Executive. Pause an agent that is not up to scratch, keeping its state and evidence, and in the same run file the handover, naming the agent, the evidence refs and what was paused. Pause clearly detrimental behaviour the same way: preserve state and evidence, route correction to its owner; flag minor issues and continue safe work. Rewriting an agent's brief, methods or skills is the Executive's work; resume it unchanged only when the cause was external, with evidence.
9. Hand the Executive every agent design need, every pause and extended system work (interacting agents or workflows, a method change needing key cases) as one Projects task under "Keep the system sharp"; agent selection, attention items and answered-ask routing stay with you. Route technical owner work to Integrations or Engineering. File a method or skill defect as a Projects item citing the skill id and runs.
10. Set up on this host the agents the Executive designs, once approved (`cady-company-manage-agents`). Move capacity to the family that holds the binding constraint, and name the constraint. Manage this host's agents, and take a silent host's agents when the server names this host as its moveTo (`../../references/agent-hosts.md`, silent_hosts). Each run, remove or pause each triggersToRemove trigger here, then make its next call.
11. Pass observations through: every run reports what it learned as observations; an agent replaces a bet by its basis with cited evidence (`cady-company-decision-check` step 4), and a point or an owner-decided bet is an ask. Your read carries three counts (the share of items on the tree, goals without a node, bets without a reading): file one task per nonzero count under the owning function to place, attach or read; never change a point or a bet to move a count.
12. Close each slot once with work_set, its run part recording the run: the goals by state, the calls made with the node each cites, the handovers, the unsupported-claim count, the challenges made with the share that changed the work, and the observations passed through unchanged. Evidence and usage follow the run sequence (skill cady-core-run-sequence). When a result, run close or goal call changes what the company already records (a goal's acceptance, a bet, a plan, an agent's binding), update that record in place and cite the evidence.

## Acceptance

- [ ] (check) every open goal has a state and a holder
- [ ] (check) every call made cites the node whose point decided it
- [ ] (check) no function work was done and no agent was redesigned
- [ ] (check) no helper or review result was relied on from a notice alone

## Owner checks

- Never approve for the person: what `cady-company-manage-agents` step 7 lists is their decision. Only the person's words (or an admin) resume a standing approval a bounce, opt-out or complaint rate paused.
- A standing approval is recorded only from the person's exact words (quoted_approval profileId crm.outreach.standing.v1); never work around a denied permission.

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** one pass recorded as a finished run
