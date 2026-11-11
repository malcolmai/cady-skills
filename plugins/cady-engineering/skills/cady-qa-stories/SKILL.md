---
name: "cady-qa-stories"
description: "User stories: keep, walk and read. Use when: Edit or retire a user story, walk one blind as a fresh user, read story status, or file a finding on a step. Not for: Rating or reproducing a bug (use `cady-qa-triage`), the accessibility audit (use `cady-design-wcag-audit`) or the release go/no-go (`cady-product-manage` decides)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.qa.stories"
  version: "58f709c6d2de7686d837"
  library: "d31a1ceb5b37afff"
  function: "qa"
---
# User stories: keep, walk and read

**Point:** Walk real user goals blind as a stranger would, so story status shows what a new user actually meets.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Upload a step picture from its file and let the tool check the hash; the model never carries the bytes. Instead of: Paste or retype the image's base64 into the tool call.
- Brief the walker with only the story id, environment, build and account; a hinted pass is a finding, never a verification. Instead of: Give the walker the PR, routes or earlier reports so the walk goes faster.
- Treat a check as information: nothing waits on its badge, and the step picture belongs to the story. Instead of: Hold work until a story check is green, or tie the picture to one run.
- Read 'verified' as the steps passing blind at this revision, and check separately that the goal still matters. Instead of: Read a verified story as proof of user value.
- Close a failure only by a new blind walk of the story at the fixed build. Instead of: Close on the producer's 'fixed' or a green CI run.

Edit or retire a user story, walk one blind as a fresh user, read story status, or file a finding on a step.

**Not for:** Rating or reproducing a bug (use `cady-qa-triage`), the accessibility audit (use `cady-design-wcag-audit`) or the release go/no-go (`cady-product-manage` decides).

**Unit of work:** one story, or one blind walk of it. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- story:<slug> (the story id from stories_read)
- the environment to walk and test-account access
- beta feedback as a request or its source reference

## Procedure

1. A story is one user goal in the user's words: actor, goal, start state, entry, then 3 to 12 steps. Each step has do (an action a person takes) and expect (what they see, observable). A hint (route, tool, selector) is optional and only for testers who are stuck; expect never names routes, tools, tables or code. A branch is its own story. Check that the story still reflects a real user goal, citing the user evidence behind it (an interaction, research or feedback); flag one no current evidence supports to the story's owner and keep walking it until they decide. Read first with stories_read, then edit; do not duplicate a story that exists. When the product has a saved flow map (a .logicmap.json File), link each step to its box: stories_set links [{kind:'logic_map', ref:'file:<mapId>', stepId, node:<box id>}] (it sets the step's box; an empty node clears it).
2. Change stories with stories_set. No story.id creates a story and an id edits it. A wording fix, step change or retirement of a story you own goes in directly with a one-line summary; change steps by id in story.steps (no id adds a step, an id edits it, remove true drops it, after places it), and an edit that touches only existing steps by id needs no expectedRevision. Feedback on a step is a note on it, story.steps [{id, note}], recorded as you with the time; stories_read view full shows each step's notes, people's feedback included, so read them before changing a step. There is no request to file or decide: when a story should be added or removed, do it, or ask the owner in conversation to review it. Stories carry no priority: link a story to a goal (kind goal) and lists order by that goal's due date. Retire, never delete. Pass expectedRevision and re-read on a conflict. Attach a screenshot or video to a step at any time with stories_set story.steps [{id, media:{add:['file:<id>']}}] (upload as step 3 says): it is the story's own picture, shown at once and editable, and a check never adds one. A check is QA, not a gate: its result is a badge, and nothing waits on it.
3. Walk blind as a fresh walker: a subagent or person briefed with only the story id, environment, target build/version and test account before starting. Read no work context, repo, PR or earlier report. Act through the real surface, never code or the database. stories_set storyId and environment start the check (build is the target build: omit it if unknown, never use Cady’s service SHA) and return the first step without hints, status or history. For each step act, then record it with stories_set runId, stepId: result pass, fail, blocked or skipped, and observed (what you saw, no judgement). A fail or blocked needs evidence. Give each step a picture as file:<id>; quote:<text> shows no picture. Upload from the file, never by retyping its bytes: in the browser, with `cady files upload <path>`, or with the upload link from files_set mode begin_upload (begin, POST the bytes with the returned Authorization header, then reference file:<id>). Reveal a hint (runId, stepId, hint true) only when stuck; a hinted pass is itself a finding and never verifies the story. Finish with runId and outcome; only then do prior results appear.
4. Never walk a story you just implemented as if you were fresh. If you must, the run is a self-check and you say so; a separate walker still has to verify it.
5. After a release you were told cites a story (release.stories on its work item, shipped), the story reads rewalkDue until a blind walk starts after it: walk it again. Read status from stories_read: verified (latest blind run at this revision passed with no hints), failing or blocked (first bad step shown), disputed (two runs at the same revision and build disagree), stale (the story's step wording changed since the run) and unwalked. Verified means the steps passed blind at this revision; it does not show the goal still matters (step 1). Results are never edited. Resolve a dispute with another blind run by a different walker.
6. Review at two levels. First why: does the work serve the purpose one level up? Ask why until you reach a recorded goal, direction or decision, and list each assumption with its evidence or mark it unsupported. A why that is missing goes back to the requester as a question. A why that evidence contradicts is a blocker even when the details are sound. A why that conflicts with an owner's recorded decision goes to that owner; you do not reverse it. Then review the details. An obviously purposeful small fix needs one line on why. The detail level is the blind walk and its filed failures. File each failure after finishing, as a Projects item citing story:<slug>#<stepId>@<runId> (slug is the story id from stories_read, stepId the step id, runId the run from stories_set start; leave out @<runId> when no run applies) with the evidence file. Rate it with `cady-qa-triage`. Close it by a new blind run of that story at the fixed build, not by the producer's word; a reported fix awaits that passing rewalk. Finish returns unfiledFindings with the next Projects call; a blocked step becomes an owner ask. Review notes on walks are open Projects work exposed in stories_read: pick them up directly.

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
