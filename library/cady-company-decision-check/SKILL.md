---
name: "cady-company-decision-check"
description: "Who decides: the decision journey. Use when: Before a choice or an effect: whether it is already decided, who decides, and how to record it. Not for: The Executive's full process for one company decision (`cady-company-executive-review`) or doing the task itself."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision_check"
  version: "270d5dcd9a65cbf49333"
  library: "e60c542620b38cff"
  function: "company"
---
# Who decides: the decision journey

**Point:** Settle whether a choice or effect is decided, whose it is, and record it once.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Decide or ask by risk (what breaks, for whom, how reversibly) and independent review, not by the decision's layer. Instead of: Ask the owner about every decision labelled company-level and decide everything below that alone.
- Spend the owner's time only on top-level judgement they have not stated and on authority only they hold. Instead of: Check with the owner whenever a choice feels important, to be safe.
- Write the chain from the goal down to the choice, with impact, the strongest alternative and why it loses, and dated premises. Instead of: Decide from judgement and report the choice, leaving the reasoning in the conversation.
- Record an outcome the person states in chat as company state, in their own words, before any work item exists. Instead of: Wait for a work item, then summarise what the person said into its brief.
- Override or withdraw any decision, the owner's included, when the reason is quoted from a goal, a dimension or the user on current context. Instead of: Leave a decision someone else made, especially the owner's, in place and ask before changing it.

Before a choice or an effect: whether it is already decided, who decides, and how to record it.

**Not for:** The Executive's full process for one company decision (`cady-company-executive-review`) or doing the task itself.

**Unit of work:** one choice or effect. **Kind:** strategy. **Parallel:** yes. 

## Always

- Check what is decided, and whether it still holds, before deciding; a stated default is never asked back.
- Every outside effect needs the person's approval (in Cady, or their exact quoted words) or a standing approval covering it; otherwise prepare it and ask once.

## Inputs

### Evidence refs

- the governing decisions and goal
- the company permission mode or grant that covers an effect

## Procedure

