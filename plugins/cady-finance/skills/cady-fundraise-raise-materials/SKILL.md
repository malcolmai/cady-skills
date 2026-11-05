---
name: "cady-fundraise-raise-materials"
description: "Raise materials, data room and investor updates. Use when: Draft or revise an investor memo, deck narrative, data room or monthly investor update for a founder. Not for: Deciding amount, instrument or terms (use `cady-fundraise-raise-plan`), choosing which investors to pitch, sending, or recording share issues."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.fundraise.raise_materials"
  version: "0d1dac85addaa12e9ceb"
  library: "25ca7976ab432995"
  function: "fundraise"
---
# Raise materials, data room and investor updates

**Point:** Make the investor case checkable, with one metric definition, dated sources and first objections answered, so diligence confirms it.

**Company context:** `context_read({"area": "fundraise/raise", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.fundraise.raise_materials": "0d1dac85addaa12e9ceb@25ca7976ab432995"}})`

**Bets** (where this differs from the default):
- Answer the target investor's first three objections in the draft with exact evidence, or name each as an open risk. Instead of: Write the strongest positive narrative and leave objections for the meeting.
- Define each metric once (MRR or ARR, bookings or revenue, retention basis) and use that definition in deck, model, data room and updates. Instead of: Use whichever metric looks strongest on each slide.
- Send the monthly update with the same metric rows every month and bad news early and plainly. Instead of: Report highlights and pick the metrics that look good this month.
- Have the data room ready before priced-round diligence, fixing gaps that stall a close (IP assignments, unapproved grants, cap table against register, 83(b)) first. Instead of: Assemble the data room after a term sheet arrives.

Draft or revise an investor memo, deck narrative, data room or monthly investor update for a founder.

**Not for:** Deciding amount, instrument or terms (use `cady-fundraise-raise-plan`), choosing which investors to pitch, sending, or recording share issues.

**Unit of work:** one work item per commissioned material or tightly coupled set. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- company direction, financing and traction source refs
- existing Files document refs

### Work fields

- requested material and audience
- period for an update
- decision and acceptance

## Procedure

1. Read records_read company:direction, existing work with work_read and exact source documents with files.read_text. Separate accepted facts, founder choices, bets, dated metrics, inferred claims and missing evidence. Ask only for a decision that changes the commissioned material.
2. Draft only the requested kind. A memo makes a checkable investor case; a deck narrative states each slide's question, claim, proof and limit. Keep internal choices distinct from investor-facing claims. Define each metric once and use it everywhere (MRR versus ARR, bookings versus revenue, logo versus net revenue retention, cohort start rule); investors check that the deck, model and data room agree. For cash and burn figures use `cady-finance-runway` and state each figure's basis (assumption or observed); name the plan file if one exists; Cady never classifies files. Then read it as the target investor would: the three objections they would raise first, each answered in the draft with its evidence (quotes exact) or named as an open risk, and how the round fits their thesis (stage, sector, check size) from their own record, labelled assumed where unsourced. Judge it with the taste check (../../references/taste-check.md, investor part) before review.
3. Monthly investor update, drafted for a fixed send day: subject with company, month and one-line headline; 1) highlights (2 to 3 wins with numbers); 2) metrics table, same rows every month (revenue or MRR, growth, customers, burn, runway months, cash); 3) lowlights and what you are doing about them; 4) asks, specific and actionable (an intro to a named role, a hire, a customer type); 5) thanks. Under 400 words; bad news early and plainly; never change a metric definition without saying so.
4. Data room, ready before priced-round diligence (lighter for a SAFE): incorporation and governing documents, board and shareholder consents; fully diluted cap table reconciled to the share register and every SAFE, note and option grant with its board approval; IP assignments from every founder, employee and contractor; key customer, supplier and financing contracts; monthly financials for the last 12 to 24 months and the model; metric definitions; team and option list; material filings and disputes. Common gaps that stall a close: a missing IP assignment, an unapproved option grant, a cap table that does not match the register, or no evidence that a US 83(b) election was filed in time (the deadline cannot be cured later).
5. Reconcile every material number and claim to an exact dated source. Make the narrative and export usable to its audience. Draft to people in your voice pack (`../../references/outreach-drafting.md`, sender_voice); do not create a separate voice card. Check placeholders, stale figures and unsupported traction.
6. Save the document through the host Files route using files_update or files_create with mode "begin", files_update or files_create with mode "validate" and files_update or files_create with mode "complete" where available. Give it a meaningful name and location, and relate its exact ref to this claimed work through work_write(action: 'checkpoint'); Cady does not classify documents. Read back with work_read and files.read_text when supported.
7. Report checked File refs, missing evidence and the next founder decision with work_write. A monthly update remains a draft until it is sent through `cady-fundraise-investor-outreach`.

## Acceptance

- [ ] (check) the requested document is usable and linked from work
- [ ] (check) material claims and metrics reconcile to source, date and one definition
- [ ] (fresh) a partner seeing it cold can say in two minutes what the company does, the evidence and the ask
- [ ] (person) the founder approves the document, and any update is explicitly unsent

## Owner checks

- source-linked claims and figures
- Files upload and work readback

## Result

### Artifact refs

- file:<fileId>
- company:work:<workId>
- **Transition:** the claim holder reports the result

## References
- Read [Taste check](../../references/taste-check.md) when judging a draft or design before review.
