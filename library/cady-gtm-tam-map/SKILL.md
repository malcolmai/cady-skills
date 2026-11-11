---
name: "cady-gtm-tam-map"
description: "TAM map. Use when: Find who wants, where they gather: people, communities, prospects, leads, target customers, companies or accounts. Not for: Trigger-only lists or preparing messages; use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message` for outreach."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.tam_map"
  version: "96f369b0201114d9cc66"
  library: "24d354b05663abe0"
  function: "gtm"
---
# TAM map

**Point:** Find people who clearly fit a persona; prefer several narrow personas over one broad, weakly fitting offer.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Gate on clear fit to the persona; sourced signs of its trigger only rank. Instead of: Rank accounts by how much can be sourced about them or by firmographic match.
- Prefer several narrow personas, even overlapping, to one broad list with a weakly fitting offer. Instead of: Build one large list to maximise reach.
- Source a short list by hand; for a long one, check a few identities by hand across sources before building a collector. Instead of: Scrape or buy a large list first and clean it afterwards.
- A name you cannot source stays out of the CRM, and a field you cannot source stays 'unknown'. Instead of: Fill the list from general knowledge and guessed addresses.
- Identity evidence, CRM membership, contact permission and send approval are separate facts. Instead of: Treat a sourced identity, CRM membership, contact basis and review approval as one permission.
- Give each candidate a one-line reason for inclusion or exclusion. Instead of: Exclude or include candidates without explaining the decision.

Find who wants, where they gather: people, communities, prospects, leads, target customers, companies or accounts.

