---
name: "cady-fundraise-raise-materials"
description: "Raise materials, data room and investor updates. Use when: Draft or revise an investor memo, deck narrative, data room or monthly investor update for a founder. Not for: Deciding amount, instrument or terms (use `cady-fundraise-raise-plan`), choosing which investors to pitch, sending, or recording share issues."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.fundraise.raise_materials"
  version: "67e3deb065442e361610"
  library: "fb0ed0826641a359"
  function: "fundraise"
---
# Raise materials, data room and investor updates

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.fundraise.raise_materials": "67e3deb065442e361610"}})`

Draft or revise an investor memo, deck narrative, data room or monthly investor update for a founder.

**Not for:** Deciding amount, instrument or terms (use `cady-fundraise-raise-plan`), choosing which investors to pitch, sending, or recording share issues.

**Unit of work:** one work item per commissioned material or tightly coupled set. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- company direction, financing and traction source refs
- existing Files document refs

### Statement fields

- requested material and audience
- period for an update
- decision and acceptance

## Procedure

1. Read read_cady company:direction, existing work with get_company_work and exact source documents with files.read_text. Separate accepted facts, founder choices, bets, dated metrics, inferred claims and missing evidence. Ask only for a decision that changes the commissioned material.
2. Draft only the requested kind. A memo makes a checkable investor case; a deck narrative states each slide's question, claim, proof and limit. Keep internal choices distinct from investor-facing claims. Define each metric once and use it everywhere (MRR versus ARR, bookings versus revenue, logo versus net revenue retention, cohort start rule); investors check that the deck, model and data room agree. For cash and burn figures use `cady-finance-runway` and state each figure's basis (assumption or observed); name the plan file if one exists; Cady never classifies files.
3. Monthly investor update, drafted for a fixed send day: subject with company, month and one-line headline; 1) highlights (2 to 3 wins with numbers); 2) metrics table, same rows every month (revenue or MRR, growth, customers, burn, runway months, cash); 3) lowlights and what you are doing about them; 4) asks, specific and actionable (an intro to a named role, a hire, a customer type); 5) thanks. Under 400 words; bad news early and plainly; never change a metric definition without saying so.
4. Data room, ready before priced-round diligence (lighter for a SAFE): incorporation and governing documents, board and shareholder consents; fully diluted cap table reconciled to the share register and every SAFE, note and option grant with its board approval; IP assignments from every founder, employee and contractor; key customer, supplier and financing contracts; monthly financials for the last 12 to 24 months and the model; metric definitions; team and option list; material filings and disputes. Common gaps that stall a close: a missing IP assignment, an unapproved option grant, a cap table that does not match the register, or no evidence that a US 83(b) election was filed in time (the deadline cannot be cured later).
5. Reconcile every material number and claim to an exact dated source. Make the narrative and export usable to its audience. Draft to people in your voice pack (message rules, sender_voice); do not create a separate voice card. Check placeholders, stale figures and unsupported traction.
6. Save the document through the host Files route using files.upload with mode "begin", files.upload with mode "validate" and files.upload with mode "complete" where available. Give it a meaningful name and location, and relate its exact ref to this claimed work through transition_company_work(action: 'checkpoint'); Cady does not classify documents. Read back with get_company_work and files.read_text when supported.
7. Report checked File refs, missing evidence and the next founder decision with report_company_work. A monthly update remains a draft until it is sent through `cady-fundraise-investor-outreach`.

## Acceptance

- [ ] the requested document is usable and linked from work
- [ ] material claims and metrics reconcile to source, date and one definition
- [ ] any update is explicitly unsent

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- source-linked claims and figures
- Files upload and work readback

## Result

### Artifact refs

- file:<fileId>
- company:work:<workId>
- **Transition:** the claim holder reports the result
