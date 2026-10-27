---
name: "cady-finance-tax-cycle"
description: "Entity tax and filing cycle. Use when: Plan or review an entity's tax obligations, filing preparation and material strategy changes. Not for: Filing, payment, legal advice, invented jurisdiction rules or a universal daily tax agent; use `cady-accounting-method` for period close."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.finance.tax_cycle"
  version: "a95c04c8dff83e289c19"
  library: "d0d7a4ecb1120309"
  function: "finance"
---
# Entity tax and filing cycle

**Company context:** `get_cady_context({"area": "finance/plan", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.finance.tax_cycle": "a95c04c8dff83e289c19@d0d7a4ecb1120309"}})`

Plan or review an entity's tax obligations, filing preparation and material strategy changes.

**Not for:** Filing, payment, legal advice, invented jurisdiction rules or a universal daily tax agent; use `cady-accounting-method` for period close.

**Unit of work:** one entity, return and period. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- CRM entity record
- current official obligation and adviser or provider evidence

### Statement fields

- entity and jurisdiction
- obligation and period
- filing and payment deadlines if applicable

## Procedure

1. Start from the entity's current filing: decisions (get_company_work with decisions {state: "current", subjectPrefix: "filing:"}; `cady-company-operations-compliance-register`) and the exact entity from crm.manage_company_records. Prepare one return-period. A missing requirement, or one past its reviewBy, goes back to the register; missing evidence is a question, not an exemption.
2. For each obligation and period, distinguish preparation, review, filing and payment. Source each filing and payment deadline separately; create or update Projects work with dueDate for preparation well ahead of the controlling deadline and dependsOn for evidence, review and submission dependencies. Use the existing Projects work rather than a second tax clock. Work backwards using preparation effort, reviewer availability and correction buffer; escalate lost slack before the statutory date. Reuse the existing entity-period close when several obligations need it.
3. Prepare source-linked figures, records and questions at the depth the obligation warrants. Identify who can sign, file and pay through the actual authority and provider route. A draft return or completed preparation is not a filed return or paid liability; verify those states only from their source receipts. A tax provision can change the accounts: reconcile adjustments with Accounting and recheck affected calculations and approvals against the revised accounts. Use follow-up work rather than a cyclic dependsOn chain.
4. Revisit tax strategy when a material change in entity, activity, location, revenue, funding or law could change the choice. Otherwise set the compliance cadence from applicable obligations and source freshness; use a specialist for material nonstandard interpretation or sign-off.
5. Report each entity-period status, source dates, preparation owner, separate deadline and exact pending action. Hold filing or payment when its checked executor or authority is absent while continuing independent preparation.

## Acceptance

- [ ] entity-period work has sourced obligations and dated dependencies
- [ ] preparation precedes separate filing and payment deadlines
- [ ] unverified effects remain pending

## Owner checks

- exact CRM entity
- official or qualified obligation source
- separate filing/payment due dates
- filing and payment receipts only from their owners

## Result

### Artifact refs

- company:work:<workId>
- crm:entity:<entityId>
- **Transition:** prepared obligation plan or qualified handoff
