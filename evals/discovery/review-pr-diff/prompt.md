---
name: review-pr-diff
description: "An independent review of a diff touching authority, with a verdict, is the review skill."
expected_outcome: "Loads cady-engineering-independent-review through the cady front door"
tags: [discovery, positive]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Review this pull request before we merge it; it changes how API keys are checked.
