---
name: "cady-gtm-launch"
description: "GTM launch session. Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing segments (use `cady-gtm-offer-and-segments`) or drafting outreach."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.gtm_launch"
  version: "4d068d4ac378c9ede5fa"
  library: "6b1ea9adc2f4463d"
  function: "gtm"
---
# GTM launch session

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.gtm_launch": "4d068d4ac378c9ede5fa@6b1ea9adc2f4463d"}})`

Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing segments (use `cady-gtm-offer-and-segments`) or drafting outreach.

## Gtm launch

- **Job:** From the company context and the user's outbound request, prepare the complete internal motion in one session. A missing sender, provider or scheduler blocks activation only, never internal preparation.
- **Rule:** A prepared review is not approval or delivery. A live claim and matching skill are required at prepare and release. Approval and release follow outreach_release in `../../references/outreach-message-rules.md`; never invent user assent or present a quote of the user as approval. Record prepared, authorized, released and executor-sent states distinctly, and reconcile uncertain effects before retrying.

### Steps

- 1. Read get_cady_context with the area you are working in (omit it for the map) and get_company_work. If no work item fits, create one with submit_company_work_checkpoint using a new workId, expectedRevision null and a current methodId. Keep company priorities in direction through update_company_direction; goals are goal work items. Split substantial independent channel/cohort work only within host and plan limits.
- 2. State each channel's audience, offer, proof, stop and review condition. Verify the sending account and its executor (Cady's server for API channels, the local cady executor for the rest) before treating a channel as operational; missing access holds that channel while independent work continues.
- 3. If the CRM of record is undecided, apply the first-use rule from get_cady_context (company.modules): check the tools you can access, record external or native with company.modules.set, and ask the sponsor only if you cannot look. Do not hold work for it; no unsupported CRM readiness read is implied.
- 4. During sourcing, persist eligible source-backed identities in the selected CRM before preparing outreach. For Cady CRM use the existing reviewed identity/List import, receipt, recovery and membership readback in the tam-map import reference (`../../references/tam-map-import.md`); keep a selected external CRM canonical. Report researched candidates, saved/matched parties and List members separately, plus any shortfall. Unknown contact basis holds contact, not otherwise eligible identity persistence; prepare no send without the existing permission, review and release authority.
- 5. Prepare one crm.prepare_outreach_review per eligible cohort of at most 50 parties, under a live Projects claim and a matching skill for its channel. Read crm.get_outreach_review and report the approvalId. Approve and release only as outreach_release in `../../references/outreach-message-rules.md` says (send nothing unapproved), and never ask for addresses, bodies or credentials.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.
