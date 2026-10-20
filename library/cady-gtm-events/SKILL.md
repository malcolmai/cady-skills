---
name: "cady-gtm-events"
description: "Events: attend or host. Use when: Choose, prepare for or host an event that can advance the company purpose through real conversations. Not for: Treating an attendee directory as intent; use `cady-gtm-tam-map` for research and `cady-gtm-warm-email` or `cady-gtm-linkedin-message` for separate messages."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.events"
  version: "88325f9e87bfedf618a24e9df0ea4a688c145c355d508816ac89fb09616fcc9e"
  library: "3beca7fa80e90672"
  function: "gtm"
---
# Events: attend or host

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.events": "88325f9e87bfedf618a24e9df0ea4a688c145c355d508816ac89fb09616fcc9e"}})`

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
2. Attend: choose by fit and likely conversation density, cost and founder time. Set a target for substantive conversations and next steps; directory presence alone is not intent. Host: establish the event purpose, co-host, date and venue, then plan a small hosted event that creates a useful community for the company and co-host.
3. Attend: during sourcing, persist source-backed eligible speakers and attendees in the selected CRM research List through the applicable reviewed import method (for Cady CRM, `cady-gtm-tam-map`); read import completion and actual membership. Then choose 10 to 15 priority people. Host: persist source-backed eligible co-host and guest identities into the selected CRM List through the applicable reviewed import method; read import completion and actual membership. Build a focused cohort of about 20, rank by fit and real common ground, and request introductions with a ready-to-forward blurb where useful. In both modes report researched, saved and member counts separately; shortfalls remain explicit, and people remain cold until a real readable relationship exists.
4. Attend: prepare a one-line introduction, a few discovery questions by segment and one useful item to offer; ask organisers about speaking, volunteering or a side dinner. Prepare a soft pre-event LinkedIn note only when genuine common ground supports it. Host: offer a low-effort partnership—the user handles venue, event page, follow-up and costs; the co-host invites a small group and shares hosting. Expect 20 to 40 personal asks before the first yes. Use the event platform as the RSVP system of record; set a date about six weeks out, meet the co-host every two weeks, invite about ten people to seat six to eight, and plan milestones at six, four and two weeks before, the Friday before, event day and three days after.
5. Host: route each co-host request to a separate work item bound to the appropriate email or LinkedIn skill. Invitations come from the co-host and are sent by the user; do not imply Cady sends them. Keep the run of show and guest question sheet in Files using files.upload with mode "begin" and files.upload with mode "complete". Prepare them for the co-host on the Friday before and retain the completion receipt in the event work item.
6. Attend: the user attends and has conversations, listening for current work and pain rather than pitching. Host: the user hosts in person—arrive 30 minutes early, welcome guests, surface common ground, guide one table-wide discussion so everyone speaks, then leave room to mingle.
7. Attend: for each person actually met, capture one specific follow-up hook in this work item and prepare a personal follow-up through `cady-gtm-warm-email` or `cady-gtm-linkedin-message`. Host: after the event, use the same personal follow-up route. In both modes use crm.record_interactions for a one-to-one meeting the user actually attended (kind meeting) or a substantive conversation (kind event_conversation), with occurredAt the interaction time and sourceRef the event platform ID or event slug plus date. Keep the event platform authoritative for attendance and RSVPs; listed attendees stay cold, never bulk-message the attendee List, respect current opt-outs and suppression, and deliver promised items. These actual interactions make the party engaged.
8. Attend: record one short keep-or-drop learning note on the event work item. Host: record one keep-or-drop learning note on this event work item.

## Acceptance

- [ ] event choice has a conversation goal
- [ ] eligible sourced speakers, attendees, co-hosts and guests are persisted in the selected CRM List with import completion and membership readback; shortfalls are explicit
- [ ] researched candidates, saved parties and List members are reported separately
- [ ] only actual conversations route to warm follow-up
- [ ] event platform remains RSVP source of truth
- [ ] Files contain a checked run of show and guest questions when hosting
- [ ] in-person hosting remains the user's action

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
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
