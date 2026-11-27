---
name: "cady-company-taste-review"
description: "Writing craft and taste decisions. Use when: Write or edit a post, article, web copy or other public text, or review a design (judge with the taste check). Not for: Pass/fail checks a script or test can decide (run those first), a direct message to one person, or writing a prompt or skill and changing how agents behave (`cady-company-change-agent-behaviour`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.taste_review"
  version: "a97e139d9fe4fc999705"
  library: "7bf126ff6bc82cee"
  function: "company"
---
# Writing craft and taste decisions

**Point:** Judge writing and design by whether the intended reader acts as hoped, learning the owner's taste from corrections.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Start from the reader, what they must do or decide, and the one trade-off, before writing a word. Instead of: Start from the content to cover, then polish the prose.
- Your own sense of how it lands is not a verdict: judge why first, then details, against the taste components. Instead of: Reread your own draft and call it good when it reads well to you.
- Promote an owner correction to a general preference only after two or three consistent judgements, and never record a universal ban. Instead of: Turn each correction into a standing rule at once.

Write or edit a post, article, web copy or other public text, or review a design (judge with the taste check).

**Not for:** Pass/fail checks a script or test can decide (run those first), a direct message to one person, or writing a prompt or skill and changing how agents behave (`cady-company-change-agent-behaviour`).

**Unit of work:** one artifact and its decision. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the artifact or draft
- the bets on the node the work serves and its parents (the owner's preferences)
- the owner's corrections

## Procedure

1. Start from the reader and purpose: who gets the work, what it must get them to do or decide, the one trade-off. Read the owner's preferences first: the bets on the node the work serves and its parents, which cady_start serves.
2. Writing public text (a LinkedIn, X or blog post, article, script, caption or website copy): create, edit or review it with the written-content craft (its written-content reference).
3. Judge what you wrote at two levels, the details with `references/taste-post.md` for public text and the ui or visual part of `references/taste-check.md` for a design. Review at two levels. First why: does the work serve the purpose one level up? Ask why until you reach a recorded goal, bet or decision, and list each assumption with its evidence or mark it unsupported. A why that is missing goes back to the requester as a question. A why that evidence contradicts is a blocker even when the details are sound. A why that conflicts with an owner's recorded decision goes to that owner; you do not reverse it. Then review the details. An obviously purposeful small fix needs one line on why. Your own sense of how it lands is not a verdict.
4. Learn from feedback: an owner correction becomes a bet on the node it governs, the root when it is company-wide (decisions_set {path, bet: {chosen: the preference, insteadOf: what it rules out, why: a short trigger, reason, trade-off, exception and confidence}}); a bet replacing one names it in replaces. A one-off stays low confidence and scoped to its work; promote it to a general preference only after two or three consistent judgments; never record a universal ban; replace rather than overwrite. Replace a wrong preference bet in one call, the owner's included; optionally add your justification as its why: the real alternatives (A, B, neither or equal) and one line on each, in the same why field a correction-bet holds its trigger.

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
- node:<path> (the preference bet)
- **Transition:** the draft is handed on with what was and was not judged; a preference becomes a bet on its node

## References
- Read [Taste check](references/taste-check.md) when judging a draft or design before review.
- Read [Taste check: message](references/taste-message.md) when judging a message draft before review.
- Read [Taste check: post](references/taste-post.md) when judging a post draft before review.
- [Text content craft](references/written-content.md)
