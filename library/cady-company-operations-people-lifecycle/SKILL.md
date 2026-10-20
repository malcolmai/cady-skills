---
name: "cady-company-operations-people-lifecycle"
description: "Joiners, movers and leavers. Use when: Plan, track and verify the paperwork and account access a hire, role change or leaver needs. Not for: Running payroll, buying licences, or employment or immigration legal advice."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company_operations.people_lifecycle"
  version: "bcf4a63e589d1d5f942e81f7a742d15e6f99b387d7c76a21a5c5b4f85e7162a6"
  function: "company_operations"
---
# Joiners, movers and leavers

Plan, track and verify the paperwork and account access a hire, role change or leaver needs.

**Not for:** Running payroll, buying licences, or employment or immigration legal advice.

**Unit of work:** one joiner, mover or leaver event tracked as one Projects work item. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- CRM party and employing entity
- current hr: and access: decisions
- system-of-record links

### Statement fields

- event and worker type; for a leaver, planned or immediate
- role (old role for a mover), manager, employing entity and work jurisdiction
- start date, change date or last day

## Procedure

1. Claim this work item with transition_company_work(action: 'claim'); stop on CONFLICT. Resolve the person with crm.list_parties and crm.get_party or, if missing, add name and work email only through the reviewed CRM import (crm.get_import preview and prepare, then crm.run_import). Resolve the employing entity with crm.manage_company_records (action 'list', then 'get'). Each document lives in its system of record (HRIS, payroll or benefits provider, or Files); Cady keeps references, status and dates only. Never write government ID or tax numbers, bank details, salary or pay, health, disability or leave reasons, reason for leaving, disciplinary, performance or grievance detail, background-check results, immigration details, home address or date of birth into any work text, ask or File; cite the record by its system link or file:<fileId>.
2. Read the current hr: and access: decisions (requirement_register step 1). If access:systems is missing or stale, inventory every system (identity provider, email and calendar, chat, code hosting, cloud hosting, domains and DNS, finance, banking and payroll, HRIS, CRM, Cady, password manager, devices, shared and vendor accounts) with owner, admins, how access is granted and how removal is read back. An unknown owner is a gap to resolve. Upload it (files.upload) and record access:systems citing it, reviewBy at most three months away, then one access:role-<role> per role, each a hypothesis until the register check settles it: each system and access level, least privilege, admin or owner access only as a named, reasoned exception. For a mover, list removals from the old role and additions.
3. Per jurisdiction and worker type, check every paperwork category: worker classification under that jurisdiction's test; the engagement document and its required terms; the right-to-work or eligibility check and when it is due; pre-employment checks needing consent (background, references, licences); tax and payroll registration; benefits and pension or retirement enrolment, including any automatic enrolment duty; policies to acknowledge; confidentiality and IP assignment, explicit for a contractor; what a new role, hours, location or entity triggers; for a leaver, final pay timing with accrued leave and expenses, notices, certificates or statements, benefits exit, return of property and record retention.
4. Research, check and record each new or changed requirement with requirement_register steps 2 to 5. Use subject hr:<jurisdiction>-<worker type>-<requirement> (illustrative: hr:<country>-employee-eligibility-check). statement: what, when relative to the event and who completes it; rationale: exemptions, system of record and proof of completion. Set reviewBy at most six months away. Common mistakes for the checker: eligibility after the start, wrong worker type, missed enrolment or registration deadlines, outdated forms, no IP assignment, wrong retention. For access: records it looks for missed systems, excess access and wrong owners, or a system owner checks. Visa sponsorship, a worker abroad, a dismissal or dispute, or classification risk goes to an employment adviser.
5. Track the event, paperwork and access together, as one Projects work item created with submit_company_work_checkpoint, with methodId and methodVersion from get_cady_context selectedMethod for company_operations (`cady-company-operations-method`; pass function "company_operations" if yours differs) so Ops Deadlines lists it and flags it overdue; skill-bound work is not listed. Set statement (event, role, date), evidenceRefs crm:party:<partyId>, dueDate (the event date) and dependsOn: up to eight step items, each with its own dueDate, one per requirement or small group, access steps grouped by system owner. Reuse existing items. Joiner steps finish before the start: identity account and work email, each system on the role list, device ordered and enrolled, Cady membership only if the role needs it, security setup, paperwork by its deadline. Leaver steps run on the last day, or at once for an immediate leaver. First suspend the identity account, end its sessions and remove Cady membership. Then revoke every system the person held, including non-single-sign-on and shared accounts. Set mail forwarding or auto-reply and delegated mailbox access. Transfer data and ownership (files, repositories, calendars, mail, domains, vendor, billing and system-owner roles, CRM lanes). Confirm no retention duty or legal hold before deleting data or wiping devices. Recover and wipe devices; rotate every shared secret and key the person could use.
6. Offers, signing or sending for signature, tax or payroll submissions, enrolments and account changes need current company authority for that exact act. Without it, prepare the draft or exact change (system, account, action, access level), set the step BLOCKED with the held act in nextAction, then raise an ask alone with submit_company_work_checkpoint (kind "sign", "send" or "access", for the person who holds that authority, readyRefs citing the step); it shows on their Needs you. Asks follow the step 1 privacy list. Cady membership is not an agent tool: an owner or admin invites, changes or removes members in Cady settings, confirming each change. Agents never grant admin or owner access; owner transfer is the owner's own act. Never put passwords, recovery codes, keys, tokens or MFA secrets in work text, Files or chat; rotated secrets go to the company's secret store, recording only the fact and place.
7. A step is done only from readback of its system: the document signed, submitted, enrolled or acknowledged in its system of record, or an admin console, audit log, API or the Cady members list showing the account, role, sessions, licence or device state. Cite the link or a dated File holding no secrets. An assertion, even the owner's or your own, is never done. Reconcile against the inventory: every system the person held has an evidenced end state or an open step. Close the event only when every step has readback. A leaver step past its dueDate is a security exposure: raise it to an owner or admin the same day. Report each step's state (done with evidence, due, overdue, held for whom), residual access risk and next action.

## Acceptance

- [ ] every paperwork category checked, not-applicable ones with the reason
- [ ] one event work item with dated steps covering the paperwork and every system on the role list or held by the leaver
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
- Apply `cady-company-operations-requirement-register` (`../cady-company-operations-requirement-register/SKILL.md`).

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company_operations.people_lifecycle": "bcf4a63e589d1d5f942e81f7a742d15e6f99b387d7c76a21a5c5b4f85e7162a6"}})`
