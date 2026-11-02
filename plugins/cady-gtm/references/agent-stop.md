# Agent stop

## Recognise

- Stop when continuing could harm a person or the account, or when you cannot tell whether a write happened, for example an identity check, restriction or rate-limit notice; bounces, complaints, a blocklist or provider block in send results; a refusal that names no next call. A hold or refusal that names a next call is not a stop: take that call and carry on.
- Stop on a missing or unreadable ref the brief needs.
- **Scope:** Stop all work on the affected account or mailbox at once: prepare, release and send nothing more on it. Work on other accounts goes on.
- **Pause:** If a grant covers it, pause the grant: crm_outreach_grants_update with mode 'pause_grant', grantId, decisionId and nonce (new UUIDs you generate), and reason. Do not pause your own agent record; it must stay active to file this run's report.
- **Report:** Close with one work_report: run {outcome: 'partial', stopCause: {kind, evidenceRef}} (kind: account_check, deliverability, uncertain_write, complaint, refusal, missing_ref), and one item on the work with claim: 'blocked', resultSummary "Stopped: <cause>, <evidence>, <what is paused>" and nextAction the owner's exact step (for example "Owner: clear the LinkedIn check, then resume grant <id>"). That item is your one ask. A stop is not progress: never report the work done.
- **Workaround:** Never retry, wait it out, resend, or switch tool, domain, mailbox, account or browser automation. Settle an uncertain write by reading it back with records_read, never by sending again.
- **Owner:** Change nothing about your own setup or method. The owner, or channel strategy, fixes the cause; only the owner resumes an anomaly-paused grant. Do not request a resume yourself after a stop.
