---
name: "cady-finance-vendor-spend-review"
description: "Vendor spend review: new purchase or renewal. Use when: Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment. Not for: Bookkeeping, a finance ledger, payment, provider billing changes, supplier order execution or technical qualification; use `cady-finance-budget-review` for the current budget plan."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.finance.vendor_spend_review"
  version: "99e90755e89e5562fdc7"
  library: "f898539963d87619"
  function: "finance"
---
# Vendor spend review: new purchase or renewal

**Point:** Decide each purchase or renewal on full commitment against no-buy and cheaper workarounds, so money goes where use proves value.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Compare every purchase against no-buy, the existing tool and a cheaper workaround, listing the free or zero-incremental option first. Instead of: Compare paid vendors with each other and pick the best value among them.
- Price the full-term commitment and when the cash leaves (setup, minimums, overages, prepay, escalation, notice) beside the annualized run-rate. Instead of: Compare headline monthly prices.
- Decide a renewal on actual use (active seats, usage against tier) inside its notice window. Instead of: Renew by default while the tool is still in use somewhere.
- Reuse a current value review when need, vendor, terms and usage are unchanged; a small covered request gets a scope and limit check. Instead of: Run a fresh vendor study for every request.

Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment.

**Not for:** Bookkeeping, a finance ledger, payment, provider billing changes, supplier order execution or technical qualification; use `cady-finance-budget-review` for the current budget plan.

**Unit of work:** one work item per vendor and plan or purchase decision. **Kind:** strategy. **Parallel:** yes. 

## Inputs

### Evidence refs

- crm:party:<vendorPartyId>
- dated contract, invoice, message or File refs
- current company need and Finance plan
- dated offers, terms, usage and existing-tool evidence

### Work fields

- vendor and plan
- review horizon
- decision sought
- outcome sought
- decision date and useful life
- requesting owner and proposed vendor

## Procedure

1. Name the decision: a new purchase, or a renewal, trial end or cancellation. Keep a shortlist of several vendors as a List created with purpose vendor and mark each chosen or rejected with crm_set (fit or excluded) and a reason; a vendor List never starts a pipeline. Follow the matching reference (`references/vendor-purchase.md` or `references/vendor-renewal.md`) for evidence, comparison and commitment. Route provider capability, security, access and credential fit to Integrations or the relevant owner. Reuse a current value review for unchanged need, vendor, terms and usage; a small covered request needs a scope/limit check, not another vendor study.
2. Keep cost views distinct: annualized run-rate, full-term commitment and period cash timing. Unknown amount is not zero; annual equivalent is not booked spend; a register line is evidence, not a reservation.
3. Continue authorized research and preparation. For any dependent paid effect without an applicable verified scoped user grant and permitted executor, checkpoint a BLOCKED Projects item with exact vendor, amount, currency, term, decision owner, terms and next action. A future delegated envelope needs owner-enforced limits, reservation, expiry and receipt; do not claim it exists now. Reuse unchanged valid exact authority without another ask. No cancellation is sent and no money is reserved from this skill. When the commitment is a contract with a term (annual software, an agency, a lease), its terms go through `cady-company-operations-contract-checks` (vendor commitment); this skill judges value.
4. Report the recommendation or register and dated next action with work_set after CRM and work readback. A sent notice is not vendor acknowledgement; an acknowledged future effective end is not ended service. Keep work open for dated outcome evidence.

## Acceptance

- [ ] one justified recommendation and a credible cheaper or no-buy alternative
- [ ] full commitment, annualized cost and cash timing are distinct
- [ ] unsupported spend is held with an exact handoff
- [ ] the vendor party and renewal are read back
- [ ] a linked commitment has fields, dates and unknowns
- [ ] notice work is dated and cancellation remains unsent

## Owner checks

- dated price and term sources
- current entitlement and applicable executor authority
- separate provider/access/security checks
- no payment or contract effect from advisory method
- CRM provider role and renewal receipt
- dated evidence and notice recheck
- exact user review before any cancellation effect

## Result

### Artifact refs

- company:work:<workId>
- crm:party:<vendorPartyId>
- **Transition:** decision recommendation or blocked exact authority handoff

## References
- Read [New purchase review](references/vendor-purchase.md) when you decide a new paid tool or vendor purchase.
- Read [Renewal, trial or cancellation](references/vendor-renewal.md) when you decide a renewal, trial end or cancellation.
