# Integration vendor choice

## Bets

- Reuse a suitable tool the company already has or chose, even when a newer one looks better. Instead of: Recommend the best-in-class tool for the job.
- For messaging and social accounts, prefer the highest-trust route that does the exact operation, and state the account risk of any unofficial connector. Instead of: Pick whichever connector supports the operation, official or not, without naming the account risk.
- Gather broad public or competitor content through search or a selected data provider, never through a signed-in account. Instead of: Browse or scrape walled gardens through the user's logged-in session.
- Treat a connector reviewed on another host or by another company as unreviewed here until its fixes are reproduced and checked on this host. Instead of: Reuse a connector because another host or company already runs it.

## Integrations

- **Social surface:** Own accounts: choose through channel_connectors for the exact operation; prefer an official API that fits, but a knowingly selected unofficial connector is valid with its account risk stated. Verify the actual account (authentication), qualify the chosen operation, read posts and insights, and draft; scheduling and publishing stay with the publication approval. Competitor posts: prefer official discovery (Instagram Business Discovery for public business or creator accounts, YouTube search and channel reads, approved Threads keyword search, X search), then public web search, then a paid public-data vendor proposed under selection, stating whether it uses official APIs or scraping. TikTok's Research API and Meta's Content Library serve vetted researchers only; LinkedIn offers no read of other companies' posts. Never collect through a logged-in account (walled_gardens). Save each post as positioning_context describes.
- **Walled gardens:** For broad public research involving walled gardens, prefer the host's default web search or the user's selected dedicated data provider, within verified access, permissions and spend. Do not scrape search-result pages or use authenticated personal accounts as bulk scrapers. Reserve account-specific access for bounded work requiring private state. A vendor example is not a selected tool, connection proof or authority grant.
- **Point:** Choose the tool that does the exact job with least commitment and risk, reusing what the company already has.
