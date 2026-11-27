---
name: "cady-company-change-agent-behaviour"
description: "Change agent behaviour. Use when: Change what agents do: edit a skill, role card, run sequence, tool text or an agent's goal. Not for: Making, scheduling or retiring an agent (`cady-company-manage-agents`), or writing or judging a post or design."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.change_agent_behaviour"
  version: "6f3ea94d5b6f2bb3606d"
  library: "8416516769c74893"
  function: "company"
---
# Change agent behaviour

**Point:** Agents act better where they fell short, without growing, duplicating or weakening the guidance agents read.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- If code or a tool result can make the rule true, change that, not the text. Instead of: Add a sentence to the prompt telling the agent to do the right thing.
- Keep reasons, evidence and objections in source-only logic and serve only the distilled rule. Instead of: Put the rationale in the served prompt so the agent understands why.
- Cut any served line that does not trace to a judgement or dependency; always-on text grows only by removing a line. Instead of: Keep a line if it seems helpful or might prevent a problem someday.
- Check once what can be checked, write the wording once from the stated intent, and revise it from patterns across real runs. Instead of: Gate every guidance change on a writing review and key cases, and run review rounds on its wording.

Change what agents do: edit a skill, role card, run sequence, tool text or an agent's goal.

**Not for:** Making, scheduling or retiring an agent (`cady-company-manage-agents`), or writing or judging a post or design.

**Unit of work:** one behaviour change and its record. **Kind:** execution. **Parallel:** no. 

## Inputs

### Evidence refs

- the failure or goal that motivates the change, with the runs or records that show it
- the text or rule being changed, at its current home

## Procedure

1. Place it. Open the changed method's served text with its point, and keep that point through revisions. Write the logic first (judgements, evidence and objections, in the method's source-only `logic`), then distil the served text from it; every served line traces to a judgement or dependency in `logic.trace`. State the behaviour you want different in one sentence, with the failure that shows the gap. A rule lives in exactly one home; every other place holds a pointer to it. Strongest first: code and tool results; recorded decisions; the role card (one function) and the skill (one activity); host and project files, which only point. A rule whose absence could cause an unauthorised effect, a cross-company read or a false "done" is enforced in code, never only in a method. A company's own values (style, thresholds, names) are bets on the node they govern, not method text.
2. Size it. A small tweak or cleanup (a typo, a wrong id, a stale fact, a fix a failing check proves) follows the trail: before you edit, find what the text touches (callers, lines and tools that rely on it, neighbouring branches) and check each still holds. Larger is anything that changes what an agent does at a decision, or a cut in always-on, hard-limit or external-facing text, or a cut of a line that prevents a named risk; it takes step 4 as well.
3. Pruning, for any edit: keep a line if it changes behaviour, prevents a named risk or carries a decision the agent must not guess; cut it if it repeats another line or pads. Record each served line you cut in the method's logic.cuts (date, the line, the kept line that carries it or none, why). A reworded line is recorded with carried_by naming its new form. Run `publish_methods.py --deletion-ledger <base ref> --strict` to list cuts with no row: the ref builds the base's full library projection, and a retired skill's lines are held to the skill that replaces it.
4. A larger behaviour change, in order. (a) Refine what is useful: say what a good result is in the domain's own best practice and cut what does not serve it before adding anything. (b) Walk the full flow as it runs today, from the product's flow maps in Cady (`cady_read file:<id>`) or its repository diagram maps: its branches, what each relies on, the upstream and downstream effects that matter. (c) Reason the causation from transcript evidence first: the analysis earns its place by the clause it changes. Observation verifies, non-gating: the transcript scorecard's counts confirm a behaviour they count, a read of the transcripts confirms the rest, and neither gates. Key cases are optional evidence, not a gate, except for a clause that governs sends, spend, permissions or anything a customer or recipient sees, which takes them before it lands: where a run would settle a doubt, or for such a clause, pick a few, consolidated, sized to the biggest risks, include the nearby case that must not change, and run them with and without the change in the mock or sandbox, with the checks written first, one per dimension, each scored separately so one strong point cannot hide a regression; an A/B read by a person de-risks, real results verify. Record the cases and result in the PR body and the behaviours register row. Write the text once, from the stated intent, for a capable colleague: outcome, constraints, useful judgement and an observable finish line, reusing what already works. Its name and use_when say what it does, when it applies and how it differs from its neighbours; keep the core self-contained and move conditional detail into references; leave out duplicated instructions and checks a tool already enforces. Length alone is not a quality verdict.
5. Guard it so it does not drift: a behaviours register row (id, the departure it prevents, its home), a deterministic test where code holds the mechanism, otherwise the row names its eval; the cut-record check holds the served text. A company's local skill with no register records one decision covering the same facts.
6. Ship, check and read back: queue at hand-back; the change review (`cady-engineering-independent-review`), by an agent that neither produced nor watched the work, covers what can be checked: each statement is true of the code, no line contradicts another line an agent is served, and the publisher and its tests pass; a larger change (step 2) that spans methods or touches always-on, hard-limit or external-facing text gets a plan review before it is built. The wording gets no review rounds: it lands, is used, and changes when a pattern shows across real runs, not when a reviewer or a single case suggests a better sentence. Edit the company's local skill, which is the company's own, and record why; contributing the change upstream is optional; an agent's goal text goes through agents_set with the current revision (`cady-company-manage-agents`). Read the served or installed text back, check its links and named tools resolve, and confirm it is what you changed.

## Acceptance

- [ ] (check) the change sits at its one home, with a pointer elsewhere and no restated copy
- [ ] (fresh) the checkable part checked once: each statement true of the code, no contradiction with another served line; key cases, where run, judged against checks written first, including the nearby case
- [ ] (person) the owner decided any change to an always-on line, a hard limit or an external-facing line; correcting a line that names a call, field or behaviour the code no longer has needs only the review

## Owner checks

- for a larger change, the key cases and their result, where any were run

## Result

### Artifact refs

- decision:<change-id>
- company:work:<workId>
- **Transition:** record the home, the evidence and the readback