**Not for:** Trigger-only lists or preparing messages; use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message` for outreach.

**Unit of work:** one work item per persona; the work creates its List (step 6), then enriches it and records bases (step 7). **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- core:direction ref
- source refs

### Work fields

- ICP key
- persona
- geography and source scope
- planning N and identity type (people or organisations)
- source and channel coverage; List membership acceptance

## Procedure

1. Read cady_read company:direction and CRM Lists with crm_read mode lists. Use the accepted ICP or current persona assumption, and drop accounts its disqualifiers exclude. Every prospect must clearly fit the persona. Prefer several narrow personas (they may overlap when prospecting) to one broad persona with a weakly fitting offer. Fit to the persona gates; sourced signs of its trigger (`cady-gtm-persona-profile` part 4) rank. Recorded customer evidence or a current company decision governs breadth. Before sourcing, reuse or update this work item's brief and brief.doneWhen with the GTM owner's planning N, identity type (people or organisations), source and channel coverage, deduplication, import completion receipt, actual List membership readback and honest shortfall. For a first motion, 150-300 people is a sensible target, fewer for highly specialised industries. For an established motion, the more the better: cover as much of the market as you can. Keep it independent of mailbox setup, send quota, grant capacity and contact eligibility. Measures are evidence, never targets.
2. Build named identities toward the existing brief's planning N, counting its people or organisation identity type. For short lists (about 30-50 people or fewer), source by hand without automation. For longer lists, set the strategy, check a few named identities by hand across source types for fit, reachable routes and extraction reliability, then build a bounded, resumable collector with deduplication, saved failures and progress. Give each account its identity source (an http(s) URL, a Cady file as file:<fileId> or a Cady list as crm:list:<listId>), a named person or role with a reachable public route, and an explicit "unknown" for every field you cannot source. General knowledge is an assumption to source, not a list: a name you cannot source stays out of the CRM and goes in the sourcing plan. Give each account a one-line reason, in words, why it is in (fits the profile) or out, or mark it unknown. Distinguish sourced facts from inference; a row with an unconfirmed or stale role stays a Candidate without a fit reason, outside N and in the shortfall. For a people outcome, count individually sourced people, not organisations, roles or a directory's total members; report reachable people and unknown routes separately. N counts source-backed identities, independently of contact eligibility or send capacity; deduplicate before counting and do not pad to meet N. A shortfall against N first widens the sources and criteria within the persona and ICP, then reports; the report is an input to the goal call, not a stop.
3. With no way to look things up (no web search and no source files), the first result is the persona and sourcing plan: the criteria, where its names will come from and who will fetch them. It lists no company or person names. Report it as the work result and ask once for the sources or the owner's export, stating your default for everything else. The enrich reference holds the rest.
4. A community or institution you would approach is a sourced organisation party, typed community or institution; its staff are the contact point, and its members are reached only when each is individually reachable and permitted. The enrich reference holds the rest.
5. Check identity with crm_read or cady_read party:<partyId>. Use crm_set to record company_name, industry and approved customer proof where sourced. Read permission and engagement with cady_read party:<partyId>; record observed engagement with crm_interactions_set.
6. For sourced accounts, create the persona List with crm_lists_set (name) (purpose customer, or partner for a partner motion) and import them through the selected CRM's reviewed import (for Cady CRM, crm_lists_set preview (csv, mapping, kind) and status "prepared", then status "running", as the reviewed import reference says: `../../references/tam-map-import.md`). For new people, each row needs a real email, LinkedIn URL or namespaced external identity plus source; companies use domain or external identity. To group people already saved in Cady, map a CSV column to party_id with their returned partyId, optionally display_name, and ignore other columns; use the existing List as destinationListId through the same reviewed import. This adds membership only and grants no contact permission; preserve social destinations and source on the saved person. Names alone are refused. Read final completion with crm_read mode imports step "completion" and actual membership with crm_read; keep the completion receipt in evidenceRefs. If another CRM is selected, use its authorized reviewed route and keep it canonical. A sourced party enters as a Candidate. A Candidate is Reachable when it has a recorded basis with a source and one verified email and no opt-out, suppression or deferral (crm_read mode lists returns reachableCount). Add to pipeline (crm_interactions_set with where {listId}, motion, stage prospect and expectCount) makes the reachable Candidates Prospects; it skips the rest with reasons. Qualified is a later stage, after contact. When starting relationships, supply a known persona; leave unknown persona and unassigned Owner empty.
7. With the List and parties created and the import completion read, enrich the cohort (50 or fewer parties) from lawful sources only, verify emails (crm_set verifications), then decide each party's contact basis from target and jurisdiction and record it (crm_set basis). Where prior consent is needed or the jurisdiction is unknown, apply no basis: retain eligible identities and held review preparation, and record the release hold with its reason. Never overwrite an opt-out, suppression or existing basis; a basis is not send authority. The enrich reference holds the rules.
8. In the result summary, name each open assumption and how this result moves it. Report researched candidates, CRM parties created or matched, and actual List members separately, by the agreed identity type, with planning N, actual count, honest shortfall and source/channel coverage limits. Report reachable channels, unverified or unknown destinations, unknown basis and duplicates separately. Link the List and source evidence in the work result. Close with the import completion receipt (receipt:<receiptId>) in evidenceRefs; the List ref alone does not prove import completion or membership.

## Acceptance

- [ ] the existing brief and brief.doneWhen name planning N, people versus organisations, source and channel coverage, actual List membership readback and an honest shortfall; results use that identity unit
- [ ] each CRM party has a source or stated unknown; no party exists only from general knowledge or a name-only row
- [ ] when eligible sourced identities exist, the reviewed CRM import is complete and the actual List membership is read back with its completion receipt; report researched, parties saved/matched and members separately
- [ ] with no lookup route the result is a sourcing plan with no names
- [ ] contact basis is recorded or excluded with reason without invention; unknown basis holds release, not identity persistence or held review preparation
- [ ] existing opt-outs and suppressions remain untouched

## Owner checks

- CRM import completion
- source and fit evidence per candidate

## Result

### Artifact refs

- crm:list:<listId>

### Evidence refs

- receipt:<receiptId>
- **Transition:** the claim holder reports the map and coverage

## References
- Read [TAM map enrichment, no-lookup and community cases](../../references/tam-map-enrich.md) when you enrich the cohort and record contact bases, have no way to look things up, or approach a community or institution.
- Read [Reviewed CRM import](../../references/tam-map-import.md) when you save sourced accounts into a CRM List.
