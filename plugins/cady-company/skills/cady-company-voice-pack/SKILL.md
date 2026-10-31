---
name: "cady-company-voice-pack"
description: "Build or refresh a texture-only voice pack. Use when: Owner sets up or refreshes how their messages sound, or drafts read generic. Builds the pack from their sent messages. Not for: Drafting rules (relationship, substance, ask: the shared message rules, sender_voice), reviewing or sending outreach (crm.prepare_outreach_review), company brand voice (`cady-company-taste-review`)."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "skill.company.voice_pack"
  version: "869e09b1edb01bcf3b72"
  library: "f7ed85a0f29eb359"
  function: "company"
---
# Build or refresh a texture-only voice pack

**Company context:** `get_cady_context({"area": "ops/records", "task": "<what you are about to do, in one sentence>", "knownMethods": {"skill.company.voice_pack": "869e09b1edb01bcf3b72@f7ed85a0f29eb359"}})`

Owner sets up or refreshes how their messages sound, or drafts read generic. Builds the pack from their sent messages.

**Not for:** Drafting rules (relationship, substance, ask: the shared message rules, sender_voice), reviewing or sending outreach (crm.prepare_outreach_review), company brand voice (`cady-company-taste-review`).

**Unit of work:** one member's pack. **Kind:** execution. **Parallel:** no. **Can release:** no. 

## Always

- Texture only: how the person sounds. Never who to write to, what reason to give or what to ask.
- Never seed from the agent's own reviewed outreach, never copy typos or lowercase as voice, never invent a sent side.
- Avoid lines are quoted phrases or characters a check can find, at most 6; no style judgements.

## Inputs

### Evidence refs

- voice:me
- the owner's pasted samples, or the connectors the owner authorised for reading their own sent messages

## Procedure

1. Read voice:me and keep its revision; an existing pack is a candidate to improve, not truth. If the owner pasted samples, use them and skip collection (still apply step 2). Otherwise read their sent messages read-only and bounded through connectors they authorised (messaging connectors, LinkedIn conversations, Slack, email Sent), preferring replies to people they know, short logistics or decision messages and warm messages they started. Do not interview the owner.
2. Exclude, keeping each reason for the audit: anything prepared through crm.prepare_outreach_review or released under a grant (an interaction with an approvalId, or text matching a review's or grant's copy: a pack seeded with the agent's own copy teaches it to imitate itself); sequence, campaign or bulk sends; cold first touches since 2023 unless the owner says they typed them; the same text sent to several people; materials such as decks and posts; quoted or forwarded text. Flag possible AI with the tells part of the taste check (`../../references/taste-check.md`); the owner may reinstate any, and their verified pre-2023 habits win.
3. Include an example only when you are confident it is the owner's own organic writing at the target texture; when in doubt leave it out. Zero examples is a valid, good outcome (a pack may be description and avoid lines only); prefer 3 to 5 strong ones when they exist. Choose for spread, not polish: two channels if they write in several, replies plus one they started, one short and one longer, and each relationship stage they write in. Put the most typical email and chat first (the drafting summary shows the first two for the channel). Paste each exactly as sent with channel, stage, origin organic and a sourceRef they can reopen. Pick for rhythm and warmth; a typo, lowercase or slang is a quirk of one moment, never the voice, so never choose a message for it and never add one. Add contrasts only from real rewrites: an agent draft the owner rewrote becomes {draft, sent, note naming the texture that differs}, origin owner_rewrite. With no real rewrites, skip contrasts and never write a sent side yourself. Never pad to reach a count.
4. Describe texture only, with counts and verbatim fragments, the 300 most decisive characters first (the summary clips there): length and rhythm, openings and sign-offs by stage, punctuation, casing, warmth markers, spelling. Write nothing about who to address, what reason to give, what to offer or ask: the shared message rules own those. Content order and ask shape are not texture; the shared message rules own them. Add no personalisation rules. Write at most 6 avoid lines, each a quoted phrase or a character from the owner's rejected drafts or the taste check tells; drop any that restates the baseline or the message rules.
5. Audit with the owner before saving, in chat or a Cady file: each chosen message verbatim with channel, date, stage, sourceRef and why chosen; excluded messages grouped by reason (reviewed or approved copy, template, possible AI with signals, off-voice) so they can reinstate any; the description, contrasts and avoid lines; and, for one real upcoming message, two unlabelled drafts, with and without the pack, for them to pick and edit. Save with crm.manage_voice_pack only after they approve (expectedRevision from step 1). Act on returned warnings by replacing a flagged example with a message they typed. Read voice:me back and report the revision and digest.

## Acceptance

- [ ] (person) the owner approved the exact pack before the write
- [ ] (check) no example is prepared, reviewed, sequenced or templated copy, and the save returned no review-match warning (or the owner knowingly kept it)
- [ ] (check) every example has a sourceRef they can reopen and a relationship stage
- [ ] (check) the description is texture only (counts and verbatim habits), with no relationship, reason or ask rules and no personalisation
- [ ] (check) avoid has at most 6 lines, each a quoted phrase or character
- [ ] (check) the audit listed chosen and excluded messages with reasons and the with/without draft check
- [ ] (check) voice:me readback matches the saved revision

## Owner checks

- the owner approved the exact pack before the write
- voice:me readback matches the saved revision and digest

## Result

### Artifact refs

- voice:me
- **Transition:** the claim holder reports the result

## References
- Read [Avoid and contrast](references/avoid-and-contrast.md) when writing the avoid lines or the with/without draft check.
- Read [Taste check](../../references/taste-check.md) when flagging possible AI writing in the owner's samples.
