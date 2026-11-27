---
name: "cady-company-manage-agents"
description: "Manage company agents. Use when: Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task. Not for: Native helpers, subagents, one-off work items and agents on a host that is in contact."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.manage_agents"
  version: "25792c9e83afbbdffecc"
  library: "be33cb4841a22c36"
  function: "company"
---
# Manage company agents

**Point:** One agent per ongoing responsibility nobody serves, on a node or none; its owner or their agent sets it live.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- An agent is one recurring responsibility on a node or on none; reuse or update the agent that serves the outcome before creating one, but several agents may share a goal or node. Instead of: Create a new agent for each new need or parallel stream of work.
- Class risk by reach and reversibility, and make the first task one real cycle at its finish line. Instead of: Class agents by how important their work is, and start with a trivial smoke task.
- Count a schedule, pause or retirement as real only after reading the host scheduler back. Instead of: Treat the agent record in Cady, or a successful create call, as the schedule's state.
- Judge an agent by what it changed for its goal and the rigour of its decisions; fix the tool, check or placement before its duties. Instead of: Judge by runs completed and records written, and rewrite the agent's prompt when it fails.

Create and bind, schedule, review or retire a company agent: whether one is warranted, its design and first task.

**Not for:** Native helpers, subagents, one-off work items and agents on a host that is in contact.

**Unit of work:** one company agent and one judged goal. **Kind:** execution. **Parallel:** no. 

## Inputs

### Design

- agent name and function
- one goal
- risk class (critical or standard)
- measure and its data (on the goal it serves)
- cadence or trigger, with why
- skills
- owner member
- first task, its checks and evaluation criteria
- end or escalation condition

## Procedure

1. Reuse first. An agent is one ongoing responsibility nobody serves; due tasks are work items and a one-off is a helper run. Read agents_read, work and the node's point and bets: if an agent serves the outcome, change it with agents_set and stop. An agent sits on the node it serves or on none; several may share a goal or node when their jobs differ. Parallel sessions and subagents are runs of that agent.
2. Scope and class. State the outcome, one measure with its data on the goal it serves, a cadence or trigger with why, and an end condition. Critical: sending or publishing to non-members, spending, signing, filing, sharing data externally, changing external access, deleting owner records, or drafts released automatically; every other agent is standard. Re-class on any grant, tool, access or trigger change.
3. Skills. Name the agent's skills as the plain folder names the host holds (the library's roster.json lists them), or none; reuse them unchanged unless a failure, tool mismatch or missing judgement is evidenced.
4. First task: one cycle of the real deliverable at its finish line that exercises its hardest judgement and touches each tool the duty needs. Its brief.doneWhen holds 2-5 reader tests tagged (check), (fresh) or (person), and brief.stopIf the early-stop limit.
5. Set up with agents_set (agents_systems_set for a published system), file the first task with cady_start calls.work, and follow each result's next to bind and go live. Bind only an agent with no host or on your own host; one on another host moves only when the owner asks. Count a schedule, pause or retirement only after the host readback the result asks for.
6. Review by class. Critical: the effects of its first released cycle, then a sample. Standard: after its first task, then only on a signal (owner correction, refusals, missed or empty runs, a cost spike, a claim without readback). Evidence is runs, receipts and transcripts cited host:transcript:<uuid>, never bodies; a missing transcript means unknown, and a done claim without readback is unsupported. Judge by what it changed for its goal and the rigour of its decisions, not activity.
7. Pause and hand over. Pause an agent that is not up to scratch and file one handover task under the Executive's goal "Keep the system sharp", naming the agent, the evidence and what was paused; never rewrite its brief or skills yourself. Resume it unchanged only for an external cause, with evidence. Retire only an obsolete agent or one that met its end condition.
8. Wake for use. Wake an agent for a useful action or signal, never to keep it busy; fit cadence to duty, deadlines and evidence freshness. When an agent's machine is not connected, note it in your run record and continue some other way. Every live agent has open work: file its next task under its goal, or hand the gap to the Executive. A scheduled task you adopt with secrets in its prompt: tell the owner, never upload them.

## Acceptance

- [ ] one responsibility that its work items cite
- [ ] the first task carries its evaluation criteria and stopIf
- [ ] the Cady binding and any recurring host task are read back

## Owner checks

- current company and member grant
- the agent's node or none, and the owner who holds its lifecycle
- host schedule readback
- reviewed receipt

## Result

### Artifact refs

- company:agent:<agentId>
- company:work:<workId>
- host task reference
- reviewed receipt
- **Transition:** status live takes the agent live (draft, paused or retired to live), set by the owner or the owner's own agent

## References
- Read [Model selection: model, effort and budget for scheduled work](references/model-selection.md) when you set up or change a scheduled run, or choose a model, effort or budget for work.
