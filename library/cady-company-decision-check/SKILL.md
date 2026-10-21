---
name: "cady-company-decision-check"
description: "Decision layers and second look. Use when: Deciding a choice's layer (owner, function head or task), or rechecking it before others build on it. Not for: The Executive's full founder-level decision process (`cady-company-executive-review`) or re-deciding a settled question."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision_check"
  version: "6dec61094161e82bb799b13132bb7d5023dd384091737ac29ba1d17c574b4202"
  library: "725c50982aeed34b"
  function: "company"
---
# Decision layers and second look

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.decision_check": "6dec61094161e82bb799b13132bb7d5023dd384091737ac29ba1d17c574b4202"}})`

Deciding a choice's layer (owner, function head or task), or rechecking it before others build on it.

**Not for:** The Executive's full founder-level decision process (`cady-company-executive-review`) or re-deciding a settled question.

**Unit of work:** one recorded decision. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- the decision item just recorded (decision id)
- the evidence titles it cites

## Procedure

1. Find the decision's layer. L1 is the owner's: goals with a target and date, ICP and offer, stage and quality bar, spend and authority envelope, anything irreversible or visible at scale. Propose it with options and a recommendation as one batched ask and keep working on everything that does not wait on it. Current owner records decide L1; an L2 choice that contradicts or extends an L1 one is an L1 question.
2. L2 is the function head's: how the function pursues an L1 goal. Restate the outcome one level up from the parent goal, company direction and current decisions (get_company_work decisions, filtered by subject when known), choose, and record a decision with alternatives, the key assumption and what would reverse it. L3 is any agent's: how one task is done; take the decided change narrowly with the owner's exact constraints and finish line, and flag evidence it is wrong rather than reopen it. Asking the owner an L2 or L3 question is a stall, not caution. Resolve an L2 or L3 conflict by recording a decision that cites both; only a conflict touching L1 becomes one ask.
3. For an important decision others will build on, take the second look below; layers put each choice with the cheapest competent decider, and the look catches oversimplification before it spreads.
4. Take one fresh look before acting, with a fresh-context subagent if available (the same model is fine). Give it the decision record only: goal served, chosen option, alternatives, key assumption, evidence cited.
5. Ask four things: does it make sense, is it well justified, does it consider nuance, and does it avoid diluting focus beyond the current goals and decisions.
6. Fix what the look finds, record what it found or changed in the decision's rechecked field (one short note), and act. Nothing waits on the look.
7. Raise an owner ask only if the look finds something it cannot resolve.

## Acceptance

- [ ] a decision item carrying rechecked
- [ ] for an unresolved finding, one owner ask with options and a recommendation

## Owner checks

- the look ran in fresh context from a short brief
- what it found or changed is in rechecked

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** fix what was found and act; ask the owner only for what cannot be resolved
