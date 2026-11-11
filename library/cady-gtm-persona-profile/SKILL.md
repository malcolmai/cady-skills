---
name: "cady-gtm-persona-profile"
description: "Persona profile. Use when: Write or revise one persona's profile (customer, investor, partner or supplier) before positioning, sourcing or copy. Not for: Choosing the offer or promise (`cady-gtm-offer-and-segments`), sourcing a List (`cady-gtm-tam-map`) or preparing a message."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.gtm.persona_profile"
  version: "6e30b050a9f42f336c45"
  library: "1ff500e2120fed4b"
  function: "gtm"
---
# Persona profile

**Point:** Understand one persona from what they actually do and where they are heading, so positioning, sourcing and copy start there.

**Company context:** `cady_read {"search": {"query": "<what you are about to do, in one sentence>"}}`

**Bets** (where this differs from the default):
- Keep the few pieces of evidence that drove the decision, linked to where each was read. Instead of: Summarise sources into labelled claims and counts ('7 of 10 say X') with no link back to where each was read.
- In fast-moving markets the latest evidence outranks the larger older pile, and the insight should say where the pain is heading. Instead of: Weight evidence by volume, so the largest body of reviews and posts sets the insight whatever its age.
- Thin research is a failure of stopping rule, not of effort: stop when new sources only repeat what you have. Instead of: Gather a fixed number of sources, or stop once a plausible story forms.
- An investor is known by what they did and whether they can still do it, not by their stated thesis. Instead of: Rank investors by their thesis page, website and fit of stated focus.
- Someone who sells to the persona is not evidence for it, but may be a possible partner or a candidate persona of their own, outside the count. Instead of: Count sellers to the persona as members, or throw away their distinct audience.

Write or revise one persona's profile (customer, investor, partner or supplier) before positioning, sourcing or copy.

**Not for:** Choosing the offer or promise (`cady-gtm-offer-and-segments`), sourcing a List (`cady-gtm-tam-map`) or preparing a message.

**Unit of work:** one work item per persona. **Kind:** strategy. **Parallel:** yes. 

## Inputs

### Evidence refs

- the persona (cady_read personas), its assumption decision
- existing profile File, interviews and research quotes

### Work fields

- persona_key

## Procedure

1. Read the persona (cady_read personas: personaKey, profileRef) and its assumption (the persona's hypothesis bet in your context read's orchestrator.bets, or its task). Continue the existing one; do not register a second. Edit the existing profile rather than starting over. Interview evidence enters through `cady-product-customer-interview`.
2. Research across current tools, workarounds, reviews (review sites, forums: what they praise and why they left), recurring complaints with costs, stories, and reasoned inference until new sources only repeat what you have. Where the market moves fast, start from the latest evidence (a month can make it stale). Inferred and unknown lines are assumptions: work leaning on one tests it.
3. Write one profile per persona before positioning, sourcing or copy: a Files document set as profile_ref and cited by the persona's hypothesis bet (evidenceRefs). The page is at most about 400 words and opens with the insight, no status, legend or method header first; below a divider the same File holds the appendix (disqualifiers, assumption register and kill condition, full source list, research log). The page has five parts. (1) The insight: the question, the answer in one or two sentences, how widely it holds (one person, a few independently, or a measured share) and, where the market moves fast, where the pain is heading once today's is solved. (2) Their words: telling words from persona members about themselves, with who and where, including counter-evidence; use the 5-8 most telling exact quotes, each with who and where. A quote in quotation marks is copied verbatim from its source; anything rephrased has no quotation marks. Vendor copy is the market's wording and is labelled rather than treated as the persona's account. (3) What they use now and what it costs them, a short table. (4) How they buy and whom they trust: what starts a search, where they look, which names make a stranger credible; the rest unknown. (5) Unknowns and the next cheapest test. Mark a claim inferred or unknown where it is; keep the one or two sources that carried each insight. Write part 1 last, after a recount: take every flagged source (a seller to the persona, someone outside it, a quote not found at its source, AI or vendor writing) out of the insight support, how-widely count and assumption evidence, then restate the insight on what remains, even if it is unknown.
4. For an investor, read the parts from what they did, not their marketing: the insight is their pattern in the investments made (stage, cheque, sector, lead or follow, how recent; recent deals count most) and whether they can still invest (a fund: its last raise and how far into it; an angel: source of wealth and recent activity); their words are their own posts and talks; what they use now is their portfolio and the competing deals; how they decide is who introduces them and what makes a stranger credible. For a partner, read these as mandate and thesis, how they decide, credibility and published words.
5. Make the decision this work is for: state the profile's insight and keep with it the few pieces of evidence that drove it, each linked to where it was read (URL, File id or interview note id), so the next agent sees why without re-researching. Anything else is context below the divider or omitted. Someone who sells to the persona is not evidence for it; note them as a possible partner or a candidate persona of their own, outside the count. People outside it, stale funds and marketing-only theses are not evidence for that decision. A story is one person’s own account; never merge people or credit words to non-authors. Evidence of no need is recorded against the assumption and stops that angle once it meets the evidence bar in the GTM domain method. Use check_quote when a quote goes into outward copy. Before saving or returning the page, check each figure and deal fact you cite (cheque, fund size, share of rounds led, who led, sector) against its cited page: with check_quote, pass the page's exact words that state it as speakerRole unknown, adding figure for a number; without it, reread the page. What the page does not state gets a page that does, or is written as an estimate with its basis. Save the page as the persona's Cady File with files_set, linked from the persona, and say where it was saved; never leave the profile only in chat.
6. End with the move this profile enables, following the finish-line rule in the reporting section of skill cady-core-run-sequence.

## Acceptance

- [ ] (check) the page opens with the insight and five parts within about 400 words; decision-driving evidence is linked to where it was read and every claim has a reliability label; each cited figure or deal fact is stated by its cited page or written as an estimate with its basis
- [ ] (fresh) a reader can say the question, answer and how widely it holds, without a merged story or sourceless inference
- [ ] (fresh) no flagged source counts toward the insight or its how-widely figure; where the market moves fast the insight says where the pain is heading; an investor insight says what they funded and whether they can still invest
- [ ] (check) the profile is saved as the persona's Cady File, linked from the persona, and the result says where

## Owner checks

- the profile File is set as the persona's profile_ref

## Result

### Artifact refs

- file:<profile>
- **Transition:** the claim holder reports the profile File and its profile_ref
