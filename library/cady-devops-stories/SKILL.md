---
name: "cady-devops-stories"
description: "Stories: keep and capture. Use when: Write or edit a Story, capture its flow as screenshots for review, or file a failed step. Not for: Finding and fixing a failure's cause (`cady-engineering-fix`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.devops.stories"
  version: "a270cdd170f8c7ec9ce7"
  library: "d493e3230725f90b"
  function: "devops"
---
# Stories: keep and capture

**Point:** Keep each key user flow as a Story with screenshots, so a person can review what users actually meet.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

Write or edit a Story, capture its flow as screenshots for review, or file a failed step.

**Not for:** Finding and fixing a failure's cause (`cady-engineering-fix`).

**Unit of work:** one Story, or one capture of it. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- story:<slug> (the Story id from stories_read)
- the environment and a test account

## Procedure

1. A Story is one user goal in the user's words: who, the goal, the start, then 3 to 12 steps of do and expect. Read first (`stories_read`); edit the Story that exists.
2. Capture it fresh: an agent or person given only the Story id, the environment and a test account, acting through the real surface. A builder's own capture is a self-check; say so.
3. Record each step as pass, fail or blocked with what was seen and its screenshot, uploaded from the file (`stories_set`).
4. Finish the flow before reporting; file each failure as a task citing the Story and step, with its evidence File. The task closes only on a new fresh capture.
5. A person's note on a step is critique for the product manager; leave it on the Story.

## Acceptance

- [ ] (fresh) every step shows what was seen and its screenshot, from a capture by someone who did not build it

## Result

### Artifact refs

- story:<slug>#<stepId>@<runId>
- file:<fileId>
- company:work:<workId>
- **Transition:** failures are filed as tasks; a person reviews the captured flow
