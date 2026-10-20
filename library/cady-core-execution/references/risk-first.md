## Risk first

- Before code, name consequential effects, the company's critical paths and worst failures; derive focused edge-case and security tests, then implement the smallest controls.
- For two emails, journal each logical message separately before dispatch; key by company, operation and message identity. After first success and second timeout, retain the first receipt and reconcile the second with the provider. Never rerun the whole batch or blindly resend an uncertain effect. A local lock alone cannot guarantee exactly-once delivery.
- For effectful integrations, cover relevant failure boundaries: duplicate delivery, crash near provider acceptance, partial success, timeout, rate limit, cancellation, revoked permission and wrong account/tenant. Select tests for changed behavior and plausible consequence; reuse existing evidence where it suffices. Use provider idempotency where supported; otherwise stop ambiguous sends for reconciliation.
- Where untrusted input reaches execution, test relevant source/model manipulation, shell/path/URL injection and secret leakage. Use argument arrays, validated paths/destinations, schema validation, least privilege and redacted receipts. Dry runs must have no external effects; cap calls, tokens, cost, runtime and concurrency.

See [Scheduled model selection](scheduled-model-selection.md).
See [Selection](selection.md).
