---
name: "cady-company-operations-compliance-register"
description: "Compliance register and monthly filing review. Use when: What statutory and registry filings the company owes and when (annual returns, confirmation statements, state reports). Not for: Preparing one tax return (`cady-finance-tax-cycle`), submitting any filing or payment, or legal advice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company_operations.compliance_register"
  version: "bd9400c5e2efd6959a3e"
  library: "fceb362826942aaa"
  function: "company_operations"
---
# Compliance register and monthly filing review

**Point:** Know every filing the company owes and start each early enough, so no deadline becomes a penalty or lost standing.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Re-scan when an event changes the facts (a financing, new officers, a hire, a new state, a threshold crossed), not only on the calendar. Instead of: Keep last year's list of filings and check it once a year.
- Check every category for each entity and jurisdiction, and record each one that does not apply with its reason. Instead of: List the filings the founder already knows about, or the ones a quick search surfaces.
- Date the work at the preparation start, worked back from the deadline with buffer for its dependencies. Instead of: Track the legal due date as the deadline.
- Record what each filing means commercially: cost, how the late penalty escalates and what it knocks on (good standing, an exemption, the next filing). Instead of: Record only what is due and when.

What statutory and registry filings the company owes and when (annual returns, confirmation statements, state reports).

**Not for:** Preparing one tax return (`cady-finance-tax-cycle`), submitting any filing or payment, or legal advice.

**Unit of work:** one register review: every entity and jurisdiction, one decision record per requirement. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- CRM entity records
- the filing register (register-filing.md)
- official guidance and adviser evidence

### Work fields

- entities and jurisdictions in scope
- review period

## Procedure

1. Read the filing register (register-filing.md, requirement_register step 1) and any exact saved policy or contract that governs the requested filing question and each entity from its ops:entity decision lines (cady_read {search: {query: "ops:entity", kinds: ["decision"]}}, then decision:<subject> for each) and incorporation files. Read cady_read changes {since: the last register review, important: false} for events that create or change obligations: a financing or share issue, new officers, shareholders or addresses, hires and payroll, a new country or state, revenue or headcount crossing a threshold, a new regulated activity. A full pass (step 2 for every entity) runs when there is no filing register File yet or an entity, jurisdiction or event changed; otherwise review only what changed and the requirements past their reviewBy. A completed contract with no entry in register-contract.md goes to `cady-company-operations-contract-checks` (act).
2. For each entity and jurisdiction, check every category: registry annual and event filings, tax, securities and financing notices, foreign-investment and statistical reports, payroll and employment, mandatory insurance, sector licences, data-protection registration. Research each with requirement_register steps 2 and 3. You may run one research subagent per jurisdiction, each given the entity facts, the categories and those steps, returning dated sources and findings; you merge them. State each category that does not apply, with the reason.
3. For each applicable requirement, record how to file: the authority, portal or form, who may sign and file, the credentials needed (never stored in Cady) and the fee. Record what it means commercially: the cost, the late penalty and how it escalates, and the effect on other obligations (accounts before tax, a notice tied to the next close, good standing, loss of an exemption). Work back from the deadline to a preparation start with buffer.
4. Check and record each new or changed requirement with requirement_register steps 4 and 5. Give the checker the common mistakes: wrong entity or period, a missed trigger, a misread exemption, the wrong clock. Name the entry <jurisdiction>-<authority>-<obligation> in register-filing.md (illustrative: <country>-<registry>-annual-return): the obligation and the entity in one short sentence, then jurisdiction, authority, the due date or rule, exemptions considered, how to file and the implications. Set reviewBy at the preparation start, sooner if the rule or the facts it depends on are likely to change, and tomorrow if the start has passed.
5. Each upcoming occurrence is Projects work with due at the preparation start and brief.dependsOn for evidence, review and the filer; reuse existing work. Create it with work_write {kind: task, path: operations} (the method comes from the path), so Ops Deadlines lists the work and marks it overdue. Tax returns follow `cady-finance-tax-cycle`, one return-period each. Agents submit no government filing or payment: set the step blocked for the person or adviser who files (work_write {id, status: blocked, next}), raise an ask alone (asks_write, kind "send", readyRefs citing the step), and verify filed or paid only from the authority's receipt.
6. Close by updating register-filing.md (files_set mode patch). It lists the entities, jurisdictions and categories covered, the changes found and the open questions, with a review date at most a month away, and the next register task (work_write {kind: task, path: operations, due, evidenceRefs: [the register's fil-<n>]}) due then. Report each requirement's state (settled, assumption or with a specialist), its next due date and the pending action.

## Acceptance

- [ ] on a full pass, every entity and jurisdiction has each category checked; otherwise every change and every requirement past its reviewBy is rechecked, with applicable requirements recorded and the rest stated as not applicable with the reason
- [ ] each requirement record carries authority, due rule, exemptions considered, how to file, implications, dated sources, check findings and reviewBy
- [ ] each upcoming occurrence is dated Projects work on Ops Deadlines
- [ ] register-filing.md is updated with a review date at most a month away

## Owner checks

- exact CRM entity
- official or qualified source for each requirement
- kind decision only with recorded independent-check findings
- filing and payment states only from authority receipts

## Result

### Artifact refs

- company:work:<workId>
- crm:entity:<entityId>
- **Transition:** reviewed filing register with dated next review

## References
- Apply `cady-company-operations-requirement-register` (`../cady-company-operations-requirement-register/SKILL.md`) when you research or record one requirement's rule, exemptions and sources.
