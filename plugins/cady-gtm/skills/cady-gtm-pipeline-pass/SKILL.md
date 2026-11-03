---
name: "cady-gtm-pipeline-pass"
description: "Warm pipeline pass. Use when: Pass over due tracks of one motion (customer for GTM, investor for fundraising, partner) and their next steps. Not for: Writing one message (use `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`) or working one deal in depth."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.pipeline_pass"
  version: "b55c2d0a39b5cc27b90d"
  library: "ae40c76cb73327f0"
  function: "gtm"
---
# Warm pipeline pass

**Point:** Give every due track an evidence-backed next action, routing each contact to its channel slice.

**Company context:** `context_read({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.pipeline_pass": "b55c2d0a39b5cc27b90d@ae40c76cb73327f0"}})`

**Bets** (where this differs from the default):
- Work replies first, then due follow-ups, then first touches. Instead of: Work the queue in due-date order.
- Check each contact's latest outcome before routing a follow-up. Instead of: Send each due follow-up as scheduled.
- Review a stale backlog before acting; never replay it blindly. Instead of: Catch up an overdue queue by sending everything due.
- Close a track only on a definitive answer; never drop an interested lead. Instead of: Close quiet tracks to keep the pipeline clean.

Pass over due tracks of one motion (customer for GTM, investor for fundraising, partner) and their next steps.

**Not for:** Writing one message (use `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`) or working one deal in depth.

**Unit of work:** one scheduled pass over due tracks. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- crm:relationship_track:<trackId>

### Work fields

- cadence
- due tracks
- motion

## Procedure

1. Call crm_parties_read({mode: 'tracks', motion: <the pass's motion>, dueBefore: now}) and work every due CRM track, not Projects items. Never infer a stage; preserve current persona and owner.
2. Route replies first to `cady-gtm-reply`, then due follow-ups to `cady-gtm-warm-email` or `cady-gtm-linkedin-message`, then today's first touches to `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message`. Before routing any follow-up, run `../../references/outreach-release.md` Outcome check; apply its Follow up part. Review stale items; never replay a backlog of external sends blindly.
3. When no contact action fits, update crm_tracks_set. Set each touched party's evidence-backed next action and due date. Handle routine work and owner questions as `../../references/outreach-drafting.md`, Authority says. A refusal returns the exact next call; follow it.
4. Close a track only on a definitive answer, in the same crm_tracks_set call with reason, reasonKind and any evidence. Set recontact only on a lost or paused track; never drop an interested lead. Reopen a held track only with an explicit reason. Recontact policies are '1m', '2m', '3m', '6m', 'date' and 'unless_changed'.
5. Record product signup or activation with crm_interactions_create, matching by email and using each product event id as sourceRef (up to 25 per call); preserve sourceRef on retries for idempotency. Pass the captured cref for attribution; keep UTMs in product analytics. The user's agent or automation runs the sync.
6. On each touched track, keep the exact review receipt; do not copy it into a Projects work item.
7. Stop: on any condition in `../../references/agent-stop.md`, stop and report as it says.

## Acceptance

- [ ] every due track has a next action and due date
- [ ] track stage and next action remain evidence-backed

## Owner checks

- current contact permission
- product sign-up checked before a trial nudge

## Result

### Artifact refs

- crm:relationship_track:<trackId>
- **Transition:** the pass updates each touched track

## References
- Read [Agent stop](../../references/agent-stop.md) when before acting and whenever a stop condition arises.
- Read [Outreach drafting](../../references/outreach-drafting.md) when deciding routine work and owner questions.
- Read [Outreach release](../../references/outreach-release.md) when before routing a follow-up, read Outcome check and Follow up.
