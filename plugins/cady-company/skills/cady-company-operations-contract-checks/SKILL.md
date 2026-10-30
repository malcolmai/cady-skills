---
name: "cady-company-operations-contract-checks"
description: "Contract checks: before signing, after completion. Use when: A contract that commits the company is about to be signed or was just signed: what to settle first and what it starts. Not for: Posts or updates about it, the yearly filing calendar (`cady-company-operations-compliance-register`), general legal questions, or a contract not yet in view."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company_operations.contract_checks"
  version: "021b82543d0671241eeb"
  library: "fe3f13ff23b3e9dc"
  function: "company_operations"
---
# Contract checks: before signing, after completion

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company_operations.contract_checks": "021b82543d0671241eeb@fe3f13ff23b3e9dc"}})`

A contract that commits the company is about to be signed or was just signed: what to settle first and what it starts.

**Not for:** Posts or updates about it, the yearly filing calendar (`cady-company-operations-compliance-register`), general legal questions, or a contract not yet in view.

**Unit of work:** one contract, one phase: plan before signing or act after completion. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Always

- Work from this company's facts, not a home jurisdiction: a rule you know from another country is a question to check, not an answer.
- Recommend the standard market form for that jurisdiction and stage, and why; a specialist only for a material, non-standard case.
- Recommend and prepare only: never file, sign, pay or send. Run once per contract and phase.

## Inputs

### Evidence refs

- entity records (crm.manage_company_records)
- the contract's terms or its existing work item
- current filing:, hr:, legal: and contract: decisions

### Work fields

- contract kind and counterparty
- phase, and the completion date once signed
- jurisdictions in scope

## Procedure

1. Name the contract and phase. Plan: terms are being agreed and nothing is signed (a term sheet, an offer, a statement of work, an order form). Act: it is signed, paid, issued or started, and that date starts the clocks. If neither is true, stop: there is nothing to check yet. Look up contract:<kind>:<ref> with get_company_work decisions {state: "current", subjectPrefix: "contract:"}; if it is current for this phase and the facts have not materially changed, use it and stop.
2. Name the jurisdictions in scope from the facts: the contracting entity and where it is registered (crm.manage_company_records action 'list', then 'get'), and where the counterparty, workers and customers are. If a counterparty's or worker's country is unknown, ask once as a BLOCKED item and continue with the jurisdictions you know.
3. Consider the points every contract shares, then the kind's own row (`../../references/contract-kinds.md`). Shared: who contracts and who may sign, with any board or shareholder approval; what the company gets (ownership of what is made, data and confidentiality); what it commits to (amount, term, renewal and notice, exit, liability); money and tax (payment terms, currency, tax where the work is done or the customer is); what completion starts (clocks, registrations, registers). Record the points that do not apply in one line in the decision record; report only the applicable ones to the owner.
4. Plan: for each point that applies, ask what gets harder or dearer to change after signing, and keep only those, usually one to five. For each: the choice, your recommended default, the credible alternative and what changing it later would cost. Add them to the contract's existing work item; a choice reserved to the founder becomes a BLOCKED decision with your recommendation.
5. Act: settle each applicable obligation with requirement_register steps 2 to 5, reusing a current filing:, hr: or legal: decision. Compute each deadline from the completion date as the authority states it, never from an illustration. If one is already passed or too close for the owner to act in time (about 30 days by default), tell the owner today (the date, the consequence and who must act) before anything else; if it has passed, say so and what late relief exists. If the completion date is unknown, ask for it first. Then create dated Projects work for each obligation with submit_company_work_checkpoint, with methodId and methodVersion from get_cady_context selectedMethod for company_operations: dueDate is the deadline minus a buffer, and dependsOn names the evidence and the filer. Elections, filings, signatures and payments are BLOCKED asks for the person who files; mark one done only from the authority's receipt.
6. Record a contract:<kind>:<ref> decision with submit_company_work_checkpoint (phase, jurisdictions, points checked and ruled out, the work created; supersede the plan record at act). Report the items that need someone else, soonest deadline first.

## Acceptance

- [ ] jurisdictions in scope are named from the company's facts
- [ ] the shared points and the kind's row were considered; only those that apply are reported
- [ ] plan: only choices that get costlier after signing, each with a default and an alternative
- [ ] act: each obligation is dated work citing its deadline source, any close or passed clock was raised today, and the agent filed, signed and paid nothing

## Owner checks

- exact contracting entity and jurisdictions from records
- deadlines from the authority, counted from the completion date
- filed, signed or paid only from the authority's receipt

## Result

### Artifact refs

- company:work:<workId>
- crm:entity:<entityId>
- **Transition:** contract:<kind>:<ref> decision with plan choices or dated obligations

## References
- Read [Contract kinds](../../references/contract-kinds.md) when the contract's kind may add points to the shared ones.
- Apply `cady-company-operations-requirement-register` (`../cady-company-operations-requirement-register/SKILL.md`) when you settle an obligation the contract starts.
