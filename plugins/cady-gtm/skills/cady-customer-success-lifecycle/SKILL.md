---
name: "cady-customer-success-lifecycle"
description: "Customer lifecycle: first value to renewal. Use when: Run one customer account after the sale: onboarding to first value, health, risk, renewal, expansion or cancellation. Not for: Open deals before signature (`cady-sales-deal-motion`), the company's own vendor renewals (`cady-finance-vendor-spend-review`), or message copy alone (`cady-gtm-reply` or `cady-gtm-warm-email`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.customer_success.lifecycle"
  version: "305dc311b4c12a850797"
  library: "f2ab4ebd3a461f29"
  function: "customer_success"
---
# Customer lifecycle: first value to renewal

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.customer_success.lifecycle": "305dc311b4c12a850797@f2ab4ebd3a461f29"}})`

Run one customer account after the sale: onboarding to first value, health, risk, renewal, expansion or cancellation.

**Not for:** Open deals before signature (`cady-sales-deal-motion`), the company's own vendor renewals (`cady-finance-vendor-spend-review`), or message copy alone (`cady-gtm-reply` or `cady-gtm-warm-email`).

**Unit of work:** one work item per customer account and lifecycle moment. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- crm:party:<partyId>
- sales handoff file ref
- interaction and communication refs
- contract or plan dates

### Work fields

- first-value outcome and date
- renewal and notice dates
- lifecycle moment

## Procedure

1. Claim this work item with transition_company_work(action: 'claim') (the server fills attemptId and claimProof); on CONFLICT stop and report the holder.
2. Read the account: crm.get_party (role customer, renewalDate), its won track via crm.list_parties mode tracks, the sales handoff note with files.read_text, and interactions such as signup, activation, meeting and note. Missing evidence is unknown, not failure: ask before judging. Go to the moment the account is in.
3. Onboarding: at kickoff, restate the goal from the handoff so the customer does not repeat the sales conversation, then agree in their words the first value: the first observable result they bought for, such as a first report delivered or a first batch processed, and a date. Default 30 days for an assisted setup and 14 for self-serve. List the few setup steps with an owner each; clear your side's blockers first. Record crm.record_interactions kind activation when the result is observed, not when an account is created. Past the date without first value, the account is at risk however friendly the customer is.
4. Health: judge four dimensions separately, never as one score. Outcome: are they getting the result they bought? Adoption: the necessary use, by the right people, at the job's natural cadence. Relationship: champion present and engaged, sponsor known, sentiment in their words. Commercial: payment on time, usage or seats against the contract, renewal distance. Early risk signals: champion left or quiet, use missing for two natural cycles, a serious issue open over a week, a reorganisation, acquisition or budget cut, questions about export, terms or notice period, a failed payment.
5. At risk: within a week of a signal, name the one risk, its evidence and the likely cause. Speak to the customer directly with a specific question, not "just checking in". Agree a recovery plan: the outcome, steps each side owns and a check date, saved with files.put_text and set as the track's nextAction and nextActionDueAt. Own a delivery failure plainly: what happened, the fix and its date. Send product defects to the product owner with evidence. A discount does not fix a value problem. If their need changed or they have decided to leave, go to cancellation. Judge it with the taste check (../../references/taste-check.md, message part) before review.
6. Renewal: for an annual contract start 90 days before renewalDate (30 days for a monthly plan), or before the contract's notice deadline if that is earlier. At 90 days review outcomes delivered against the kickoff goal and open risks; at 60 hold the renewal conversation with value in their numbers and any price change, announced no later than the contract's notice period; at 30 complete the paperwork. Send every notice the contract or law requires with no promotion in it, on the lane message rules (lanes) give it, and never let an auto-renewal surprise the customer. Afterwards send crm.update_party role customer with the new renewalDate in its own call, and record the signed renewal with crm.record_interactions kind note (sourceRef the order or invoice ref, no document text).
7. Expansion: only once first value is reached and no risk is open. Real triggers are hitting a plan limit, another team asking, or a new use case the customer raised. Ask what result the expansion buys; when it needs a proposal, run it through `cady-sales-deal-motion`.
8. Cancellation: acknowledge the request the same day and ask once why. Make one save attempt only when a real remedy fits that reason (the fix with a date, a pause, a smaller plan, or terms the owner approved); offer nothing the owner has not approved. If they decline or repeat the decision, honour it by the date they asked: no extra steps, repeated calls or guilt. Confirm in writing the end date, final invoice, access and data export; the cancellation itself is made by the billing owner. Record the reason with crm.record_interactions kind note (no message body), when the contract ends send crm.update_party role other with renewalDate null so the account no longer counts as a customer, and set recontact 'unless_changed' unless they asked for a date. Cancelling is not an opt-out, and not consent to marketing either.
9. Every customer message goes through `cady-gtm-reply` or `cady-gtm-warm-email`; nothing sends from this skill. The same churn or risk reason across three or more accounts is a proposal to the product owner or `cady-gtm-offer-and-segments`. Report with report_company_work once records and files read back.

## Acceptance

- [ ] (check) first value is defined in the customer's words with a date, and activation is recorded only when observed
- [ ] (check) each health judgement names its evidence per dimension and its unknowns
- [ ] (check) an at-risk account has a recovery plan with owners and a check date
- [ ] (check) renewal work starts by 90 days or the notice deadline
- [ ] (check) a cancellation got at most one save attempt and was honoured by the requested date
- [ ] (fresh) a reader who sees only the account facts and the recovery plan or notice can say what happens next, who owns it and by when
- [ ] (person) the owner approved any retention offer, price change or notice before it reached the customer
- [ ] (check) nothing is sent from this skill

## Owner checks

- exact CRM party
- contract renewal and notice dates
- owner-approved retention offer
- Files readback
- contact permission before any message

## Result

### Artifact refs

- crm:party:<partyId>
- crm:relationship_track:<trackId>
- file:<fileId>
- company:work:<workId>
- **Transition:** the claim holder reports the account moment, its evidence and the next dated action

## References
- Read [Taste check](../../references/taste-check.md) when judging a draft or design before review.
