# The siddur moved — 2026-09-20

**It lives at https://sefergraph.com/siddur/index.html now.**

`siddur-shoresh.vercel.app` was deleted on 2026-09-20, together with two forgotten twins that
were serving the identical siddur — `siddur-full.vercel.app` and `siddur-site.vercel.app`.
Three deployments of one thing, all live, none of them mentioned in this README. His
instruction was one home, and this is that.

Nothing was lost or rebuilt. The whole of `site/` — 2,749 static pages: 451 tefillos and the
root pages over 9,618 roots — was copied byte for byte into `sefer-docs/public/siddur/`.
Every link in this tree is relative and nothing references a leading slash, which is why it
mounts under a prefix without a single rewrite. That was measured before the move, not hoped.

**One thing did change, and it is the honest headline: the siddur is behind sign-in now.**
This README used to promise "no install, no account", and the account half is no longer true.
It follows his D4 ruling of 2026-09-19 — *"by public I really mean sign in at this stage,
nothing is public yet"* — which governs everything on sefergraph.com. Sign-in there is a
Sefer API key, and the gate is a single list: `GATED_PREFIXES` in `sefer-docs/lib/seforim/crypto.ts`.
Taking `/siddur` out of that list is what makes it public again, whenever he rules so.

This repo remains the source. It is still where the siddur is built and where a change to it
belongs; `sefer-docs/public/siddur/` is a copy of its output, refreshed by copying `site/`.
