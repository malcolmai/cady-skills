---
name: filing-not-tax-return
description: "Corporate filings and their due dates are the compliance register; the franchise tax is listed there and handed to the tax cycle."
expected_outcome: "Loads cady-company-operations-compliance-register through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

What does our Delaware C-corp have to file with the state in the next few months?
