---
name: "cady-design-wcag-audit"
description: "Accessibility audit (WCAG 2.2 AA). Use when: Audit a web or app interface against WCAG 2.2 AA with real tools and report ranked, reproducible findings. Not for: Visual direction or layout critique (use `cady-design-method`), functional journey QA (use `cady-qa-method`) or a legal conformance statement (needs a qualified specialist)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.design.wcag_audit"
  version: "33381e7d80431aa67dee13efa0f048fff41506de591926e1506cd1cf78c34fe5"
  library: "d9d01922e6210604"
  function: "design"
---
# Accessibility audit (WCAG 2.2 AA)

**Company context:** `get_cady_context({"area": "product/<productId>/ui", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.design.wcag_audit": "33381e7d80431aa67dee13efa0f048fff41506de591926e1506cd1cf78c34fe5"}})`

Audit a web or app interface against WCAG 2.2 AA with real tools and report ranked, reproducible findings.

**Not for:** Visual direction or layout critique (use `cady-design-method`), functional journey QA (use `cady-qa-method`) or a legal conformance statement (needs a qualified specialist).

**Unit of work:** one product surface or journey at one build. **Kind:** execution. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- the build URL and SHA
- story:<slug> for the journeys in scope

## Procedure

1. Scope it. List the journeys and states to cover: sign-in, the core task, forms with errors, dialogs and menus, empty, loading and denied states. Fix the build URL and SHA. Choose at least one desktop screen reader pairing (NVDA with Firefox or Chrome on Windows, or VoiceOver with Safari on macOS) and, for mobile, VoiceOver on iOS or TalkBack on Android.
2. Automated pass first, as leads only: axe DevTools or axe-core (for example @axe-core/playwright in the test suite), Lighthouse accessibility and WAVE. Verify each hit by hand. Automated rules catch only a minority of real issues, so zero violations is not conformance.
3. Keyboard (2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11): put the mouse away and complete each journey with Tab, Shift+Tab, Enter, Space, arrow keys and Esc. Every control is reachable and operable, nothing traps focus, order follows reading order, a dialog keeps focus inside and returns it to its trigger on close, a skip link reaches main content, and the focus indicator is always visible and never hidden under a sticky header or banner.
4. Contrast (1.4.3, 1.4.11, 1.4.1): body text 4.5:1, large text (24px, or 18.66px bold) 3:1, control boundaries, focus rings and meaningful icons 3:1. Check hover, focus, placeholder and text over images, using the browser devtools contrast picker or the Colour Contrast Analyser on rendered pixels. Colour is never the only signal of state or error.
5. Names, labels and errors (1.3.1, 2.5.3, 3.3.1, 3.3.2, 3.3.3, 4.1.2, 4.1.3): read the devtools accessibility tree. Every input has a programmatic label, not a placeholder alone; the visible label text is inside the accessible name; icon-only buttons have names. An error is stated in text, tied to its field, announced through a live region or status, and says how to fix it.
6. Semantics (1.3.1, 2.4.2, 2.4.6, 3.1.1): a unique page title, the lang attribute, one h1 and heading levels that outline the page, landmarks, real lists and tables with headers. Prefer native elements to ARIA; a div with role=button but no keyboard handling fails. Then run each core journey with the screen reader and listen for name, role and state (expanded, selected, checked) and for announcements of dynamic changes.
7. Motion (2.2.2, 2.3.1): content that moves for more than 5 seconds can be paused, and nothing flashes more than three times a second. Honouring prefers-reduced-motion is good practice (2.3.3 is AAA), not AA.
8. Pointer and touch (2.5.7, 2.5.8): targets are at least 24 by 24 CSS px or spaced so a 24px circle fits; aim for 44px on primary touch controls. Any drag has a single-pointer alternative.
9. Zoom and reflow (1.4.4, 1.4.10, 1.4.12, 1.3.4): at 200% zoom nothing is lost; at 320 CSS px wide (1280px at 400%) text content needs no horizontal scrolling; the text-spacing override clips nothing; orientation is not locked.
10. WCAG 2.2 additions: help appears in a consistent place (3.2.6); users are not asked to re-enter what they already gave in the same process (3.3.7); sign-in needs no cognitive test, so paste and password managers work (3.3.8).
11. Report one finding per issue per component, merging repeats of a shared component into one finding with its instances. Each finding: criterion number and name, location (page, state and selector, or story:<slug>#<stepId>), steps with the tool or screen reader used, expected versus actual, who is blocked, a severity from `cady-qa-triage` and a suggested fix. A keyboard trap or an unlabelled primary action on a core journey is a blocker; failing body-text contrast is critical or major. Keep captures as Files and record findings as Projects items. List what passed, what failed and what was not tested with the reason.
12. Also check: text alternatives for images, with empty alt for decorative ones and names for icons (1.1.1); autocomplete tokens on personal-data fields (1.3.5); tooltips and hover or focus menus are dismissible, hoverable and persistent (1.4.13); link text states its purpose (2.4.4); captions and transcripts for media (1.2.x); no context change on focus or input (3.2.1, 3.2.2); a skip link or landmarks bypass repeated blocks (2.4.1).
13. Verify fixes with the same tool and screen reader that found them, then rerun the automated pass.
14. Gotchas: adding aria-label everywhere is not a fix and can hide visible text; aria-hidden on a focusable element creates a ghost stop; an overlay widget does not make a site conformant; a sampled audit never supports a 'WCAG compliant' claim, so state the scope and build audited.

## Acceptance

- [ ] every core journey in scope completed by keyboard and by screen reader
- [ ] findings ranked by user impact with suggested fixes
- [ ] fixed findings re-verified with the tool that found them

## Owner checks

- manual keyboard and screen reader passes, not automated rules alone
- each finding names a WCAG criterion, location and reproduction
- scope, build and untested areas stated

## Result

### Artifact refs

- company:work:<workId>
- file:<fileId>
- **Transition:** findings go to the design or engineering owner; QA verifies each fix
