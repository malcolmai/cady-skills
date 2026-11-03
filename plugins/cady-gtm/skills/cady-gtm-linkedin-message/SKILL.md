---
name: "cady-gtm-linkedin-message"
description: "Social direct message. Use when: Draft a first social DM, LinkedIn connection note or one no-reply follow-up. Not for: Public comments or posts are publishing; email or a reply in a live thread use their own skills."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.linkedin_message"
  version: "b5d6c54ac250e5791709"
  library: "a63d7695f1bd83d4"
  function: "gtm"
---
# Social direct message

**Point:** Open a real conversation with one honest reason, paced so the account stays safe.

**Company context:** `context_read({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.linkedin_message": "b5d6c54ac250e5791709@a63d7695f1bd83d4"}})`

**Bets** (where this differs from the default):
- A connection note gives one honest reason to connect, with no pitch, ask or company name. Instead of: Pitch the product in the connection request.
- Pace sends across working hours and count the owner's own manual sends in the limit. Instead of: Send the day's batch at once, up to the platform cap.
- When acceptance falls, revise targeting or the note; never raise volume. Instead of: Send more invitations to keep accepted connections up.
- Use only common ground the recipient would recognise; mention a mutual connection only when they identified it. Instead of: Name-drop mutual connections or shared groups found on the profile.
- Pass motion on the prepare call when the person is new to every board. Instead of: Leave the relationship type to inference.

Draft a first social DM, LinkedIn connection note or one no-reply follow-up.

**Not for:** Public comments or posts are publishing; email or a reply in a live thread use their own skills.

**Unit of work:** one work item per cohort of 20 or fewer. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Always

- In a review body, put a line with only --- between messages.

## Inputs

### Evidence refs

- brief profileRef and recipient profile or shared-context refs
- brief List or crm:party:<partyId> refs
- brief voice, brand, governing decision and grant refs

### Work fields

- relationship state
- senderLabel
- chosen angle and what is new

## Procedure

1. Read the brief’s profileRef and recipient context; use the profile’s words and name it in the justification (`../../references/outreach-drafting.md`, Brief). If the profile is unchecked, stop and report under `../../references/agent-stop.md`. Read each party and act on holds as `../../references/outreach-release.md`, Permission says.
2. Choose a connection note, first direct message or follow-up; keep each in a distinct cohort. A connection note gives one honest reason to connect, with no pitch, ask or company name. A first DM gives a subtle personal note about what you are working on, why it may matter now and that you would be glad to chat; omit product names and links. Use only common ground the recipient would recognise; mention a mutual connection only when they identified it. 
3. For LinkedIn, pace at most 20 messages per rolling day and 100 per rolling week, including messages the owner sends by hand, spread across working hours. Tell the owner which invitations have been pending over three weeks. A falling acceptance rate calls for revised targeting or notes, not higher volume. An identity check, restriction or rate-limit notice is a stop (`../../references/agent-stop.md`).
4. Apply `../../references/outreach-release.md`, Outcome check and Follow up for a follow-up; hand a replier to `cady-gtm-reply`.
5. Run the draft check (`../../references/outreach-drafting.md`, Draft check), then the taste check (`../../references/taste-message.md`). Prepare and read the review as `../../references/outreach-release.md`, Preparation says, with a one-line justification for why this send now. On the prepare call, pass motion when the person is new to every board.
6. Follow `../../references/outreach-release.md`, Release for this route's mechanics; the sending rule is execution authority.
7. Stop: on any condition in `../../references/agent-stop.md`, stop and report as it says.

## Acceptance

- [ ] (check) the connection note or first DM follows its channel-specific form and uses recognised common ground
- [ ] (check) LinkedIn sends stay within rolling caps and are spread across working hours
- [ ] (check) at most one LinkedIn follow-up is prepared under `../../references/outreach-release.md`, Follow up
- [ ] (check) the draft check precedes the taste check and the review is readable
- [ ] (person) release follows `../../references/outreach-release.md`, Release and execution authority's sending rule

## Owner checks

- current contact permission

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- **Transition:** the claim holder reports the prepared review

## References
- Read [Agent stop](../../references/agent-stop.md) when recognising and reporting a stop.
- Read [Outreach drafting](../../references/outreach-drafting.md) when before drafting, including the brief and draft check.
- Read [Outreach release](../../references/outreach-release.md) when checking permission, preparing, releasing or checking outcomes and follow-ups.
- Read [Taste check: message](../../references/taste-message.md) when judging a draft after its draft check.
