---
name: "cady-sales-method"
description: "Sales role card: what this function owns and decides. Load when acting as the Sales agent or choosing among its skills. Not for doing a task: load the task skill."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.sales"
  version: "ba3d31f0a38c38762f70fe99102fd0febf2c5813af798374a9080e3f8f705323"
  library: "cf93c1d9ce44e1ac"
  function: "sales"
---
# Sales

**Company context:** `get_cady_context({"area": "gtm/outreach", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.method.sales": "ba3d31f0a38c38762f70fe99102fd0febf2c5813af798374a9080e3f8f705323"}})`

Shared by every role card: `../../references/role-card-common.md`.

## Parent function
gtm

## Selected judgment
- When sourcing promises a prospect, investor, attendee or co-host cohort, persist real source-backed identities and selected CRM List membership before message preparation; use `cady-gtm-tam-map` for the reviewed import, completion receipt and membership readback. Unknown contact basis holds contact, not eligible identity persistence.
- Establish the actual buying trigger, current alternative, buyer, user and approver, budget and switching barriers. For outreach, bind the exact relationship, recipient, thread and source to current contact permission. Qualification and permission are different decisions; a plausible buyer is not a permitted send.

## Domain method

### Customer job

#### Frameworks

- **Avoid when:** Do not replace observed situations with demographics, personas or feature requests.
- **Decision:** Which customer progress is important enough to build around?
- **Evidence bar:** Prefer observed behavior, commitment and outcomes over stated preference; keep industry independent unless evidence makes it a real boundary. A specific audience and situation, current approach, desired progress and obstacles are hypotheses until supported by customer evidence.

#### Execution

- Describe the narrow group in the situation where the job arises, what they do now, what better state they seek and what prevents it. Keep each unknown explicit. Use this account to choose a useful offer or question, not to imply that everyone in the group is ready to buy.
- **Key:** customer_job
- **Label:** Customer job and alternative

#### Output

- situation
- job
- current_alternative
- stakes
- observable_outcome
- frequency

#### Questions

- In what situation does the customer try to make progress?
- What do they do today, including doing nothing?
- What makes the current alternative costly or inadequate?
- What observable outcome would count as progress?
- How often does the triggering situation recur?

#### Sources

| Label | Ref | Url |
|---|---|---|
| Christensen Institute — Jobs to Be Done |  | https://www.christenseninstitute.org/theory/jobs-to-be-done/ |

- **Use when:** Problem, segment or value mechanism is uncertain; useful for people, companies and aggregate audiences.
- **Rule:** Frameworks are scoped perspectives, never universal truth, authority or personalities to imitate. Owner evidence controls. Prefer directional learning criteria over false precision. Select for the decision, including unlisted methods. ACTIVE status or populated fields cannot validate hypotheses. Preserve sound accepted choices unless the request or evidence warrants revision. Questions and outputs guide the work; they are not required record fields. Advice alone needs no persisted state; retain material decisions through their existing owner when warranted. For CUSTOMER outreach, use the matching `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`; otherwise match the motion's described use case.

### Stakeholder decision

#### Frameworks

- **Avoid when:** Do not force enterprise buying roles onto aggregate, self-serve or early problem-discovery evidence.
- **Decision:** Why would this stakeholder act, and how will they decide?
- **Evidence bar:** Record the customer's language and exact interaction evidence; unknown is preferable to a model-completed field. A reply, curiosity or trial signup is a signal to assess, not qualification or purchase intent by itself.

#### Execution

- Use the conversation or observed next action to test whether the problem, consequence, timing and decision path justify a sales next step. Offer a proportionate low-commitment way to inspect value when evidence is thin; do not force a call or fill a qualification framework. Keep the exact reply in its source system and route any reply through the existing interaction and Sales owner boundary, not a new outbound follow-up assumption.
- **Key:** stakeholder_decision
- **Label:** Stakeholder decision (SPICED)

#### Output

- situation
- pain
- impact
- critical_event
- decision

#### Questions

- What is the current situation?
- What concrete pain or friction exists?
- What is the impact of solving or ignoring it?
- Which event makes timing material?
- Who and what govern the decision?

#### Sources

| Label | Limitation | Ref | Url |
|---|---|---|---|
| Winning by Design — SPICED | Commercial methodology; a complete record is not evidence of buyer commitment. |  | https://winningbydesign.com/spiced-framework/ |

- **Use when:** An identified customer or stakeholder conversation needs structured discovery and a credible next commitment.
- **Rule:** Frameworks are scoped perspectives, never universal truth, authority or personalities to imitate. Owner evidence controls. Prefer directional learning criteria over false precision. Select for the decision, including unlisted methods. ACTIVE status or populated fields cannot validate hypotheses. Preserve sound accepted choices unless the request or evidence warrants revision. Questions and outputs guide the work; they are not required record fields. Advice alone needs no persisted state; retain material decisions through their existing owner when warranted. For CUSTOMER outreach, use the matching `cady-gtm-cold-email-cycle`, `cady-gtm-warm-email`, `cady-gtm-reply` or `cady-gtm-linkedin-message`; otherwise match the motion's described use case.
