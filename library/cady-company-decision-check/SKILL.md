---
name: "cady-company-decision-check"
description: "Who decides: the decision journey. Use when: Before a choice or an effect: whether it is already decided, who decides, and how to record it. Not for: The Executive's full process for one company decision (`cady-company-executive-review`) or doing the task itself."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision_check"
  version: "f949c7e19ef0ec4e4042"
  library: "cadefeacac8a12cd"
  function: "company"
---
# Who decides: the decision journey

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.decision_check": "f949c7e19ef0ec4e4042@cadefeacac8a12cd"}})`

Before a choice or an effect: whether it is already decided, who decides, and how to record it.

**Not for:** The Executive's full process for one company decision (`cady-company-executive-review`) or doing the task itself.

**Unit of work:** one choice or effect. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Always

- Check what is decided, and whether it still holds, before deciding; a stated default is never asked back.
- Effects go through self-approval or a grant first; ask only when neither covers the exact effect.
- Decide when testing and independent review leave you confident; ask only a truly controversial call, and quote each decision's reason from a goal, a dimension or the user.
- A sensitive decision or note is marked sensitive when written; everything else is company record every member reads.

## Inputs

### Evidence refs

- the governing decisions and goal
- the company permission mode or grant that covers an effect

## Procedure

1. Already decided? Read the governing decisions and goal (get_company_work decisions {state: "current", subject} and the goal). Before following one, check it still holds: past its reviewBy, a premise it names has changed, or it conflicts with newer direction or a newer goal. Context over a week old (a reading, a status, a premise) is checked and updated before it decides anything. If it holds, follow it and do not ask again. If not, recheck it at its own layer (step 3) and cite what changed.
2. An effect (send, spend, sign, file, publish, share, invite, change access, delete or export data, anything irreversible)? First, self-approve it: its category's permission mode decides, and Cady refuses when a person must approve; in notify mode it goes through and the owner is told. Second, does a current grant cover its exact terms (a grant.* decision, an active outreach grant, grant.release)? Either way act and keep the receipt. If neither, prepare the whole effect and ask once as a ready packet (BLOCKED ask: the exact effect, the prepared material, minutes needed and what happens next), and keep working on what does not wait. Payments, signatures and filings are always a person's; prepare them. Grants are the only standing permissions: record none in a goal, decision or role card.
3. Otherwise it is a choice. Its layer says whose it is: L1 changes a goal or the company: starting, stopping or reshaping a goal (its target, stop condition or expected cost), ICP and offer, stage and quality bar, a bet, a hire or other material commitment, a spend envelope or a grant. L2 is how a function pursues a goal: its head decides. L3 is how one task is done: any agent decides. An L2 or L3 choice that contradicts or extends an L1 one is L1. Whether to decide or ask turns on risk and review, not layer. Size the risk: what breaks, for whom, how reversibly. Cut it with tests at the lowest proving layer and the independent review (step 5), then decide when you have high confidence, as most small items and refactors allow. Ask only a truly controversial call: after testing and review, no option is clearly better by the goals, dimensions and recorded decisions. A high-risk change you cannot test or review is held, not shipped. Asking anything else, beyond step 2's reserved effects, is a stall.
4. L1 by an agent, usually the Executive: only when the company's decisions mode is notify (Cady refuses an agent's L1 decision in approval mode and tells you to ask), and never for a grant, an approval or a payment, which stay the person's (step 2); and one option is clearly better: it serves the company as a whole and the user's recorded direction, its reason and strongest alternative are written, and the independent review (step 5) agrees. Then record it: the owner is told and can reverse it. Otherwise raise it as a BLOCKED ask with a recommendation and options (each option’s impact says what happens if the owner picks it), batched, and keep working on what does not wait.
5. For a decision others will build on, or one with real risk (a refactor, a release, a change users meet), get an independent review before acting: a fresh-context reviewer that did not produce the choice (a subagent; the same model is fine), given only the record (goal served, choice, alternatives, key assumption, evidence, tests run), asks whether it makes sense, is justified, considers nuance and keeps focus. It replaces the owner's review of refactors and releases. Fix what it finds, note it in rechecked and act; ask only what it cannot resolve.
6. Record it in place. A new or changed outcome stated by the person in chat is company state before execution, even if no work item exists yet. Use the existing own-words answer/decision path: preserve source chat, their exact quote and decidedBy, with context.type goal, the appropriate company/product scope, concern outcome_workflow and the returned writeAs.appliesTo; link the goal when one exists. Read back the saved record so a later run can find it. Reuse a matching recorded answer; do not invent words, infer a grant, or ask them to repeat an outcome already supplied. For other decisions: for a goal change, an L1 decision with subject goal:<goalId> beside the goal write (a stop is the goal call: goal.call:<goalId> with chosen stop and its stop reason); otherwise a decision item with subject, layer, rationale, alternatives, reversal and reviewBy. The rationale quotes its reason from a goal, a dimension or the user. Keep provenance. A person's decision carries their exact words (source chat, quote, decidedBy) and, in the rationale, your inference of why they chose it at that time, marked as inferred. Your own carries authority agent. Mark the decision sensitive (sensitive true, optional sharedWith) when it holds personal, HR, legal, financial-account or customer-confidential detail; it is then visible only to you, people you share it with, and admins who turned on See everything. Everything else is company record, whichever agent wrote it.
7. To correct a recorded decision send corrects {ref, as: supersede|wrong, why}; wrong records 'Ruled wrong: ...' on the same subject. You may override or withdraw any decision, a person's included, when why quotes the reason from a goal, a dimension or the user and the context it rests on is current (step 1); who made it is no reason to ask, so decide it as step 3 says. In approval mode Cady refuses it and you raise a BLOCKED ask; in notify mode it is recorded and shown to the owner, who can revert it. An override never creates or widens a grant, a person-approval category, a payment or a reserved release step, and never undoes an owner's stop (initiative.stop or a goal stop).

## Acceptance

- [ ] decisions looked up and checked for currency before deciding
- [ ] every effect acted on cites its self-approval or grant; otherwise it is one ready-packet ask
- [ ] every agent L1 choice has its quoted reason, alternative and independent review on record
- [ ] a person's decision records their words and the inferred reason

## Owner checks

- the independent review ran from a short brief, and what it found is in rechecked
- an effect cites its self-approval mode or grant
- an override of a person's decision quotes its reason from a goal, a dimension or the user and reaches the owner

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** the choice or effect recorded at its layer, with provenance
