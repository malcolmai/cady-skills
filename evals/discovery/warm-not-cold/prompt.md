---
name: warm-not-cold
description: "A follow-up to an unanswered cold email belongs to the follow-up method, not a new cold cycle."
expected_outcome: "Loads cady-gtm-warm-email through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Follow up with everyone who didn't answer last week's cold email.
