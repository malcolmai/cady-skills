---
name: "cady-marketing-post"
description: "Post one piece. Use when: Create or edit one post for the audience, topic and placement chosen in the brief. Not for: Choosing a content strategy, pillars or distribution plan."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.marketing.post"
  version: "d22d646cad253562516a"
  library: "77b2da60520f8542"
  function: "marketing"
---
# Post one piece

**Point:** Publish one useful, true piece for the brief's audience, judged in placement, only after approval.

**Company context:** `context_read({"area": "gtm/content", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.marketing.post": "d22d646cad253562516a@77b2da60520f8542"}})`

Create or edit one post for the audience, topic and placement chosen in the brief.

**Not for:** Choosing a content strategy, pillars or distribution plan.

**Unit of work:** one work item per post. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- profileRef
- source and claim refs
- voice and brand pack subjects
- governing decision refs
- grant ref when applicable
- existing draft ref when editing

### Work fields

- topic and pillar
- audience
- placement and account
- doneWhen
- stopIf

## Procedure

1. Read the brief and its refs (`../../references/outreach-drafting.md`, Brief); follow its audience, topic, pillar and placement. Do not re-plan the content strategy.
2. Create or edit the post using the written-content craft in `../../references/taste-post.md`. For an edit, preserve accepted work outside the requested change. Apply `../../references/outreach-drafting.md`, Truth and grounding, Claims and Brand pack to the evidence and allowed claims.
3. Have a fresh judge check the post in its intended placement using `../../references/taste-post.md`, including the tells scan and source checks. For hooks and headlines, shortlist for the owner to pick.
4. Save the exact post and placement preview to Files and present the exact text and placement for the person's approval. Cady has no native publish review: publish nothing without that approval or an exact covering grant. After approval or grant, use the authorized connector and record the channel's receipt and post id; report a held post as held.
5. Record exposure, response and business outcome separately from their evidence; engagement is a signal, not proof of demand. Record owner corrections on the work item for the brief’s author (channel strategy).
6. Stop: on any condition in `../../references/agent-stop.md`, stop and report as it says.

## Acceptance

- [ ] The post follows the brief and its claims and links are checked against sources.
- [ ] A fresh judge checks the post in placement; the owner picks any hook or headline from the shortlist.
- [ ] The exact text and placement are presented for approval; nothing is published without approval or an exact covering grant.
- [ ] A published post has a channel receipt and post id; a held post is reported as held.
- [ ] Exposure, response and business outcome are recorded separately when available.

## Owner checks

- source and claim evidence
- exact text and placement approval or covering grant
- channel receipt

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- channel receipt or post id
- **Transition:** the claim holder reports the held post or publication and receipt

## References
- Read [Agent stop](../../references/agent-stop.md) when before acting and whenever a stop condition arises.
- Read [Outreach drafting](../../references/outreach-drafting.md) when use only truth, claims and brand guidance for the post.
- Read [Taste check: post](../../references/taste-post.md) when a fresh judge checks the post in its intended placement.
