---
name: uk-confirmation-statement
description: "A registry filing, not a tax return."
expected_outcome: "Loads cady-company-operations-compliance-register through the cady front door"
tags: [discovery, paraphrase]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Is our Companies House confirmation statement due yet?
