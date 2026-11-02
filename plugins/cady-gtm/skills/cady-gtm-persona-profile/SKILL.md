---
name: "cady-gtm-persona-profile"
description: "Persona profile. Use when: Write or revise one persona's profile (customer, investor, partner or supplier) before positioning, sourcing or copy. Not for: Choosing the offer or promise (`cady-gtm-offer-and-segments`), sourcing a List (`cady-gtm-tam-map`) or preparing a message."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.persona_profile"
  version: "7f2c480edcf3c76df784"
  library: "633b489e153e68a4"
  function: "gtm"
---
# Persona profile

**Point:** Understand one persona from what they actually do and where they are heading, so positioning, sourcing and copy start there.

**Company context:** `context_read({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.gtm.persona_profile": "7f2c480edcf3c76df784@633b489e153e68a4"}})`

Write or revise one persona's profile (customer, investor, partner or supplier) before positioning, sourcing or copy.

**Not for:** Choosing the offer or promise (`cady-gtm-offer-and-segments`), sourcing a List (`cady-gtm-tam-map`) or preparing a message.

**Unit of work:** one work item per persona. **Kind:** strategy. **Parallel:** yes. **Can release:** no. 

## Inputs

### Evidence refs

- the persona (records_read personas), its hypothesis decision
- existing profile File, interviews and research quotes

### Work fields

- persona_key

## Procedure

1. Read the persona (records_read personas: personaKey, profileRef) and its hypothesis hypothesis:persona.<persona_key>. Read any existing hypothesis:gtm.<persona_key> (or hypothesis:<persona_key>) for this persona and continue it under its recorded subject; do not register a second one under persona. Edit the existing profile rather than starting over. Interview evidence enters through `cady-product-customer-interview`.
2. Write one profile per persona before positioning, sourcing or copy: a Files document set as profile_ref and cited from hypothesis:persona.<persona_key> (evidenceRefs). The page is at most about 400 words and opens with the insight, no status, legend or method header first; below a divider the same File holds the appendix (disqualifiers, hypothesis register and kill condition, full source list, research log). Research across the kinds below until new sources only repeat what you have: current tools, workarounds, reviews (review sites, forums: what they praise and why they left), recurring complaints with costs, stories, and reasoned inference. Where the market moves fast, start from the latest evidence (a month can make it stale). The page: (1) The insight: the question, the answer in one or two sentences, how widely it holds (one case, a pattern across N sources, a measured share) and, where the market moves fast, where the pain is heading once today's is solved. (2) Their words: the 5-8 most telling exact quotes from persona members about themselves, counter-evidence included, each with who and where (vendor copy is the market's wording, labelled); (3) What they use now and what it costs them, a short table; (4) How they buy and whom they trust: what starts a search, where they look, which names make a stranger credible; the rest unknown; (5) Unknowns and the next cheapest test. For an investor, read the parts from what they did, not their marketing: the insight is their pattern in the investments made (stage, cheque, sector, lead or follow, how recent; recent deals count most) and whether they can still invest (a fund: its last raise and how far into it; an angel: source of wealth and recent activity); their words are their own posts and talks; what they use now is their portfolio and the competing deals; how they decide is who introduces them and what makes a stranger credible. For a partner, read these as mandate and thesis, how they decide, credibility and published words. Label every claim with its source and reliability: factual (measured or recorded: their exact words, a purchase, usage data, a survey with method), reputable (established report, review aggregate, press, public pricing), anecdotal (one person's account: review, post, call), inferred (your reasoning from cited lines, naming what would confirm it) or unknown. A story is one named person's own account (never merge people or credit words to non-authors; AI or vendor-written content is not a customer's account); with thin evidence an inference cites its lines or stays unknown. Inferred and unknown lines are hypotheses: work leaning on one tests it. Evidence of no need is recorded against the hypothesis and stops that angle.
3. Write part 1 last, after a recount: take every source you flagged (a seller to the persona, someone outside it, a quote not found at its source, AI or vendor writing) out of the insight's support, the how-widely count and the hypothesis register's evidence, then restate the insight on what is left, even if that leaves it unknown; a label without the recount still misleads the founder. For an investor, a stale fund (no recent deals or no money left) and a thesis found only in their marketing are flagged too. Later edits keep the insight unless evidence changes it. A seller's words are the market's, not the buyer's; one whose needs matter goes in the appendix as a candidate persona.

## Acceptance

- [ ] (check) the page opens with the insight and the five parts, within about 400 words, with a reliability label on every claim
- [ ] (fresh) a reader given only the page can say the question, the answer and how widely it holds, and finds no merged story or sourceless inference
- [ ] (fresh) no flagged source counts toward the insight or its how-widely figure; where the market moves fast the insight says where the pain is heading; an investor's insight says what they funded and whether they can still invest

## Owner checks

- the profile File is set as the persona's profile_ref

## Result

### Artifact refs

- file:<profile>
- **Transition:** the claim holder reports the profile File and its profile_ref
