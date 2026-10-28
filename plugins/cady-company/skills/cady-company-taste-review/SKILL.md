---
name: "cady-company-taste-review"
description: "Writing craft and taste decisions. Use when: Write or edit a post, article, web copy, prompt or skill, or review a design (judge with the taste check). Not for: Pass/fail checks a script or test can decide (run those first), a direct message to one person, or changing how agents behave (`cady-company-change-agent-behaviour`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.taste_review"
  version: "7e8d2fb1ec6009f0aeca"
  library: "f2ab4ebd3a461f29"
  function: "company"
---
# Writing craft and taste decisions

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.taste_review": "7e8d2fb1ec6009f0aeca@f2ab4ebd3a461f29"}})`

Write or edit a post, article, web copy, prompt or skill, or review a design (judge with the taste check).

**Not for:** Pass/fail checks a script or test can decide (run those first), a direct message to one person, or changing how agents behave (`cady-company-change-agent-behaviour`).

**Unit of work:** one artifact and its decision. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Always

- Start from the reader: who gets the work and what it must get them to do or decide.
- Judge your own draft with the taste check, not by rereading it; say what was not judged.

## Inputs

### Evidence refs

- the artifact or draft
- current taste decisions (subjectPrefix taste:)
- the owner's corrections

## Procedure

1. Start from the reader and purpose: who gets the work, what it must get them to do or decide, the one trade-off. Read the owner's taste decisions first: get_company_work decisions {state: "current", subjectPrefix: "taste:"}.
2. Writing public text (a LinkedIn, X or blog post, article, script, caption or website copy): create, edit or review it with the written-content craft (its written-content reference).
3. Writing a prompt or skill: reuse what already works. For substantive changes, read [Drafting useful prompts and skills](../../references/agent-skill-drafting.md); skip the procedure for obvious corrections. Write for a capable colleague: outcome, constraints, useful judgment and observable finish line. Keep the core self-contained; move conditional detail into references. Length alone is not a quality verdict. Preserve the owner's limits and existing authority; leave out duplicated instructions and checks a tool already enforces. Place and prove a change to agent behaviour with `cady-company-change-agent-behaviour`.
4. Judge what you wrote with the taste check (`../../references/taste-check.md`): the post part for public text, the ui or visual part for a design. Your own sense of how it lands is not a verdict.
5. Learn from feedback: an owner correction becomes a decision (submit_company_work_checkpoint decision {kind: "decision", subject: "taste:<medium>-<key>", rationale, chosen, alternatives, quote, source, authority, decidedBy, supersedes}). Put a short trigger, reason, trade-off, exception and confidence in rationale; chosen is the preference, quote the owner's exact words (source chat, authority member, decidedBy their id or "me"); for your own judgment use authority agent and omit decidedBy. A one-off stays low confidence and scoped to its work; promote it to a general preference only after two or three consistent judgments; never record a universal ban; supersede rather than overwrite. Never supersede an owner's taste decision on your own authority: record the conflict and ask once with two real alternatives (A, B, neither or equal, and one line why).

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
- Read [Drafting useful prompts and skills](../../references/agent-skill-drafting.md) when writing or editing a prompt or skill.
- Read [Taste check](../../references/taste-check.md) when judging a draft or design before review.
- [Text content craft](references/written-content.md)
