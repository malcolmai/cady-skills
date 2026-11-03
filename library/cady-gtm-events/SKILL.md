---
name: "cady-gtm-events"
description: "Events: attend or host. Use when: Prepare for or host the event named in the brief to advance the company through real conversations. Not for: Choosing an event or treating an attendee directory as intent."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.events"
  version: "b4453a784a2227fe7ad3"
  library: "3fd543d54b0547f6"
  function: "gtm"
---
# Events: attend or host

**Point:** Turn one chosen event into real conversations and personal follow-ups, never a bulk list.

**Company context:** `context_read({"area": "gtm/content", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.events": "b4453a784a2227fe7ad3@3fd543d54b0547f6"}})`

**Bets** (where this differs from the default):
- An attendee directory is a source, not a relationship: listed people stay cold and the list is never bulk-messaged. Instead of: Import the attendee list as warm leads and message them all after the event.
- Follow up each person actually met with one specific hook from the conversation. Instead of: Send one 'great to meet you' template to everyone met.
- Judge an event by real conversations against its target, then record a keep-or-drop decision. Instead of: Judge an event by badge scans, leads collected or attendance.

Prepare for or host the event named in the brief to advance the company through real conversations.

**Not for:** Choosing an event or treating an attendee directory as intent.

**Unit of work:** one work item per event. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- event URL or ID
- event platform URL or ID
- CRM List ref
- governing decision refs

### Work fields

- event mode (attend or host)
- conversation target
- co-host, date and venue when hosting
- doneWhen
- stopIf

## Procedure

1. Claim the event work item with work_change(action: 'claim'); read the brief and its refs. Follow its event, mode and conversation target; if any is missing, stop and report.
2. Follow `../../references/events-attend.md` when attending or `../../references/events-host.md` when hosting; for a host cohort use `../../references/intro-request.md` where useful. The event platform remains the RSVP source of truth.
3. Persist source-backed eligible speakers, attendees, co-hosts and guests in the brief's CRM List through the reviewed import (`../../references/tam-map-import.md`); read completion and actual membership. Report researched, saved and member counts separately and make shortfalls explicit.
4. After the event, record each actual one-to-one meeting with crm_interactions_create as kind meeting, or substantive conversation as kind event_conversation, with occurredAt and sourceRef the event platform ID or event slug plus date. Directory presence alone is not intent: listed attendees stay cold and the attendee List is never bulk-messaged.
5. For each person actually met, record one specific follow-up hook on the work item and route a personal follow-up to a separate `cady-gtm-warm-email` or `cady-gtm-linkedin-message` work item. Deliver promised items; record one short keep-or-drop learning note on the event work item.
6. Stop: on any condition in `../../references/agent-stop.md`, stop and report as it says.

## Acceptance

- [ ] (check) The brief names the event, mode and conversation target.
- [ ] (check) Eligible source-backed people are imported into the brief’s List; completion, membership, separate counts and shortfalls are recorded.
- [ ] (check) Only actual conversations route to personal follow-up; the attendee List is never bulk-messaged.
- [ ] (check) The event platform remains the RSVP source of truth.
- [ ] (person) Hosting has a checked run of show and guest questions in Files; the user hosts in person.

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
- Read [Agent stop](../../references/agent-stop.md) when before acting and whenever a stop condition arises.
- Read [Attending an event](../../references/events-attend.md) when attending the event.
- Read [Hosting an event](../../references/events-host.md) when hosting the event.
- Read [Introduction request](../../references/intro-request.md) when requesting an introduction for a host cohort.
- Read [Reviewed CRM import](../../references/tam-map-import.md) when adding sourced people to the brief’s List.
