---
name: "cady-accounting-period-close"
description: "Month-end and period close. Use when: Run a month, quarter or year-end close checklist in the company's own ledger and hand exceptions to its bookkeeper. Not for: Preparing a tax return (use `cady-finance-tax-cycle`), budgets or runway, posting entries or locking the ledger without its owner, or audit sign-off."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.accounting.period_close"
  version: "985977da666ba2b8b0a470692e1ba778f910a8c78cc13d51236bc64b1dfdf1f9"
  function: "accounting"
---
# Month-end and period close

Run a month, quarter or year-end close checklist in the company's own ledger and hand exceptions to its bookkeeper.

**Not for:** Preparing a tax return (use `cady-finance-tax-cycle`), budgets or runway, posting entries or locking the ledger without its owner, or audit sign-off.

**Unit of work:** one entity and accounting period. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Always

- Reconcile to the statement, not the bank feed; missing access is unknown, never a zero balance.
- Revenue follows delivery: prepaid annual cash is deferred, processor payouts are grossed up for fees.

## Inputs

### Evidence refs

- the company's ledger for the period
- bank, card, payment processor, payroll, invoice and bill sources

### Statement fields

- entity, period and accounting basis (cash or accrual)
- ledger, preparer and reviewer
- materiality amount and close deadline

## Procedure

1. Scope. Name the entity, period, basis, the ledger the company already uses and who prepares, reviews and locks. Agree a materiality amount with the reviewer (default: about 1% of monthly expenses); always investigate anything unexplained in cash, tax or payroll accounts regardless of size. Default deadline: month-end closed by business day 10. Quarter and year-end add the deeper items marked below. Books stay in that ledger; Cady keeps the checklist, exceptions and receipts.
2. Cash first. Reconcile every bank, card, payment processor and payroll clearing account to the statement closing balance, not to the bank feed. Gross up processor payouts into sales, fees, refunds and chargebacks. Investigate reconciling items older than 30 days. Clear uncategorised and suspense to zero or list each item.
3. Revenue and receivables. Every delivered or billable item is invoiced; the receivables aging ties to the ledger balance; review anything over 90 days for credit notes or a doubtful debt provision. Recognise revenue when delivered, not when billed or paid: an annual subscription paid upfront goes to deferred revenue and releases monthly; signed but undelivered work is not revenue. Usage and milestone billing follow the contract.
4. Payables, accruals and prepayments. Bills received are entered and the payables aging ties. Accrue services received but not billed (contractors, legal, hosting usage, commissions) and reverse last period's accruals. Annual software, insurance and deposits sit in prepayments and amortise; the schedule ties to the balance.
5. Payroll. The payroll register ties to wage expense and to each liability (net pay, employer taxes, pension and benefits); liabilities clear when remitted. Accrue unpaid bonuses and, where local practice requires, holiday pay. Contractor invoices are not payroll.
6. Balance sheet. Fixed assets over the capitalisation threshold are capitalised and depreciated; disposals removed. Sales tax or VAT accounts tie to the returns filed or due. SAFEs, notes and loans (including founder loans and interest) are recorded as the accountant's policy says, never as revenue. With more than one entity: intercompany balances agree on both sides in one currency, are settled or documented, and are eliminated on consolidation; intercompany charges go to the adviser for transfer pricing. Revalue foreign-currency balances at the period-end rate. Quarter and year-end: income tax provision with `cady-finance-tax-cycle`, equity roll-forward to the cap table, and a fixed asset count.
7. Flux review. Compare the P&L and balance sheet with last period and the budget; explain every line that moves more than 10% and more than the materiality amount. An unexplained move is an exception, not a pass.
8. Exceptions. Record one row per item: account; amount and currency; source ref; issue (unmatched, missing document, cut-off, misclassified, unexplained flux); proposed entry (debit and credit accounts); owner; due date; status. Put the list in Projects work for the bookkeeper with dueDate; do not post it.
9. Review and sign-off. Where staffed, the reviewer is not the preparer. The reviewer confirms every reconciliation ties, every exception has a disposition, flux is explained and the balance sheet accounts are reconciled, then signs off; the ledger owner locks the period. Report closed only after a ledger readback shows the lock and names the sign-off; otherwise report prepared, pending or blocked with the open exceptions.

## Acceptance

- [ ] every cash account is reconciled to its statement or listed as an exception
- [ ] receivables, payables, accruals, prepayments, payroll and deferred revenue tie to their schedules
- [ ] exceptions use the template with owner and due date
- [ ] the period is reported closed only with lock readback and sign-off

## Owner checks

- the company's ledger, period and lock owner
- reconciliations tie to statements
- preparer and reviewer recorded
- ledger lock readback before a closed claim

## Result

### Artifact refs

- company:work:<workId>
- ledger period lock receipt
- **Transition:** close checklist and exception handoff, or verified closed period

**Company context:** `get_cady_context({"area": "finance/plan", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.accounting.period_close": "985977da666ba2b8b0a470692e1ba778f910a8c78cc13d51236bc64b1dfdf1f9"}})`
