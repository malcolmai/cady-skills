---
name: "cady-gtm-events"
description: "Events: attend or host. Use when: Choose, prepare for or host an event that can advance the company purpose through real conversations. Not for: Treating an attendee directory as intent; use `cady-gtm-tam-map` for research and `cady-gtm-warm-email` or `cady-gtm-linkedin-message` for separate messages."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.events"
  version: "fc153c9b1f9a7d127022"
  library: "591145ab2187b638"
  function: "gtm"
---
# Events: attend or host

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.events": "fc153c9b1f9a7d127022@591145ab2187b638"}})`

Choose, prepare for or host an event that can advance the company purpose through real conversations.

**Not for:** Treating an attendee directory as intent; use `cady-gtm-tam-map` for research and `cady-gtm-warm-email` or `cady-gtm-linkedin-message` for separate messages.

**Unit of work:** one work item per event. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- company direction ref
- CRM List refs
- event URL or ID
- event platform URL or ID

### Statement fields

- event purpose
- target conversations
- next-step goal
- co-host
- date and venue

## Procedure

1. Claim the event work item with transition_company_work(action: 'claim') (the server fills attemptId and claimProof).
2. Choose the mode. Attend: choose by fit and likely conversation density, cost and founder time; set a target for substantive conversations and next steps; directory presence alone is not intent. Host: establish the event purpose, co-host, date and venue for a small event that creates a useful community for the company and co-host. Then follow that mode's reference (`../../references/events-attend.md` or `../../references/events-host.md`).
3. During sourcing, persist source-backed eligible speakers, attendees, co-hosts and guests in the selected CRM List through the applicable reviewed import method (for Cady CRM, `cady-gtm-tam-map`); read import completion and actual membership. Report researched, saved and member counts separately; shortfalls remain explicit, and people remain cold until a real readable relationship exists.
4. After the event, use crm.record_interactions for a one-to-one meeting the user actually attended (kind meeting) or a substantive conversation (kind event_conversation), with occurredAt the interaction time and sourceRef the event platform ID or event slug plus date. These actual interactions make the party engaged and route to a personal follow-up. Keep the event platform authoritative for attendance and RSVPs; listed attendees stay cold, never bulk-message the attendee List, respect current opt-outs and suppression, and deliver promised items.
5. Record one short keep-or-drop learning note on the event work item.

## Acceptance

- [ ] event choice has a conversation goal
- [ ] eligible sourced speakers, attendees, co-hosts and guests are persisted in the selected CRM List with import completion and membership readback; shortfalls are explicit
- [ ] researched candidates, saved parties and List members are reported separately
- [ ] only actual conversations route to warm follow-up
- [ ] event platform remains RSVP source of truth
- [ ] Files contain a checked run of show and guest questions when hosting
- [ ] in-person hosting remains the user's action

## Owner checks

- source and fit evidence
- actual conversation before warm routing
- Projects work readback
- Files upload readback

## Result

### Artifact refs

- company:work:<workId>
- crm:list:<listId>
- file:<fileId>
- event URL or ID

### Evidence refs

- receipt:<importCompletionReceiptId> when a CRM List is promised
- **Transition:** the claim holder reports preparation and, after the event, learning

## References
- Read [Attending an event](../../references/events-attend.md) when you attend an event.
- Read [Hosting an event](../../references/events-host.md) when you host an event.
