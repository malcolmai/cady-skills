# Cold email deliverability

## Setup

- Check the sender before the first cycle and after any change; Cady cannot see DNS or mailbox reputation, so the user or host checks and you record what was shown.
- Domain: cold mail goes from a secondary domain that redirects to the main site, at least two weeks old to protect the main domain.
- Authentication: SPF lists only the real senders (one record, under 10 lookups); DKIM signs with the From domain (2048-bit); DMARC exists with reporting, p=none first, quarantine once aligned. Verify on a test send to a seed mailbox that SPF, DKIM and DMARC all show pass.
- Warm-up: a new mailbox sends normal human mail for two to four weeks first, then cold at about 10 a day, rising by about 10 a day each week to 30 to 50 per mailbox at most; add mailboxes rather than push one harder. The company's own cold email caps also apply.
- Record: Cady applies the mailbox's own daily cap (context_read controls.mailboxes, capToday), which is the warm-up limit it enforces; it cannot see the mailbox's age, so record the sending domain, the test-send result and the mailbox's start date in the cycle task's result for the next check to read.
- **Recovery:** For a flagged mailbox, find the cause (stale list, volume jump, broken authentication, links or images, complaint-prone copy) and fix it. After one to two weeks of clean normal mail, return at half the previous volume; see `outreach-release.md` outcome_check for the grant resume rule.
