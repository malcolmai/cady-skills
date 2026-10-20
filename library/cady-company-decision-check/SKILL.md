---
name: "cady-company-decision-check"
description: "Decision second look. Use when: You recorded an important decision others will build on. Not for: L3 execution or re-deciding the question; use `cady-company-executive-review` for an executive decision."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.decision_check"
  version: "0b4a4004599c826afd42db08b51d1665074d5421e741f2584901d058e8420952"
  function: "company"
---
# Decision second look

You recorded an important decision others will build on.

**Not for:** L3 execution or re-deciding the question; use `cady-company-executive-review` for an executive decision.

**Unit of work:** one recorded decision. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- the decision item just recorded (decision id)
- the evidence titles it cites

## Procedure

1. Take one fresh look before acting, with a fresh-context subagent if available (the same model is fine). Give it the decision record only: goal served, chosen option, alternatives, key assumption, evidence cited.
2. Ask four things: does it make sense, is it well justified, does it consider nuance, and does it avoid diluting focus beyond the current goals and decisions.
3. Fix what the look finds, record what it found or changed in the decision's rechecked field (one short note), and act. Nothing waits on the look.
4. Raise an owner ask only if the look finds something it cannot resolve.

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

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.decision_check": "0b4a4004599c826afd42db08b51d1665074d5421e741f2584901d058e8420952"}})`
