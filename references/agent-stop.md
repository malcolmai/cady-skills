# Agent stop

## Recognise

- Account: identity check, CAPTCHA or forced sign-in, restriction, warning, weekly or rate limit, unusual-activity message.
- Deliverability: hard bounces above 2%, complaints above 0.1%, 550 5.7.x or 421 4.7.x, blocklist, low reputation.
- Write: timeout or no receipt.
- Other: complaint or hostile opt-out (record the opt-out as your skill says first), a refusal with no next call, a missing or unreadable ref.
- A hold or refusal that names a next call is not a stop: take that call and carry on.
- **Scope:** Stop all work on the affected account or mailbox at once: prepare, release and send nothing more on it. Work on other accounts goes on.
- **Pause:** If a grant covers it, pause the grant: crm_outreach_grants_update with mode 'pause_grant', grantId, a new decisionId and nonce, and reason. Do not pause your own agent record; it must stay active to file this run's report.
- **Report:** Close with one work_report: run {outcome: 'partial', stopCause: {kind, evidenceRef}} (kind: account_check, deliverability, uncertain_write, complaint, refusal, missing_ref), and one item on the work with claim: 'blocked', resultSummary "Stopped: <cause>, <evidence>, <what is paused>" and nextAction the owner's exact step (for example "Owner: clear the LinkedIn check, then resume grant <id>"). That item is your one ask. A stop is not progress: never report the work done.
- **Workaround:** Never retry, wait it out, resend, or switch tool, domain, mailbox, account or browser automation. Settle an uncertain write by reading it back with records_read, never by sending again.
- **Owner:** Change nothing about your own setup or method. The owner, or channel strategy, fixes the cause; see `outreach-release.md` outcome_check for the grant resume rule. Do not request a resume yourself after a stop.
