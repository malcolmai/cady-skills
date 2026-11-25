---
name: "cady-engineering-fix"
description: "Fix a bug or failing check. Use when: Find and fix the root cause of a bug, failing check or incident, from report to verified close. Not for: Reviewing someone's diff (`cady-engineering-independent-review`) or building a planned task (the engineering card)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.engineering.fix"
  version: "5dc5a55274cc498c7a85"
  library: "47de76558e13273c"
  function: "engineering"
---
# Fix a bug or failing check

**Point:** Find the real cause from evidence and fix it where it lives, so every place sharing that cause stays fixed.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

Find and fix the root cause of a bug, failing check or incident, from report to verified close.

**Not for:** Reviewing someone's diff (`cady-engineering-independent-review`) or building a planned task (the engineering card).

**Unit of work:** one failure, from first signal to verified fix. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the report, failing check or alert
- the exact error, logs and failing build

## Procedure

1. Search open tasks for the same failure (`cady_read`); add your evidence to a duplicate.
2. Read the full error and the first failure in the log, then list what changed since it last worked.
3. Reproduce on the exact build at the lowest layer that shows it; confirm the code you think is running is running.
4. Rate by user impact, higher when silent, irreversible or widespread. If users are affected now, mitigate first by turning the change off or back, not by patching around it.
5. Write one candidate cause and the observation that would disprove it. After three misses, re-read the error.
6. Write the test that fails first, fix the cause where it lives, and fix or list every other place with the same cause. That list is the fix's risks to watch, in place of a plan review; the change review checks the cause and the list. If the fix needs a design change, stop: it becomes a task with a plan (the engineering card).
7. Close by rerunning the original steps on the fixed build; put the root cause and evidence in the result (`work_set`).

## Acceptance

- [ ] (check) a test failed before the fix and passes after, the original reproduction no longer fails, and every place sharing the cause is fixed or listed; a fix that needed a design change became a task with a plan

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the task closes with the root cause and the rerun as evidence
