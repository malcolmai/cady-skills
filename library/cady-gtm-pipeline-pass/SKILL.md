---
name: "cady-gtm-pipeline-pass"
description: "Warm pipeline pass. Use when: Review the pipeline: a scheduled or requested pass over due customer tracks and their next steps. Not for: Writing one message (use `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`) or working one deal in depth. Keep due relationship tracks consistent."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.pipeline_pass"
  version: "e886288d66129721c443e5ced2fd301789cc01280b4f9a02d2235416d5b41ff5"
  library: "c524ef7ffada6715"
  function: "gtm"
---
# Warm pipeline pass

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.pipeline_pass": "e886288d66129721c443e5ced2fd301789cc01280b4f9a02d2235416d5b41ff5"}})`

Review the pipeline: a scheduled or requested pass over due customer tracks and their next steps.

**Not for:** Writing one message (use `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`) or working one deal in depth. Keep due relationship tracks consistent.

**Unit of work:** one scheduled pass over due tracks. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- crm:relationship_track:<trackId>

### Statement fields

- cadence
- due tracks

## Procedure

1. The pass uses CRM tracks, not Projects items.
2. Call crm.list_parties({mode: 'tracks', motion: 'customer', dueBefore: now}) and work every due track. Reply, prepare warm email, LinkedIn or post-call follow-up, or update crm.set_track when no contact action fits. Never infer a stage. Set each touched party's next action and due date.
3. For a cold or not-interested lead, set crm.set_track recontact only on a lost or paused track: never means Never contact; unless_changed means Do not contact unless circumstances change; 1m, 2m, 3m, 6m or a lead-suggested date create a Plan re-contact action seven days before the due date. An interested lead is never dropped. Each follow-up follows the follow-up rule in the outreach message rules (an engaged recipient is paced to the thread's tempo and not counted; an unengaged non-replier gets at most 2, counted); check permission, release through outreach review, and reopen a held track only with an explicit reason.
4. Product sign-up sync: record signup or activation with crm.record_interactions. Match by email and use each product event id as sourceRef (up to 25 per call); preserve sourceRef on retries for idempotency. Pass the captured cref to attribute the sign-up to email, click and variant. Keep UTMs in your own product analytics; no site script is needed. Cady does not run the sync: the user's agent or automation does.
5. Schedule a host recurring task named 'Warm pipeline (<Company>)' weekly or at the user's chosen cadence. Each run starts with get_cady_context and reads due tracks. Review stale items; never replay a backlog of external sends blindly.
6. The pass updates each touched CRM track and keeps its exact review receipt without Projects work state.

## Acceptance

- [ ] every due track has a next action and due date
- [ ] track stage and next action remain evidence-backed

## Owner checks

- METHOD_NOT_CURRENT
- current contact permission
- product sign-up checked before a trial nudge

## Result

### Artifact refs

- crm:relationship_track:<trackId>
- **Transition:** the pass updates each touched track
