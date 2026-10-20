---
name: budget-not-runway
description: "Allocating spend for a period is the budget review; runway is an input it reads."
expected_outcome: "Loads cady-finance-budget-review through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Put together next quarter's budget for hiring and marketing.
