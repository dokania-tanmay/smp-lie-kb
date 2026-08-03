# content/ — lesson template

Generated reading material with practice problems. Root conventions in [../CLAUDE.md](../CLAUDE.md) apply.

One file per topic, `NN-slug.md`, flat, numbered by the lesson number in [00-study-plan.md](00-study-plan.md). Lessons do not correspond 1:1 with `notes/` — `notes/` is three monolithic subject files, `content/` is many small lessons.

## Sizing (hard limits)

- **One lesson ≈ 150 lines.** If it does not fit, the topic is two lessons.
- **3–5 problems per lesson.** Each solvable in under 20 minutes with pen and paper.
- **No problem requiring a result not stated in the lesson, already in `notes/`, or delivered by an earlier-numbered lesson.** Check the prereq chain in [00-study-plan.md](00-study-plan.md) before assuming background.

Small and finishable beats complete. A lesson that gets solved is worth more than one that gets abandoned.

## Structure

```markdown
---
tags: [topic, ...]
---
# <Topic>

**Prereq:** [[note-a]], [[note-b]]        <- must already exist in notes/
**Goal:** one sentence, what you can do after this.

## Definitions
Stated, minimal, in `:::info[Definition]` callouts. Notation fixed here and not changed later.

## Worked example
One concrete instance — a matrix group, explicit entries. Show the computation, not the result.

## Theorems
Statements in `:::tip[Theorem]`. Proofs only when the proof is the lesson; otherwise cite [[@citekey]].

## Problems
1. Recall/state — force recall of a definition.
2. Compute — plug the definition into $SO(3)$ or $SE(3)$.
3. Prove — a corollary reachable in a few lines from the definitions above.
4. Break it — an example where a hypothesis fails and the conclusion does too.

## Solutions
At the bottom, after a `---`. Never inline with the problems.
```

Problem 4 matters most: understanding shows up as knowing where the statement stops being true. Include it.

## The standing question

The repo exists to get **tight, coordinate-free** tube bounds (see [../CLAUDE.md](../CLAUDE.md) § The thesis). So for any quantity a lesson introduces, be explicit about which of the three it is:

1. **Intrinsic** — chart-independent (curvature, injectivity radius, geodesic distance, sectional-curvature bounds).
2. **Chart-dependent but harmless** — computed in a chart, provably equal across charts (Christoffel symbols assembling into $\nabla$; the [[mechanical-systems-on-lie-groups|exterior derivative]]).
3. **Chart-dependent and load-bearing in a bound** — $\sup|\partial g_{ij}|$, $\sup|\partial^2 g_{ij}|$, and friends. **This is the conservatism the project is trying to remove.** Whenever one appears, say what the intrinsic replacement would be.

Where a lesson touches a bound of type 3, the "break it" problem should be exactly that: exhibit two charts giving different constants for the same system.
