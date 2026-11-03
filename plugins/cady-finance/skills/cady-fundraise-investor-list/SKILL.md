---
name: "cady-fundraise-investor-list"
description: "Ranked investor list. Use when: Decide who to pitch for a round: a ranked list of named investors and partners, sourced, with warm paths. Not for: Deciding whether, when or how much to raise (use `cady-fundraise-raise-plan`), drafting materials, setting terms or contacting investors."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.fundraise.investor_list"
  version: "e16e4008b0d34bfcc72a"
  library: "ae40c76cb73327f0"
  function: "fundraise"
---
# Ranked investor list

**Point:** Rank real investors by what they funded and can still fund, so founder time goes where a yes is likely.

**Company context:** `context_read({"area": "fundraise/raise", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.fundraise.investor_list": "e16e4008b0d34bfcc72a@ae40c76cb73327f0"}})`

**Bets** (where this differs from the default):
- Rank by deals actually made and capacity to invest now. Instead of: Rank by stated thesis fit and warm path.
- Show warmth in its own column; it orders only investors of similar fit. Instead of: Fold warm-intro strength into the fit score.
- Leave capacity as unknown when it is not public, and show the gap. Instead of: Infer capacity from fund size, brand or thesis to complete the row.
- Rank only investors that pass the eligibility judgement, each on a dated deal; put the rest on a watch list with the reason. Instead of: Rank everyone found and caveat the weak rows.

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

1. Read records_read company:direction and the exact financing objective, cash timing, milestone proof and founder constraints. Read or write the investor persona's profile (`cady-gtm-persona-profile`); its stage, cheque, geography and thesis are hypotheses unless accepted. Without an active round, no investor outreach is overdue.
2. Canvass the founder's network and accessible relationship sources, then recent backers of comparable companies and directories. For each real firm, cite its public identity source; a generic thesis page is a proxy, not an activity trigger; never invent a firm, introduction or cheque.
3. Build the N named, reachable investors in this work item's acceptance criteria (default 10): for each, a named partner or role and a reachable public page, published address or role-level route; whether they lead or follow at this stage; their recent deals (dated and sourced: stage, cheque, sector) or a stated proxy; whether they can still invest now (a fund's last raise and how far into it; an angel's source of wealth and recent activity); warm path; and unknown fields. Apply `cady-gtm-persona-profile`’s evidence judgement to eligibility and its figure check to every cited cheque, fund size and deal fact. Not eligible and never counted toward N: a fund with no dated deal in the last 12 months or no money left, a thesis found only in its own marketing, and anyone who sells services to founders or charges them to pitch. Rank by likelihood times value (likelihood: fit from what they did, capacity now and lead/follow; value: cheque size, ability to lead and help) and state the rule; Rank only eligible investors, each row naming the dated deal it rests on and its capacity evidence or 'unknown'; an ineligible investor goes to a watch list with its reason, because a ranked name is the one the founder approaches first. show warmth in its own column; it never enters the fit score and orders only investors of similar fit; stop when N meet this bar. Find a public, verifiable source first (registries, filings, directories, company sites); only when none can serve the N, ask the owner once for source access or a dataset as an access boundary with a ready packet; keep unresolved identities out of CRM.
4. Check crm_parties_read (mode "lists") for duplicates and create exact sourced identities with crm_parties_set or crm_parties_update mode "create", investor role set, receipts read back. Before any message preparation, persist eligible real identities into the selected CRM List (in Cady, created with purpose investor) through `cady-gtm-tam-map`'s reviewed import, completion receipt and membership readback; prepare is not import. Another selected CRM uses its authorized reviewed route and stays canonical. Start selected relationships with crm_tracks_set as `cady-gtm-tam-map` says: supply the persona; leave unknown persona and unassigned Owner empty.
5. Record ranked sources and gaps through work_write(action: 'checkpoint'), linked to any list and party refs; follow the reporting section of skill cady-core-run-sequence for the finish line; read back with work_read. Save the ranked page as the persona's Cady File with files_create, linked from the persona, and say where it was saved; never leave the list only in chat. Report completion or exact source-access shortfall with work_write. Report and close as `cady-gtm-tam-map` does (researched, saved/matched and member counts separately; import receipt in evidenceRefs). List membership grants no investor contact authority. Without a List, cite the shortfall's owner record.

## Acceptance

- [ ] a ranked investor cohort or sourced shortfall is visible
- [ ] each eligible source-backed identity is persisted in the selected CRM List with import completion and actual membership readback; report researched, saved/matched and member counts separately
- [ ] every listed party has fit from deals made, capacity now (or unknown), source, lead/follow status, a dated deal or proxy, warm path and its rank under the stated rule
- [ ] contact basis is distinct from identity persistence, and no investor is contacted
- [ ] the ranked page is saved as the persona's Cady File and linked from the persona

## Owner checks

- real identity and source per CRM party
- CRM create, role and import receipts

## Result

### Artifact refs

- crm:list:<listId>

### Evidence refs

- receipt:<receiptId>
- **Transition:** the claim holder reports the result
