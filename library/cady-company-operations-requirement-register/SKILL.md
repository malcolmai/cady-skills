---
name: "cady-company-operations-requirement-register"
description: "Requirement register: research, check and record. Use when: Research, independently check and record one compliance requirement as a Cady Projects decision. Not for: Tracking occurrences or events (the calling skill does that), filing, signing or legal advice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company_operations.requirement_register"
  version: "61daeffcd86281dc5989"
  library: "9c7400a46a1d124f"
  function: "company_operations"
---
# Requirement register: research, check and record

**Point:** Settle one compliance requirement from the authority's own source, checked independently, so the register can be trusted.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Research from the authority's own guidance, statute or form first, then dated secondary sources. Instead of: Rely on the summaries and blog posts that rank first in search.
- Check with a fresh reviewer given only the facts and the question, asked for the common mistakes, never shown your conclusion. Instead of: Have someone review your research and conclusion.
- Treat missing evidence as an open question, never as an exemption or a 'not required'. Instead of: Assume the company qualifies for the common small-company exemption when a fact is unknown.

Research, independently check and record one compliance requirement as a Cady Projects decision.

**Not for:** Tracking occurrences or events (the calling skill does that), filing, signing or legal advice.

**Unit of work:** one requirement in one register File (register-filing.md, register-hr.md, register-access.md, register-legal.md or register-contract.md). **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- current decisions under the subject prefix
- official guidance, statute or form
- the company facts the requirement depends on

### Work fields

- subject prefix
- jurisdiction and who the requirement binds
- the question to settle

## Procedure

1. Read the register: one File per kind, named register-<kind>.md, found with files_read q "register <kind>" (q matches name and text terms, so take the hit whose name is exactly that) and read with cady_read; once it exists refer to it by its fil-<n> (replies show it; files_read, files_set and cady_read take it), and the dated work items cite it in evidenceRefs. Note each entry's name and review date. A record past its reviewBy is rechecked before any work relies on it. When a request depends on a saved company policy or contract, read that exact current source and the relevant current owner route before making an absence claim or handoff; report “not found in checked locations” when the search was bounded, never global absence.
2. Research from the authority's own guidance, statute or form first, then dated secondary sources. Do not repeat a broad search when the exact current source and owner route settle the question. Establish the trigger, the deadline or rule, thresholds, who completes it, what proves completion and every exemption.
3. Compare each exemption and threshold with the company's facts: which facts would remove an exemption or start a clock, and how close they are. Missing evidence is an open question, never an exemption or a not-required.
4. Independent check: run one fresh-context subagent given only the facts and the question, not your research or conclusion, and ask it for the common mistakes on this requirement and their consequences. If no subagent is available, use a second dated source. Unresolved disagreement or a material or non-standard case goes to a specialist; until then the requirement stays an assumption.
5. Record one register entry in register-<kind>.md (files_set mode save_text when the File does not exist yet, else mode patch at its expectedGeneration after reading it), named <slug>, lowercase with hyphens. State the rule in at most 1,000 characters with up to 4 dated sources, one short line each, and a check line of at most 300 characters: who or what checked, the verdict and what changed. Add alternatives and the key assumption. Upload longer research as its own File and cite file:<fileId> in the entry. If step 1 found an entry on this subject, replace it in place. An entry with a deadline also gets a dated task (work_set {kind: task, path: operations, due, evidenceRefs: [the register's fil-<n>]}) Mark the entry settled only when the check line holds the findings and no material question is open; otherwise mark it an assumption.

## Acceptance

- [ ] the record carries rule, exemptions considered, dated sources, check findings and reviewBy
- [ ] missing evidence is recorded as an open question

## Owner checks

- official source first
- check by a fresh context given only facts and question
- settled only with recorded check findings
- same-subject entry replaced in place, not duplicated

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** current requirement decision or assumption with a dated review
