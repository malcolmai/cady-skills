---
name: "cady-company-weekly-review"
description: "Weekly review. Use when: The weekly review: assess the company, call every goal and initiative, check bets, hand changes to the orchestrator. Not for: A new company's setup (`cady-company-onboarding`), pushing work along, scheduling or dispatching agents or doing function work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.weekly_review"
  version: "39403053a66956856b16"
  library: "3462e1dbd5e6b840"
  function: "company"
---
# Weekly review

**Point:** Call every goal against its prediction, weigh each initiative and hand the changes to the orchestrator, so calls stay calibrated.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Call every open goal at the weekly review, a persist in one line with its reading; between reviews take one decision only on a trigger. Instead of: Pick one decision per pass and let the other goals stand unrecorded.
- Judge by results against intended conditions and dates, scoring each reading against the last prediction; a missing reading is unknown with a dated check. Instead of: Judge a goal from run reports, closed tasks, files created or its trend, and call it on track without the prediction.
- Weigh each open initiative to a verdict each weekly review: start it as a goal, fold it into one, or decline it with the reason and a reopening trigger. Instead of: Leave a founder idea open until it seems timely, or add it as work without weighing it against the point and bets.
- Each weekly review, check every current bet against the latest readings of the goals that test it; a contradicted bet is an observation on its node. Instead of: Score goals and leave the bets unexamined.
- End the pass in one instruction to the orchestrator listing every change, each tied to its goal and outcome, with a Next and Check line; do none of the work yourself. Instead of: Filing function tasks yourself, or handing next steps down as a recommendation.

The weekly review: assess the company, call every goal and initiative, check bets, hand changes to the orchestrator.

**Not for:** A new company's setup (`cady-company-onboarding`), pushing work along, scheduling or dispatching agents or doing function work.

**Unit of work:** one weekly review of every open goal and initiative. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- the open goals with their readings and last predictions
- open initiatives and open handovers

### Sources

- cady_start (the root's point and bets)
- the finance plan read (cash, burn, runway)
- cady_read changes since your last review
- each function head's current situation call

## Procedure

1. Assess. cady_start {loop: "outer"} returns the goals due a call, the bets to check, the open handovers and the agents. This is the weekly pass, or any pass where a goal's callReasons include no_recent_call; between reviews take only the one decision with the highest cost of delay (`cady-company-decision`), or write nothing and end with 'goals stand'. Judge results and dates against intended conditions, not task counts; disclose incomplete coverage; work first on the one or two problems that decide whether the company wins.
2. Decisions due: score any decision past its reviewBy against its prediction, and keep, change or stop it (`cady-company-decision` step 1).
3. Goals (`references/company-goals.md`, `references/executive-weekly.md`, goal calls): call every open goal, scoring its reading against the last prediction (unknown with a dated check when there is none), then persist, pivot, parallel or stop it, aimed at the goal's binding constraint (the step with the longest wait, the lowest throughput or the missing input; before product-market fit it is usually customer evidence: check the GTM pipeline from list to calls for the proposed ICP before adding product work).
4. Initiatives (`references/executive-weekly.md`, initiatives): give each open one a verdict, start, fold or decline, with its reason.
5. Handovers (`references/executive-weekly.md`, handovers): answer each open task under "Keep the system sharp" and read the library CHANGELOG.md since your last agent review; change an agent only through `cady-company-change-agent-behaviour`.
6. Bets against readings: compare each current bet (the root's bets and orchestrator.bets) with the latest reading of the goals that test it. A contradicting reading is work_set observations [{nodeKey, text, sourceRef}] on that bet's node; a bet with no reading is unknown, so name the read that would get one.
7. Loop drift and load (`references/executive-weekly.md`, load and fit): flag an agent acting outside its loop as an observation on the methods node, and hand work that should move to the orchestrator under step 8.
8. Hand the changes to the orchestrator as one instruction (`references/executive-weekly.md`, hand-off): each change names the goal or decision it serves and the outcome, not how. Designing an agent stays yours (step 5); file no task under another function and do no function work yourself.
9. Close the result with two lines. Next: each change to the next runs, naming the agent, method or goal it changes, routed as step 8 says. Check: whether this review judged from readings against the point, where it went deep, and what to judge differently.

## Acceptance

- [ ] (check) every open goal has a new call with its reading scored against its prediction, or unknown with a dated check; every stopped goal has a stop reason, evidence and driverComparison
- [ ] (check) every open initiative has a verdict with its reason; every open handover is answered; every current bet is checked against its readings
- [ ] (check) changes sent as one orchestrator instruction; no task filed under another function and no function work done
- [ ] (fresh) the result shows outcomes against intended conditions, not activity, and ends with a Next and a Check line

## Owner checks

- every goal call cites the prediction it scored
- the orchestrator instruction names a goal and an outcome per change, never steps

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** the Executive records its calls and verdicts; the orchestrator acts on its one instruction

## References
- Read [Company goals](references/company-goals.md) when you start, reshape or stop a goal, or an idea becomes one.
- Read [Executive weekly review: goal calls, initiatives, handovers, load and hand-off](references/executive-weekly.md) when you run the weekly review's goal calls, initiative verdicts, handovers, load and fit, or the hand-off to the orchestrator.
