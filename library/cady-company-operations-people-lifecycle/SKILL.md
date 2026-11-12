---
name: "cady-company-operations-people-lifecycle"
description: "Joiners, movers and leavers. Use when: Plan, track and verify the paperwork and access for a new hire or contractor, a role change or someone leaving. Not for: Running payroll, buying licences, or employment or immigration legal advice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company_operations.people_lifecycle"
  version: "a04e3c180b0de96055f3"
  library: "ced6b4a7a67c21c5"
  function: "company_operations"
---
# Joiners, movers and leavers

**Point:** Get each joiner, mover and leaver's paperwork and access right, proven by system readback, holding no sensitive personal detail.

**Company context:** `cady_read {"search": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Default a joiner to member access to every company system, with admin access a named, reasoned exception, until the company records a restricted default. Instead of: Apply least privilege per role from day one.
- Close a leaver only when every system on the inventory shows an evidenced end state; raise a leaver step past its due date to an admin the same day. Instead of: Disable the main email or sign-in account and treat offboarding as done.
- Keep only references, status and dates in Cady; documents and personal detail stay in their system of record. Instead of: Store the documents and HR details alongside the tracking for convenience.

Plan, track and verify the paperwork and access for a new hire or contractor, a role change or someone leaving.

**Not for:** Running payroll, buying licences, or employment or immigration legal advice.

**Unit of work:** one joiner, mover or leaver event tracked as one Projects work item. **Kind:** execution. **Parallel:** yes. 

## Inputs

### Evidence refs

- CRM party and employing entity
- the hr and access registers
- system-of-record links

### Work fields

- event and worker type; for a leaver, planned or immediate
- role (old role for a mover), manager, employing entity and work jurisdiction
- start date, change date or last day

## Procedure

1. Resolve the person with crm_read and cady_read party:<partyId> or, if missing, add name and work email only through the reviewed CRM import (crm_lists_set preview (csv, mapping, kind) and status "prepared", then status "running"). Resolve the employing entity from its ops:entity decision line. Each document lives in its system of record (HRIS, payroll or benefits provider, or Files); Cady keeps references, status and dates only. Never write government ID or tax numbers, bank details, salary or pay, health, disability or leave reasons, reason for leaving, disciplinary, performance or grievance detail, background-check results, immigration details, home address or date of birth into any work text, ask or File; cite the record by its system link or file:<fileId>.
2. Read the grant.access-default record and the hr and access registers (requirement_register step 1). With no grant.access-default record, prepare member access to every company system on the inventory for a joiner, the startup default (step 6 says who grants it); if it says restricted, use one access role entry per role in register-access.md (each system and level, least privilege), an assumption until the register check settles it. Admin access is always a named, reasoned exception. If the person gets or holds system access and access:systems is missing or stale, inventory every system with owner, admins, grant route and removal readback (`references/people-checklists.md`, systems inventory), upload it (files_set) and record the systems entry in register-access.md citing it, reviewBy at most three months away; an unknown owner is a gap. A contractor with no access needs no inventory. For a mover, list removals and additions. Only an admin changes the default, as a grant.access-default record (full or restricted) in their own words.
3. Per jurisdiction and worker type, check every paperwork category in the checklists (`references/people-checklists.md`, paperwork categories); a category that does not apply is recorded with the reason. The engagement contract itself (offer, contract or statement of work) goes through `cady-company-operations-contract-checks`: plan before it is signed, act at the start.
4. Research, check and record each new or changed requirement with requirement_register steps 2 to 5. Name the entry <jurisdiction>-<worker type>-<requirement> in register-hr.md (illustrative: <country>-employee-eligibility-check): what is required in one short sentence, then when relative to the event, who completes it, exemptions, system of record and proof of completion. Set reviewBy at most six months away. Common mistakes for the checker: eligibility after the start, wrong worker type, missed enrolment or registration deadlines, outdated forms, no IP assignment, wrong retention. For access: records it looks for missed systems, excess access and wrong owners, or a system owner checks. Visa sponsorship, a worker abroad, a dismissal or dispute, or classification risk goes to an employment adviser.
5. Track the event, paperwork and access together, as one Projects work item created with work_set {kind: task, path: operations} (the method comes from the path), so Ops Deadlines lists it and flags it overdue; skill-bound work is not listed. Set headline (event, role, date), evidenceRefs crm:party:<partyId>, due (the event date) and brief.dependsOn: up to eight step items, each with its own due, one per requirement or small group, access steps grouped by system owner. Reuse existing items. Joiner and leaver steps follow the checklists (`references/people-checklists.md`): joiner steps finish before the start; leaver steps run on the last day, or at once for an immediate leaver, starting with suspending the identity account, ending its sessions and removing Cady membership.
6. Offers, signing or sending for signature, tax or payroll submissions, enrolments and account changes need current company authority for that exact act. Without it, prepare the draft or exact change (system, account, action, access level), set the step blocked with the held act in next (work_set {id, status: blocked, next}), then raise an ask alone with asks_set (kind "sign", "send" or "access", for the person who holds that authority, readyRefs citing the step); it shows on their Needs you. Asks follow the step 1 privacy list. Cady membership is not an agent tool: an admin invites, changes or removes members in Cady settings, confirming each change. Agents never grant admin access; owner transfer is the owner's own act. Never put passwords, recovery codes, keys, tokens or MFA secrets in work text, Files or chat; rotated secrets go to the company's secret store, recording only the fact and place.
7. A step is done only from readback of its system: the document signed, submitted, enrolled or acknowledged in its system of record, or an admin console, audit log, API or the Cady members list showing the account, role, sessions, licence or device state. Cite the link or a dated File holding no secrets. An assertion, even the owner's or your own, is never done. Reconcile against the inventory: every system the person held has an evidenced end state or an open step. Close the event only when every step has readback. A leaver step past its due date is a security exposure: raise it to an admin the same day. Report each step's state (done with evidence, due, overdue, held for whom), residual access risk and next action.

## Acceptance

- [ ] every paperwork category checked, not-applicable ones with the reason
- [ ] one event work item with dated steps covering the paperwork and every system the person gets (all of them under full access, the role list when restricted) or held as a leaver
- [ ] every done step cites readback; every held step names who holds the authority

## Owner checks

- exact CRM party, employing entity and role list
- no sensitive personal data or credentials in work text
- done states only from system readback

## Result

### Artifact refs

- company:work:<workId>
- crm:party:<partyId>
- **Transition:** event with evidenced, dated steps

## References
- Read [People lifecycle checklists](references/people-checklists.md) when you build the system inventory or the joiner and leaver steps.
- Apply `cady-company-operations-requirement-register` when you record or check a paperwork requirement.
