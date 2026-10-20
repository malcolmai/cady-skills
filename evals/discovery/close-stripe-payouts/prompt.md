---
name: close-stripe-payouts
description: "Processor payout reconciliation is part of the period close."
expected_outcome: "Loads cady-accounting-period-close through the cady front door"
tags: [discovery, paraphrase]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Our Stripe payouts don't match the revenue in Xero for last month. Sort out the month-end.