1. Already decided? Read the governing decisions and goal (cady_read decision:<subject> and the goal). Before following one, check it still holds: past its reviewBy, a premise it names changed, or newer direction or a newer goal conflicts. Context over a week old (a reading, a status, a premise) is checked and updated before it decides anything. If it holds, follow it and do not ask again; if not, recheck it at its own layer (step 3) and cite what changed.
2. An effect (send, spend, sign, file, publish, share, invite, change access, delete or export data, anything irreversible) needs the person's approval or a standing approval covering it (a grant.* decision, an active standing approval, grant.release), under execution authority's one approval rule. With one, act and cite it as evidence on the work. Otherwise prepare the whole effect and ask once as a ready ask (run sequence step 5), and keep working on what does not wait. Payments, signatures and filings are always a person's; prepare them. Standing approvals (grants) are the only standing permissions: record none in a goal, decision or role card.
3. Otherwise it is a choice. (a) Whose: what changes where resources go or how functions work together is strategy, a point or a bet on the tree (step 6), and the bet's basis says who decides (step 4). Other choices go by layer. L1 changes a goal or the company: starting, stopping or reshaping a goal (its target, stop condition or expected cost), a hire or other material commitment, a spend envelope or a grant. L2 is how a function pursues a goal: its head decides. L3 is how one task is done: any agent decides. An L2 or L3 choice that contradicts or extends strategy or an L1 one is that one. The owner's choices are only top-level judgement (the ICP, the customer problem, the offer, stage, a bet, a material commitment) and the permission edge (a grant, authority, an account or address they own, a fact only they hold); one they already stated is recorded as theirs with their quote (step 6), never asked back or chosen for them. (b) Risk: beyond those, whether to decide or ask turns on risk and review, not layer. Size the risk: what breaks, for whom, how reversibly. Cut it with tests at the lowest proving layer and the independent review (step 5), then decide when you have high confidence, as most small items and refactors allow. A high-risk change you cannot test or review is held, not shipped. (c) Chain: before you decide, write the chain down from the goal (one line for a small call): who the company serves and wins for, the ICP use case or pain this choice serves, what that needs the product or plan to emphasise, then this choice; with its impact, the strongest alternative and why it loses, and its premises dated (step 1 rechecks stale ones).
4. Strategy by an agent: with cited evidence you replace a bet whose basis is validated, hypothesis or resource constraint, and add a hypothesis or resource-constraint bet (a validated one needs its citation); it is current and the owner is told. A point, an owner-decided bet, a grant, an approval, a payment and any top-level judgement the owner has not stated stay the person's, and so does a one-way door: raise an ask (asks_write) with a recommendation and options (each option's impact says what happens if the owner picks it), batched, and keep working on what does not wait. An L1 goal change you make yourself only where the company's decisions mode is notify, with the owner told. Where Cady records your item as proposed or refuses it, raise the ask it names. Be sure first: one option is clearly better, it serves the company as a whole, its reason and strongest alternative are written, and the independent review (step 5) agrees.
5. For a decision others will build on, or one with real risk (a refactor, a release, a change users meet), get an independent review before acting: a fresh-context reviewer that did not produce the choice (a subagent; the same model is fine), given only the record (goal served, choice, alternatives, key assumption, evidence, tests run). It checks each link of the chain from the goal, re-reads any premise it doubts, and asks whether the strongest alternative was weighed fairly and the work changes the goal rather than only looking helpful. It replaces the owner's review of refactors and releases. Fix what it finds, note it in rechecked and act; ask only what it cannot resolve.
6. Record it in place. A new or changed outcome the person states in chat is company state before execution, even with no work item yet: record it in their own words (decisions_write with their exact quote and authority manager, admin for an Admin), read it back, and never invent words, infer a grant or ask them to repeat it. The record reference holds the fields. A strategy item is a point (what the node is for) or a bet: we do X, not Y, because W, with its basis (validated: a reading or two independent runs; hypothesis: accept if A, reject if B, after doing C; owner decided: their words; or resource constraint) and the measure that would settle it, at the highest node it is fully relevant to. Write it with decisions_write {path, bet {chosen, insteadOf, why, basis, measure} or point}: the path is the node's keys from its family, such as go-to-market/outreach, listed in your context read as orchestrator.paths; an unknown path is refused with the nearest ones. Structure is its own call, never beside a bet or point: decisions_write {node: {create: <path>, point}} adds a node only where work needs decisions its siblings should not inherit (otherwise the decision goes on the node that exists), and {node: {retire: <path>}} retires one. A company with no strategy tree yet has no path to write to, so decisions_write refuses that path as unknown: the tree is set up first, and decisions_write {subject, chosen, rationale} takes only the fact subjects listed below, never a strategy item. Narrow knowledge goes to its owning home, not the tree: product behaviour to the product map, an enforceable rule to a test or check, function practice to a method, a one-off to the work result. Other records: a goal change is the goal write itself (work_write {kind: goal} or {id, brief}, its reason in brief.why); a goal call, a stop included, is work_write {id: the goal, call, note, stop}; a fact a page reads by subject is decisions_write {subject, chosen, rationale} (it refuses any subject outside brand:company, icp:, system:, taste:, outreach:sender, fundraise:round-, ops:entity, finance:agent-budget, finance:api-discount, grant.release:, crm.resubscribe:, product:offering-, availability:); any other narrow call is the work result. The rationale is the step 3 chain (goal, use case or pain, emphasis, choice), the impact, the losing alternative and the premises checked with their dates, quoting its reason from a goal, a dimension or the user. Cite the one or two pieces of evidence that decided it. A person's decision carries their exact words (quote, authority manager or admin) and, in the rationale, your inference of why they chose it then, marked as inferred; your own carries authority agent. Mark it sensitive (sensitive true) when it holds personal, HR, legal, financial-account or customer-confidential detail; the record reference says who then sees it.
7. To correct a recorded decision, replace it (replaces, with citesWhy on decisions_write) or rule it out (decisions_write ruleOut {id, why}; decisions_write {subject, status: wrong, why} records 'Ruled wrong: ...' on the subject). You may override or withdraw any decision, a person's included, when why quotes the reason from a goal, a dimension or the user and the context it rests on is current (step 1); who made it is no reason to ask, but a point or an owner-decided bet is replaced only by the ask in step 4. The result is recorded and shown to the owner, who can revert it in one call. An override grants no outside-effect permission: it never creates or widens a grant, a person-approval category, a payment or a reserved release step, and never undoes an owner's stop (initiative.stop or a goal stop).
8. An owner's correction of an agent's work is evidence for the next run: fix the work and record the correction as theirs (step 6; replaced or ruled out, step 7, when it rules a decision wrong). When your context serves orchestrator.node, the work_write that finishes the work also sends observations [{nodeKey: that node, text: their words, sourceRef: the decision ref}].

## Acceptance

- [ ] decisions looked up and checked for currency before deciding
- [ ] every effect acted on cites the person's approval (in Cady or quoted) or a grant; otherwise it is one ready ask
- [ ] every agent decision others build on records its chain from the goal, impact, losing alternative and dated premises; an agent L1 also its independent review
- [ ] no top-level judgement or permission-edge call taken by an agent; an owner's stated call recorded as theirs with their quote
- [ ] a person's decision or correction records their words and the inferred reason; with a node served, a correction is also an observation

## Owner checks

- the independent review got only the record, and what it found is in rechecked
- an override of a person's decision quotes its reason and reaches the owner

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** the choice or effect recorded at its layer, with provenance

## References
- Read [Recording a stated outcome and a sensitive decision](../../references/decision-check-record.md) when you record an outcome the person states in chat, or a decision with personal, HR, legal, financial or customer-confidential detail.
