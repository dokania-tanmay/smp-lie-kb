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
Stated, minimal, in `ad-def` callouts. Notation fixed here and not changed later.

## Worked example
One concrete instance — a matrix group, explicit entries. Show the computation, not the result.

## Theorems
Statements in `ad-thm`. Proofs only when the proof is the lesson; otherwise cite [[@citekey]].

## Problems
1. Recall/state — force recall of a definition.
2. Compute — plug the definition into $SO(3)$ or $SE(3)$.
3. Prove — a corollary reachable in a few lines from the definitions above.
4. Break it — an example where a hypothesis fails and the conclusion does too.

## Solutions
At the bottom, after a `---`. Never inline with the problems.
```

Problem 4 matters most: understanding shows up as knowing where the statement stops being true. Include it.
