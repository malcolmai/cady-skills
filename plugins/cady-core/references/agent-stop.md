# Agent stop

**Point:** Stop on real risk or an uncertain write, so harm stays on one account until the owner fixes the cause.

## Recognise

- Stop when continuing could harm a person or the account, or when you cannot tell whether a write happened, for example an identity check, restriction or rate-limit notice; bounces, complaints, a blocklist or provider block in send results; a refusal that names no next call. A hold or refusal that names a next call is not a stop: take that call and carry on.
- Stop on a missing or unreadable ref the brief needs.
- **Scope:** Stop all work on the affected account or mailbox at once: prepare, release and send nothing more on it. Work on other accounts goes on.
- **Pause:** Do not pause your own agent record; it must stay active to file this run's report.
- **Report:** Close with one work_write {id, status: blocked, run: {outcome: 'partial', stopCause: {kind, evidenceRef}}, result "Stopped: <cause>, <evidence>, <what is paused>", next the owner's exact step (for example "Owner: clear the LinkedIn check, then resume grant <id>"). That item is your one ask. A stop is not progress: never report the work done.
- **Workaround:** Never retry, wait it out, resend, or switch tool, domain, mailbox, account or browser automation. Settle an uncertain write by reading it back with cady_read, never by sending again.
- **Owner:** Change nothing about your own setup or method. The owner, or channel strategy, fixes the cause.
