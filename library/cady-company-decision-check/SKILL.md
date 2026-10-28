---
name: "cady-company-decision-check"
description: "Who decides: the decision journey. Use when: Before a choice or an effect: whether it is already decided, who decides, and how to record it. Not for: The Executive's full process for one company decision (`cady-company-executive-review`) or doing the task itself."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision_check"
  version: "c5ead3c4062a4e8e5e0c"
  library: "f2ab4ebd3a461f29"
  function: "company"
---
# Who decides: the decision journey

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.decision_check": "c5ead3c4062a4e8e5e0c@f2ab4ebd3a461f29"}})`

Before a choice or an effect: whether it is already decided, who decides, and how to record it.

**Not for:** The Executive's full process for one company decision (`cady-company-executive-review`) or doing the task itself.

**Unit of work:** one choice or effect. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Always

- Check what is decided, and whether it still holds, before deciding; a stated default is never asked back.
- Effects go through self-approval or a grant first; ask only when neither covers the exact effect.
- An agent's L1 choice needs a high bar, a written reason, a fresh look and the owner told.
- A sensitive decision or note is marked sensitive when written; everything else is company record every member reads.

## Inputs

### Evidence refs

- the governing decisions and goal
- the company permission mode or grant that covers an effect

## Procedure

1. Already decided? Read the governing decisions and goal (get_company_work decisions {state: "current", subject} and the goal). Before following one, check it still holds: past its reviewBy, a premise it names has changed, or it conflicts with newer direction or a newer goal. If it holds, follow it and do not ask again. If not, recheck it at its own layer (step 3) and cite what changed.
2. An effect (send, spend, sign, file, publish, share, invite, change access, delete or export data, anything irreversible)? First, self-approve it: its category's permission mode decides, and Cady refuses when a person must approve; in notify mode it goes through and the owner is told. Second, does a current grant cover its exact terms (a grant.* decision, an active outreach grant, grant.release)? Either way act and keep the receipt. If neither, prepare the whole effect and ask once as a ready packet (BLOCKED ask: the exact effect, the prepared material, minutes needed and what happens next), and keep working on what does not wait. Payments, signatures and filings are always a person's; prepare them. Grants are the only standing permissions: record none in a goal, decision or role card.
3. Otherwise it is a choice; find its layer. L1 changes a goal or the company: starting, stopping or reshaping a goal (its target, stop condition or expected cost), ICP and offer, stage and quality bar, a bet, a hire or other material commitment, a spend envelope or a grant. L2 is how a function pursues a goal: its head decides. L3 is how one task is done: any agent decides. An L2 or L3 choice that contradicts or extends an L1 one is L1. Asking the owner an L2 or L3 question is a stall.
4. L1 by an agent, usually the Executive: only when the company's decisions mode is notify (Cady refuses an agent's L1 decision in approval mode and tells you to ask), and never for a grant, an approval or a payment, which stay the person's (step 2); and the choice clears a high bar. It serves the company as a whole and the user's recorded direction, its reason and strongest alternative are written, and the fresh look (step 5) agrees. Then record it: the owner is told and can reverse it. Otherwise raise it as a BLOCKED ask with a recommendation and options, batched, and keep working on what does not wait.
5. For an L1 or L2 decision others will build on, take one fresh look before acting: a fresh-context subagent (the same model is fine) given only the record (goal served, choice, alternatives, key assumption, evidence) asks whether it makes sense, is justified, considers nuance and keeps focus. Fix what it finds, note it in rechecked and act; ask only about what it cannot resolve.
6. Record it in place: for a goal change, an L1 decision with subject goal:<goalId> beside the goal write (a stop is the goal call: goal.call:<goalId> with chosen stop and its stop reason); otherwise a decision item with subject, layer, rationale, alternatives, reversal and reviewBy. Keep provenance. A person's decision carries their exact words (source chat, quote, decidedBy) and, in the rationale, your inference of why they chose it at that time, marked as inferred. Your own carries authority agent. Mark the decision sensitive (sensitive true, optional sharedWith) when it holds personal, HR, legal, financial-account or customer-confidential detail; it is then visible only to you, people you share it with, and admins who turned on See everything. Everything else is company record, whichever agent wrote it.
7. To correct a recorded decision send corrects {ref, as: supersede|wrong, why}; wrong records 'Ruled wrong: ...' on the same subject. Correcting a person's decision is a discouraged exit hatch: only on new evidence that the reason they chose it no longer holds, with that evidence in why. In approval mode Cady refuses it and you raise a BLOCKED ask; in notify mode it is recorded, the owner is told and can revert it. Never for a grant, an approval or a stop. When in doubt, ask instead.

## Acceptance

- [ ] decisions looked up and checked for currency before deciding
- [ ] every effect acted on cites its self-approval or grant; otherwise it is one ready-packet ask
- [ ] every agent L1 choice has its reason, alternative and fresh look on record
- [ ] a person's decision records their words and the inferred reason

## Owner checks

- the fresh look ran from a short brief, and what it found is in rechecked
- an effect cites its self-approval mode or grant
- a correction of a person's decision carries new evidence and reaches the owner

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** the choice or effect recorded at its layer, with provenance
