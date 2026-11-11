---
name: "cady-company-taste-review"
description: "Writing craft and taste decisions. Use when: Write or edit a post, article, web copy, prompt or skill, or review a design (judge with the taste check). Not for: Pass/fail checks a script or test can decide (run those first), a direct message to one person, or changing how agents behave (`cady-company-change-agent-behaviour`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.taste_review"
  version: "188ef78aba13c35b374a"
  library: "f07f44f6654894c0"
  function: "company"
---
# Writing craft and taste decisions

**Point:** Judge writing and design by whether the intended reader acts as hoped, learning the owner's taste from corrections.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Start from the reader, what they must do or decide, and the one trade-off, before writing a word. Instead of: Start from the content to cover, then polish the prose.
- Your own sense of how it lands is not a verdict: judge why first, then details, against the taste components. Instead of: Reread your own draft and call it good when it reads well to you.
- Promote an owner correction to a general preference only after two or three consistent judgements, and never record a universal ban. Instead of: Turn each correction into a standing rule at once.
- Write a prompt or skill for a capable colleague: outcome, constraints, useful judgement and finish line; length is no measure of quality. Instead of: Add a rule or caveat for every failure seen, so the prompt covers every case.

Write or edit a post, article, web copy, prompt or skill, or review a design (judge with the taste check).

**Not for:** Pass/fail checks a script or test can decide (run those first), a direct message to one person, or changing how agents behave (`cady-company-change-agent-behaviour`).

**Unit of work:** one artifact and its decision. **Kind:** execution. **Parallel:** no. 

## Always

- Start from the reader: who gets the work and what it must get them to do or decide.
- Judge your own draft with the taste check, not by rereading it; say what was not judged.

## Inputs

### Evidence refs

- the artifact or draft
- current taste decisions (subjectPrefix taste:)
- the owner's corrections

## Procedure

1. Start from the reader and purpose: who gets the work, what it must get them to do or decide, the one trade-off. Read the owner's taste decisions first: cady_read {search: {query: "taste", kinds: ["decision"]}}.
2. Writing public text (a LinkedIn, X or blog post, article, script, caption or website copy): create, edit or review it with the written-content craft (its written-content reference).
3. Writing a prompt or skill: reuse what already works. Write for a capable colleague: outcome, constraints, useful judgment and observable finish line; its name and use_when say what it does, when it applies and how it differs from its neighbours. Keep the core self-contained; move conditional detail into references. Length alone is not a quality verdict. Preserve the owner's limits and existing authority; leave out duplicated instructions and checks a tool already enforces. Place and prove a change to agent behaviour with `cady-company-change-agent-behaviour`.
4. Judge what you wrote at two levels, the details with `../../references/taste-post.md` for public text and the ui or visual part of `../../references/taste-check.md` for a design. Review at two levels. First why: does the work serve the purpose one level up? Ask why until you reach a recorded goal, direction or decision, and list each assumption with its evidence or mark it unsupported. A why that is missing goes back to the requester as a question. A why that evidence contradicts is a blocker even when the details are sound. A why that conflicts with an owner's recorded decision goes to that owner; you do not reverse it. Then review the details. An obviously purposeful small fix needs one line on why. Your own sense of how it lands is not a verdict.
5. Learn from feedback: an owner correction becomes a decision (decisions_write {subject: "taste:<medium>-<key>", chosen, rationale, alternatives, quote, authority, replaces, citesWhy}). Put a short trigger, reason, trade-off, exception and confidence in rationale; chosen is the preference, quote the owner's exact words (authority manager, admin for an Admin); for your own judgment use authority agent. A one-off stays low confidence and scoped to its work; promote it to a general preference only after two or three consistent judgments; never record a universal ban; replace rather than overwrite. Never replace an owner's taste decision on your own authority: record the conflict and ask once with two real alternatives (A, B, neither or equal, and one line why).

## Acceptance

- [ ] (check) reader, purpose and the one trade-off named
- [ ] (fresh) the draft judged with the taste check, or stated not inspected in medium
- [ ] (person) preferences recorded with the owner's quote, evidence and confidence

## Owner checks

- current taste decisions read before writing
- owner quote for any owner preference recorded

## Result

### Artifact refs

- company:work:<workId>
- decision:taste:<medium>-<key>
- **Transition:** the draft is handed on with what was and was not judged; a preference becomes a taste decision

## References
- Read [Taste check](../../references/taste-check.md) when judging a draft or design before review.
- Read [Taste check: message](../../references/taste-message.md) when judging a message draft before review.
- Read [Taste check: post](../../references/taste-post.md) when judging a post draft before review.
- [Text content craft](references/written-content.md)
