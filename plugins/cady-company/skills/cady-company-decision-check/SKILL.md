---
name: "cady-company-decision-check"
description: "Who decides: the decision journey. Use when: Before a choice or an effect: whether it is already decided, who decides, and how to record it. Not for: The Executive's full process for one company decision (`cady-company-executive-review`) or doing the task itself."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision_check"
  version: "e510597361fcd7a1d171"
  library: "2a94b0b4645d6de9"
  function: "company"
---
# Who decides: the decision journey

**Point:** Settle whether a choice or effect is decided, whose it is, and record it once.

**Company context:** `context_read({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.decision_check": "e510597361fcd7a1d171@2a94b0b4645d6de9"}})`

**Bets** (where this differs from the default):
- Decide or ask by risk (what breaks, for whom, how reversibly) and independent review, not by the decision's layer. Instead of: Ask the owner about every decision labelled company-level and decide everything below that alone.
- Spend the owner's time only on top-level judgement they have not stated and on authority only they hold. Instead of: Check with the owner whenever a choice feels important, to be safe.
- Write the chain from the goal down to the choice, with impact, the strongest alternative and why it loses, and dated premises. Instead of: Decide from judgement and report the choice, leaving the reasoning in the conversation.
- Record an outcome the person states in chat as company state, in their own words, before any work item exists. Instead of: Wait for a work item, then summarise what the person said into its brief.
- Override or withdraw any decision, the owner's included, when the reason is quoted from a goal, a dimension or the user on current context. Instead of: Leave a decision someone else made, especially the owner's, in place and ask before changing it.

Before a choice or an effect: whether it is already decided, who decides, and how to record it.

**Not for:** The Executive's full process for one company decision (`cady-company-executive-review`) or doing the task itself.

**Unit of work:** one choice or effect. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Always

- Check what is decided, and whether it still holds, before deciding; a stated default is never asked back.
- Every outside effect needs the person's approval (in Cady, or their exact quoted words) or a grant covering its exact terms; otherwise prepare it and ask once.

## Inputs

### Evidence refs

- the governing decisions and goal
- the company permission mode or grant that covers an effect

## Procedure

