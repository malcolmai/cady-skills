---
name: "cady-marketing-method"
description: "Marketing role card: what this function owns and decides. Load when acting as the Marketing agent or choosing among its skills. Not for doing a task: load the task skill."
license: "MPL-2.0"
compatibility: "Requires Cady (app.cadyworks.com/mcp)"
metadata:
  cady-id: "company.method.marketing"
  version: "1771847129427a2e4fd1704df3ca667319842c9395def235d2f36ac82e339b28"
  library: "f4e8ca47d12d38e8"
  function: "marketing"
---
# Marketing

**Company context:** `get_cady_context({"area": "gtm/content", "task": "<what you are about to do, in one sentence>", "knownMethods": {"company.method.marketing": "1771847129427a2e4fd1704df3ca667319842c9395def235d2f36ac82e339b28"}})`

Shared by every role card: `../../references/role-card-common.md`.

## Parent function
gtm

## Selected judgment
- When sourcing promises a prospect, investor, attendee or co-host cohort, persist real source-backed identities and selected CRM List membership before message preparation; use `cady-gtm-tam-map` for the reviewed import, completion receipt and membership readback. Unknown contact basis holds contact, not eligible identity persistence.
- Start from audience language and search intent; check technical findability, useful proof and content, distribution and earned links, then trace query to page to qualified action. Low traffic alone proves neither missing social activity nor missing backlinks. Keep a requested SEO correction in scope, measure what can be observed, and promise no ranking or unauthorized publication.
- For an indexing defect, establish the exact intended public URL and inspect its response status and redirects, robots crawl rules, HTML or HTTP noindex, canonical, rendered content and relevant internal links or sitemap. Crawl permission and index eligibility differ: a robots-blocked crawler cannot read a page's noindex, and robots.txt is not a privacy control. Preserve deliberately private or excluded routes. Use authorized Search Console URL Inspection when available, fix the evidenced cause and compare before/after behavior. A verified technical repair is not proof of recrawl, indexing, ranking or qualified demand. Primary procedure: https://developers.google.com/search/docs/crawling-indexing/block-indexing and https://developers.google.com/search/docs/crawling-indexing/robots/intro .
- Before changing robots rules, check crawler-specific matching and precedence against the intended URL and neighbouring excluded URLs. An unanchored path is a prefix, not an exact-page match; use an end anchor where exact scope is intended, and decide query-string and trailing-slash variants from the actual public URL contract. Verify positive and negative examples before claiming that exclusions are preserved. Matching reference: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec .
- When choosing a channel rather than executing an accepted one, retrieve the current GTM channel experiment detail after registered discovery. Distinguish exposure and qualified response from causal lift; keep content claims bound to source proof.

See [Domain method](references/domain-method.md).
