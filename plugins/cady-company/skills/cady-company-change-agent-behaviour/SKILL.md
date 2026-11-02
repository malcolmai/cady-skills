---
name: "cady-company-change-agent-behaviour"
description: "Change agent behaviour. Use when: Change what agents do: edit a skill, role card, run sequence, charter line, tool text or an agent's goal. Not for: Making, scheduling or retiring an agent (`cady-company-manage-agents`), or writing or judging a post or design."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.change_agent_behaviour"
  version: "c9f10bf148b0f6f675c8"
  library: "74d98e825b54225d"
  function: "company"
---
# Change agent behaviour

**Point:** Change one agent behaviour at its strongest single home, proven before it lands, so guidance stays small and undiluted.

**Company context:** `context_read({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.change_agent_behaviour": "c9f10bf148b0f6f675c8@74d98e825b54225d"}})`

Change what agents do: edit a skill, role card, run sequence, charter line, tool text or an agent's goal.

**Not for:** Making, scheduling or retiring an agent (`cady-company-manage-agents`), or writing or judging a post or design.

**Unit of work:** one behaviour change and its record. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Always

- Place the rule and follow what it touches before you edit.
- A rule has one home. Fix the check in code before adding a sentence.
- Add always-on text only by removing a line.

## Inputs

### Evidence refs

- the failure or goal that motivates the change, with the runs or records that show it
- the text or rule being changed, at its current home

## Procedure

1. Place it. A behaviour change states the method's point first and keeps it through revisions. Write the logic first (judgements, evidence and objections, in the method's source-only `logic`), then distil the served text from it; every served line traces to a judgement or dependency in `logic.trace`, and objections never enter served text. State the behaviour you want different in one sentence, with the failure that shows the gap. A rule lives in exactly one home; every other place holds a pointer or one registered cue. Strongest first: code and tool results; the charter, only for what must hold on a host with no skills; recorded decisions; the role card (one function) and the skill (one activity); host and project files, which only point. If code or a tool result can make the rule true, change that and not the text: a sentence that covers for a missing check is a defect in the check. A rule whose absence could cause an unauthorised effect, a cross-company read or a false "done" is enforced in code or the charter, never only in a method. A company's own values (style, thresholds, names) are recorded decisions with a placement, not method text.
2. Size it. A small tweak or cleanup (a typo, a wrong id, a stale fact, a fix a failing check proves) follows the trail: before you edit, find what the text touches (callers, lines and tools that rely on it, neighbouring branches, any registered cue) and check each still holds. Larger is anything that changes what an agent does at a decision, or a cut in always-on, hard-limit or external-facing text, or a cut of a line that prevents a named risk; it takes step 4 as well.
3. Pruning, for any edit: keep a line if it changes behaviour, prevents a named risk or carries a decision the agent must not guess; cut it if it repeats another line, restates a rule served elsewhere or pads. When you cut a line another served line carries, name the kept line. Always-on text is paid for in every session: add a line there only by removing one.
4. A larger behaviour change, in order. (a) Refine what is useful: say what a good result is in the domain's own best practice and cut what does not serve it before adding anything. (b) Walk the full flow as it runs today, from the product's flow maps in Cady (`records_read file:<id>`) or its repository diagram maps: its branches, what each relies on, the upstream and downstream effects that matter. (c) Pick a few key cases, consolidated, sized to the biggest risks and how deep the complexity is, and include the nearby case that must not change. Run them with and without the change. Write the checks first, one per dimension, and score each separately so one strong point cannot hide a regression. Run by hand only for a single decision point with no tool or schema effect (enough for a fork). Land when it is clearly better and the nearby case is unchanged. Record the cases and result in the PR body and the behaviours register row. Take most care with sends, spend, permissions and anything a customer or recipient sees. Write the text with `cady-company-taste-review`.
5. Guard it so it does not drift: a behaviours register row (id, the departure it prevents, its home), a deterministic regression test at the lowest layer, and any repeated cue registered against the id. A fork without a register records one decision for the same facts.
6. Review, then ship and read back. Review per `cady-engineering-independent-review` (two_reviews): the logic review checks the served text against the logic, and the writing review reads the served text alone. Upstream guidance ships as a release; a fork commits it with the reason and records the decision; an agent's goal text goes through agents_update or agents_create or agents_change with the current revision (`cady-company-manage-agents`). Read the served or installed text back and confirm it is what you changed.

## Acceptance

- [ ] (check) the change sits at its one home, with a pointer or registered cue elsewhere and no restated copy
- [ ] (fresh) larger change: key cases judged against checks written first, including the nearby case
- [ ] (person) the owner decided any change to an always-on line, a hard limit or an external-facing line

## Owner checks

- for a larger change, the key cases and their result

## Result

### Artifact refs

- decision:<change-id>
- company:work:<workId>
- **Transition:** the claim holder records the home, the evidence and the readback
