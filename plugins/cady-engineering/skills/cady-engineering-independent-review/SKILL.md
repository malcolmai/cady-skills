---
name: "cady-engineering-independent-review"
description: "Independent review. Independently review a diff or artifact: rerun its checks, rank findings and return land, fix or redesign. Use when: a change needs review before merge. Not for: root-causing a bug, triaging a bug report or running helpers (cady-core-execution)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.independent_review"
  version: "e7019b6629da742883d7"
  library: "d0d7a4ecb1120309"
  function: "engineering"
---
# Independent review

**Company context:** `get_cady_context({"area": "product/<productId>/engineering", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.independent_review": "e7019b6629da742883d7@d0d7a4ecb1120309"}})`

Independently review a diff or artifact: rerun its checks, rank findings and return land, fix or redesign. Use when: a change needs review before merge. Not for: root-causing a bug, triaging a bug report or running helpers (cady-core-execution).

## Independent review

### Change classes

- **Authority and security:** Identity and tenant come from the verified credential, never from input; every query, list, count, export and cache key is scoped; access is denied by default and fails closed on error; inputs are validated at the boundary; secrets and personal data stay out of logs and errors; external effects are idempotent or reconciled. Evidence: negative tests (another tenant, a missing permission, an expired or forged token) that fail without the change, and a read of every new entry point.
- **Data and migrations:** Shipped migrations are never edited; a change expands first and runs under both the old and the new code; drops and renames come later as their own contract step; backfills are bounded, resumable and idempotent; new query paths have indexes; long-running statements and full-table rewrites are avoided. Evidence: the migration applied to a copy from empty and from the last released state, with the resulting schema read back, and a stated rollback.
- **Every change:** Edge cases (empty, null, duplicate, very large, concurrent, retried), error paths, a parallel path that duplicates an existing owner (search the same nouns and verbs), dead code and stale docs.
- **Tests:** Each new test fails without the change (in a scratch copy or a separate worktree at the base SHA, never the reviewed tree, revert the fix and watch it fail); it asserts the contract, not the implementation; it has no sleeps, order dependence or live provider calls; a deleted, skipped or loosened test carries its reason. Evidence: your rerun counts and, for a bug fix, the regression test failing on the base.
- **Ui:** Loading, empty, error, denied and long-content states; keyboard operation, labels and focus; representative viewports; copy that says what happened and what to do next. Evidence: rendered captures of the changed states at representative viewports; code reading alone cannot prove a UI change. Accessibility depth follows `cady-design-wcag-audit`.
- **Checks:** Rerun the checks the producer names, and any you doubt, at the reviewed head on a clean tree, and report your own command and counts. A result from another SHA, a dirty tree or a relayed message is unrun, not passed. Read beyond the changed lines: callers of changed functions, the other writers of the same data, and what is missing (a test, a migration, a doc, a second entry point).
- **Findings:** Rank by consequence. Blocker: wrong behaviour, a security, isolation or authority defect, data-loss risk, or a claimed check that does not hold; it must be fixed before merge. Should fix: a real defect or maintenance cost; it lands only with the owner's acceptance and a tracked item. Nit: optional and labelled as such. Each finding gives file:line, what is wrong, the failure it causes and a suggested fix, and says whether it is verified or suspected. Name real strengths briefly; an approval with no findings is valid when the evidence supports it.
- **Gotchas:** Approving from the summary; nitpicking style while missing an authority hole; reviewing only the diff and not its callers; treating 'tests pass' as proof the tests test anything; one reviewer reviewing their own fix.
- **Independence:** Refuse a review of work you produced or watched being produced, and say so; the requester finds another reviewer. Start from the brief, acceptance and the exact diff at named base and head SHAs (git diff <base>...<head>), not the producer's summary or verdict; read the producer's reasoning only after your own findings are written.
- **Verdict:** End with land, fix (the blockers to clear) or redesign (why the approach is wrong and the alternative). Write the ranked findings and a receipt (producer, reviewer, base and head SHA, checks rerun with results, verdict) to the file the requester names; the producer never edits it. At most two rounds: the second checks only the fixes and what they touch, and later fixes go to the next combined review.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.
