# AGENTS.md

## What this repo is

The **deliverable is the skills**, not an application. The three skills in `skills/` are the product being built here — they are not harness configuration that happens to sit beside the real code, and there is no app to run, build or test.

| Skill | Subjects | References |
|---|---|---|
| `primary-school-math-teacher` | Mathematics P1-P6 | `math.md`, `math-levels/`, `math-problem-sums.md`, `paper-template.md`, `revision-guide-template.md` |
| `primary-school-science-teacher` | Science P3-P6 | `science.md`, `science-answering-techniques.md`, `science-answering/`, `paper-template.md`, `revision-guide-template.md` |
| `primary-school-language-teacher` | English and Chinese P1-P6 | `english.md`, `chinese.md`, `chinese-characters.json` |

Each teaches, sets practice for, marks and answers questions about its part of the Singapore MOE primary syllabus. Below, a bare `references/…` path means that file inside whichever skill the table above gives it to. `README.md` has the layout and the provenance of each reference; each skill's `SKILL.md` has how that skill behaves.

Work in this repo is therefore almost always one of: distilling more of a syllabus PDF into a reference, correcting a reference against its source, or changing how a skill reasons.

**The three `SKILL.md` files are deliberate near-duplicates.** Pitch, boundary discipline and the four modes recur in all three, each specialised to its subject — Math's boundaries are range limits, Science's are prose "not required" statements, the languages' are the level an outcome begins. A behaviour change to one is a decision about whether the other two need it too; make that decision explicitly rather than by omission.

## Syllabus content comes from `docs/`, never from memory

This is the rule the repo exists to protect. Every factual claim in a reference — a topic, a level, a boundary, a character count — traces to a PDF in `docs/syllabus/`. Extract it and read it with the repo's own tool, which labels each page so a reference can cite one:

```sh
tools/pdf_to_markdown.py --outline docs/syllabus/syllabus-primary-math.pdf
tools/pdf_to_markdown.py --pages 31-40 docs/syllabus/syllabus-primary-math.pdf
```

The tool lives at the repo root rather than inside a skill: it reads `docs/`, which never ships, so it is authoring equipment and belongs to no one subject.

It runs through `uv` on its own, with no install step. `--help` has the rest; `--layout` is the mode for the wide Science outcome tables, whose columns markitdown interleaves.

`tools/parse_chinese_characters.py` is the other piece of authoring equipment there, reading `docs/` the same way: it regenerates the Chinese character data and checks it. See **Character data has invariants**.

Plausible-sounding syllabus content is the failure mode here, because MOE syllabuses are close enough to other countries' that invented detail reads as correct. A parent setting a paper from a fabricated boundary has no way to catch it. When `docs/syllabus/` is silent on something a user needs, say it is not in the source rather than filling the gap.

Nothing outside `docs/syllabus/` may be cited as syllabus. Two references carry classroom practice instead, each distilled from a non-MOE PDF kept locally in `docs/references/`: `references/math-problem-sums.md`, the named concepts behind Singapore problem sums, and `references/science-answering-techniques.md` with the topic files it routes to in `references/science-answering/`, the frames an open-ended Science answer is marked against. Both are labelled classroom practice throughout, and `references/math.md` and `references/science.md` remain the authority on what a level covers. Where such a file's phrasing crosses a "not required" boundary — *elastic potential energy* and *stomata* are both excluded — the file says so explicitly rather than carrying the term unmarked.

**The two classroom-practice references are tracked**, along with the topic files one routes to, so a clone, an install and a release zip all carry them. What keeps that safe is the labelling, not absence: each file opens by saying it is classroom practice rather than MOE syllabus and names `math.md` or `science.md` as the authority on what a level covers, and neither file identifies its source anywhere. Hold any new one to that standard before tracking it — no title, no publisher, no page citation.

The six pointers into them — in `math.md`, `science.md`, the two `SKILL.md` files and the two `revision-guide-template.md` files — stay written as conditional even so: read the file when it ships, and otherwise fall back to the syllabus reference, which each pointer names. That way pulling a file back out of version control cannot leave a skill promising content it does not have, which is a bug this repo has already shipped once. `grep -rn "math-problem-sums\|science-answering" $(git ls-files skills)` lists every pointer, which is how to check that each still names its fallback.

Those two source PDFs stay on the authoring machine, untracked and **not shipped with the skills**, so both distilled files have to stand on their own: everything an agent needs to apply a concept or mark an answer is in the file itself. When you extend either file, the test is whether it still works for an agent that has only that file.

**Nothing in version control identifies a non-MOE source.** No title, no publisher, no page citation — not here, not in `README.md`, not in a reference. Keep it that way: leave the two classroom-practice documents unnamed wherever they are described, and keep shipped references free of `(pNN)` markers and source lines, which in any case point nowhere for a reader who does not have the document.

What the shipped files must keep is the **labelling**, which is a safety property and not an attribution: each says it is classroom practice rather than MOE syllabus, and names `math.md` or `science.md` as the authority on what a level covers. That holds whether or not the source is named.

Where a reference states something the PDFs do not, it is labelled as such — the Singapore maths heuristics in `references/math.md` are marked classroom practice rather than quoted syllabus, as are the CPA sequence and the bar model, which this edition of the Math syllabus never names, and the English composition marking criteria, which the 2020 EL syllabus does not contain in any form. Keep new additions to that standard: label it, or leave it out.

