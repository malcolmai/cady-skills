---
name: "cady-company-decision-questions"
description: "Key questions and research. Use when: A goal or decision you own needs evidence: frame its key questions and pick the cheapest research route. Not for: Dashboards, reports or data no decision needs; company goals and strategy (use `cady-company-executive-review`); deciding the answer for another owner."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision_questions"
  version: "858e41094cc14b6eb852"
  library: "1ed15292f0f09aa6"
  function: "company"
---
# Key questions and research

**Point:** Ask only questions whose answers would change a decision, and settle each by the cheapest sufficient evidence.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Start from the decision: name the answer that would reverse it and when it is needed, and drop any question no decision depends on. Instead of: Research the topic broadly, then see which decisions the findings inform.
- Take the cheapest route that could settle it: evidence the company holds, then a feed from work already happening, then desk research, then primary research. Instead of: Commission new research (a survey, interviews, a broad search) first, since fresh data feels more rigorous.
- Fit the method to the question: interviews about past behaviour for why, a pre-registered behavioural test for whether they will act, a sample for how many. Instead of: Ask customers what they want or whether they would buy.
- Answer with observed, reported and inferred evidence separated, a confidence, the strongest counter-evidence and what would change it; a partial answer stays open. Instead of: Present the findings as a conclusion.

A goal or decision you own needs evidence: frame its key questions and pick the cheapest research route.

**Not for:** Dashboards, reports or data no decision needs; company goals and strategy (use `cady-company-executive-review`); deciding the answer for another owner.

**Unit of work:** one key question and the decision it serves. **Kind:** strategy. **Parallel:** yes. 

## Inputs

### Evidence refs

- the goal or decision item the question serves
- existing evidence refs (Files, CRM interactions, decisions)

## Procedure

1. Ownership. The Executive owns strategy: which goals and decisions matter. You own your function's decisions, including whether their evidence is fresh enough. This skill is method only; it decides nothing.
2. Start from the decision, not the data. Name the few questions whose answers would change a goal or decision you own: what must be true, what would reverse it, and by when you need to know. Drop a question no decision depends on. Look up existing ones first with work_read (a task whose headline is the question) and continue them; never record one twice.
3. Record each question as a task (work_write {kind: task, goal: the goal it serves, headline: the question, next, due: when the decision needs the answer, brief: {why: the decision or goal it serves (company:work:<id>), your current belief and confidence, and which answer would change the decision}}). Keep it short and cite a File for detail. An experiment (`cady-company-experiment` tests one answer to a question) is a task of its own that cites the question it tests. These are work records, not tree items: only an assumption whose answer would change where resources go becomes a hypothesis bet on the tree (accept if A, reject if B, after doing C; `cady-company-decision-check` step 6), and its outcome settles it (supported: validated, citing the reading; refuted: replaced). Keep missing owner facts in asks (asks_write) and research questions in tasks, not company-context unknowns.
4. Take the cheapest route that could settle it: evidence the company already holds (decisions, Files, CRM interactions, the company's analytics or finance tools through this host), then a feed from work already happening, then desk research, then primary research. Fit the route to the question: why people buy, stay, leave or switch needs interviews about what they actually did, not opinions; whether they will act needs a behavioural test (waitlist, fake door, landing or pricing page) pre-registered with `cady-company-experiment`; how many or how much needs data or a sample big enough to tell; what the alternatives offer follows competitor_intelligence in `cady-company-review`. With little traffic, prefer interviews and behavioural tests to A/B tests the sample cannot settle.
5. Feeds stay with their owners. To have another agent capture something (for example the loss reason and the alternative chosen when a deal closes), ask the orchestrator to change that agent; never edit another agent yourself. Cite facts where they live; never copy them.
6. Primary research is an outside effect: interview requests go through outreach checks; pages, ads and spend need their existing authority, with a ready packet at that boundary. Be honest about who you are, ask consent before recording, and never seek a rival's confidential information, including from its customers or former staff. Keep notes as dated, attributed Files.
7. Staff it to its size. One-off synthesis or research: spin up a subagent with fresh context and a self-contained prompt (question, decision, sources, bar, stop conditions, what to return; tiers from the models registry), and check its findings against the sources before relying on them. Evidence that must stay fresh (win/loss on each closed deal, a rival's pricing against a reversal trigger): ask the orchestrator to add it to your own responsibility's duty order and cadence. Many questions or continuous collection: ask the orchestrator for a dedicated agent whose responsibility is those questions; you keep the decisions.
8. Answer for the decision. Separate observed, reported and inferred evidence; state confidence, the strongest counter-evidence and what would change the answer. Record a settled answer in the task's result (work_write {id, status: done, result, evidenceRefs}), and say what it means: confirm the decision or change it. A partial answer keeps the task open (status open, result what is known, next the step that remains, a new due). If it bears on a decision someone else owns, hand it to that owner; strategy or goal implications go to the Executive.
9. Refresh only for a reason: reviewBy, a reversal trigger or a new decision. Retire questions and sources that never change a decision. Good work: every question traces to a decision, is answered before it is needed, uses the cheapest sufficient evidence and states its confidence.

## Acceptance

- [ ] a question item tied to a decision or goal
- [ ] a result that answers it, citing evidence

## Owner checks

- each question names the decision it serves and when the answer is needed
- the route is the cheapest that could settle it
- feeds and outside effects go through their owners
- the answer cites evidence and states confidence

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the decision owner acts on the answer; strategy implications go to the Executive