1. Already decided? Read the governing decisions and goal (work_read decisions {state: "current", subject} and the goal). Before following one, check it still holds: past its reviewBy, a premise it names changed, or newer direction or a newer goal conflicts. Context over a week old (a reading, a status, a premise) is checked and updated before it decides anything. If it holds, follow it and do not ask again; if not, recheck it at its own layer (step 3) and cite what changed.
2. An effect (send, spend, sign, file, publish, share, invite, change access, delete or export data, anything irreversible) needs the person's approval or a current grant covering its exact terms (a grant.* decision, an active outreach grant, grant.release), under execution authority's one approval rule. With one, act and cite it as evidence on the work. Otherwise prepare the whole effect and ask once as a ready ask (run sequence step 5), and keep working on what does not wait. Payments, signatures and filings are always a person's; prepare them. Grants are the only standing permissions: record none in a goal, decision or role card.
3. Otherwise it is a choice. (a) Whose: its layer says. L1 changes a goal or the company: starting, stopping or reshaping a goal (its target, stop condition or expected cost), ICP and offer, stage and quality bar, a bet, a hire or other material commitment, a spend envelope or a grant. L2 is how a function pursues a goal: its head decides. L3 is how one task is done: any agent decides. An L2 or L3 choice that contradicts or extends an L1 one is L1. The owner's choices are only top-level judgement (the ICP, the customer problem, the offer, stage, a bet, a material commitment) and the permission edge (a grant, authority, an account or address they own, a fact only they hold); one they already stated is recorded as theirs with their quote (step 6), never asked back or chosen for them. (b) Risk: beyond those, whether to decide or ask turns on risk and review, not layer. Size the risk: what breaks, for whom, how reversibly. Cut it with tests at the lowest proving layer and the independent review (step 5), then decide when you have high confidence, as most small items and refactors allow. A high-risk change you cannot test or review is held, not shipped. (c) Chain: before you decide, write the chain down from the goal (one line for a small call): who the company serves and wins for, the ICP use case or pain this choice serves, what that needs the product or plan to emphasise, then this choice; with its impact, the strongest alternative and why it loses, and its premises dated (step 1 rechecks stale ones).
4. L1 by an agent, usually the Executive: only when the company's decisions mode is notify (Cady refuses an agent's L1 decision in approval mode and tells you to ask), and never for top-level judgement the owner has not stated (step 3), a grant, an approval or a payment, which stay the person's; and one option is clearly better: it serves the company as a whole and the user's recorded direction, its reason and strongest alternative are written, and the independent review (step 5) agrees. Then record it; the owner is told and can reverse it. Otherwise raise a BLOCKED ask with a recommendation and options (each option's impact says what happens if the owner picks it), batched, and keep working on what does not wait.
5. For a decision others will build on, or one with real risk (a refactor, a release, a change users meet), get an independent review before acting: a fresh-context reviewer that did not produce the choice (a subagent; the same model is fine), given only the record (goal served, choice, alternatives, key assumption, evidence, tests run). It checks each link of the chain from the goal, re-reads any premise it doubts, and asks whether the strongest alternative was weighed fairly and the work changes the goal rather than only looking helpful. It replaces the owner's review of refactors and releases. Fix what it finds, note it in rechecked and act; ask only what it cannot resolve.
6. Record it in place. A new or changed outcome the person states in chat is company state before execution, even with no work item yet: use the existing own-words answer/decision path, preserving source chat, their exact quote and decidedBy, with context.type goal, the company/product scope, concern outcome_workflow and the returned writeAs.appliesTo; link the goal when one exists. Read back the saved record so a later run can find it. Reuse a matching recorded answer; do not invent words, infer a grant, or ask them to repeat an outcome already supplied. Other decisions: a goal change is an L1 decision with subject goal:<goalId> beside the goal write (a stop is goal.call:<goalId> with chosen stop and its stop reason); otherwise a decision item with subject, layer, rationale, alternatives, reversal and reviewBy. The rationale is the step 3 chain (goal, use case or pain, emphasis, choice), the impact, the losing alternative and the premises checked with their dates, quoting its reason from a goal, a dimension or the user. Cite the one or two pieces of evidence that decided it. A person's decision carries their exact words (source chat, quote, decidedBy) and, in the rationale, your inference of why they chose it then, marked as inferred; your own carries authority agent. Mark it sensitive (sensitive true, optional sharedWith) when it holds personal, HR, legal, financial-account or customer-confidential detail; only you, those shared and admins who turned on See everything then see it; everything else is company record every member reads.
7. To correct a recorded decision send corrects {ref, as: supersede|wrong, why}; wrong records 'Ruled wrong: ...' on the same subject. You may override or withdraw any decision, a person's included, when why quotes the reason from a goal, a dimension or the user and the context it rests on is current (step 1); who made it is no reason to ask. In approval mode Cady refuses it and you raise a BLOCKED ask; in notify mode it is recorded and shown to the owner, who can revert it. An override never creates or widens a grant, a person-approval category, a payment or a reserved release step, and never undoes an owner's stop (initiative.stop or a goal stop).

## Acceptance

- [ ] decisions looked up and checked for currency before deciding
- [ ] every effect acted on cites the person's approval (in Cady or quoted) or a grant; otherwise it is one ready ask
- [ ] every agent decision others build on records its chain from the goal, impact, losing alternative and dated premises; an agent L1 also its independent review
- [ ] no top-level judgement or permission-edge call taken by an agent; an owner's stated call recorded as theirs with their quote
- [ ] a person's decision records their words and the inferred reason

## Owner checks

- the independent review got only the record, and what it found is in rechecked
- an override of a person's decision quotes its reason and reaches the owner

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** the choice or effect recorded at its layer, with provenance