Before recording something as unrecoverable, try harder than text extraction. The per-grade spans of the Chinese objectives were documented as lost for exactly that reason — the syllabus marks them with colour shading — and they turned out to be sitting in the PDF as vector fill paths, one per course colour, recoverable by mapping each shaded cell against the grade-header glyph centres. A layout or vector read is worth attempting on any table whose meaning is carried by colour, rule or position rather than by text.

## Quote boundaries, don't paraphrase them

A **boundary** is a syllabus statement that an idea is *not required* at a level, and it is the most load-bearing content in the references. Science states its boundaries in prose and they are reproduced close to verbatim; paraphrase loses the precision that makes them usable. "The terms transparent/translucent/opaque are not required" tells you what to say instead. "Keep light simple at P4" does not.

## Character data has invariants

`references/chinese-characters.json` holds the two 《欢乐伙伴》 character lists as course → semester → **lesson** → {识读字, 识写字}; a semester is the concatenation of its lessons, with no aggregate string, so the lessons are the single source of truth. `tools/parse_chinese_characters.py` regenerates it from the PDFs and runs the checks below, refusing to write when one fails.

The parse is **geometric, from the table's own ruling lines** (`page.get_drawings()` for the column and row boundaries, each glyph placed in a cell by its bbox), because the gap between the 识读字 and 识写字 columns collapses to a single space whenever the read column is full — whitespace splitting silently produces wrong but plausible data. The rules **shift from page to page** (the 华文 read|write rule is 382.6 on pages 1-4 and 389.7 from page 5 on), so read them per page: a hardcoded column boundary corrupts the later grades, which is the bug this data already suffered once.

Any reparse holds these four, the first three of which failed under earlier wrong column boundaries:

- Every character in a write list appears in some read list, with zero exceptions, in both courses.
- End-of-P6 totals land inside the syllabus's stated bands: 华文 1655 read / 1076 written, 高级华文 1815 / 1425.
- 华文 and 高级华文 read lists are set-identical through 四下 (1219 characters) and diverge from 五上.
- **Reconstitution**: a semester's lessons concatenated in document order byte-match the known-good per-semester data — `parse_chinese_characters.py --baseline <old.json> --check`, over all 48 lists. This is what proves a restructure lossless. It is also **blind to lesson boundaries**: characters shifted between two adjacent lessons still concatenate identically, so where a lesson starts and ends needs its own check against the source.

Check all four before trusting a reparse, and update the tables in `references/chinese.md` and `README.md` together with the JSON — the counts and the lesson structure appear in all three.

The per-grade spans on the Chapter 4 objectives were recovered the same way, from tables rotated 90° on the page: the shading is a vector fill path per course colour (green 华文, orange 高级华文, pink 基础华文) whose sub-rectangles are the shaded cells, mapped to the 一…六 header glyph centres. Any reparse of those spans holds two checks, both of which the current data passes: an independent pixel sample of the page rendered at 3× agrees row for row, and 自评和互评 comes out as CL 5-6 · HCL 4-6, which is what the syllabus's own prose states.

A note on the character bands: the 《欢乐伙伴》 lists and the 2024 syllabus bands coincide only at end-of-P6. At the mid-stage checkpoints they diverge — end of P2, recognition is 630 against a band of 700-750; end of P4, 1219 against 1300-1350. That is a property of the sources, not a parse error. `references/chinese.md` records it; quote whichever of the two a user is actually asking about.

## Editing conventions

- **Changing a skill's wording or structure**: use the `writing-for-agents` skill. A `SKILL.md` is a document an agent consumes, so it is subject to that skill's own levers — progressive disclosure, single source of truth, positive phrasing over prohibition.
- **`skills/<name>/` is where a teacher skill lives**, the layout `npx skills add` installs from. `.claude/skills/<name>` and `.agents/skills/<name>` are symlinks into it, so both runtimes see the one copy — edit any of the three paths.
- **After adding or renaming a skill**, `npx skills add . --list` reads the repo the way an installer does and should print exactly the teacher skills, each with its description.
- **A push to `main` that touches `skills/` publishes a release** — `.github/workflows/release-skills.yml` zips each skill with its folder at the archive root and attaches all three to a dated tag, so every release is a complete set. Releasing needs nothing by hand; `gh workflow run release-skills.yml` re-releases the current `main` when a release is wanted without a skill edit.
- **Skills this repo consumes stay out of `skills/`** — `grill-me`, `handoff`, `writing-for-agents` sit in `.agents/skills/`, fetched from `mattpocock/skills` and pinned by hash in `skills-lock.json`. Leave them to the vendoring tool; hand-edits break the hash. `skills/` is what this repo publishes, so nothing vendored belongs there.
- **Scope of a reference**: a reference loads only when its subject is in play, so subject-specific content, boundaries and marking conventions belong in the reference rather than in `SKILL.md`. A `SKILL.md` carries what every task in that subject needs — pitch, boundary discipline, the four modes — and nothing a single topic would use.
- **A new subject is a new skill**, with its own `skills/<name>/SKILL.md`, its own `references/` and a symlink from each runtime directory, rather than another reference bolted onto an existing one. The exception is a second language, which joins `primary-school-language-teacher` behind its subject-routing table.
