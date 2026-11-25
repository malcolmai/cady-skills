---
name: "cady-product-customer-interview"
description: "Customer discovery interviews. Use when: Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions. Not for: Research from published sources (`cady-product-research`) or a sales call (`cady-gtm-calls`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.product.customer_interview"
  version: "f459752ba67ab92d6e3f"
  library: "420ee7c3b26ee692"
  function: "product"
---
# Customer discovery interviews

**Point:** Learn what customers actually did and paid, not what they say they would, so product decisions rest on behaviour.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

Plan, run and synthesise customer discovery interviews about past behaviour, without leading questions.

**Not for:** Research from published sources (`cady-product-research`) or a sales call (`cady-gtm-calls`).

**Unit of work:** one interview round for one question or bet. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- the question, task or bet it serves
- file:<fileId> discussion guide

## Procedure

1. Start from the decision: the question or bet it serves, and the answers that would change it.
2. Recruit people who had the problem recently and acted on it; stop when interviews stop changing the pattern. A request to talk is outreach and needs approval.
3. Ask about specific past instances: the last time, what they did next, what it cost. No hypotheticals, no leading questions, no pitch.
4. End by asking for a commitment that costs them something; record accepted, declined or deflected.
5. A person runs a live interview and asks consent to record; the agent prepares and synthesises.
6. Save one File per interview (`files_set`), quotes marked as quotes.
7. Synthesise as n of m, keep the disconfirming cases, and add the File refs to the task or bet.

## Acceptance

- [ ] (person) each interview records a real recent instance and a commitment outcome

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the decision owner reads the synthesis against the question it serves
