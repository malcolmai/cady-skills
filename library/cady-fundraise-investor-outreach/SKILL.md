---
name: "cady-fundraise-investor-outreach"
description: "Investor outreach and updates. Use when: Write to investors: a warm intro request, a personalised first note, round follow-ups, or the monthly update send. Not for: Choosing which investors to pitch (use `cady-fundraise-investor-list`), deciding the round (use `cady-fundraise-raise-plan`) or drafting the deck, memo or update (use `cady-fundraise-raise-materials`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.fundraise.investor_outreach"
  version: "49014c31f2b4d4b2bfab54de3c46688d691000a88fce1577d0ebe13e68d00475"
  library: "73aaf078d0621530"
  function: "fundraise"
---
# Investor outreach and updates

**Company context:** `get_cady_context({"area": "gtm/strategy", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.fundraise.investor_outreach": "49014c31f2b4d4b2bfab54de3c46688d691000a88fce1577d0ebe13e68d00475"}})`

Write to investors: a warm intro request, a personalised first note, round follow-ups, or the monthly update send.

**Not for:** Choosing which investors to pitch (use `cady-fundraise-investor-list`), deciding the round (use `cady-fundraise-raise-plan`) or drafting the deck, memo or update (use `cady-fundraise-raise-materials`).

**Unit of work:** one work item per batch of 20 or fewer investors, or one monthly update send. **Kind:** execution. **Parallel:** yes. **Can release:** yes. 

## Inputs

### Evidence refs

- crm:list:<listId> or crm:party:<partyId> from the ranked investor pool
- the round record and the accepted raise plan
- file:<fileId> for the blurb, deck or update

### Statement fields

- roundId
- senderLabel
- each investor's stage and warm path

## Procedure

1. Read the accepted raise plan and the round (crm.manage_company_records action 'get', investor tracks with crm.list_parties mode "tracks" and roundId). Write only to investors in the ranked pool from `cady-fundraise-investor-list`, leads first; read crm.get_party for each before preparing anything.
2. Warm intro first. Where a warm path exists, ask the connector for a double opt-in introduction with a forwardable blurb, as `../../references/intro-request.md` says; build the blurb from the accepted materials, with no traction you cannot source. Write cold only when no credible path exists.
3. First note: one partner per note. Give a sourced, dated reason this partner (a recent deal, a stated thesis or portfolio fit), what the company does for its customer and the result so far in the reader's terms: describe the result, not the work; mechanism waits until they ask how. One ask suited to their process (a 20-minute first meeting, or whether to send the deck). Under 150 words, no attachment, a link only if asked. If a product or buyer fact is missing, keep the draft with that exact gap rather than inventing it.
4. Pace the round from the raise plan: send first notes and intro asks as one batch so first meetings land in its 2 to 3 week window. After a meeting, follow up within a day with the next step and date (an engaged recipient, paced); an investor who never replied gets the unengaged follow-up rule (message rules, follow_up). On a pass, record the reason with crm.set_track and stop. Move each investor's track through its stage with crm.set_track and roundId.
5. Monthly update: send the update drafted with `cady-fundraise-raise-materials` on the plan's fixed send day as one reviewed batch with the same body. Every recipient goes on the marketing lane with a one-line opt-out (message rules, lanes). Answer each reply through `cady-gtm-reply`.
6. Preparation: RECIPIENTS_EXCLUDED for no_basis, destination_unverified, destination_invalid, opted_out, suppressed, deferred, recent_contact; held by SENDING_ACCOUNT_NOT_CONFIRMED, skill_required, claim_required, claim_expired, REPLIED_SINCE_RELEASE, CAP_REACHED, TRACKED_LINKS_OFF. Not held by platform_paused, company_paused, executor_unavailable. Prepare each batch with crm.prepare_outreach_review (recipientBodies, one per investor; a follow-up carries followUp {delayDays, nonRepliersOnly: true}), read crm.get_outreach_review, then follow release. Sent copy, positive interest, a term sheet, signed documents and money received are distinct states; record replies as the outcome check says.

## Acceptance

- [ ] each investor had a warm path tried first, or the note states why it is cold
- [ ] every first note names one partner, a sourced reason and one ask, under 150 words
- [ ] batches follow the raise plan's pacing and every investor's stage is on its track
- [ ] nothing is sent before approval; sent, interest, commitment and funds stay distinct

## Owner checks

- WORK_NOT_FOUND
- METHOD_NOT_CURRENT
- SKILL_CHANNEL_MISMATCH
- investor in the ranked pool and the round
- current contact permission
- COPY_RULE_FAILED

## Result

### Artifact refs

- crm:outreach_review:<approvalId>
- crm:party:<partyId>
- **Transition:** the claim holder reports prepared reviews and track updates

## References
- [Introduction request](../../references/intro-request.md)
- [Outreach message rules](../../references/outreach-message-rules.md)
