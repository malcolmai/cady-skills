---
name: "cady-company-operations-compliance-register"
description: "Compliance register and monthly filing review. Use when: Find, verify and record statutory filing requirements, or run the monthly review for changes and upcoming filings. Not for: Preparing one tax return (`cady-finance-tax-cycle`), submitting any filing or payment, or legal advice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company_operations.compliance_register"
  version: "d199d4751e18e6e5b825d242e1d15b3667ba22d08adde57c96084184058ef9e1"
  function: "company_operations"
---
# Compliance register and monthly filing review

Find, verify and record statutory filing requirements, or run the monthly review for changes and upcoming filings.

**Not for:** Preparing one tax return (`cady-finance-tax-cycle`), submitting any filing or payment, or legal advice.

**Unit of work:** one register review: every entity and jurisdiction, one decision record per requirement. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- CRM entity records
- current filing: decisions
- official guidance and adviser evidence

### Statement fields

- entities and jurisdictions in scope
- review period

## Procedure

1. Claim this work item with transition_company_work(action: 'claim'); stop on CONFLICT. Read the current filing: decisions (requirement_register step 1) and each entity with crm.manage_company_records (action 'list', then 'get'). Read list_recent_changes since the last filing:register review for events that create or change obligations: a financing or share issue, new officers, shareholders or addresses, hires and payroll, a new country or state, revenue or headcount crossing a threshold, a new regulated activity.
2. For each entity and jurisdiction, check every category: registry annual and event filings, tax, securities and financing notices, foreign-investment and statistical reports, payroll and employment, sector licences, data-protection registration. Research each with requirement_register steps 2 and 3. You may run one research subagent per jurisdiction, each given the entity facts, the categories and those steps, returning dated sources and findings; you merge them. State each category that does not apply, with the reason.
3. For each applicable requirement, record how to file: the authority, portal or form, who may sign and file, the credentials needed (never stored in Cady) and the fee. Record what it means commercially: the cost, the late penalty and how it escalates, and the effect on other obligations (accounts before tax, a notice tied to the next close, good standing, loss of an exemption). Work back from the deadline to a preparation start with buffer.
4. Check and record each new or changed requirement with requirement_register steps 4 and 5. Give the checker the common mistakes: wrong entity or period, a missed trigger, a misread exemption, the wrong clock. Use subject filing:<jurisdiction>-<authority>-<obligation> (illustrative: filing:<country>-<registry>-annual-return). statement: the entity, jurisdiction, authority, and the due date or rule. rationale: exemptions considered, how to file and the implications. Set reviewBy no later than a month away or the preparation start, whichever is earlier, and tomorrow if the start has passed.
5. Each upcoming occurrence is Projects work with dueDate at the preparation start and dependsOn for evidence, review and the filer; reuse existing work. Create it with submit_company_work_checkpoint, with methodId and methodVersion copied from get_cady_context selectedMethod for company_operations (call it with function "company_operations" if yours differs), so Ops Deadlines lists the work and marks it overdue. Tax returns follow `cady-finance-tax-cycle`, one return-period each. Agents submit no government filing or payment: set the step BLOCKED for the person or adviser who files, raise an ask alone (kind "send", readyRefs citing the step), and verify filed or paid only from the authority's receipt.
6. Close with a filing:register decision whose decision.supersedes names the current filing:register workId, if any. It lists the entities, jurisdictions and categories covered, the changes found and the open questions, with reviewBy at most a month away. A filing: decision past its reviewBy shows on Needs you as a missed review, for its decider or, when an agent decided it, for owners and admins. Report each requirement's state (settled, hypothesis or with a specialist), its next due date and the pending action.

## Acceptance

- [ ] every entity and jurisdiction has each category checked, with applicable requirements recorded and the rest stated as not applicable with the reason
- [ ] each requirement record carries authority, due rule, exemptions considered, how to file, implications, dated sources, check findings and reviewBy
- [ ] each upcoming occurrence is dated Projects work on Ops Deadlines
- [ ] the filing:register decision is superseded with reviewBy at most a month away

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
- Apply `cady-company-operations-requirement-register` (`../cady-company-operations-requirement-register/SKILL.md`).

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company_operations.compliance_register": "d199d4751e18e6e5b825d242e1d15b3667ba22d08adde57c96084184058ef9e1"}})`
