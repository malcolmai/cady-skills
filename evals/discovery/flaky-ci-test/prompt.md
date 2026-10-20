---
name: flaky-ci-test
description: "An intermittent test on unchanged code needs flaky classification (race, shared state or infrastructure) before anyone debugs product code."
expected_outcome: "Loads cady-qa-triage through the cady front door"
tags: [discovery, positive]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

test_invoice_totals fails about one run in ten on CI but always passes on my laptop. What do we do with it?
