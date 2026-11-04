---
name: "cady-company-experiment"
description: "Pre-registered experiment. Use when: Test the riskiest assumption with a pre-registered experiment and a decision rule set before any work starts. Not for: Routine delivery whose desired behavior is clear, or reliability fixes with acceptance; use `cady-engineering-method` for implementation."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.experiment"
  version: "23f1d5d7f92cb796dab8"
  library: "4f2bb2a29c877c2e"
  function: "company"
---
# Pre-registered experiment

**Point:** Test the riskiest assumption against pass and fail lines set beforehand, so the result changes a decision, not a story.

**Company context:** `context_read({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.experiment": "23f1d5d7f92cb796dab8@4f2bb2a29c877c2e"}})`

**Bets** (where this differs from the default):
- Test first the assumption that would most change the plan if wrong and that you are least sure of. Instead of: Test what is easiest to measure, or what the team is already building.
- Fix the metric, the pass and fail lines and the decision each triggers before any work starts. Instead of: Run the test, look at the data, then interpret what it means.
- Measure what people do (sign up, pay, return, reply), not what they say. Instead of: Count interview enthusiasm, survey intent or likes as demand.
- A result between the lines on too small a sample is inconclusive, not a fail; settle it with a pre-registered larger rerun. Instead of: Call it a fail and move on, or re-cut the data until it passes.
- For demand, run conversations, then a manual or concierge test, then a build; a measured build is the smallest test only for a feasibility crux. Instead of: Build an MVP to find out whether people want it.

Test the riskiest assumption with a pre-registered experiment and a decision rule set before any work starts.

**Not for:** Routine delivery whose desired behavior is clear, or reliability fixes with acceptance; use `cady-engineering-method` for implementation.

**Unit of work:** one hypothesis and the decision that settles it. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- the hypothesis decision item
- the Files and CRM records the test produces

## Procedure

1. Pick the riskiest assumption: the one that would most change the plan if wrong and that you are least sure of. Test it before easier ones.
2. Look it up first: work_read decisions {state: "current", subject: "hypothesis:<function>.<slug>"} (a persona's hypothesis is hypothesis:persona.<personaKey>). If a current hypothesis exists, continue it; never register it twice.
3. Pre-register before any work, recorded as `cady-company-decision-questions` step 3 records (subject convention there), as a hypothesis decision item (work_write or decisions_write or asks_write, status OPEN, decision {kind: "hypothesis", subject: "hypothesis:<function>.<slug>", rationale, authority "agent" and no decidedBy: Cady records it as your agent}): the hypothesis; one behavioural metric (what people do, not what they say); a pass line and a fail line; the decision taken on each outcome; sample size and time box; stop conditions; a sourced cost ceiling or explicit unknown; zero incremental external cost is the evaluation fallback without a selected budget, while any paid effect requires checked current authority. Put the full design in a File the item cites. Cite the question:<slug> it tests, when there is one.
4. Design the smallest test that could change the decision, varying one main thing: for demand and usability assumptions, conversations first, then a manual or concierge test, then a build; for a quality or feasibility crux, the smallest test is a measured build. Prepare everything yourself; come to the person only at a boundary (a call, filming, spend outside verified authority, a send, a signature, access) with a ready packet.
5. Run it as Projects work citing company:work:<hypothesisId>. Stop early when a stop condition is met. If the instrument or environment changes during the run, take a new baseline before comparing.
6. Judge it only against the pre-registered lines. Record the outcome as a decision (status COMPLETE) that supersedes the hypothesis (subject "hypothesis.outcome:<function>.<slug>", authority as in step 3), with the evidence refs and the decision it triggers. A result between the lines because the sample was too small is inconclusive, not a fail; to settle it, pre-register a larger rerun. When the user requested validation, leave a scoped next action on the resulting work; retire or replace a prior nextAction only after checking the exact current work and confirming the successor, using the supported owner transition.
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
