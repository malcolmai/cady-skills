---
name: "cady-finance-runway"
description: "Burn and runway. Use when: Work out burn, runway months and default alive or dead from actual cash, then decide when to cut and what first. Not for: Drafting a budget or allocation (use `cady-finance-budget-review`), deciding a raise (use `cady-fundraise-raise-plan`), approving spend or moving money."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.finance.runway"
  version: "e17e9e8f816d6c5432a4"
  library: "457f4d559b15c7f7"
  function: "finance"
---
# Burn and runway

**Company context:** `get_cady_context({"area": "finance/plan", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.finance.runway": "e17e9e8f816d6c5432a4@457f4d559b15c7f7"}})`

Work out burn, runway months and default alive or dead from actual cash, then decide when to cut and what first.

**Not for:** Drafting a budget or allocation (use `cady-finance-budget-review`), deciding a raise (use `cady-fundraise-raise-plan`), approving spend or moving money.

**Unit of work:** one company cash position at one as-of date. **Kind:** strategy. **Parallel:** no. **Can release:** no. 

## Always

- Unpaid receivables, unfunded commitments and collected sales tax are not cash.
- Burn comes from bank movements; annual prepayments, payroll and tax land in the month they are paid.

## Inputs

### Evidence refs

- bank, card and payment processor statements for the last 3 to 6 months
- payroll register, signed contracts, committed hires and known annual or quarterly bills

### Statement fields

- as-of date and reporting currency
- decision the runway figure informs

## Procedure

1. Objective. Answer one question for the person who decides spend and hiring: how long the cash lasts, whether the company is default alive, and if not when to cut and what first. A figure without its as-of date and source is not an answer; if cash cannot be tied to statements, say so and give a labelled estimate.
2. Cash. Read each bank and money market balance at one as-of date and convert at a stated rate. Cash is money in the bank, not: unpaid receivables, undrawn credit or venture debt (show as a separate line), signed but unfunded SAFEs or term sheets, restricted deposits, or sales tax and VAT collected but owed. Read read_cady finance:plan for the last recorded figures and their basis.
3. Burn from the bank, not the P&L. Gross burn is all cash out in a month: fully loaded payroll (employer taxes, pension, benefits), contractors, rent, software, hosting, cost of sales, interest. Net burn is gross burn minus cash collected (collections, not invoiced or booked revenue). Default trend: trailing 3-month average, with one-offs (raise legal fees, a deposit) removed and annual bills (insurance, annual software, audit) spread over 12 months for the trend only.
4. Forward view. When burn is changing, build a month-by-month cash table for 18 to 24 months instead of dividing once. Put each committed hire at its start month and loaded cost, each annual or quarterly bill in the month it is actually paid, payroll on its real dates (a month with three pay runs, bonuses, a 13th month), and tax payments on their due dates (VAT or sales tax remittance, payroll tax, corporate estimates). Collections follow actual payment terms and the receivables aging, not invoice dates.
5. Runway. Report two dates: cash at zero, and cash below a floor (default: 3 months of gross burn, enough to close a raise or wind down in order with payroll, notice and final taxes paid). Runway in months is to the floor unless the person asks for zero. A month with positive net cash flow does not end burn; keep the table running.
6. Scenarios, each with the same as-of cash. Base: committed spend and hires, collections at the trailing growth rate. Cut: the specific cuts in step 8 applied from next month, with notice and severance costs. Raise delay: the planned raise closes 6 months late, or not at all. For each, give the zero date, the floor date and the raise-start date (floor date minus 9 to 12 months: a raise usually takes 3 to 6 months to cash, plus slippage).
7. Default alive or dead. Hold expenses at the current plan and grow collections at the trailing 3-month month-on-month rate: if monthly collections reach monthly expenses before cash hits the floor, the company is default alive. State the growth rate that would be needed and how sensitive the answer is; a few points of monthly growth often flip it. For recurring revenue, also show the burn multiple (net burn divided by net new ARR over the same period; under 1 is efficient, above 2 needs a reason).
8. When to cut and what first. Cut when default dead with under 12 months to the floor and no credible raise path (term sheets in hand, not first meetings), or at once under 9 months. Cut once, deep enough to reach default alive or 18 months; repeated small cuts cost more trust than one clear one. Order: unused or duplicate software, agencies and contractors, unmeasured marketing, travel and events, office; then open and planned hires; then pay (founders first); headcount last. Protect what produces collections and the next milestone. Also pull cash forward: collect overdue receivables, offer annual prepay, renegotiate vendor terms. Route any people change to `cady-company-operations-people-lifecycle` for local employment rules.
9. Record and report. Report the as-of date, sources, cash, gross and net burn, both runway dates, the three scenarios, the alive or dead result and the next review trigger (default monthly, weekly under 6 months). If authorized, update the plan with manage_company_finance_plan (cashMinor, monthlyNetBurnMinor, asOf, currency, cashBasis and burnBasis observed only when tied to statements), then read it back with read_cady finance:plan. A cut list is a recommendation; any contract, payment or people effect stays with its owner.

## Acceptance

- [ ] cash, gross burn, net burn and both runway dates carry as-of date and source
- [ ] three scenarios with stated assumptions and a raise-start date
- [ ] default alive or dead with the growth rate it depends on
- [ ] any cut list is ordered, costed and marked as a recommendation

## Owner checks

- cash ties to bank statements at the as-of date
- net burn ties to bank outflows less collections
- finance plan readback when written

## Result

### Artifact refs

- company:plan:finance_plan
- **Transition:** return the runway view and recommendation; spending and people changes remain separate
