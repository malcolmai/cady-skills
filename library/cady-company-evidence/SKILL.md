---
name: "cady-company-evidence"
description: "Key questions and behaviour tests. Use when: A decision you own needs evidence: frame its questions, take the cheapest route, pre-register any test of behaviour. Not for: Dashboards, reports or data no decision needs; company goals and strategy (`cady-company-weekly-review`); deciding the answer for another owner; routine delivery whose desired behaviour is clear (`cady-engineering-method`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.evidence"
  version: "e819a8ce01f76d86ccc8"
  library: "f5e8b22b566aee82"
  function: "company"
---
# Key questions and behaviour tests

**Point:** Ask only what would change a decision and settle it by the cheapest sufficient evidence, pre-registering any test of behaviour.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Start from the decision: name the answer that would reverse it and when it is needed, and drop any question no decision depends on. Instead of: Research the topic broadly, then see which decisions the findings inform.
- Take the cheapest route that could settle it: evidence the company holds, then a feed from work already happening, then desk research, then primary research. Instead of: Commission new research (a survey, interviews, a broad search) first, since fresh data feels more rigorous.
- Fit the method to the question: interviews about past behaviour for why, a pre-registered behavioural test for whether they will act, a sample for how many. Instead of: Ask customers what they want or whether they would buy.
- For a behaviour test, fix the metric, the pass and fail lines and the decision each triggers before any work, and measure what people do, not what they say. Instead of: Run the test, look at the data, then interpret it, or count interview enthusiasm, survey intent or likes as demand.

A decision you own needs evidence: frame its questions, take the cheapest route, pre-register any test of behaviour.

**Not for:** Dashboards, reports or data no decision needs; company goals and strategy (`cady-company-weekly-review`); deciding the answer for another owner; routine delivery whose desired behaviour is clear (`cady-engineering-method`).

**Unit of work:** one key question and the decision it serves. **Kind:** strategy. **Parallel:** yes. 

## Inputs

### Evidence refs

- the goal or decision item the question serves
- existing evidence refs (Files, CRM interactions, decisions)
- the assumption task and the Files and CRM records a test produces

## Procedure

1. Start from the decision, not the data (the Executive owns strategy, you your function's decisions, and this skill decides nothing). Name the few questions whose answers would change a goal or decision you own: what must be true, what would reverse it, and by when you need to know. Drop a question no decision depends on. Look up existing ones first with cady_read and continue them; never record one twice.
2. Record each question as a task (work_set {kind: task, goal, headline: the question, next, due: when the decision needs the answer, brief: {why: the decision or goal it serves, your current belief and confidence, and which answer would change the decision}}), with a File for detail. These are work records, not tree items: only an assumption whose answer would change where resources go becomes a bet with its measure, what would confirm or reject it (decisions_set). Owner-only facts go in asks (todos_set).
3. Take the cheapest route that could settle it: evidence the company already holds, then a feed from work already happening, then desk research, then primary research. Fit the route to the question: why people buy or leave needs interviews about what they did, not opinions; whether they will act needs a behaviour test (step 6); how many needs a sample big enough to tell; what the alternatives offer follows `cady-product-research`. With little traffic, prefer interviews and behaviour tests to A/B tests the sample cannot settle.
4. Feeds stay with their owners: to have another agent capture something, ask for that agent to be changed (`cady-company-manage-agents`). Primary research is an outside effect: interview requests go through outreach checks, and pages, ads and spend need their existing authority, with a ready packet at that boundary. Be honest about who you are, ask consent before recording, and never seek a rival's confidential information.
5. Staff it to its size: a one-off synthesis goes to a fresh-context subagent with a self-contained prompt, its findings checked against the sources; evidence that must stay fresh, or many questions, become a duty on your responsibility or a dedicated agent (`cady-company-manage-agents`). You keep the decisions.
6. Behaviour test, when the question is whether people will act. Test first the assumption that would most change the plan if wrong and that you are least sure of (look it up in the bets on your node and above (your cady_start read) and your tasks; never register it twice). Pre-register before any work (`references/behaviour-test.md`). Run the smallest test that could change the decision, varying one thing: for demand, conversations, then a manual or concierge test, then a build (a measured build only for a feasibility crux). Stop early on a stop condition; judge only against the registered lines; a result between them on too small a sample is inconclusive, so pre-register a larger rerun. Before concluding no demand, separate the causes (for outreach: offer, persona, message, format, channel, timing, deliverability).
7. Answer for the decision: separate observed, reported and inferred evidence; state confidence, the strongest counter-evidence and what would change the answer. Record it in the task's result (work_set {id, status: done, result, evidenceRefs}) and say whether it confirms or changes the decision; a test's outcome names the decision it triggers, and the bet it tests is validated or replaced with decisions_set. A partial answer keeps the task open with what is known and the next step. Hand an answer that bears on another owner's decision to that owner, strategy implications to the Executive, and retire questions that never change a decision.

## Acceptance

- [ ] (check) a question task tied to a decision or goal, naming when the answer is needed
- [ ] (check) a behaviour test is registered before any work: one behavioural metric, pass and fail lines and the decision each triggers
- [ ] (fresh) the result answers it, citing evidence with its type and confidence, and judges a test only against its registered lines

## Owner checks

- each question names the decision it serves and when the answer is needed
- a test's assumption was registered before work and judged only against the registered lines

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the decision owner acts on the answer; strategy implications go to the Executive

## References
- Read [Behaviour test](references/behaviour-test.md) when the question is whether people will act and you register a behaviour test.
