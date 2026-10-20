---
name: wcag-audit-signup
description: "A conformance pass with keyboard, screen reader and contrast checks is the accessibility audit, not visual design critique."
expected_outcome: "Loads cady-design-wcag-audit through the cady front door"
tags: [discovery, boundary]
runs: 3
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Check our signup flow against WCAG 2.2 AA before launch.
