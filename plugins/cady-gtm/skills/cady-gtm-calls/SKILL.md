---
name: "cady-gtm-calls"
description: "Sales calls: prepare and follow up. Use when: Prepare for a sales or customer call (account brief, agenda, questions), then record its follow-up and next step. Not for: Dialling, recording audio, cold email, or an unverified call note; use `cady-gtm-warm-email` for a separately authorized message."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.calls"
  version: "29cf8ad1302a77ea9331"
  library: "015714eb283c43b7"
  function: "gtm"
---
# Sales calls: prepare and follow up

**Point:** Prepare the user for one conversation, then capture what the buyer said and the promised next step.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Separate what the buyer said from our inference; friendly interest is not a commitment. Instead of: Write the call up as an upbeat summary with assumed next steps.
- Hold an uncertain notes match rather than guess the party. Instead of: Attach the call note to the likeliest party by name.
- Set a stage only when the user states it. Instead of: Advance the stage from how the call seemed to go.

Prepare for a sales or customer call (account brief, agenda, questions), then record its follow-up and next step.

**Not for:** Dialling, recording audio, cold email, or an unverified call note; use `cady-gtm-warm-email` for a separately authorized message.

**Unit of work:** one work item per call and relationship. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- profileRef
- offerRef
- crm:party:<partyId>
- call note id
- communication refs
- voice and brand pack subjects
- governing decision refs
- grant ref

### Work fields

- partyIds
- senderLabel
- call purpose
- call date
- participants
- doneWhen
- stopIf

## Procedure

1. Read the brief and its refs (`../../references/outreach-drafting.md`, Brief), including qualification criteria from offerRef; read cady_read party:<partyId> for each exact person. Keep cold and warm context distinct. For cold calls, remind the user that they decide lawfulness and UK numbers may need Telephone Preference Service (TPS) and Corporate Telephone Preference Service (CTPS) screening; this is not clearance.
2. Prepare one sheet per call using `../../references/call-prep.md`, sheet; save it to Files with files_set, with upload begin and complete, verify the receipt and reference it on the work item. Report unavailable steps outside the sheet. The user makes the call; Cady never dials and never records audio.
3. After the call, match the notes-system record to the exact party, date and participants (`../../references/call-follow-up.md`, match); hold an uncertain match. Record one interaction with crm_interactions_set, interaction kind call, with occurredAt and sourceRef citing the call note id; keep only connected/not connected, qualified yes/no and next step in note. Never store a transcript, phone number or audio. Preserve sourceRef on retry.
4. Separate what the buyer said from inference and commitments (`../../references/call-follow-up.md`, separate); handle commitments and act versus ask under `../../references/outreach-drafting.md`, Authority. A connected conversation makes the party engaged; set a stage with crm_interactions_set (the interaction's motion and stage) only when the user states it. Record supported ICP learning on the work item for the brief’s author (channel strategy).
5. Draft the follow-up using `../../references/call-follow-up.md`, draft and `../../references/outreach-drafting.md`, Truth and grounding, Claims, Format, Easy yes, Booking and Unknowns; run Draft check before `../../references/taste-message.md`. Show the exact unsent proposal for user review; route it through cady-gtm-warm-email. Report the prepared outcome and linked work and source refs with work_write after owner readbacks; do not claim delivery.
6. Stop: on any condition in `../../references/agent-stop.md`, stop and report as it says.

## Acceptance

- [ ] (check) an evidence-grounded sheet per call is saved in Files, with qualification criteria from offerRef
- [ ] (check) the user makes the call; no audio or transcript is recorded
- [ ] (check) the interaction cites the call note id and records only outcome, qualification and next step; uncertainty is visible
- [ ] (check) stages change only when the user states one and commitments remain findable on existing work
- [ ] (person) the exact unsent follow-up is shown for review and routed through warm_email; no delivery is claimed

## Owner checks

- accepted offer and qualification criteria
- exact CRM party identity
- completed Files upload readback
- user-made call outcome
- exact party and call match
- contact permission before message preparation

## Result

### Artifact refs

- file:<fileId>
- crm:interaction:<interactionId>
- crm:party:<partyId>
- company:work:<workId>
- **Transition:** the claim holder reports the saved sheet and verified interaction receipts

## References
- Read [Agent stop](../../references/agent-stop.md) when before acting and whenever a stop condition arises.
- Read [Call follow-up](../../references/call-follow-up.md) when matching a call note, separating evidence and drafting the follow-up.
- Read [Call prep: the call sheet](../../references/call-prep.md) when preparing a sheet before a call.
- Read [Outreach drafting](../../references/outreach-drafting.md) when use the named parts for drafting and authority.
- Read [Taste check: message](../../references/taste-message.md) when after the draft check, when judging the follow-up.
