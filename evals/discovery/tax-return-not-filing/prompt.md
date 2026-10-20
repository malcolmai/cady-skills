---
name: tax-return-not-filing
description: "Preparing an income tax return is the entity tax cycle."
expected_outcome: "Loads cady-finance-tax-cycle through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Get our federal corporate income tax return for last year ready for the accountant.
