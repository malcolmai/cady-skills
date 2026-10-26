---
name: "cady-company-decision-questions"
description: "Key questions and research. Use when: A goal or decision you own needs evidence: frame its key questions and pick the cheapest research route. Not for: Dashboards, reports or data no decision needs; company goals and strategy (use `cady-company-executive-review`); deciding the answer for another owner."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision_questions"
  version: "8f5bd4934fc4463547f8"
  library: "806df94fde5b1055"
  function: "company"
---
# Key questions and research

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.decision_questions": "8f5bd4934fc4463547f8@806df94fde5b1055"}})`

A goal or decision you own needs evidence: frame its key questions and pick the cheapest research route.

**Not for:** Dashboards, reports or data no decision needs; company goals and strategy (use `cady-company-executive-review`); deciding the answer for another owner.

**Unit of work:** one key question and the decision it serves. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- the goal or decision item the question serves
- existing evidence refs (Files, CRM interactions, decisions)

## Procedure

1. Ownership. The Executive owns strategy: which goals and decisions matter. You own your function's decisions, including whether their evidence is fresh enough. This skill is method only; it decides nothing.
2. Start from the decision, not the data. Name the few questions whose answers would change a goal or decision you own: what must be true, what would reverse it, and by when you need to know. Drop a question no decision depends on. Look up existing ones first with get_company_work decisions {state: "current", subject: "question:<slug>"} and continue them; never record one twice.
3. Record each question as a hypothesis decision item (submit_company_work_checkpoint, status OPEN, decision {kind: "hypothesis", subject: "question:<slug>", rationale, reviewBy, reversal, authority "agent" and no decidedBy: Cady records it as your agent}). The rationale names the decision or goal it serves (company:work:<id>), your current belief and confidence, and which answer would change the decision; reviewBy is when the decision needs the answer. Keep it short and cite a File for detail. One subject convention for every record: an open question is question:<slug>; a hypothesis or experiment (`cady-company-experiment` tests one answer to a question) is hypothesis:<function>.<slug>, for example hypothesis:gtm.smb-pain, citing the question it tests; the settled forms are question.answer:<slug> and hypothesis.outcome:<function>.<slug>. Continue a record already held under its recorded subject.
4. Take the cheapest route that could settle it: evidence the company already holds (decisions, Files, CRM interactions, the company's analytics or finance tools through this host), then a feed from work already happening, then desk research, then primary research. Fit the route to the question: why people buy, stay, leave or switch needs interviews about what they actually did, not opinions; whether they will act needs a behavioural test (waitlist, fake door, landing or pricing page) pre-registered with `cady-company-experiment`; how many or how much needs data or a sample big enough to tell; what the alternatives offer follows competitor_intelligence in `cady-company-review`. With little traffic, prefer interviews and behavioural tests to A/B tests the sample cannot settle.
5. Feeds stay with their owners. To have another agent capture something (for example the loss reason and the alternative chosen when a deal closes), ask the orchestrator to change that agent; never edit another agent yourself. Cite facts where they live; never copy them.
6. Primary research is an outside effect: interview requests go through outreach checks; pages, ads and spend need their existing authority, with a ready packet at that boundary. Be honest about who you are, ask consent before recording, and never seek a rival's confidential information, including from its customers or former staff. Keep notes as dated, attributed Files.
7. Staff it to its size. One-off synthesis or research: spin up a subagent with fresh context and a self-contained prompt (question, decision, sources, bar, stop conditions, what to return; tiers from the models registry), and check its findings against the sources before relying on them. Evidence that must stay fresh (win/loss on each closed deal, a rival's pricing against a reversal trigger): ask the orchestrator to add it to your own responsibility's duty order and cadence. Many questions or continuous collection: ask the orchestrator for a dedicated agent whose responsibility is those questions; you keep the decisions.
8. Answer for the decision. Separate observed, reported and inferred evidence; state confidence, the strongest counter-evidence and what would change the answer. Record a settled answer as a COMPLETE decision item (kind "decision", subject "question.answer:<slug>" (needs no layer), supersedes [the question's decision id], authority "agent" and no decidedBy) with the evidence as the checkpoint's evidenceRefs, and say what it means: confirm the decision or change it. A partial answer keeps the question OPEN with what is still unknown and a new reviewBy. If it bears on a decision someone else owns, hand it to that owner; strategy or goal implications go to the Executive.
9. Refresh only for a reason: reviewBy, a reversal trigger or a new decision. Retire questions and sources that never change a decision. Good work: every question traces to a decision, is answered before it is needed, uses the cheapest sufficient evidence and states its confidence.

## Acceptance

- [ ] a question item tied to a decision or goal
- [ ] an answer decision that supersedes it, citing evidence

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
