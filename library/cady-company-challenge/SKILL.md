---
name: "cady-company-challenge"
description: "Challenge a result by its stakes. Use when: Reading a result one level down before accepting it, as the orchestrator or a family orchestrator. Not for: Independent review before a merge (cady-engineering-independent-review), the Executive's own decisions, or redoing the work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.challenge"
  version: "7e781e31a1e246824093"
  library: "94cbfa32dc5a1bac"
  function: "company"
---
# Challenge a result by its stakes

**Point:** Catch a response whose thinking is thinner than its stakes, and get it fixed by the cheapest fresh pass.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Treat a smell as a gap between the stakes and the thinking shown, never as a kind of work: the same email can be fine or a smell, depending on what it risks. Instead of: A list of work types that always get challenged.
- Ask for a fresh pass against a named consideration, then a skilled subagent, then evidence, the cheapest rung first. Instead of: Asking the agent to explain or justify its result.

Reading a result one level down before accepting it, as the orchestrator or a family orchestrator.

**Not for:** Independent review before a merge (cady-engineering-independent-review), the Executive's own decisions, or redoing the work.

**Unit of work:** one result. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- the result as reported
- the goal or node it serves

## Procedure

1. Read the response, not the activity: judge what it shows and never investigate the work behind it. Challenge one level down only: the orchestrator reads family orchestrators' passes and cross-family results, a family orchestrator reads its agents' results, and where a family has no orchestrator the orchestrator reads its agents. Challenging a family pass names the missing consideration and the family revises its own call; its calls inside its family still stand.
2. Match the stakes to the thinking they need. Complex or costly work shows research, an alternative weighed or a feasibility check. An external action (outreach, a post, a commitment) shows the recipient's view, why they would care and how it could be misread, and the impact on us: a client lost if it is too pushy, a commercial goal missed with no follow-up. A claim that something is done, working or fixed shows how it was tested and its readback. A confident recommendation names its key assumption and what would show it wrong. A report of much work says how it moves the point it serves.
3. A smell is a response whose thinking is thinner than its stakes. A one-way door is not a smell; it raises the bar for each line in step 2. With no smell, accept the result and move on: trust is the default. A minor gap is flagged in the result while the work continues.
4. With a smell, send the result back for a fresh pass against the named consideration, for example: 'do a fresh pass on the recipient's view: why would they care, and how could this be misread?' Never ask the agent to justify itself; a request to explain invites a defence, a fresh pass invites a revision.
5. If the fresh pass comes back unchanged and judging it needs craft you lack, have a skilled subagent review it against the same consideration. Where it turns on whether something works, get the test run or the result read back instead.
6. Accept when the named consideration is addressed, by changed work or by evidence that it already was; a cosmetic change or prose that defends the result is not an answer. Allow one round per rung; after the last rung with no answer, mark the result at risk and count the smell toward step 7.
7. The same smell from the same agent in two comparable windows is a design need: hand it to the Executive with the responses as evidence, and never rewrite the agent yourself.
8. Record each challenge on the result's work item: the smell, the rung reached and whether the work changed. When challenges rarely change anything, challenge less.

## Acceptance

- [ ] (fresh) each challenge named a missing consideration the stakes called for
- [ ] (check) each challenge records its rung and whether the work changed
- [ ] (fresh) no result without a smell was held back

## Owner checks

- a challenge names the consideration that is missing
- accepted work is changed work or evidence, never a defence

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** the result accepted, or sent back with its named consideration
