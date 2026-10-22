---
name: "cady-gtm-tam-map"
description: "TAM map. Use when: Build a list of target companies or accounts to sell to (for a region, segment or ICP), sourced and reachable. Not for: Trigger-only lists or preparing messages; use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message` for outreach."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.tam_map"
  version: "51c78ce68ceaa1d2a37a6b73dcf8510ae2d1a22e6b30071526a594384eb5bf32"
  library: "b7c6052adb03e788"
  function: "gtm"
---
# TAM map

**Company context:** `get_cady_context({"area": "gtm/prospecting", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.tam_map": "51c78ce68ceaa1d2a37a6b73dcf8510ae2d1a22e6b30071526a594384eb5bf32"}})`

Build a list of target companies or accounts to sell to (for a region, segment or ICP), sourced and reachable.

**Not for:** Trigger-only lists or preparing messages; use `cady-gtm-cold-email-cycle` or `cady-gtm-linkedin-message` for outreach.

**Unit of work:** one work item per segment; the work creates its List (step 6), then enriches it and records bases (step 7). **Kind:** execution. **Parallel:** yes. **Can release:** no. 

See [Inputs](references/inputs.md).
## Procedure

1. Read get_company_direction and CRM Lists with crm.list_parties with mode "lists". Define the segment from the accepted ICP or current first-segment hypothesis, and drop accounts its disqualifiers exclude. Match breadth to conviction: while the ICP is a hypothesis with little customer evidence, keep discovery wide; intent, dated triggers and situations that suggest fit rank accounts, never gate them. Narrow only on recorded customer evidence or a current company decision, which governs.
2. Build named accounts toward N, the list target from plan_into_work in the gtm method unless this work item's acceptance names another number, from sources you can open: public, verifiable ones first (registries, filings, directories, company sites, web search), then the owner's files, Lists, CRM and connected stores. Give each account its identity source (an http(s) URL, a Cady file as file:<fileId> or a Cady list as crm:list:<listId>), a named person or role with a reachable public route, and an explicit "unknown" for every field you cannot source. General knowledge is a hypothesis to source, not a list: a name you cannot source stays out of the CRM and goes in the sourcing plan. Give each account a one-line reason it fits, with its source, or mark it unknown; distinguish sourced facts from inference. Source about 1.5-2x N so N remain eligible after attrition. Stop at N eligible accounts that meet this bar; do not pad. A shortfall against N first widens the segment, sources and criteria within the ICP and direction, then reports; the report is an input to the goal call, not a stop.
3. With no way to look things up (no web search and no source files), the first result is the segment decision plus a sourcing plan: the segments, the criteria, where each segment's names will come from (directories, registers, exports, the owner's contacts) and who will fetch them. It lists no company or person names. Report it as the work result and ask once for the sources or the owner's export as an access boundary with a ready packet, stating your default for everything else (for example the region) as a choice, not a question.
4. Check identity with crm.list_parties or crm.get_party. Use crm.update_party to record company_name, industry and approved customer proof where sourced. Read permission and engagement with crm.get_party; record observed engagement with crm.record_interactions.
5. For sourced accounts, create the segment List with crm.create_list and import them through the selected CRM's reviewed import (for Cady CRM, crm.get_import preview and prepare, then crm.run_import, as the reviewed import reference says: `../../references/tam-map-import.md`). Each row needs a real email, LinkedIn URL or domain plus source; names alone are refused. Read final completion with crm.get_import mode "completion" and actual membership with crm.list_parties; keep the completion receipt in evidenceRefs. If another CRM is selected, use its authorized reviewed route and keep it canonical.
6. With the List and parties created and the import completion read, enrich the cohort (50 or fewer parties) from lawful sources only: public company sites, registries, filings, professional directories, and connected provider tools within their terms. No scraping behind logins and no guessed addresses; verify a business route with an authorised tool or mark it unknown. Verify emails with the company's host verifier and record results with crm.update_party mode verification {provider, results [{identifier, verdict, evidenceRef?}]}; with no verifier, hand off only the verified or LinkedIn-reachable subset and report "verification unavailable" as the exact blocker for the rest, never guessing. Then decide each party's contact basis from target and jurisdiction and record it with crm.apply_contact_basis {basisKind, source (a cited https:, file: or crm:list: reference), partyIds (batches of up to 100) for the parties that qualify}; use listId only when every eligible party in the List qualifies. Business-role address and relevant B2B offer: legitimate_interest where the jurisdiction allows B2B marketing email. Where prior consent is needed (personal addresses, consent-first jurisdictions) apply no basis: record an exclusion with its reason in the work result exclusions (a crm.update_party fitNote also needs a cited source) or pick another channel. Apply no basis when the jurisdiction is unknown. Never overwrite an opt-out, suppression or existing basis. A basis is not send authority: the owner approves the exact outreach review before release.
7. In the final reply, name each open hypothesis and how this result moves it. Report researched candidates, CRM parties created or matched, and actual List members separately, with N, target shortfall and coverage limits. Unknown contact basis holds outreach only; persist every otherwise eligible source-backed identity. Link the List and source evidence in the work result. Close with the import completion receipt (receipt:<receiptId>) in evidenceRefs; the List ref alone does not prove import completion or membership.

## Acceptance

- [ ] the sourced accounts, toward N, each have an identity source and a reachable route or a stated unknown, or the exact shortfall is reported
- [ ] each CRM party has a source or stated unknown; no party exists only from general knowledge or a name-only row
- [ ] when eligible sourced identities exist, the reviewed CRM import is complete and the actual List membership is read back with its completion receipt; report researched, parties saved/matched and members separately
- [ ] with no lookup route the result is a sourcing plan with no names
- [ ] contact basis is recorded or excluded with reason before any outreach handoff; an unknown basis holds contact, not identity persistence
- [ ] existing opt-outs and suppressions remain untouched

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- CRM import completion
- source and fit evidence per candidate

## Result

### Artifact refs

- crm:list:<listId>

### Evidence refs

- receipt:<receiptId>
- **Transition:** the claim holder reports the map and coverage

## References
- [Reviewed CRM import](../../references/tam-map-import.md)
