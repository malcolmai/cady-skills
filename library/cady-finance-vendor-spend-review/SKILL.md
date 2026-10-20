---
name: "cady-finance-vendor-spend-review"
description: "Vendor spend review: new purchase or renewal. Use when: Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment. Not for: Bookkeeping, a finance ledger, payment, provider billing changes, supplier order execution or technical qualification; use `cady-finance-budget-review` for the current budget plan."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.finance.vendor_spend_review"
  version: "4a6670bf746d93b4b1ea6edac4ab5a3c32d7474b491375db3710c935e3c487db"
  library: "3beca7fa80e90672"
  function: "finance"
---
# Vendor spend review: new purchase or renewal

**Company context:** `get_cady_context({"area": "finance/plan", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.finance.vendor_spend_review": "4a6670bf746d93b4b1ea6edac4ab5a3c32d7474b491375db3710c935e3c487db"}})`

Decide whether to buy, trial, renew or cancel a paid tool or vendor: cost, actual use, alternatives and commitment.

**Not for:** Bookkeeping, a finance ledger, payment, provider billing changes, supplier order execution or technical qualification; use `cady-finance-budget-review` for the current budget plan.

**Unit of work:** one work item per vendor and plan or purchase decision. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- crm:party:<vendorPartyId>
- dated contract, invoice, message or File refs
- current company need and Finance plan
- dated offers, terms, usage and existing-tool evidence

### Statement fields

- vendor and plan
- review horizon
- decision sought
- outcome sought
- decision date and useful life
- requesting owner and proposed vendor

## Procedure

1. New purchase: establish the actual outcome, scale and constraint; ask what current tool, manual workaround or no-buy path can achieve it. Free alone is neither a business case nor permission to create an account. Route provider capability, security, access and credential fit to Integrations or the relevant owner. Reuse a current value review for unchanged need, vendor, terms and usage; a small covered request needs a scope/limit check, not another vendor study. Renewal, trial or cancellation: resolve one real CRM vendor party with crm.get_party or crm.list_parties. If needed, create it with crm.update_party with mode "create" and read it back. Read exact host terms and dated evidence, including Files text with files.read_text where applicable; do not copy payment credentials or full messages into Cady.
2. New purchase: compare the proposed vendor with one credible cheaper effective alternative and doing nothing or deferring. Check benefit and evidence at expected use, failure consequences, switching and maintenance burden, lock-in and exit; prefer the best justified net outcome, not the lowest sticker price. Renewal, trial or cancellation: record provider role and sourced renewal date on that party through crm.update_party with its current revision and read back crm.get_party. Keep one party-linked commitment per vendor and plan in Company Work with amount, currency, cadence, trial end, renewal date, notice period and notice date, auto-renew status, owner, evidence refs, confidence and explicit unknowns. Unknown amount is not zero; annual equivalent is not booked spend. Distinguish annualized run-rate, full-term commitment and period cash exposure; include seats, metering caps, tax or FX, trial conversion and exit cost when relevant. A register line is evidence, not a reservation.
3. New purchase: source the full commitment by currency and period: setup, seats, usage caps and overages, trial conversion, contract minimum, tax or FX where relevant, renewal escalation, cancellation/notice and exit. Distinguish annualized run-rate, full-term obligation and period cash timing. Renewal, trial or cancellation: calculate notice deadline from evidenced terms and renewal date, naming date uncertainty. Create a dated Company Work next action with submit_company_work_checkpoint, or update a claimed one with transition_company_work(action: 'checkpoint'), for a timely recheck; read back with get_company_work. Assess actual value and exit effects from a stated observation window, including rare critical use, before recommending cancellation. Compare realized benefit against the current solution and a credible cheaper effective workaround.
4. New purchase: check the current Finance plan, known commitments and actual authorization route. Recommend one option with rationale, the credible alternative, total cost and a dated revisit trigger. A budget draft, recommendation, role approvalLimits prose or free tier grants no spending, account, data or contract authority. For setup-session spend advice, give the free or zero-incremental option first, then the cheapest adequate paid option, then step-ups, each with its monthly cost beside the commitment. Rest a paid option's return only on existing or secured revenue, cited as revenueRef, never on projections; without it, recommend the adequate free option and say why, or say none is adequate and hold the cost as the owner's decision without a return claim. This is advice, not spending authority. Renewal, trial or cancellation: for cancellation prepare exact steps and an unsent proposal with sending account, recipient or portal route, subject, full notice body, attachments, deadline, effective date, savings and consequences. Recheck current terms, party, account and notice date immediately before presenting it. Show full proposal for exact user review and hold the external action; a standing outreach grant does not substitute for this review.
5. Continue authorized research and preparation. For any dependent paid effect without an applicable verified scoped user grant and permitted executor, checkpoint a BLOCKED Projects item with exact vendor, amount, currency, term, decision owner, terms and next action. A future delegated envelope needs owner-enforced limits, reservation, expiry and receipt; do not claim it exists now. Reuse unchanged valid exact authority without another ask. No cancellation is sent and no money is reserved from this skill.
6. Report the recommendation or register and dated next action with transition_company_work(action: 'report_result') after CRM and work readback. A sent notice is not vendor acknowledgement; an acknowledged future effective end is not ended service. Keep work open for dated outcome evidence.

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
- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- CRM provider role and renewal receipt
- dated evidence and notice recheck
- exact user review before any cancellation effect

## Result

### Artifact refs

- company:work:<workId>
- crm:party:<vendorPartyId>
- **Transition:** decision recommendation or blocked exact authority handoff
