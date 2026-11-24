---
name: "cady-manager-sense-check"
description: "Sense-check a final response. Use when: Reading an agent's final response before accepting it, as the manager. Not for: A detailed review (cady-engineering-independent-review), making or changing agents (cady-company-manage-agents), or redoing the work."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.manager.sense_check"
  version: "9a80fd59247669184fd4"
  library: "e8872d5e32bf66b3"
  function: "manager"
---
# Sense-check a final response

**Point:** Catch a response that misses its node's point, breaks a bet or leaves a key risk open, using pointed questions.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Judge a response by its node's point and bets and by the key risks left open, not by how much thinking it shows. Instead of: Matching each kind of work to the thinking it should show.
- Ask one pointed question per gap that does not suggest its answer; the agent may be asked to explain. Instead of: Sending the result back for a fresh pass and never asking the agent to explain.

Reading an agent's final response before accepting it, as the manager.

**Not for:** A detailed review (cady-engineering-independent-review), making or changing agents (cady-company-manage-agents), or redoing the work.

**Unit of work:** one final response. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- the final response as reported
- the node its task sits on

## Procedure

1. Read the final response only, with the task's node open: its point and bets (cady_read node:<path>).
2. Ask yourself: does it serve the point? Does it break a bet? Which key risk does it leave open: a one-way action, an outside effect, a deletion, a claim that something works?
3. No gap: accept it and move on.
4. A gap: ask one pointed question per gap, and do not suggest the answer. "What tests did you run?" "Who receives this?" "What did you delete, and what used it?"
5. Accept a fact or changed work. A vague answer gets one sharper question; after that, tell the person which risk is still open.
6. Do not open the work, rerun it or review it line by line. A detailed review is a reviewer's job.

## Acceptance

- [ ] (fresh) each question asked for a fact the response did not show, without suggesting the answer
- [ ] (fresh) no response without a gap was held back
- [ ] (check) the work behind the response was not opened, rerun or reviewed line by line

## Owner checks

- each question names one gap and does not suggest its answer

## Result

### Artifact refs

- company:work:<workId>
- **Transition:** the response accepted, sent back with its question, or raised to the person with the open risk

## References
- Read [Host care](references/host-care.md) when before you start an agent, or when an agent plans to delete files or database rows.
