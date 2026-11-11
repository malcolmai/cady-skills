---
name: "cady-engineering-independent-review"
description: "Independent review. Independently review a diff or artifact: rerun its checks, rank findings and return land, fix or redesign. Use when: a change needs review before merge. Not for: root-causing a bug, triaging a bug report or running helpers (cady-core-execution)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.independent_review"
  version: "afa77cdc86fdcc786ad4"
  library: "d31a1ceb5b37afff"
  function: "engineering"
---
# Independent review

**Point:** A reviewer who did not produce the work checks the actual diff and evidence, so approval means it holds.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

Independently review a diff or artifact: rerun its checks, rank findings and return land, fix or redesign. Use when: a change needs review before merge. Not for: root-causing a bug, triaging a bug report or running helpers (cady-core-execution).

## Bets

- Report only what answers two questions of the change: is there a simpler yet effective way, and is it a real defect or an uncovered gap (not trivial or already covered). Instead of: A broad audit that reports every observation with equal weight.
- Step back to the relevant point(s) and how the change fits them before reviewing the diff. Instead of: Review the diff alone against its own acceptance.
- Start from the brief, acceptance and actual diff at named SHAs; read the producer's reasoning only after your own findings are written. Instead of: Read the producer's summary first and verify its claims.
- Treat unverified evidence as unrun, and rerun affected checks at the reviewed head on a clean tree. Instead of: Accept the producer's report that the tests pass.
- Rank by consequence and look for authority, isolation and data-loss holes before style. Instead of: Comment on everything visible in the diff, style included, with equal weight.
- Read beyond the changed lines to find and to prove or refute findings: callers, other writers of the same data, and missing tests, migrations or entry points. Instead of: Review only the lines in the diff.

## Independent review

### Change classes

- **Authority and security:** Identity and tenant come from the verified credential, never from input; every query, list, count, export and cache key is scoped; access is denied by default and fails closed on error; inputs are validated at the boundary; secrets and personal data stay out of logs and errors; external effects are idempotent or reconciled. Evidence: negative tests (another tenant, a missing permission, an expired or forged token) that fail without the change, and a read of every new entry point.
- **Data and migrations:** Shipped migrations are never edited; a change expands first and runs under both the old and the new code; drops and renames come later as their own contract step; backfills are bounded, resumable and idempotent; new query paths have indexes; long-running statements and full-table rewrites are avoided. Evidence: the migration applied to a copy from empty and from the last released state, with the resulting schema read back, and a stated rollback.
- **Every change:** Edge cases (empty, null, duplicate, very large, concurrent, retried), error paths, a parallel path that duplicates an existing owner (search the same nouns and verbs), dead code and stale docs.
- **Tests:** Tests assert the contract, not the implementation, without sleeps, order dependence or live provider calls; a deleted, skipped or loosened test carries its reason. For a regression or guard claim, show the relevant test fails without the fix in a scratch copy or separate worktree, never the reviewed tree. Report check results and the evidence for the claim.
- **Ui:** Loading, empty, error, denied and long-content states; keyboard operation, labels and focus; representative viewports; copy that says what happened and what to do next. Evidence: rendered captures of the changed states at representative viewports; code reading alone cannot prove a UI change. Accessibility depth follows `cady-design-wcag-audit`.
- **Checks:** Inspect prior review and check evidence for the claims it covers. Reuse a check only when its relevant content, baseline/head relationship, selection, toolchain and environment remain valid; a producer assertion alone is not proof. Serious findings, conflicts, or stale, missing or doubtful evidence invalidate affected conclusions: investigate and rerun the affected checks at the reviewed head on a clean tree. Report commands, revisions and results; unverified evidence is unrun, not passed. Actual effect authority and live environment checks stay fresh. Read beyond changed lines to find and to prove or refute findings: callers, other writers of the same data and missing tests, migrations, docs or entry points. When a software brief names owner × quality cells, use them as lenses with `../../references/quality-classes.md`; otherwise use the change classes below. Those classes remain the evidence floor.
- **Findings:** Report only findings that are a real defect, an uncovered gap, or a simpler way that works as well; leave out what is trivial or already covered. Rank by consequence: a blocker (wrong behaviour; a security, isolation or authority defect; data-loss risk; a claimed check that does not hold) is fixed before merge; a should-fix lands only with the owner's acceptance and a tracked item. Give each in one or two lines: file:line, the failure, a fix, and whether it is verified or suspected. No findings is a valid approval when the evidence supports it.
- **Independence:** Before reviewing, step back to the relevant point(s) (the map page's, the method's, the goal's) and how this change fits them; a minor map change (wording, a status, a row) needs no explicit review, a larger one or a plan does. Refuse a review of work you produced or watched being produced, and say so; the requester finds another reviewer. Start from the brief, acceptance and actual diff at named baseline and head SHAs, not the producer’s summary or verdict; read the producer’s reasoning only after your own findings are written. Review may build on sound independent coverage of an integrated baseline: inspect the new delta and affected dependencies and seams, so the named integrated head is covered without restarting unchanged review.
- **Levels:** Review at two levels. First why: does the work serve the purpose one level up? Ask why until you reach a recorded goal, direction or decision, and list each assumption with its evidence or mark it unsupported. A why that is missing goes back to the requester as a question. A why that evidence contradicts is a blocker even when the details are sound. A why that conflicts with an owner's recorded decision goes to that owner; you do not reverse it. Then review the details. An obviously purposeful small fix needs one line on why.
- **Two reviews:** A larger method or agent-behaviour text change gets two reviews by two separate agents, neither the producer. Logic review reads the method's logic and the served text: does every served line follow from the logic, and does the flow hold end to end, nearby case included? Writing review reads the served text alone (record reads: served): does it tell an agent what to do, with nothing repeated, missing or contradicted? A small text fix gets only the writing review; a code change gets one review.
- **Verdict:** End with land, fix (the blockers to clear) or redesign (why the approach is wrong and the alternative). Write ranked findings and a receipt (producer, reviewer, baseline and head SHAs, prior coverage reused, checks and results, verdict) to the file the requester names; the producer never edits it. At most two rounds per lane; review later fixes and affected seams as the integrated state changes.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.
