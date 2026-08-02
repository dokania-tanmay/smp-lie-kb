# CLAUDE.md

Knowledge base for proving probabilistic tube guarantees on Lie groups / Riemannian manifolds.
Read [README.md](README.md) for the research pathway and target results. This file is conventions only.

## Layout

| Dir | Owner | Contents |
|---|---|---|
| `refs/` | tool-generated | Source papers (`@citekey.pdf`, `@citekey/` LaTeX tree) + a `@citekey.md` rewrite for cheap retrieval |
| `notes/` | **the user** | Their own understanding. Three monolithic files by subject — geometry, probability, mechanics. Deliberately not atomic |
| `content/` | Claude | Lessons + practice problems, plus `00-study-plan.md`. See [content/CLAUDE.md](content/CLAUDE.md) |
| `tools/` | Claude | `fetch.py` — arXiv LaTeX and Zotero PDFs |

## Rules

1. **Never edit `notes/` unless explicitly asked.** That folder is the record of what the user actually understands — it is the input that tells you where to start, not a scratchpad. Read it before writing any `content/`.
2. [content/00-study-plan.md](content/00-study-plan.md) is the backlog, ordered, with a critical path. When asked what to work on next, start there. Update it as lessons land.
3. In `content/`, new topic ⇒ new file. `notes/` is the exception: it stays three files, and sections get appended to the right one — only on explicit request.
4. Wikilinks only: `[[filename]]`, no path, no extension — this is an Obsidian vault and links resolve by basename. Keep basenames unique across the whole repo.
5. Cite sources as `[[@citekey]]` (Better BibTeX key, matching the file in `refs/`). Add a section pointer in prose: `[[@khanMeansRandomVariables2025]] §3.2`.
6. Callouts use the Obsidian admonition syntax already in the vault: ` ```ad-def `, ` ```ad-thm `, ` ```ad-question `. Use `ad-question` for anything unresolved — do not paper over a gap.
7. Frontmatter is `tags:` only. No status fields, no dates.
8. Math in `$…$` / `$$…$$`. MathJax, not KaTeX.

## Mathematical conventions

- **Matrix Lie groups first.** Loosen to homogeneous manifolds, then Riemannian manifolds. Do not open with the general case.
- **Coordinate-based treatment of intrinsic objects.** Write things in a chart, but only claim results that are chart-independent.
- When a construction has more than one source (most importantly `exp`/`log` — see [[exp-and-log-maps]]), **state which one is meant**. Never silently pick.
- State simplifying assumptions inline at the point of use, not in a global preamble.
- Prefer $SO(3)$ / $SE(3)$ for worked examples: $SO(3)$ when bi-invariance is wanted, $SE(3)$ when its failure is the point.

## Tools

```bash
python tools/fetch.py arxiv 2503.12345 --key khanMeansRandomVariables2025
python tools/fetch.py zotero --tag lie-groups
```

Zotero needs `ZOTERO_API_KEY` and `ZOTERO_USER_ID` in the environment. Stdlib only — do not add dependencies to `fetch.py`.

The tool downloads sources; **converting a paper to `refs/@citekey.md` is your job**, not the tool's. Rewrite it so the key definitions, theorem statements and notation are retrievable without re-reading the PDF.
