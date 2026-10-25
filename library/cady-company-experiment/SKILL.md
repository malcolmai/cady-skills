---
name: "cady-company-experiment"
description: "Pre-registered experiment. Use when: Test the riskiest assumption with a pre-registered experiment and a decision rule set before any work starts. Not for: Routine delivery whose desired behavior is clear, or reliability fixes with acceptance; use `cady-engineering-method` for implementation."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.experiment"
  version: "5565b44c5303ca52f939"
  library: "fb0ed0826641a359"
  function: "company"
---
# Pre-registered experiment

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.experiment": "5565b44c5303ca52f939"}})`

Test the riskiest assumption with a pre-registered experiment and a decision rule set before any work starts.

**Not for:** Routine delivery whose desired behavior is clear, or reliability fixes with acceptance; use `cady-engineering-method` for implementation.

**Unit of work:** one hypothesis and the decision that settles it. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- the hypothesis decision item
- the Files and CRM records the test produces

## Procedure

1. Pick the riskiest assumption: the one that would most change the plan if wrong and that you are least sure of. Test it before easier ones.
2. Look it up first: get_company_work decisions {state: "current", subject: "hypothesis:<slug>"}. If a current hypothesis exists, continue it; never register it twice.
3. Pre-register before any work, as a hypothesis decision item (submit_company_work_checkpoint, status OPEN, decision {kind: "hypothesis", subject: "hypothesis:<slug>", rationale, authority "agent" and no decidedBy: Cady records it as your agent}): the hypothesis; one behavioural metric (what people do, not what they say); a pass line and a fail line; the decision taken on each outcome; sample size and time box; stop conditions; a sourced cost ceiling or explicit unknown; zero incremental external cost is the evaluation fallback without a selected budget, while any paid effect requires checked current authority. Put the full design in a File the item cites. Cite the question:<slug> it tests, when there is one.
4. Design the smallest test that could change the decision, varying one main thing: conversations first, then a manual or concierge test, then a build. Prepare everything yourself; come to the person only at a boundary (a call, filming, spend outside verified authority, a send, a signature, access) with a ready packet.
5. Run it as Projects work citing company:work:<hypothesisId>. Stop early when a stop condition is met. If the instrument or environment changes during the run, take a new baseline before comparing.
6. Judge it only against the pre-registered lines. Record the outcome as a decision (status COMPLETE) that supersedes the hypothesis (subject "hypothesis.outcome:<slug>", authority as in step 3), with the evidence refs and the decision it triggers. A result between the lines because the sample was too small is inconclusive, not a fail; to settle it, pre-register a larger rerun. When the user requested validation, leave a scoped next action on the resulting work; retire or replace a prior nextAction only after checking the exact current work and confirming the successor, using the supported owner transition.
7. A sound test changes a decision, tests the risky assumption, measures behaviour against lines set and held beforehand, has enough sample to tell, and stops on time.

## Acceptance

- [ ] a pre-registered hypothesis item
- [ ] an outcome decision that supersedes it, citing evidence

## Owner checks

- hypothesis registered before work
- one behavioural metric with pass and fail lines
- outcome judged only against the registered lines

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the claim holder records the outcome decision; the decision it triggers is handed on
