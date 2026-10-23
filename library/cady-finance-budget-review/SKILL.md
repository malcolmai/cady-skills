---
name: "cady-finance-budget-review"
description: "Budget and cash review. Use when: Draft or update a budget, spend allocation or decision forecast sized to the company's stage and obligations. Not for: Burn, runway and when to cut, posting ledger entries, reserving money or authorizing payment; use `cady-accounting-method` for close work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.finance.budget_review"
  version: "883dae95b36454305ddbcd0b02663df66e654b8fd9d051a994cdeee9e4eb5c06"
  library: "d9d01922e6210604"
  function: "finance"
---
# Budget and cash review

**Company context:** `get_cady_context({"area": "finance/plan", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.finance.budget_review": "883dae95b36454305ddbcd0b02663df66e654b8fd9d051a994cdeee9e4eb5c06"}})`

Draft or update a budget, spend allocation or decision forecast sized to the company's stage and obligations.

**Not for:** Burn, runway and when to cut, posting ledger entries, reserving money or authorizing payment; use `cady-accounting-method` for close work.

**Unit of work:** one decision horizon and current Finance plan. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Inputs

### Evidence refs

- current Finance plan and source file
- dated cash, ledger, receivable and obligation sources where available

### Statement fields

- decision and horizon
- company scale and material drivers
- currency and source freshness

## Procedure

1. Read current company direction and the current finance plan owner read. Choose planning depth from the company stage, business model, cash pressure and actual obligations; a small company need not maintain a corporate FP&A process. Identify the decision the budget must support and the few drivers that change it.
2. Reconcile dated observed cash and actuals from the chosen sources with committed obligations, any independently evidenced reservations and forecast flows. Keep those four categories distinct; missing records mean unknown coverage, never zero spend or available balance. Identify currency, period, tax and timing differences before adding figures.
3. Draft a baseline with explicit driver assumptions and material upside/downside or timing sensitivity. Include collections, payments, inventory, payroll, tax or capital only when relevant. Take cash, burn and runway from `cady-finance-runway` rather than recomputing them; state what would change the decision.
4. Recommend a proportionate allocation, stop/review trigger and owner. Attach a plan file only if one exists. Keep exact evidence refs in the company's chosen records. If authorized, update through the authorized finance plan owner write and read back the resulting plan. Omitted file, source, objective, allocation and horizon fields carry forward from the expected active revision; send null to remove the file, source or horizon, or an empty objective or allocation list to clear it, and inspect retained details on readback. A plan allocation is decision context, not a reservation or executable spending grant. Rest the return on any spend only on existing or secured revenue, never on projected revenue; forecasts stay scenarios.
5. Report the dated baseline, assumptions, unresolved sources, decision and next review trigger. Prepare independent follow-up in Projects; hold any dependent spend until an applicable current executor verifies exact scoped user authority or a future owner-enforced envelope.

## Acceptance

- [ ] a usable source-linked budget or plan update matches company scale
- [ ] actual, committed, reserved and forecast amounts remain distinct
- [ ] unknown coverage and next trigger are explicit

## Owner checks

- current Finance plan and company direction
- source dates and category separation
- plan readback
- spend authority belongs to an applicable current owner

## Result

### Artifact refs

- company:plan:finance_plan
- company:work:<workId>
- **Transition:** return a recommendation or verified plan update; spending remains separate
