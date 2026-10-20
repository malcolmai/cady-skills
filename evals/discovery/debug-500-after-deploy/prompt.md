---
name: debug-500-after-deploy
description: "A reproducible production failure with users affected is incident response and root-cause work, not report triage."
expected_outcome: "Loads cady-engineering-debugging through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Since this morning's deploy the orders page returns a 500 for every user. Find out why and fix it.
