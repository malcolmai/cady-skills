---
name: "cady-gtm-launch"
description: "GTM launch session. Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing a persona (use `cady-gtm-offer-and-segments`) or drafting outreach."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "execution.topic.gtm_launch"
  version: "cff25a4a7a14900f6a66"
  library: "b8e4e55055bf97b5"
  function: "gtm"
---
# GTM launch session

**Point:** Prepare a whole outbound motion in one session, so only activation waits on access or approval.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

Prepare a coordinated go-to-market launch from strategy through approved work. Use when: the company is starting a growth motion. Not for: choosing a persona (use `cady-gtm-offer-and-segments`) or drafting outreach.

## Bets

- Prepare every channel's audience, offer, proof and stop condition even when sending access is missing; hold only activation. Instead of: Pause the launch until the sender, provider or scheduler is connected.
- Save sourced identities in the system of record before drafting, and report researched, saved and listed counts separately. Instead of: Draft outreach from research notes and report one total of prospects found.
- Keep prepared, approved, released and sent as distinct states; never read a prepared review or a quote of the user as approval. Instead of: Mark the launch done once reviews are prepared, or take the user's enthusiasm as the go-ahead.

## Gtm launch

- **Job:** From the company context and the user's outbound request, prepare the complete internal motion in one session. A missing sender, provider or scheduler blocks activation only, never internal preparation.
- **References:** Channel plays and execution briefs: `cady-gtm-channel-plan`; reviewed List import: `references/tam-map-import.md`; approval and release: `references/outreach-release.md`, Release.
- **Rule:** A prepared review is not approval or delivery. Work not bound to a go-to-market skill needs motion to prepare; never invent user assent or present a quote of the user as approval. Record prepared, authorized, released and executor-sent states distinctly, and reconcile uncertain effects before retrying.

### Steps

- 1. Start with cady_start {task: your request, verbatim; agentId if you have one}; then act on its `do`; read more only for what it names and the task needs. If no work item fits, create one with work_set {kind: task, headline, next, path: its node, brief}; the server mints the id and takes the method from the path. Keep company priorities as goal work items; strategy goes on the tree with decisions_set. Split substantial independent channel/cohort work only within host and plan limits.
- 2. Settle the CRM of record before planning channels. If undecided, apply the first-use rule from cady_read company:modules: check the tools you can access, note an external tool in AGENTS.md or choose Cady's with company_setup, and ask the sponsor only if you cannot look. Do not hold work for it; no unsupported CRM readiness read is implied.
- 3. Use the channel plan from the References line for each chosen channel’s play, execution agent and operational readiness.
- 4. During sourcing, persist eligible source-backed identities in the selected CRM before preparing customer outreach. Use the reviewed List import from the References line for Cady CRM; keep a selected external CRM canonical. Report researched candidates, saved/matched parties and List members separately, plus any shortfall.
- 5. Prepare one review with crm_outreach (no id) per eligible cohort of at most 50 parties. Read the review with cady_read review:outreach/<approvalId> and report the approvalId. Follow the References line for approval and release, send nothing unapproved, and never ask for addresses, bodies or credentials.

## Shared execution sections

Read these sections of `cady-core-execution`: Execution guidance.
