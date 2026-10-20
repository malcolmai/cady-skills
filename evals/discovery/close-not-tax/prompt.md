---
name: close-not-tax
description: "A month-end close and its exceptions, not a tax return."
expected_outcome: "Loads cady-accounting-period-close through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Close the books for September and list what the bookkeeper needs to fix.
