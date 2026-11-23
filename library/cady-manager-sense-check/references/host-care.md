# Host care

**Point:** Keep the host able to run its agents, and catch the rare deletion that is not fine.

Memory: read the host's memory before starting each agent. Under 70% start it; from 70% wait; over 80% also stop the heaviest job.

Deletions: before an agent deletes files or database rows, have it say what goes, what uses it and how it comes back. A clear answer (nothing uses it, or it can be restored) lets it proceed; an unclear one goes to the person. This is a second look, not a ban.
