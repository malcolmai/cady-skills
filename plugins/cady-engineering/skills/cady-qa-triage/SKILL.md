---
name: "cady-qa-triage"
description: "Bug and flaky-test triage. Use when: Rate a bug's severity, write a reproducible report, triage a flaky test, or verify a fix before closing it. Not for: Finding the root cause and fixing it (use `cady-engineering-debugging`), reviewing a diff (use `cady-engineering-independent-review`) or the release go/no-go decision (QA supplies the evidence; `cady-product-manage` decides)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.qa.triage"
  version: "b1de85f9df42637c49a5"
  library: "f7ed85a0f29eb359"
  function: "qa"
---
# Bug and flaky-test triage

**Company context:** `get_cady_context({"area": "product/<productId>/release", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.qa.triage": "b1de85f9df42637c49a5@f7ed85a0f29eb359"}})`

Rate a bug's severity, write a reproducible report, triage a flaky test, or verify a fix before closing it.

**Not for:** Finding the root cause and fixing it (use `cady-engineering-debugging`), reviewing a diff (use `cady-engineering-independent-review`) or the release go/no-go decision (QA supplies the evidence; `cady-product-manage` decides).

**Unit of work:** one reported failure, from report to verified close. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- the report, failing test or alert
- story:<slug>#<stepId>@<runId> for the affected journey
- the exact build or commit SHA and environment

## Procedure

1. Reproduce before you rate. Search open items first (get_company_work) and add evidence to a duplicate instead of filing again. Try the steps on the reported build and environment, then on current main. Record reproduced, not reproduced (and what you tried) or not attempted. One failed attempt on a different build, account or data shape is not 'cannot reproduce'.
2. Rate severity by user impact, never by fix effort or who reported it. Blocker: a core journey is impossible, data is lost or corrupted, a security, tenant-isolation or authority defect is exposed, or a wrong external effect happens (wrong recipient, double charge); for example sign-in fails for everyone, or one company can read another's records. Respond now: stop the affected path or release, name an owner within the hour, mitigate the same day. Critical: a core journey fails for a segment with no workaround, or shows wrong numbers users will act on; for example an export silently drops rows. Owner today, fix within one to two days and before the next release. Major: a feature is broken but a reasonable workaround exists, or a secondary journey fails; schedule it in the current cycle. Minor: cosmetic, copy or a rare edge with no lasting harm; batch it with nearby work.
3. Adjust and gate. Raise one level when the failure is silent (the user cannot tell it went wrong), irreversible or hits most users; lower one level when it is contained behind a flag or internal only. Severity is impact; priority is when, and belongs to the owner. The company's recorded release policy names which severities block a release; with none recorded, blocker and critical block. Re-rate when evidence changes impact.
4. Write the report so someone else can reproduce it without asking. Title: the observed symptom and where ('CSV export drops rows above 1000', not 'export broken'). Steps: numbered, from a known starting state and named test data. Expected: with its source (acceptance, spec or previous behaviour). Actual: exact error text, status code and ids. Environment: SHA or build, environment, browser, OS or device, account role, data shape and flags. Frequency: every time, or n of m runs. Evidence: capture and log excerpt with timestamps or request id as file:<fileId>. Severity with a one-line reason. A suspected cause only when evidenced, labelled as a hypothesis. Record it with submit_company_work_checkpoint: headline is the report title, status OPEN, dueDate from the response time, evidenceRefs the story step and the File holding the full report. Keep secrets and personal data out; route a security report straight to its owner with restricted evidence.
5. Flaky test: one that passes and fails on the same code. Never add a sleep or raise a timeout as the fix; a bounded retry is allowed only as a quarantined mitigation with owner and date. Never treat a passing rerun as proof. Classify by evidence. Race or timing: fails under load, parallelism or a slow runner, with symptoms such as an element not yet present, an unawaited promise or clock dependence; probe by running it alone 20 to 50 times and under CPU stress; fix by awaiting the actual condition, injecting a fake clock or removing real concurrency from the test. Shared-state contamination: passes alone, fails in the suite or in one order, from leftover rows, caches, globals, env vars, unrestored mocks or fixed ids colliding; probe alone versus with neighbours and bisect the order with the runner's seed or order option; fix the polluter, not the victim, with unique data and explicit teardown. Infrastructure: the failure is outside the code under test, such as runner memory, network or DNS, a provider rate limit, a full disk or a container start timeout, often many unrelated tests failing at once with one error class; read the runner log, not just the assertion, and compare jobs in the same window; fix with hermetic fakes or resource limits and record a known environment failure with an owner. A race in product code is a product bug: report it with its severity.
6. Prove a flaky fix by failure rate: run the same N times under the triggering conditions before and after and report both rates. Quarantine (skip or a known-red tag) only with an owner, a dated reason and an open item; a quarantine without an owner is a silent deletion.
7. Close only against the original failure. Rerun the exact original steps on the fixed SHA in the same environment class, then the neighbouring boundaries the fix touched (another role, empty and large data, the recovery path). Confirm a regression test exists that failed before the fix. Record the verdict on the item: fixed at <sha>, not fixed, or cannot verify with the reason. A producer's 'fixed', a green CI run or a passing related test is not verification.
8. Scale it to the case: a clear typo needs a one-line report and a glance after the fix; a blocker needs the full report, an owner and a timed response.

## Acceptance

- [ ] another person can reproduce the failure from the report alone
- [ ] a flaky test is classified with evidence and failure rates, not rerun until green
- [ ] closure cites a rerun of the original steps on the fixed SHA

## Owner checks

- duplicates searched before filing
- severity rated by impact with a stated reason
- the report carries SHA, environment and evidence Files

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** the finding goes to its fix owner with severity and dueDate; QA records the close verdict
