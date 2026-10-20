---
name: reply-triage-mixed
description: "Answers inside threads the prospects replied to are reply triage, not a new cold cycle or a follow-up."
expected_outcome: "Loads cady-gtm-reply through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Three people answered Tuesday's cold email: one asked about price, one said to talk to their CFO, and one said take me off your list. Handle them.
