# Host care

**Point:** Keep the host able to run its agents, and catch the rare deletion that is not fine.

Memory: before heavy work or a new lane, check whether it fits above a safety buffer; if it doesn't, stop servers and jobs you started, then start it only when it fits.

Deletions: before an agent deletes files or database rows, have it say what goes, what uses it and how it comes back. A clear answer (nothing uses it, or it can be restored) lets it proceed; an unclear one goes to the person. This is a second look, not a ban.
