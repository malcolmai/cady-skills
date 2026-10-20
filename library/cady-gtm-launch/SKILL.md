---
name: "cady-gtm-launch"
description: "GTM launch session. Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing segments (use `cady-gtm-offer-and-segments`) or drafting outreach."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.gtm_launch"
  version: "f9dd85341961210f000fb5f475797782b7fca9611009fcc9fb5a8b338e0c4c5c"
  library: "3beca7fa80e90672"
  function: "gtm"
---
# GTM launch session

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.gtm_launch": "f9dd85341961210f000fb5f475797782b7fca9611009fcc9fb5a8b338e0c4c5c"}})`

Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing segments (use `cady-gtm-offer-and-segments`) or drafting outreach.

## Gtm launch

- **Job:** From the company context and the user's outbound request, prepare the complete internal motion in one session. A missing sender, provider or scheduler blocks activation only, never internal preparation.
- **Rule:** A prepared review is not approval or delivery. A live claim and matching skill are required at prepare and release; owner refusal should name the work or skill needed for recovery. Never invent user assent and never present a quote of the user as approval. In the owner's notify mode (the default) approve the exact read-back review yourself with crm.outreach.confirm after the verified self-check; the owner is notified. If it refuses with SELF_APPROVAL_OFF, give the person the reviewUrl from crm.get_outreach_review to approve in the browser, or use or propose a termed outreach grant with crm.manage_outreach_grant. Release needs one of these before it. Admin or owner invitations and payments always need the person. Record prepared, authorized, released and executor-sent states distinctly, and reconcile uncertain effects before retrying.

### Steps

- 1. Read get_cady_context with the area you are working in (omit it for the map) and get_company_work. If no work item fits, create one with submit_company_work_checkpoint using a new workId, expectedRevision null and a current methodId. Keep company priorities in direction through update_company_direction; goals are goal work items. Split substantial independent channel/cohort work only within host and plan limits.
- 2. State each channel's audience, offer, proof, stop and review condition. Verify the sending account and its executor (Cady's server for API channels, the local cady executor for the rest) before treating a channel as operational; missing access holds that channel while independent work continues.
- 3. If the CRM of record is undecided, hold that choice in a BLOCKED Projects work item or direction review with a recommended default. The sponsor answers it there; no unsupported CRM readiness read is implied.
- 4. During sourcing, persist eligible source-backed identities in the selected CRM before preparing outreach. For Cady CRM use the existing reviewed identity/List import, receipt, recovery and membership readback in the GTM list-mapping method; keep a selected external CRM canonical. Report researched candidates, saved/matched parties and List members separately, plus any shortfall. Unknown contact basis holds contact, not otherwise eligible identity persistence; prepare no send without the existing permission, review and release authority.
- 5. Prepare one crm.prepare_outreach_review per eligible cohort of at most 50 parties, under a live Projects claim and a matching skill for its channel. Read crm.get_outreach_review and report the approvalId. Release needs an approval bound to this work and review: in notify mode (the default) your own crm.outreach.confirm after the verified self-check, with the owner notified; on SELF_APPROVAL_OFF the person's browser approval or a standing purpose grant. Until it exists, keep release pending. Once authorized, a claimed release work item may call crm.get_outreach_review with mode "approved" and crm.execute_approved_outreach for only that approved review within its 72-hour window, then pass the returned ticket ids to the executor (Cady's server, or `cady exec` on a registered device); never send yourself and never ask for addresses, bodies or credentials. If the result says executor_unavailable, ask the user to install the cady CLI and register a device with `cady device register --company <org>` (the person approves it in the Cady web app; you cannot register devices), then release again with executor=device. Retain the ticket receipts.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.
