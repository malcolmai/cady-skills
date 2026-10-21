---
name: "cady-gtm-calls"
description: "Sales calls: prepare and follow up. Use when: Prepare for a sales or customer call (account brief, agenda, questions), then record its follow-up and next step. Not for: Dialling, recording audio, cold email, or an unverified call note; use `cady-gtm-warm-email` for a separately authorized message."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.calls"
  version: "0de1b5c43565c5b02f2a527be80737839f804ec0e810f68e9f38fd2b9aab64d1"
  library: "f4e8ca47d12d38e8"
  function: "gtm"
---
# Sales calls: prepare and follow up

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.calls": "0de1b5c43565c5b02f2a527be80737839f804ec0e810f68e9f38fd2b9aab64d1"}})`

Prepare for a sales or customer call (account brief, agenda, questions), then record its follow-up and next step.

**Not for:** Dialling, recording audio, cold email, or an unverified call note; use `cady-gtm-warm-email` for a separately authorized message.

**Unit of work:** one work item per segment, small cohort or call and relationship. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- accepted offer and qualification criteria
- segment evidence
- crm:party:<partyId>
- host call note or transcript ref
- communication refs

### Statement fields

- segment
- offer
- people
- call purpose
- call date
- participants
- decision or promise to follow up

## Procedure

1. Before the call: read the accepted offer and segment evidence, then crm.get_party for each exact person. Keep cold and warm context distinct; do not infer a relationship from missing history. For cold calls, remind the user that Cady is a processor and the user decides lawfulness; UK numbers may need TPS/CTPS screening. This is a reminder, not a Cady rule or clearance.
2. Before the call: prepare one call sheet per segment and person as the call prep reference says (`../../references/call-prep.md`). Save it to Files with files.upload with mode "begin" and files.upload with mode "complete"; verify the completed file receipt and reference it on this work item. Cady never dials and never records audio. Keep tool status and unavailable steps out of the sheet; report them to the user outside it.
3. After the call: once the user has made each call, record it with crm.record_interactions, kind call, occurredAt the call time, and sourceRef the call ID or a date plus number-free label. Put only connected/not connected, qualified yes/no, and the next step in note. Never store a transcript, phone number, or audio. Preserve identical sourceRef values when retrying. Record the grounded next action and due date through transition_company_work(action: 'checkpoint'), linked to the CRM party and call source; read it back with get_company_work.
4. After the call: match the note to the party, separate what the buyer said from inference, and draft the follow-up as the call follow-up reference says (`../../references/call-follow-up.md`). Show the exact unsent proposal for user review; a material change in source, relationship state or copy needs a fresh review under the relevant outreach skill.
5. After the call: report the prepared outcome with transition_company_work(action: 'report_result') after the linked work and source are checked. Carry supported ICP learning as a proposed change with contrasting evidence and a reversal condition. A connected conversation makes the party engaged; use crm.set_track only when the user states a stage, never infer one. Send the follow-up email through `cady-gtm-warm-email`.

## Acceptance

- [ ] one usable, evidence-grounded call sheet per person and segment is saved in Files
- [ ] the user alone makes calls and no audio or transcript is recorded
- [ ] each user-made call has a reference-only interaction with outcome, qualification and next step
- [ ] track stages are changed only when stated by the user
- [ ] the call source and uncertainty are visible
- [ ] one useful next action and due date are recorded
- [ ] the unsent follow-up is reviewable with no delivery claim

## Owner checks

- accepted offer and qualification criteria
- exact CRM party identity
- completed Files upload readback
- user-made call outcome
- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
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
- [Call follow-up](../../references/call-follow-up.md)
- [Call prep: the call sheet](../../references/call-prep.md)
- [Outreach message rules](../../references/outreach-message-rules.md)
