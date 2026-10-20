---
name: "cady-gtm-pipeline-pass"
description: "Warm pipeline pass. Use when: A scheduled or requested pass over due customer tracks. Not for: Writing one message; use `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`; working one deal in depth uses `cady-sales-deal-motion`. Keep due relationship tracks consistent."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.pipeline_pass"
  version: "3c8514bcfa17c4afc3030bf3b63f528875e705523787e22b441d383c37b1d118"
  function: "gtm"
---
# Warm pipeline pass

A scheduled or requested pass over due customer tracks.

**Not for:** Writing one message; use `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`; working one deal in depth uses `cady-sales-deal-motion`. Keep due relationship tracks consistent.

**Unit of work:** one scheduled pass over due tracks. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- crm:relationship_track:<trackId>

### Statement fields

- cadence
- due tracks

## Procedure

1. Run under the run sequence (claim, checkpoint, close) from get_cady_context; read `cady-core-run-sequence` if it is not in your context. The pass uses CRM tracks, not Projects items.
2. Call crm.list_parties({mode: 'tracks', motion: 'customer', dueBefore: now}) and work every due track. Reply, prepare warm email, LinkedIn or post-call follow-up, or update crm.set_track when no contact action fits. Never infer a stage. Set each touched party's next action and due date.
3. For a cold or not-interested lead, set crm.set_track recontact only on a lost or paused track: never means Never contact; unless_changed means Do not contact unless circumstances change; 1m, 2m, 3m, 6m or a lead-suggested date create a Plan re-contact action seven days before the due date. An interested lead is never dropped and there is no follow-up count limit: judge each follow-up case by case, check permission and release through outreach review, and reopen a held track only with an explicit reason.
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

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.pipeline_pass": "3c8514bcfa17c4afc3030bf3b63f528875e705523787e22b441d383c37b1d118"}})`
