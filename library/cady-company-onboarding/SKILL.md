---
name: "cady-company-onboarding"
description: "Set up a company and hand over to its Executive. Use when: A new company has no Cady setup yet: record it from what the owner says and set up its Executive agent. Not for: Designing or taking an agent live (`cady-company-manage-agents`), or building a first offering (`cady-gtm-launch`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.onboarding"
  version: "9593a5d89120ac27f56e"
  library: "4b5392d43606292b"
  function: "company"
---
# Set up a company and hand over to its Executive

**Point:** Set up the company in Cady and its Executive agent from the owner's words, then hand over.

**Company context:** `cady_start {"task": "<what you are about to do, in one sentence>"}`

**Bets** (where this differs from the default):
- Save the owner's stated company and focus as the root's point and bets early, in their words, adding nothing. Instead of: Research the company first, then write a fuller point and bets from what was found.
- Infer each function point and its starting bets from the owner's words and mark each guess; ask only what no words of theirs imply and only they hold. Instead of: Ask a questionnaire, or fill the gaps with researched detail the owner never said.
- Set the drafted agents live once bound, and hand over to the Executive once they are live. Instead of: Asking the owner for a go-ahead per agent or for the whole setup before agents go live, or running the company from setup.
- A company that builds software sets up its product system from its product map: the product agent maps the product first and engineering builds from the map. Instead of: Agents tracing the code and sparse documents to decide what to build.

A new company has no Cady setup yet: record it from what the owner says and set up its Executive agent.

**Not for:** Designing or taking an agent live (`cady-company-manage-agents`), or building a first offering (`cady-gtm-launch`).

**Unit of work:** one company's setup. **Kind:** strategy. **Parallel:** no. 

## Inputs

### Evidence refs

- what the owner said or wrote about the company (call notes, a pasted brief, chat)
- anything already recorded: point, bets, goals, decisions, work, prior onboarding

## Procedure

1. Setup gates nothing and starts here: record what you learn as you work, following the public setup page (cadyworks.com/docs/setup/); every write is safe to repeat. `cady setup` shows its first steps, the Connect page hands an AI app the same page, and MCP has no setup tool. Put any step that is a person's to them. This skill adds judgement only: change the company's point (what it is for) or a bet (a choice it is making, with its reason) only where the owner changed it.
2. Record the owner's words first. Once they say what the company does and what they are working on, save that as the company's point and bets with decisions_set, in their words and adding nothing they did not say, before any research.
3. Infer the rest from their words and the company's stage, and mark every inference. For each function's point (what that function is for, such as demand for go-to-market) that the setup asks for, write only what they said or clearly implied; where they are silent, write a labelled guess (a bet with its measure: what would confirm it and what would reject it), never a researched fact, a number or a customer.
4. Ask the owner only what changes the setup and only they can answer: a missing purpose, a conflicting choice, an account or source, who to invite. Ask at most three questions in one message, say what you will do meanwhile, and never ask again what they have answered.
5. The setup drafts one agent each for product, go-to-market and operations; shape each draft's duties and first task from what the company does (a creator business's go-to-market draft leads with content). A company that builds software sets up its product system from its product map: the product draft's first task maps the product with `cady-product-map` (from the repository, or for a new product from the owner's brief), and engineering builds from that map. Bind each draft to where it runs, then set it live (agents_set status live; no go-ahead is asked). A first task prepares work and sends or files nothing.
6. Hand over once the agents are live: from then on the Executive agent runs the company and onboarding ends. A setup is not delivery: a definition or a mock is not a build, and a first offering with its route to customers is `cady-gtm-launch`.
7. Install the host guidance file by following the host instruction on the setup page or in `cady setup`, read it back in the owner's durable company project (never a temporary folder), and keep any instructions already there.

## Acceptance

- [ ] (check) the company's point and bets are the owner's words and add nothing they did not say
- [ ] (check) every function point or bet the owner did not state is labelled a guess
- [ ] (check) at most three questions, batched, each answerable only by the owner and none already answered
- [ ] (person) the owner's own yes before any grant is added; agents go live without a go-ahead, and every outside effect waits for the person's yes or a grant; the Executive runs the company once they are live

## Owner checks

- the owner's quote is stored with the point and bets
- an existing point, bet or agent was reused, not created twice

## Result

### Artifact refs

- company:work:<workId>
- decision:<id>
- **Transition:** the company is recorded in the owner's words with each guess labelled, and the Executive agent runs the company once the agents are live
