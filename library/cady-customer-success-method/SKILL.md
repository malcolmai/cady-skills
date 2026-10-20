---
name: "cady-customer-success-method"
description: "Improve customer outcomes and manage retention through evidence-based recovery and follow-through. Use when: a customer needs onboarding, recovery, adoption or renewal support. Not for: judging a new deal (use `cady-sales-method`) or drafting outreach (use the relevant GTM outreach skill)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.customer_success"
  version: "715c54454eb52f60ef42a2781d624af7ffdb2d7c56b516e6aae8b13c175810ba"
  library: "3beca7fa80e90672"
  function: "customer_success"
---
# Customer Success

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.method.customer_success": "715c54454eb52f60ef42a2781d624af7ffdb2d7c56b516e6aae8b13c175810ba"}})`

Shared by every role card: `../../references/role-card-common.md`.

## Parent function
gtm

## Selected judgment
- Reconcile the promised outcome with adoption, unresolved delivery failure and retention evidence. Identify the owner of the failing step, recovery and verification. A support note or CRM reply is not a refund, shipment, fix or resolved customer outcome.

## Domain method

### Method

#### Frameworks

- **Avoid when:** Use proportionate reasoning, not a mandatory record schema, lifecycle, health score or industry checklist.
- **Decision:** Is value achieved? Diagnose onboarding friction, recovery or repeat-purchase gaps.
- **Evidence bar:** Separate observed outcomes, proxies and causal hypotheses. Check alternative explanations, timing, selection effects and external conditions before crediting or blaming an intervention. Bound cohort comparisons by relevant circumstances, exposure, denominator and observation window; preserve contrary evidence and unknowns. Seek additional evidence when it could change a consequential decision, not to complete fields. Existing evidence can justify direct action; a material single failure can warrant a correction without waiting for recurrence.

#### Execution

- Define: Establish desired progress in context, the expectation or commitment, and when value should be observable. Distinguish payer, beneficiary, operator and other affected participants only where their interests differ; make consequential tradeoffs and decision authority explicit. Preserve obligations and unacceptable harms. Successful one-off completion or readiness without frequent use may be the outcome; continued engagement is not inherently better.
- Observe: Compare delivered and experienced value with that expectation. Choose measures that answer this case: outcome attainment or time to value; completion and effort; reliability or readiness; participant experience and trust; continuation at the job's natural cadence; or cost to serve. Keep these health dimensions separate rather than blending them into a score or universal gates. For account health, distinguish outcome, necessary adoption, relationship confidence and commercial continuation. Do not turn them into one opaque number. Usage, satisfaction, payment and renewal can be informative proxies, not proof of value. Distinguish a failed outcome from missing evidence, an immature observation window, successful completion or changed need. For current work, read the relevant Sales/CRM commitment, Interaction or support history, Product outcome evidence and delivery result only where those owners exist and access is authorized. Check freshness and source, then name the one consequential risk or unknown; an absent record is not a failed customer.
- Intervene: Tailor effort using five factors where relevant: customer economics and value; complexity of reaching the outcome; observability of value; ability and authority to intervene; and natural frequency or time to an observable outcome. These are conditional choices for inquiry, not ratings or exhaustive inputs; account for duties, severity and conflicting participant interests. Compare feasible responses by expected customer benefit, downside, speed, cost and participant burden; choose proportionate work with a plausible mechanism, accountable owner, authority, capacity and verification point. Choices include fixing delivery, enabling progress, changing an arrangement, gathering discriminating evidence, no action, waiting or an orderly exit. Commercial economics guide discretionary investment; they do not erase duties or owed remedies. Agree changed expectations without silently rewriting the original commitment. Test uncertain changes proportionately and check participant outcomes, costs and unintended effects; completed activity alone does not close the gap. When individual observation or contact is infeasible, use proportionate aggregate evidence and upstream product, promise, packaging or distribution improvements; do not invent identities or default to check-ins.
- Learn: Verify whether the response improved the situation, needs adaptation or leaves an explicitly accepted residual gap. Route recurring failures or a consequential single failure with supporting evidence to the owner able to change the cause, such as the promise, product, delivery, policy or commercial arrangement. Separate immediate recovery from systemic improvement. Establish the owner's disposition, next action and how improvement will be checked; feedback merely logged or forwarded is not verified learning. Preserve sound accepted choices and limit generalization to the evidence. Use retention_attachment only for a deeper continuation or expansion decision. Continue through the existing owner's next action and result, not a parallel health ledger, automatic watcher or mandatory check-in cadence. A reply belongs to its current conversation owner; no method read authorizes a send or changes the original commitment.
- **Key:** customer_success
- **Label:** Customer success

#### Output

- A proportionate judgment of value and uncertainty, the chosen response and owner, and verification or learning needed; use existing owner records only where durable state matters.

#### Questions

- Whose expected value matters here, and what evidence would show it?
- What explains the gap, and which feasible response could improve it?
- Did the response work, and what should the responsible owners change?

#### Sources

| Label | Limitation | Ref | Url |
|---|---|---|---|
| Christensen Institute — Jobs to Be Done | Desired progress in context; not validation of a universal customer-success method. |  | https://www.christenseninstitute.org/resources/theory/jobs-to-be-done/ |
| GDS — using performance data | Combine relevant measures with research; government metrics are not universal requirements. |  | https://www.gov.uk/service-manual/measuring-success/using-data-to-improve-your-service-an-introduction |
| BetterEvaluation — contribution analysis | Supports plausible contribution and alternative explanations, not sole attribution or mandatory formal evaluation. |  | https://www.betterevaluation.org/methods-approaches/approaches/contribution-analysis |
| IHI — Model for Improvement | Contextual testing and verification; testing must not delay an already owed remedy. |  | https://www.ihi.org/library/model-for-improvement |

- **Use when:** Outcome evidence and intervention.

#### Worked examples

| Diagnosis | Evidence check | Intervention | Owner next action | Situation | Source read |
|---|---|---|---|---|---|
| Separate an unachieved promised outcome from successful completion with no need for frequent use; renewal timing alone does not distinguish them. | Re-read the owner result and relevant customer outcome at a suitable time. Record resolved, still unknown or accepted residual risk with the accountable owner, source refs and next decision; do not infer success from task completion. | Act only under the selected owner's authority and real capacity. A customer reply follows its existing conversation; the method does not send, schedule check-ins or start a watcher. | If delivery failed, route a bounded remedy to its delivery/Product owner; if only evidence is missing, ask the owner for one discriminating check. Keep any commercial next action with Sales and any task/result with Company Work. | A renewal is approaching after a one-off customer job should have completed. | Read the current agreement or Sales commitment, CRM identity, permitted Interaction/support history, and the Product or delivery outcome evidence. Missing or stale evidence means value is unknown, not failed. |

- **Rule:** Frameworks are scoped perspectives, never universal truth, authority or personalities to imitate. Owner evidence controls. Prefer directional learning criteria over false precision. Select for the decision, including unlisted methods. ACTIVE status or populated fields cannot validate hypotheses. Preserve sound accepted choices unless the request or evidence warrants revision. Questions and outputs guide the work; they are not required record fields. Advice alone needs no persisted state; retain material decisions through their existing owner when warranted. For CUSTOMER outreach, use the matching `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`; otherwise match the motion's described use case.

### Orientation

- Define expected value for the relevant participants in context; judge outcomes, not usage alone.
- Decide whether value is realized, uncertain or missing; explain gaps and choose a feasible response, including no action or exit.
- Verify the response and route material learning to the owner able to change its cause, with a disposition and verification point.
