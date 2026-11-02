---
name: "cady-fundraise-investor-list"
description: "Ranked investor list. Use when: Decide who to pitch for a round: a ranked list of named investors and partners, sourced, with warm paths. Not for: Deciding whether, when or how much to raise (use `cady-fundraise-raise-plan`), drafting materials, setting terms or contacting investors."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.fundraise.investor_list"
  version: "726b17c310d8217ffe1e"
  library: "12d3967af31af210"
  function: "fundraise"
---
# Ranked investor list

**Point:** Rank real, sourced investors by fit and warmth, so founder time goes to those most likely to fund this round.

**Company context:** `context_read({"area": "gtm/prospecting", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.fundraise.investor_list": "726b17c310d8217ffe1e@12d3967af31af210"}})`

Decide who to pitch for a round: a ranked list of named investors and partners, sourced, with warm paths.

**Not for:** Deciding whether, when or how much to raise (use `cady-fundraise-raise-plan`), drafting materials, setting terms or contacting investors.

**Unit of work:** one work item per investor pool. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- company financing objective and milestone refs
- existing CRM investor parties or list refs

### Work fields

- round stage and target pool size
- stage, cheque, geography and thesis hypotheses

## Procedure

1. Read records_read company:direction and the exact financing objective, cash timing, milestone proof and founder constraints. Read or write the investor persona's profile (`cady-gtm-persona-profile`) for stage, cheque, geography and thesis (as hypotheses unless accepted); rank each investor's warmth separately; no active round does not create overdue outreach.
2. Canvass the founder's network and accessible relationship sources, then recent backers of comparable companies and directories. For each real firm, cite its public identity source; a generic thesis page is a proxy, not an activity trigger; never invent a firm, introduction or cheque.
3. Build the N named, reachable investors in this work item's acceptance criteria (default 10): for each, a named partner or role and a reachable public page, published address or role-level route; whether they lead or follow at this stage; their recent deals (dated, with a source, or a stated proxy); cheque fit; warm path; and unknown fields. Rank by likelihood times value (likelihood: fit, warmth and lead/follow; value: cheque size, ability to lead and help) and state the rule; stop when N meet this bar. Find a public, verifiable source first (registries, filings, directories, company sites); only when none can serve the N, ask the owner once for source access or a dataset as an access boundary with a ready packet; keep unresolved identities out of CRM.
4. Check crm_parties_read (mode "lists") for duplicates and create exact sourced identities with crm_parties_update or crm_parties_create mode "create", investor role set, receipts read back. Before any message preparation, persist eligible real identities into the selected CRM List (in Cady, created with purpose investor) through `cady-gtm-tam-map`'s reviewed import, completion receipt and membership readback; prepare is not import. Another selected CRM uses its authorized reviewed route and stays canonical. Start selected relationships with crm_tracks_set as `cady-gtm-tam-map` says: supply the persona; leave unknown persona and unassigned Owner empty.
5. Record ranked sources, gaps and next qualification step through work_change(action: 'checkpoint'), linked to any list and party refs; read back with work_read. Report completion or exact source-access shortfall with work_report. Report and close as `cady-gtm-tam-map` does (researched, saved/matched and member counts separately; import receipt in evidenceRefs). List membership grants no investor contact authority. Without a List, cite the shortfall's owner record.

## Acceptance

- [ ] a ranked investor cohort or sourced shortfall is visible
- [ ] each eligible source-backed identity is persisted in the selected CRM List with import completion and actual membership readback; report researched, saved/matched and member counts separately
- [ ] every listed party has fit, source, lead/follow status, a dated deal or proxy, warm path and its rank under the stated rule
- [ ] contact basis is distinct from identity persistence, and no investor is contacted

## Owner checks

- real identity and source per CRM party
- CRM create, role and import receipts

## Result

### Artifact refs

- crm:list:<listId>

### Evidence refs

- receipt:<receiptId>
- **Transition:** the claim holder reports the result
