---
name: "cady-qa-stories"
description: "User stories: keep, walk and read. Use when: Edit or retire a user story, walk one blind as a fresh user, read story status, or file a finding on a step. Not for: Rating or reproducing a bug (use `cady-qa-triage`), the accessibility audit (use `cady-design-wcag-audit`) or the release go/no-go (`cady-product-manage` decides)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.qa.stories"
  version: "405fd42f180cbbd3d026"
  library: "fb0ed0826641a359"
  function: "qa"
---
# User stories: keep, walk and read

**Company context:** `get_cady_context({"area": "product/<productId>/release", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.qa.stories": "405fd42f180cbbd3d026"}})`

Edit or retire a user story, walk one blind as a fresh user, read story status, or file a finding on a step.

**Not for:** Rating or reproducing a bug (use `cady-qa-triage`), the accessibility audit (use `cady-design-wcag-audit`) or the release go/no-go (`cady-product-manage` decides).

**Unit of work:** one story, or one blind walk of it. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- story:<slug> (the story id from stories.read)
- the environment to walk and test-account access
- beta feedback as a request or its source reference

## Procedure

1. A story is one user goal in the user's words: actor, goal, start state, entry, then 3 to 12 steps. Each step has do (an action a person takes) and expect (what they see, observable). A hint (route, tool, selector) is optional and only for testers who are stuck; expect never names routes, tools, tables or code. A branch is its own story. Read first with stories.read, then edit; do not duplicate a story that exists.
2. Change stories with stories.put. A wording fix, step reorder or retirement of a story you own goes in directly with a one-line summary. Adding or removing a story because of beta feedback goes through stories.request (kind, text, askedBy, sourceRef: crm:interaction:<id>, core:research:<id> or file:<id>); a person decides, not an agent: any signed-in company member who can edit stories (by default the founder) accepts or declines in the browser with a note, and you ask them to. A decision is a Projects decision row (subject story.request:<requestId>, citing stories:request:<requestId>) and an accepted request that is not yet applied has a work item: read its workRef from stories.read view requests, apply it with a put carrying the requestId, then finish that work item. Stories carry no priority: link a story to a goal (kind goal) and lists order by that goal's due date. Record with stories.request {action:'record', kind, text, askedBy, sourceRef}. Open feedback on a story or one of its steps (a request with stepId) is the user's request: read it with stories.read view requests and act on it with a put carrying its requestId, or reply by asking a member to decide it. Retire, never delete. Pass expectedRevision and re-read on a conflict.
3. Walk blind as a fresh walker: a subagent or person briefed with only the story id, environment and test account, with no repo, PR or earlier report. Act through the real surface, never code or the database. stories.run start returns the first step without hints, status or history. For each step act, then record: result pass, fail, blocked or skipped, and observed (what you saw, no judgement). A fail or blocked needs evidence as file:<fileId> (screenshot or quoted tool output). Reveal a hint only when stuck; a hinted pass is itself a finding and never verifies the story. Finish with the outcome; only then do prior results appear.
4. Never walk a story you just implemented as if you were fresh. If you must, the run is a self-check and you say so; a separate walker still has to verify it.
5. After a release you were told cites a story (release.stories on its work item, shipped), the story reads rewalkDue until a blind walk starts after it: walk it again. Read status from stories.read: verified (latest blind run at this revision passed with no hints), failing or blocked (first bad step shown), disputed (two runs at the same revision and build disagree), stale (the story's step wording changed since the run) and unwalked. Results are never edited. Resolve a dispute with another blind run by a different walker.
6. File each failure after finishing, as a Projects item citing story:<slug>#<stepId>@<runId> (slug is the story id from stories.read, stepId the step id, runId the run from stories.run; leave out @<runId> when no run applies) with the evidence file. Rate it with `cady-qa-triage`. Close it by a new blind run of that story at the fixed build, not by the producer's word; a finding reported fixed but not accepted still counts as open.

## Acceptance

- [ ] a story reads as user actions with observable expectations
- [ ] status comes from blind runs at the current revision, never from a claim
- [ ] each finding cites story:<slug>#<stepId>@<runId> and its evidence

## Owner checks

- the walker was fresh and blind, or the run is marked a self-check
- every fail or blocked step has observed text and evidence
- wording edits carry a summary; adds and removals from feedback went through a request

## Result

### Artifact refs

- story:<slug>#<stepId>@<runId>
- file:<fileId>
- company:work:<workId>
- **Transition:** findings go to their fix owner; a company member decides open story requests in the browser
