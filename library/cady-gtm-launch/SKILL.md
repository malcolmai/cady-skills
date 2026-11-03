---
name: "cady-gtm-launch"
description: "GTM launch session. Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing segments (use `cady-gtm-offer-and-segments`) or drafting outreach."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.gtm_launch"
  version: "742aba93d304fc21cdcc"
  library: "ac5b4239e832e8db"
  function: "gtm"
---
# GTM launch session

**Point:** Prepare a whole outbound motion in one session, so only activation waits on access or approval.

**Company context:** `context_read({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.gtm_launch": "742aba93d304fc21cdcc@ac5b4239e832e8db"}})`

Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing segments (use `cady-gtm-offer-and-segments`) or drafting outreach.

## Bets

- Prepare every channel's audience, offer, proof and stop condition even when sending access is missing; hold only activation. Instead of: Pause the launch until the sender, provider or scheduler is connected.
- Save sourced identities in the system of record before drafting, and report researched, saved and listed counts separately. Instead of: Draft outreach from research notes and report one total of prospects found.
- Keep prepared, approved, released and sent as distinct states; never read a prepared review or a quote of the user as approval. Instead of: Mark the launch done once reviews are prepared, or take the user's enthusiasm as the go-ahead.

## Gtm launch

- **Job:** From the company context and the user's outbound request, prepare the complete internal motion in one session. A missing sender, provider or scheduler blocks activation only, never internal preparation.
- **Rule:** A prepared review is not approval or delivery. A live claim and matching skill are required at prepare and release. Approval and release follow `../../references/outreach-release.md`, release; never invent user assent or present a quote of the user as approval. Record prepared, authorized, released and executor-sent states distinctly, and reconcile uncertain effects before retrying.

### Steps

- 1. Read context_read with the area you are working in (omit it for the map) and work_read. If no work item fits, create one with work_create, letting the server mint the workId, with a current methodId. Keep company priorities in direction through update_company_direction; goals are goal work items. Split substantial independent channel/cohort work only within host and plan limits.
- 2. State each channel's audience, offer, proof, stop and review condition. Verify the sending account and its executor (Cady's server for API channels, the local cady executor for the rest) before treating a channel as operational; missing access holds that channel while independent work continues.
- 3. If the CRM of record is undecided, apply the first-use rule from context_read (company.modules): check the tools you can access, record external or native with company.modules.set, and ask the sponsor only if you cannot look. Do not hold work for it; no unsupported CRM readiness read is implied.
- 4. During sourcing, persist eligible source-backed identities in the selected CRM before preparing outreach. For Cady CRM use the existing reviewed identity/List import, receipt, recovery and membership readback in the tam-map import reference (`../../references/tam-map-import.md`); keep a selected external CRM canonical. Report researched candidates, saved/matched parties and List members separately, plus any shortfall. Unknown contact basis holds contact, not otherwise eligible identity persistence; prepare no send without the existing permission, review and release authority.
- 5. Prepare one crm_outreach_review_prepare per eligible cohort of at most 50 parties, under a live Projects claim and a matching skill for its channel. Read the review with records_read review:outreach/<approvalId> and report the approvalId. Approve and release only as `../../references/outreach-release.md`, release says (send nothing unapproved), and never ask for addresses, bodies or credentials.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.
