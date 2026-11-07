---
name: "cady-gtm-launch"
description: "GTM launch session. Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing a persona (use `cady-gtm-offer-and-segments`) or drafting outreach."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.gtm_launch"
  version: "2a0d58f1b89e6c795542"
  library: "ab6c9b0d71690e90"
  function: "gtm"
---
# GTM launch session

**Point:** Prepare a whole outbound motion in one session, so only activation waits on access or approval.

**Company context:** `context_read({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"execution.topic.gtm_launch": "2a0d58f1b89e6c795542@ab6c9b0d71690e90"}})`

Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing a persona (use `cady-gtm-offer-and-segments`) or drafting outreach.

## Bets

- Prepare every channel's audience, offer, proof and stop condition even when sending access is missing; hold only activation. Instead of: Pause the launch until the sender, provider or scheduler is connected.
- Save sourced identities in the system of record before drafting, and report researched, saved and listed counts separately. Instead of: Draft outreach from research notes and report one total of prospects found.
- Keep prepared, approved, released and sent as distinct states; never read a prepared review or a quote of the user as approval. Instead of: Mark the launch done once reviews are prepared, or take the user's enthusiasm as the go-ahead.

## Gtm launch

- **Job:** From the company context and the user's outbound request, prepare the complete internal motion in one session. A missing sender, provider or scheduler blocks activation only, never internal preparation.
- **References:** Channel plays and execution briefs: `cady-gtm-channel-plan`; reviewed List import: `../../references/tam-map-import.md`; approval and release: `../../references/outreach-release.md`, Release.
- **Rule:** A prepared review is not approval or delivery. A live claim and matching skill are required at prepare and release; never invent user assent or present a quote of the user as approval. Record prepared, authorized, released and executor-sent states distinctly, and reconcile uncertain effects before retrying.

### Steps

- 1. Read context_read with the area you are working in (omit it for the map) and work_read. If no work item fits, create one with work_write or decisions_write or asks_write, letting the server mint the workId, with a current methodId. Keep company priorities in direction through update_company_direction; goals are goal work items. Split substantial independent channel/cohort work only within host and plan limits.
- 2. Settle the CRM of record before planning channels. If undecided, apply the first-use rule from context_read (company.modules): check the tools you can access, record external or native with company.modules.set, and ask the sponsor only if you cannot look. Do not hold work for it; no unsupported CRM readiness read is implied.
- 3. Use the channel plan from the References line for each chosen channel’s play, execution agent and operational readiness.
- 4. During sourcing, persist eligible source-backed identities in the selected CRM before preparing customer outreach. Use the reviewed List import from the References line for Cady CRM; keep a selected external CRM canonical. Report researched candidates, saved/matched parties and List members separately, plus any shortfall.
- 5. Prepare one crm_outreach_set kind message status review per eligible cohort of at most 50 parties. Read the review with records_read review:outreach/<approvalId> and report the approvalId. Follow the References line for approval and release, send nothing unapproved, and never ask for addresses, bodies or credentials.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.
