---
name: "cady-fundraise-investor-list"
description: "Ranked investor list. Use when: Decide who to pitch for a round: a ranked list of named investors and partners, sourced, with warm paths. Not for: Deciding whether, when or how much to raise (use `cady-fundraise-raise-plan`), drafting materials, setting terms or contacting investors."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.fundraise.investor_list"
  version: "aa94328b828f5c4f8242"
  library: "010d8211a6a994a9"
  function: "fundraise"
---
# Ranked investor list

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.fundraise.investor_list": "aa94328b828f5c4f8242@010d8211a6a994a9"}})`

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

1. Read read_cady company:direction and the exact financing objective, cash timing, milestone proof and founder constraints. State stage, cheque range, geography, thesis and warmth as hypotheses unless accepted; no active round does not create overdue outreach.
2. Canvass the founder's network and accessible relationship sources, then recent backers of comparable companies and directories. For each real firm, cite its public identity source; a generic thesis page is a proxy, not an activity trigger; never invent a firm, introduction or cheque.
3. Build the N named, reachable investors in this work item's acceptance criteria (default 10): for each, a named partner or role and a reachable public page, published address or role-level route; whether they lead or follow at this stage; their recent deals (dated, with a source, or a stated proxy); cheque fit; warm path; and unknown fields. Rank by likelihood times value (likelihood: fit, warmth and lead/follow; value: cheque size, ability to lead and help) and state the rule; stop when N meet this bar. Find a public, verifiable source first (registries, filings, directories, company sites); only when none can serve the N, ask the owner once for source access or a dataset as an access boundary with a ready packet; keep unresolved identities out of CRM.
4. Check crm.list_parties and its mode "lists" for duplicates. Create exact sourced CRM identities with crm.update_party mode "create" if needed; set investor role and read back receipts. Before any message preparation, persist eligible real identities into the selected CRM List. For Cady CRM, reuse `cady-gtm-tam-map` for the reviewed import, completion receipt and actual membership readback; prepare is not import. For another selected CRM, use its authorized reviewed route and keep it canonical.
5. Record ranked sources, gaps and next qualification step through transition_company_work(action: 'checkpoint'), linked to any list and party refs; read back with get_company_work. Report completion or exact source-access shortfall with report_company_work. Read back import completion and actual List membership using the canonical method; report researched investors, CRM parties saved/matched and List members separately. Unknown contact basis holds contact, not otherwise eligible identity persistence. List membership grants no investor contact authority. When a List was created, close with the import's receipt (receipt:<receiptId> from crm.run_import or the completion read) in evidenceRefs; the List ref alone does not let you accept. Otherwise cite the shortfall's owner record.

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
