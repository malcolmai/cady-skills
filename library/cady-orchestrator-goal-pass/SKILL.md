---
name: "cady-orchestrator-goal-pass"
description: "Orchestrate the company. Use when: A due orchestrator pass, or an event: a run finished, an ask answered, a handover returned or a family trigger. Not for: Function work or redesigning an agent (the Executive's)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.orchestrator.goal_pass"
  version: "8415ea467ee4cd032244"
  library: "7d6773c56f890604"
  function: "orchestrator"
---
# Orchestrate the company

**Point:** Keep every open goal moving on its reading, each call citing its node, so nothing stalls unseen.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Judge a goal by its reading over its window, not by the activity of the agents serving it. Instead of: Counting runs, tasks or messages as progress.
- Apply the family's gate before adding effort: an evidence gate, WIP limit, runway line or lead time. Instead of: Pushing more volume, starts or spend at a stalled goal.

A due orchestrator pass, or an event: a run finished, an ask answered, a handover returned or a family trigger.

**Not for:** Function work or redesigning an agent (the Executive's).

**Unit of work:** one pass over the company's open goals. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the company's open goals with their readings
- open and blocked work
- runs and answered asks since the last pass

### Work fields

- the goals in scope
- the window each goal's reading is judged over

## Procedure

1. Read the open goals with their readings, open and blocked work, answered asks and the runs since the last pass. Run once per slot; a re-run is a no-op. Keep the Cady connection and the agents you manage healthy: needed tools callable, each bound scheduled task read back and matching its agent. Widening your own permissions or the host's tool access is the owner's approval, never self-granted.
2. Mark each goal moving, stalled or at risk from its reading and results in its window; activity alone is not movement. For a goal of a family in `references/family-checks.md`, apply its gate before adding effort. Read each result one level down with `cady-orchestrator-challenge`, and count each 'live', 'released' or 'done' claim with no readback in the transcript as unsupported. Cite host:transcript:<lowercase uuid>, never bodies; a missing transcript means unknown, not healthy. A trend needs two comparable windows.
3. Route stalled goals yourself: file the missing task under the goal's owning function; if no agent serves it, hand the gap to the Executive as its one task (step 8), even with no Executive agent yet, which designs one, and raise the owner's one selection ask (it adds cost). Check an answered ask with routeTo against that agent's task and goal, correcting what it voids; never re-ask it. Each attention item that needs a person (a go-ahead to go live, not a pause) gets one Needs-you ask.
4. Allocate work to the holder who fits, a person or an agent, by role, free capacity and any strengths visible to you; never ask for, infer or rank a strength you cannot see. Give a person a top-level brief (outcome, why it matters, constraints, deadline, done when) and no steps, check in once at about half the time to the deadline only if there has been no update, and never chase a person by message.
5. Keep dispatching a subtarget while each attempt adds new evidence; when one repeats the last result, stop: record the shortfall, what was learned and what would make another attempt worthwhile, route the acceptance question to its function owner and move on, retrying only once that condition has changed. Key each finding by agent and review window with the hostReview ids in your context.
6. Run helpers by `references/native-orchestration.md` (the pass rules): reuse healthy agents, retire helpers, and rely on a helper's actual result and the owner's evidence, never its notice.
7. Settle each conflict at the lowest node both pieces of work serve, by its point and bets, and record the call on that node. Agents escalate to you when a call crosses goals, adds cost or needs another agent. Before a call that would change a point, a bet or a goal's target, run the Executive for one bounded advice run, decide that tick and record the advice; the point or bet itself is the Executive's to write.
8. When an agent fails, trace it before judging it: the tool it called, the owner check or refusal that stopped it, or the instruction that sent it there; name the failing link with its evidence ref. The same failure in two comparable windows goes to the Executive, as does every agent design need, pause and extended system work, as one Projects task under "Keep the system sharp". Pause an agent that is not up to scratch or clearly detrimental, keeping its state, and file the handover in the same run (`cady-company-manage-agents` steps 8-9); rewriting an agent is the Executive's work.
9. Host setup for the agents the Executive designs, once approved, is `cady-company-manage-agents` step 10. Move capacity to the family that holds the binding constraint, and name the constraint.
10. Pass observations through: every run reports what it learned; an agent writes or replaces a point or a bet by its basis with cited evidence, and the owner is told (`cady-company-decision` step 4). File one task per nonzero count of your read (items on the tree, goals without a node, bets without a reading) under the owning function; never change a point or a bet to move a count.
11. Close each slot once with work_set, its run part recording the goals by state, the calls with the node each cites, the handovers, the unsupported-claim count, the challenges made with the share that changed the work and the observations passed through; for a family goal also its report line. Evidence and usage follow `references/run-reporting.md`; update any record a result or call changes in place.

## Acceptance

- [ ] (check) every open goal has a state and a holder
- [ ] (check) every call made cites the node whose point decided it
- [ ] (check) no function work was done and no agent was redesigned
- [ ] (check) no helper or review result was relied on from a notice alone
- [ ] (check) every live agent has open work and a host binding
- [ ] (check) a family goal's gate was applied before effort was added, and its report line is in the run close

## Owner checks

- Never approve for the person: what `cady-company-manage-agents` step 7 lists is their decision.

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** one pass recorded as a finished run

## References
- Read [Family checks](references/family-checks.md) when a goal of the GTM, product, finance or operations family is stalled or at risk, or one of its trigger events arrives.
- Read [Goals and work: choose, create and close work](references/goals-and-work.md) when you choose or create work, act on asks, or a goal call is due.
- Read [Model selection: model, effort and budget for scheduled work](references/model-selection.md) when you set up or change a scheduled run, or choose a model, effort or budget for work.
- Read [Native orchestration: helpers, handoff and review](references/native-orchestration.md) when you split work across helpers or hosts, hand off, cancel or resume, or review a helper's result.
- Read [Plan path](references/plan-path.md) when the work belongs to a plan, or you create or change one.
- Read [Run reporting: close and report a run](references/run-reporting.md) when you close or report a run, or judge a reported result.
