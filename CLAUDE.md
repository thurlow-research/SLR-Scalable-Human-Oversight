# Project instructions — SLR (Scalable Human Oversight)

- **Keep the local copy in sync — always.** This working tree (the OneDrive dir; `~/Code/SLR` is
  a symlink to it, one tree not two clones) must be kept current with `origin/main`: pull before
  starting work, and commit + push completed work rather than leaving it sitting uncommitted.
  Canonical remote: `https://github.com/thurlow-research/SLR-Scalable-Human-Oversight.git`.
- The repo is **PUBLIC**. Never commit: copyrighted paper full texts (`slr-phase4/txt/`),
  `Backups/`, `Downloads/`, `.envrc`/secrets, or PDFs — all gitignored; secret-scan staged
  content before every commit (see global instructions).
- **All assistant-authored changes land via PR, never direct to main** (adopted 2026-07-23):
  branch `claude/<topic>` → push → open PR with a summary of what changed and why → Scott
  reviews and approves/merges (bypass at his discretion). The assistant never merges without
  Scott's explicit say-so. After merge: pull `main`, delete the branch (sync rule above).
  This is the project's own oversight thesis applied to itself — AI-authored changes get a
  human inspect-and-gate step. Direct pushes to main are reserved for Scott's own hand edits.
- `main` is protected by a GitHub ruleset (PRs required; Scott holds bypass).
- **Flag model fit at the start of a session, unprompted.** If the work at hand is
  judgment-heavy — pressure-testing taxonomy boundaries, adjudicating contested tags, drafting
  methodology text that lands in the dissertation, resolving panel disagreements — say so and
  recommend Opus before getting into it. Errors in that work become permanent methodology
  entries, not just bad file edits, so a stronger model is worth the cost. For mechanical work
  (writing tags to Zotero, batch scripts, PR mechanics, following an already-settled
  convention), Sonnet is fine — say that too rather than upselling. Scott switches with
  `/model`; the assistant can't. Adopted 2026-08-23, after a full session of boundary
  adjudication ran on Sonnet before the question came up.
- **Literature lookups go through the research MCP** (`papersflow`), not the local `zotero`
  skill CLI — the MCP carries the current keys and retrieval logic. Adopted 2026-09-02. If it
  reports as unauthenticated, run its `authenticate` tool and hand Scott the OAuth URL rather
  than silently falling back to the skill.
- **Read documents from the local copy Zotero already holds — never refetch.** Resolve the
  item's child attachments, take the local path (`~/Zotero/storage/<attachmentKey>/<filename>`),
  and read from disk. Do not re-download a PDF from the publisher, arXiv, or a DOI resolver for
  a document the library already stores.
- **Use the TXT attached to the item; don't convert the PDF yourself.** The corpus keeps a TXT
  beside each PDF precisely so full-text reads are cheap and reproducible — an ad-hoc conversion
  produces text nobody else can reproduce. When the TXT isn't there:
  - **PDF present, no local TXT** → **ask** before converting; on approval use
    `zotero-pdf-to-text` so the result is attached back to the item, not left in a temp dir.
  - **No local copy at all** → **ask** before fetching; don't pull the file unprompted.
  - **Check the attachment labels first.** One item can carry several attachments at different
    authority levels — `59KP8GTP` holds a SUPERSEDED preprint TXT alongside the AUTHORITATIVE
    published PDF. Match the TXT to the version you mean to quote; if the authoritative version
    has no TXT, that is the "ask to convert" case above, not licence to read the superseded one.
  - *Narrow exception:* re-extracting with `pdftotext -layout` is allowed when the corpus TXT's
    reflow has destroyed structure you actually need (multi-column tables), since the stored TXT
    genuinely cannot answer the question. Say so when you do it.
- Project conventions live in the `slr-conventions` skill; methodology source of truth is
  `Methodology/`; the current handoff doc in `handoffs/` is the session entry point.
