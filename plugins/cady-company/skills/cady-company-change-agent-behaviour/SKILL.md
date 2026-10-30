---
name: "cady-company-change-agent-behaviour"
description: "Change agent behaviour. Use when: Change what agents do: edit a skill, role card, run sequence, charter line, tool text or an agent's goal. Not for: Making, scheduling or retiring an agent (`cady-company-manage-agents`), or writing or judging a post or design."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.change_agent_behaviour"
  version: "f3639b5a8d50d318dd2e"
  library: "f44961b8fb7e17b5"
  function: "company"
---
# Change agent behaviour

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.change_agent_behaviour": "f3639b5a8d50d318dd2e@f44961b8fb7e17b5"}})`

Change what agents do: edit a skill, role card, run sequence, charter line, tool text or an agent's goal.

**Not for:** Making, scheduling or retiring an agent (`cady-company-manage-agents`), or writing or judging a post or design.

**Unit of work:** one behaviour change and its record. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Always

- Place and classify before you edit; an unclassified change is not reviewed.
- A rule has one home. Fix the check in code before adding a sentence.
- Add always-on text only by removing a line.

## Inputs

### Evidence refs

- the failure or goal that motivates the change, with the runs or records that show it
- the text or rule being changed, at its current home

## Procedure

1. Place it. State the behaviour you want different in one sentence, with the failure that shows the gap. A rule lives in exactly one home; every other place holds a pointer or one registered cue. Strongest first: code and tool results (refusals, recovery, the next call); the charter, only for what must hold on a host with no skills; the company's recorded decisions; the role card (one function) and the skill (one activity); host and project files, which carry identity and point to the rest. If code or a tool result can make the rule true, change that and not the text: a sentence that covers for a missing check is a defect in the check. A rule whose absence could cause an unauthorised effect, a cross-company read or a false "done" is enforced in code or the charter, never only in a method. A company's own values (style, thresholds, names) are recorded decisions with a placement, not method text. The layers doc holds the full rules; in the library, CONTRIBUTING.md carries the fork summary.
2. Classify it, and name the kind in the commit or the record. Kind 1, an obvious fix: a typo, a wrong tool or id, a stale fact, or a fix a failing check already proves. Kind 2, a tightening: a line added or hardened because an agent departed (a new "never", a stop condition, a stricter order). Kind 3, pruning. When unsure, take the stricter kind.
3. Kind 1 and kind 3: edit, then independent review of the diff (the review rule, `cady-engineering-independent-review`); no eval. Pruning rule: keep a line if it changes behaviour, prevents a named risk or carries a decision the agent must not guess; cut it if it repeats another line, restates a rule served elsewhere or pads. Cutting a line another served line carries: name the kept line. A cut in always-on text, a hard limit, an external-facing line or a line that prevents a named risk also takes the comparison in step 4. Always-on text is paid for in every session: add a line there only by removing one.
4. Kind 2: write the expected difference first, as one line at the decision point in positive wording, naming the line it replaces. Prove it with a small eval: the failing case, a thin-evidence variant of it, and a nearby case that must not change; the same model with and without the change, at least 3 trials per arm; a fresh judge scores each case against checks written before the run, one per dimension, never one overall grade. Land it only when it is clearly better and the nearby case is unchanged; a split result extends to 10 trials per arm. Take most care with sends, spend, permissions and anything a customer or recipient sees. A company's fork has a lighter bar: classify the change, run the failing case and one nearby case by hand with and without it, and record a decision naming the line and why. Write the text itself with `cady-company-taste-review` (drafting prompts and skills).
5. Guard it, so the change is seen later and does not drift. Add a row to the behaviours register for the behaviour (its id, the departure it prevents, its home), a deterministic regression test at the lowest layer that proves it (the served text, the tool result or the code), and, if a cue repeats the rule at another decision point, register that cue against the behaviour id with the eval that justified it. A fork without a register records one decision for the same facts.
6. Ship and read it back. Upstream guidance ships as a release; a fork commits it with the reason in the message and records the decision; an agent's goal text goes through manage_company_agent with the current revision (`cady-company-manage-agents`). Read the served or installed text back and confirm it is the text you changed.

## Acceptance

- [ ] (check) the change sits at its one home, with a pointer or registered cue elsewhere and no restated copy
- [ ] (check) a regression test or recorded decision guards the behaviour
- [ ] (fresh) kind 2: judged on the failing case and the nearby case, with the checks written before the run
- [ ] (person) the owner decided any change to an always-on line, a hard limit or an external-facing line

## Owner checks

- the kind and the home named before the edit
- for kind 2, the eval result, or for a fork the recorded nearby-case check

## Result

### Artifact refs

- decision:<change-id>
- company:work:<workId>
- **Transition:** the claim holder records the kind, the home, the evidence and the readback
