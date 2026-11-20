---
name: "cady-company-decision"
description: "Who decides, and how to record it. Use when: Before a choice or an effect: whether it is decided, who decides, how to test a big call and how to record it. Not for: Gathering the evidence a call needs (`cady-company-evidence`), the weekly goal calls (`cady-company-weekly-review`), or doing the task itself."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision"
  version: "78fccac69b239e74ec49"
  library: "c7b303adeac10781"
  function: "company"
---
# Who decides, and how to record it

**Point:** Settle whether a choice is decided and whose it is, test a consequential one first, and record it once.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Decide or ask by risk (what breaks, for whom, how reversibly) and independent review, not by the decision's layer. Instead of: Ask the owner about every decision labelled company-level and decide everything below that alone.
- Spend the owner's time only on top-level judgement they have not stated and on authority only they hold. Instead of: Check with the owner whenever a choice feels important, to be safe.
- Write the chain from the goal down to the choice, with impact, the strongest alternative and why it loses, and dated premises. Instead of: Decide from judgement and report the choice, leaving the reasoning in the conversation.
- Size the process to the door: decide a reversible, cheap call now with a default and reviewBy; keep the outside view, pre-mortem and red team for one-way or consequential calls. Instead of: Run the same full analysis (options, base rates, pre-mortem, red team) on every company decision for rigour.
- Replace or rule out any bet, the owner's included, in one call; the owner is told and reverts it in one call. Instead of: Leave a decision someone else made, especially the owner's, in place and ask before changing it.

Before a choice or an effect: whether it is decided, who decides, how to test a big call and how to record it.

**Not for:** Gathering the evidence a call needs (`cady-company-evidence`), the weekly goal calls (`cady-company-weekly-review`), or doing the task itself.

**Unit of work:** one choice or effect. **Kind:** strategy. **Parallel:** yes. 

## Inputs

### Evidence refs

- the governing decisions and goal, and the decision item or escalation

## Procedure

1. Already decided? Read the governing decisions and goal (cady_read decision:<subject> and the goal) and the scored records of comparable decisions. Check each still holds (past its review date, a premise changed, a newer point, bet or goal conflicts); context over a week old is rechecked first. If it holds, follow it and never ask again; if not, recheck it at its own layer (step 2) and cite what changed.
2. Whose is it? A choice that changes where resources go or how functions work together is strategy, a point or a bet on the company tree (step 6). Others go by layer: L1 changes a goal or the company (a goal's target or stop, a hire or commitment, a spend envelope, a grant); L2 is how a function pursues a goal, its head decides; L3 is how one task is done, any agent decides; one that extends strategy or an L1 choice is that one. The owner's are the permission edge (a grant, their account, a fact only they hold) and a top-level call (the ICP, the customer problem, the offer, stage) they have not stated and step 5's review leaves contested (step 4); what they already stated is recorded at once (step 6), never asked back.
3. Frame it and size the work to the door. Write the chain from the goal down (one line for a small call): who the company serves, the pain this choice serves, then this choice, with why now, the strongest alternative, the status quo and dated premises. A two-way door is decided now with a stated default and a review date: in the measure when it is a bet, else in the work result. A consequential or one-way door adds, in order: the outside view (a sourced base rate, or 'none'); the evidence that would change it (`cady-company-evidence`); a prediction written first (a range, a confidence, a kill or reversal condition); and the review of step 5. A high-risk change you cannot test or review is held.
4. A point or a bet on any node is yours to record, replace or rule out; it is current at once and the owner is told. A top-level call the owner has not stated, still contested after step 5's review, is an ask, not yours to pick. A grant, an approval, a payment, a one-way door and any outside effect (send, spend, sign, file, publish, share, invite, change access, delete or export data, anything irreversible) stay the person's unless a grant covers it: prepare it whole and raise one batched ask (asks_set) with a recommendation and options. An effect they asked for (switch on auto-send) is carried in that ask prepared exactly as it would run, never enabled by you: grants are the only standing permissions and the person's to give, through their answer on the approval route; record none in a goal, decision, schedule or role card. A payment or one-way-door ask leads with step 3's frame: the status quo, the outside view (or 'none') and the prediction, then the recommendation. An L1 goal change is yours only in notify mode. Asked by the orchestrator, answer in that run with a recommendation, its reasons and the strongest alternative.
5. For a decision others will build on, or one with real risk, get an independent review before acting (`cady-engineering-independent-review`): a fresh-context reviewer that did not produce the choice, given only the record (goal served, choice, alternatives, key assumption, evidence, tests run); for a one-way door a pre-mortem and a red team given the frame and evidence, never your recommendation. Fix what it finds and note it in rechecked; ask only what it cannot resolve.
6. Record it in place (the record reference holds the fields). A settled call the person states in chat is company state now, even with no work item: record it at once as a bet (decisions_set {path, bet}; the tool says what a bet is and where it goes), read it back, and never infer a grant or ask it again. A premise they state with no record behind it is recorded as resting on their word, said so in why: not refused and never presented as verified. It releases no send, spend or permission; each keeps its own check or approval. What a node is for is decisions_set {path, point}; the by-subject form is not for strategy. A goal call is work_set {id, call, note}; a narrow call is the work result. A consequential call is also written whole as a File (files_set) the work result cites.
7. Replace a wrong bet or rule it out in one call, anyone's, the owner's included; no reason or quote is needed. This never undoes an owner's stop. Record an owner's correction of an agent's work at the scope they gave it, never widened (a correction of one headline is not a rule for every draft). The record reference holds the calls and what replacing a bet never grants.

## Acceptance

- [ ] (check) decisions looked up and rechecked before deciding; every agent decision others build on records its chain from the goal, losing alternative and dated premises, and a one-way door its outside view, prediction and independent review
- [ ] (person) no permission-edge call, and no unstated top-level call still contested after step 5's review, taken by an agent; a person's stated call recorded at once as a bet on its node; a correction, with a node served, also sent as an observation

## Owner checks

- a bet an agent replaced or ruled out reaches the owner

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the choice or effect recorded at its layer, with provenance

## References
- Read [Asking and refusals](references/asking.md) when you would ask, a call is refused, a permission is missing or you rely on an assumption.
- Read [Recording a decision: fields, stated outcomes and sensitive detail](references/decision-check-record.md) when you record a decision or an outcome the person states in chat, correct or replace a record, record an owner's correction, or hold sensitive detail.
