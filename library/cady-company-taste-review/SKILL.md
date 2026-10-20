---
name: "cady-company-taste-review"
description: "Taste review. Use when: Judging or choosing between artifacts, agent designs or prompt changes where quality depends on judgment. Not for: Pass/fail checks a script or test can decide; run those first."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.taste_review"
  version: "f346045709137d20e5ceca656a7f54045e3cee07780985216072cf21bf3ebab9"
  library: "3beca7fa80e90672"
  function: "company"
---
# Taste review

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.taste_review": "f346045709137d20e5ceca656a7f54045e3cee07780985216072cf21bf3ebab9"}})`

Judging or choosing between artifacts, agent designs or prompt changes where quality depends on judgment.

**Not for:** Pass/fail checks a script or test can decide; run those first.

**Unit of work:** one artifact, agent design or change, and its decision. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Always

- Start from the reader: who gets the work, what it must get them to do, and 2-4 yes/no tests a reader without context can answer.
- Write failures with why, not positive examples; agents copy examples. A number or adjective is a bar only if it names the reader's failure.
- Have a second reader judge cold first: only the work and a one-line reader, before any taste decisions or your reasoning.

## Inputs

### Evidence refs

- the artifact, design or change under review
- current taste decisions (subjectPrefix taste:)
- the owner's corrections

## Procedure

1. An agent's taste is what it notices, what it chooses and what it leaves out. Give it, in order: the reader and purpose (who gets the work, what it must get them to do or decide, the one trade-off); the bar (step 2); failures with why (step 3); the owner's taste decisions, read before judging with get_company_work decisions {state: "current", subjectPrefix: "taste:"}; a second reader (step 6).
2. The bar is 2-4 reader tests a reader without context can answer yes or no, reworded for that agent's reader. For anything a person reads, start from: Can they tell it's AI? Is it theirs, yet better or different from what they get today? Do they get it at a glance? A number or adjective is a bar only if you can name the reader's failure it prevents. Every rule names the work it is for.
3. Give failures with why, and no positive examples: agents copy them. Three recur. (1) An arbitrary bar stands in for the real one ("cold email 50-100 words"; "what a competent professional would hand over"). (2) Polish stands in for the job (asked to start outreach, it returned five researched people; a post passed legibility and palette checks with an unsurprising idea). (3) Written from the maker's side ("In today's rapidly evolving business environment..."; outreach explaining what AI can do for the reader). Record a new failure as a taste: decision (step 7) only when the owner raises the bar on a strong attempt and it is not one of these.
4. Writing a prompt or skill (Ogilvy, adapted): study one reference closely (prompts and skills only; work for many readers, like outreach, has no template and starts from its reader). Write as you would tell a capable colleague: short lines, the company's words, no internal codes. More than a short page means the outcome is not clear. Quote the owner's limits verbatim. State the outcome, finish line and first action. Leave out adjectives, ban lists (the agent moves to the next default), checks a tool can run and lines that repeat served methods. A must belongs in a tool guard; prose carries judgment. Have it reread cold before adopting.
5. Judging: inspect in the medium of consumption (a page at real sizes, an email as its recipient sees it, a prompt as the agent receives it served); if you cannot, write "not inspected in medium" and claim no quality. Answer the reader tests in the reader's words. Review direction, then structure, then detail, in at most two rounds. Between real alternatives say "A over B for this purpose because ..., giving up ..."; neither and equal are valid.
6. Changing an agent: write the expected behaviour difference first, then judge it on comparable runs (critical agent: 3-5 held-out real tasks) by one reviewer under the review rule (`cady-engineering-independent-review`). Keep the change only if it wins or fixes the named failure. Runs are prepare-only. Adoption goes through `cady-company-manage-agents` steps 7-8.
7. Learn from feedback: turn an owner correction into a decision (submit_company_work_checkpoint decision {kind: "decision", subject: "taste:<medium>-<key>", rationale, chosen, alternatives, quote, source, authority, decidedBy, supersedes}). The kind has no taste fields, so put a short trigger, reason, evidence refs, trade-off, exception and confidence in rationale; chosen is the preference, quote the owner's exact words (source chat, authority member, decidedBy their id or "me"); for your own judgment use authority agent and omit decidedBy. A one-off stays low confidence and scoped to its work; promote it to a general preference only after two or three consistent judgments; never record a universal ban; supersede rather than overwrite. Never supersede an owner's taste decision on your own authority; record the conflict and ask once (step 8).
8. When a preference is unclear and the choice matters, ask once with two real alternatives (A, B, neither or equal, and one line why) rather than asking for a philosophy.

## Acceptance

- [ ] reader, purpose and the one trade-off named
- [ ] reader tests answered in the reader's words, inspected in medium or stated not
- [ ] a second reader judged cold before seeing taste decisions or the producer's reasoning
- [ ] preferences recorded with evidence and confidence
- [ ] a change judged on comparable runs

## Owner checks

- current taste decisions read before judging
- owner quote for any owner preference recorded

## Result

### Artifact refs

- company:work:<workId>
- decision:taste:<medium>-<key>
- **Transition:** the judgment is recorded on the item under review; a preference becomes a taste decision
