---
name: customer-cancellation
description: "Cancellation with one respectful save attempt belongs to the customer lifecycle; the reply copy is a later step."
expected_outcome: "Loads cady-customer-success-lifecycle through the cady front door"
tags: [discovery, competing]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

A customer emailed that they want to cancel at the end of the month. How do we handle it?
