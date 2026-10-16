# Revision guide template — topical notes

The house format for a revision guide or topical notes on one topic: what a child revises from and a parent can teach off.

It is a **formatting convention, not MOE's** — the syllabus prescribes no notes format. `math.md` and the level file stay the authority on what the level covers and on the range limits the guide is written inside; `math-problem-sums.md`, when it ships with this skill, supplies the named concept and the method for a word-problem topic, and where it is absent the heuristics and the bar model in `math.md` do.

## How to fill it

- **One topic, one level, one stream.** A guide spanning two levels hides which range limit applies; write the second as its own guide.
- **The boundary warning is the first thing written and the hardest line to get right.** Name the range limits in the level file's own wording and the above-level route a well-meaning adult reaches for — `x` for the unknown before P6, cross-multiplying a ratio, a calculator where the outcome is tagged *without calculator*.
- **Vocabulary table**: the term as the syllabus words it, a plain-language meaning inside the boundary, and the specific thing children confuse it with — `factor` against `multiple`, "of" as multiplication, a remainder against a decimal answer.
- **Concrete before abstract** in the breakdown, and name the bar-model shape the topic uses — part-whole or comparison.
- **One worked example**, routine or two-step, solved in the taught method with the unit value stated, never with algebra.
- **Every table fits an A4 page with 2.54 cm margins** — a text width of **15.92 cm** (6.27 in). At 11-12 pt a column narrower than about 2.5 cm cannot hold an ordinary word, so six columns is the ceiling and four is comfortable; a table that needs more is two tables. Keep anything unbreakable out of cells — answer lines of underscores, long numbers or equations, URLs — and put answer space below the table instead. Rendered to Word or PDF, set the table to exactly that width, with column widths summing to 15.92 cm and the widest column given to the one carrying prose.
- **Teacher diagnosis last**: the pitfall this topic produces, named as a misconception rather than as carelessness.

## The template

```markdown
# [Level] Mathematics: [Topic Name] – Revision Guide

**Level**: Primary [1–6] | **Stream**: [Standard / Foundation] | **Syllabus**: MOE [Year] Cohort  
**Key Focus**: [Core concept / Sub-strand]  
**Boundary Warning**: [What is OUT at this level, in the level file's wording — e.g. "Denominators not exceeding 12. Do not use letters for the unknown; bars only until P6."]

---

## 1. Key Concept Summary & Vocabulary

*Define core terms using exact MOE vocabulary for the level.*

| Term / Concept | Meaning & Classroom Definition | Common Trap / Misconception |
| :--- | :--- | :--- |
| **[Term 1]** | [Plain-language definition inside the range limits] | [What children commonly confuse it with] |
| **[Term 2]** | [Plain-language definition inside the range limits] | [What children commonly confuse it with] |

### Core Concept Breakdown
- **[Sub-topic A]**: [Scaffolded bullet points; concrete before abstract]
- **[Sub-topic B]**: [Classification rules, properties, or formulas]

---

## 2. Problem-Solving Strategy (Heuristics / Model Representation)

- **Step 1 — Identify the concept**: [e.g. *Part-Whole*, *Comparison*, *Remainder / Branching*, *Constant Difference*, *Units and Parts*]
- **Step 2 — Set up the model**: [Describe the bar units clearly — how many units, what each bar stands for, where the difference sits]
- **Step 3 — State the unit value**: `1 unit = ...`
- **Step 4 — Answer the question asked**, with the unit and a statement naming what was found.

---

## 3. Quick Check & Worked Example

**Example Problem**:  
[Routine or 2-step problem in a Singapore context, inside the range limits]

**Step-by-Step Solution & Teacher Notes**:
- **Taught Method**: [Bar model, then the working line by line, with the unit value]
- **Teacher Diagnosis**: [The pitfall this topic produces — e.g. "Solves for 1 unit and stops, instead of answering for 3 units", or a missing unit in the final answer]
```

## Check the guide against itself

Read the worked example back against the boundary warning you wrote at the top. A guide whose own example needs a step the warning rules out is the common failure here, and it is also the most convincing version of the error — the child learns the above-level route from the page meant to keep them off it.
