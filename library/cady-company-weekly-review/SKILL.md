---
name: "cady-company-weekly-review"
description: "Weekly review. Use when: The weekly review: judge effectiveness, call every goal and initiative, re-test bets, hand changes to the manager. Not for: A new company's setup (`cady-company-onboarding`), pushing work along, scheduling or dispatching agents or doing function work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.weekly_review"
  version: "69d2ded9bcecce676363"
  library: "b00d595039ef50eb"
  function: "company"
---
# Weekly review

**Point:** Judge whether the work is effective and aligned, call every goal against its prediction and hand the changes over once.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Call every open goal at the weekly review, a persist in one line with its reading; between reviews take one decision only on a trigger. Instead of: Pick one decision per pass and let the other goals stand unrecorded.
- Judge by results against intended conditions and dates, scoring each reading against the last prediction; a missing reading is unknown with a dated check. Instead of: Judge a goal from run reports, closed tasks, files created or its trend, and call it on track without the prediction.
- Weigh each open initiative to a verdict each weekly review: start it as a goal, fold it into one, or decline it with the reason and a reopening trigger. Instead of: Leave a founder idea open until it seems timely, or add it as work without weighing it against the point and bets.
- Each weekly review, check every current bet against the latest readings of the goals that test it; a contradicted bet is an observation on its node. Instead of: Score goals and leave the bets unexamined.
- End the pass in one instruction to the manager listing every change, each tied to its goal and outcome, with a Next and Check line; do none of the work yourself. Instead of: Filing function tasks yourself, or handing next steps down as a recommendation.

The weekly review: judge effectiveness, call every goal and initiative, re-test bets, hand changes to the manager.

**Not for:** A new company's setup (`cady-company-onboarding`), pushing work along, scheduling or dispatching agents or doing function work.

**Unit of work:** one weekly review of every open goal and initiative. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- the open goals with their readings and last predictions
- open initiatives and open handovers

### Sources

- cady_start (the root's point and bets)
- the books (cash, burn, runway) and the finance node (the plan)
- cady_read changes since your last review
- each function head's current situation call

## Procedure

1. Assess. cady_start {loop: "outer"} returns the goals, event-due first, the bets to check, the open handovers and the agents. Between reviews take only an event's call or the one decision with the highest cost of delay (`cady-company-decision`), or write nothing and end with 'goals stand'. Disclose incomplete coverage; work first on the one or two problems that decide whether the company wins.
2. Effectiveness: judge each goal's and task's results and dates against intended conditions, not task counts, and whether they serve the root's point and bets (keeping agents unstuck is the manager's).
3. Goals (`references/company-goals.md`, `references/executive-weekly.md`, goal calls): call every open goal at each review, sooner when its callReasons name an event (no fixed clock). Score its reading against the last prediction (unknown when there is none, with a scheduled run or reminder to read it), then persist, pivot, parallel or stop it, aimed at the goal's binding constraint (the step with the longest wait, the lowest throughput or the missing input; before product-market fit it is usually customer evidence: check the GTM pipeline from list to calls for the proposed ICP before adding product work).
4. Initiatives (`references/executive-weekly.md`, initiatives): give each open one a verdict, start, fold or decline, with its reason.
5. Agents (`references/executive-weekly.md`, handovers): answer each open task under "Keep the system sharp", judge each agent's quality from its results, flag one acting outside its loop on the methods node, and read the library CHANGELOG.md since your last agent review; change an agent only through `cady-company-change-agent-behaviour`.
6. Bets and older decisions: re-test each current bet (the root's bets and betsToCheck in your cady_start read) and decision whose evidence aged or readings contradict it; keep, replace or drop it (`cady-company-decision` step 6). A contradicting reading is work_set observations [{nodeKey, text, sourceRef}] on that bet's node; a bet with no reading is unknown, so name the read that would get one.
7. Load (`references/executive-weekly.md`, load and fit): hand work that should move to the manager under step 8.
8. Hand the changes to the manager as one instruction (`references/executive-weekly.md`, hand-off): each change names the goal or decision it serves and the outcome, not how. Designing an agent stays yours (step 5).
9. Close the result with two lines. Next: each change to the next runs, naming the agent, method or goal it changes, routed as step 8 says. Check: whether this review judged from readings against the point, where it went deep, and what to judge differently.

## Acceptance

- [ ] (check) every open goal has a new call with its reading scored against its prediction, or unknown with a dated check; every stopped goal has a stop reason, evidence and driverComparison
- [ ] (check) every open initiative has a verdict with its reason; every open handover is answered; every aged or contradicted bet is re-tested
- [ ] (check) changes sent as one manager instruction; no task filed under another function and no function work done
- [ ] (fresh) the result judges outcomes and alignment, not activity, and ends with a Next and a Check line

## Owner checks

- every goal call cites the prediction it scored
- the manager instruction names a goal and an outcome per change, never steps

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** the Executive records its calls and verdicts; the manager acts on its one instruction

## References
- Read [Company goals](references/company-goals.md) when you start, reshape or stop a goal, or an idea becomes one.
- Read [Executive weekly review: goal calls, initiatives, handovers, load and hand-off](references/executive-weekly.md) when you run the weekly review's goal calls, initiative verdicts, handovers, load and fit, or the hand-off to the manager.
