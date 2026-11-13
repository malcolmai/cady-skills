---
name: "cady-company-manage-agents"
description: "Manage company agents. Use when: Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task. Not for: Native helpers, subagents, one-off work items and agents on a host that is in contact."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.manage_agents"
  version: "4eb8cb6549498b9968a0"
  library: "0b93eecfd4303f2c"
  function: "company"
---
# Manage company agents

**Point:** One agent per ongoing responsibility nobody serves, on a node or none; live on the owner's go-ahead.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- An agent is one recurring responsibility on a node or on none; reuse or update the agent that serves the outcome before creating one, but several agents may share a goal or node. Instead of: Create a new agent for each new need or parallel stream of work.
- Class risk by reach and reversibility, and make the first task one real cycle at its finish line. Instead of: Class agents by how important their work is, and start with a trivial smoke task.
- Authority comes only from the person's approval or a grant; never write approval limits into an agent's text and treat them as control. Instead of: Write the limits into the agent's instructions and trust it to stay inside them.
- Count a schedule, pause or retirement as real only after reading the host scheduler back. Instead of: Treat the agent record in Cady, or a successful create call, as the schedule's state.
- Judge an agent by what it changed for its goal and the rigour of its decisions; fix the tool, check or placement before its duties. Instead of: Judge by runs completed and records written, and rewrite the agent's prompt when it fails.

Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task.

**Not for:** Native helpers, subagents, one-off work items and agents on a host that is in contact.

**Unit of work:** one company agent and one judged goal. **Kind:** execution. **Parallel:** no. 

## Inputs

### Authority

- verified member credential
- host identity from the current Cady connection
- decisionId and nonce are the server's: to retry, repeat the exact call
- expectedRevision null for a new agent or run, else the current revision
- current agentId for changes

### Design

- agent name and function
- one goal
- risk class (critical or standard)
- measure and its data (on the goal it serves)
- cadence or trigger, with why
- approval limits
- skills
- owner member
- first task, its checks and evaluation criteria
- end or escalation condition

## Procedure

1. An agent is one ongoing responsibility; due tasks are work items and a one-off is a helper run. Read agents_read, work (work_read), the node's point and bets and this host's automations first: if an agent already serves the outcome, reuse it or change it with agents_set (rebind if its host changed) and stop. Create one when none does; a goal or node may have several agents when their jobs differ. Put an agent on a node when that node's work needs its own regular pass. An agent sits on the node it serves, or on none (a personal agent). Parallel sessions and subagents are runs of that agent, not new agents.
2. Responsibility and risk class. State the outcome, one measure with its data source, a cadence or trigger, approval limits and end condition; pass goal when it serves a goal. Critical: a hard-to-undo effect or reach outside the company, or drafts released automatically; every other agent is standard. Re-class on any grant, tool, access or trigger change.
3. Fit. Read agents_read and cady_read company:map, and name the agent's skills as plain names, the skill folders the host holds (the library's cady-core-skill-index lists them), or leave them empty; Cady serves no skill index, so do not search for one. Reuse library skills unchanged; adapt only for an evidenced failure, tool mismatch or missing expert judgment.
4. First task. One cycle of the real deliverable at its finish line; it exercises its hardest judgement. Its decision map: goal, node, trigger, decides alone, consults on, hands off.
5. Evaluation. The criteria live on the first task, not the agent record: brief.doneWhen holds 2-5 reader tests tagged (check), (fresh) or (person), and brief.stopIf the early-stop limit; a completed run is not a reported result.
6. Create and bind the agent with agents_set (host {action: bind}), file the first task with work_set, and ask the owner for the go-ahead (asks_set). On their yes, send status live with approval {quote}. A returned schedule stays configured_unconfirmed until a host readback. Change visibility or sharing only on request; it applies at once and the owner is told.
7. Authority. Read the company's permission modes first (cady_read company:map values, the permission modes line). Effects follow `cady-company-decision-check` step 2. No mode lets you send without that approval or a grant; limits text is not enforcement. Never approve for the person: their own decision covers every grant (send, spend, publish, sign, file), an invite, share or outreach effect in approval mode, new access or capture, widening permissions, a design change to a grant-holding agent and raising cadence or cost; per grant when critical. An agent acts with its owner's permissions, and its lifecycle is the owner's. Going live, from draft, paused or retired, takes the owner's go-ahead: the owner gives it, or the owner's own agent records the owner's exact words as approval {quote}. An absent owner's go-ahead: agent design, setup, review and retirement reference.
8. Review this host's agents by risk class, with evidence from runs, receipts, cady_read changes {kind: agents} and transcripts (never bodies). Pause one that is not up to scratch (step 9); redesigning it is the Executive's (`cady-company-executive-review` step 15), never the pausing agent's.
9. Retire or pause an agent only when it is confirmed obsolete or met its end condition, and adopt an existing company scheduled task only on the owner's yes: read the agent design, setup, review and retirement reference (it confirms an unscheduled task with agents_set host {action: removed}).

## Acceptance

- [ ] one responsibility that its work items cite
- [ ] the first task carries its evaluation criteria and stopIf; nothing was released before the agent was live
- [ ] every grant has the owner's own approval for its exact terms; a no-grant agent's policy approval is recorded and the owner notified
- [ ] the Cady binding and any recurring host task are read back

## Owner checks

- current company and member grant
- the agent's node or none, and the owner who holds its lifecycle
- the agent is live (the owner's go-ahead) before it takes an outside action
- agent.approve:<agentId> (policy only while no grant is held)
- host schedule readback
- reviewed receipt
- anomaly grant gate

## Result

### Artifact refs

- company:agent:<agentId>
- company:work:<workId>
- host task reference
- reviewed receipt
- **Transition:** the owner's go-ahead takes the agent live (draft, paused or retired to live)

## References
- Read [Agent host tasks, library and silent hosts](references/agent-hosts.md) when you install, change or review a recurring host task, adopt skills, or check hosts for agents whose host went silent.
- Read [Agent design, setup, review and retirement](references/agent-lifecycle.md) when you design an agent or change its responsibility, create, bind or take an agent live, review an agent or judge a reported result, pause or retire an agent, adopt a scheduled task, or install the baseline roster.
- Read [Execution agent brief](references/execution-agent-brief.md) when you set up a channel execution agent.
