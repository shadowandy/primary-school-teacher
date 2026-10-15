# AGENTS.md

## What this repo is

The **deliverable is the skills**, not an application. The three skills in `skills/` are the product being built here — they are not harness configuration that happens to sit beside the real code, and there is no app to run, build or test.

| Skill | Subjects | References |
|---|---|---|
| `primary-school-math-teacher` | Mathematics P1-P6, Standard and Foundation | `math.md` → `math-levels/` (4), `math-problem-sums.md`, `paper-template.md`, `revision-guide-template.md` |
| `primary-school-science-teacher` | Science P3-P6, Standard and Foundation | `science.md`, `science-answering-techniques.md` → `science-answering/` (5), `paper-template.md`, `revision-guide-template.md` |
| `primary-school-language-teacher` | English P1-P6 by band; Chinese 华文 / 高级华文 / 基础华文 | `english.md`, `chinese.md`, `chinese-characters.json` |

Each teaches, sets practice for, marks and answers questions about its part of the Singapore MOE primary syllabus. Below, a bare `references/…` path means that file inside whichever skill the table above gives it to. Each skill's `SKILL.md` has how that skill behaves. `README.md` carries the layout and the full provenance story — which edition each reference was distilled from, how each PDF was read, how the character data was checked — so it is what answers *where did this come from*. What follows here is the rules that constrain an edit, not the history behind one.

Work in this repo is therefore almost always one of: distilling more of a syllabus PDF into a reference, correcting a reference against its source, or changing how a skill reasons.

## Syllabus content comes from `docs/`, never from memory

This is the rule the repo exists to protect. Every factual claim in a reference — a topic, a level, a boundary, a character count — traces to a PDF in `docs/syllabus/`. Extract it and read it with the repo's own tool, which labels each page so a reference can cite one:

```sh
tools/pdf_to_markdown.py --outline docs/syllabus/syllabus-primary-math.pdf
tools/pdf_to_markdown.py --pages 31-40 docs/syllabus/syllabus-primary-math.pdf
```

Plausible-sounding syllabus content is the failure mode here, because MOE syllabuses are close enough to other countries' that invented detail reads as correct. A parent setting a paper from a fabricated boundary has no way to catch it. When `docs/syllabus/` is silent on something a user needs, say it is not in the source rather than filling the gap.

Before recording something as unrecoverable, try harder than text extraction. The per-grade spans of the Chinese objectives were documented as lost for exactly that reason — the syllabus marks them with colour shading — and they turned out to be sitting in the PDF as vector fill paths, one per course colour, recoverable by mapping each shaded cell against the grade-header glyph centres. A layout or vector read is worth attempting on any table whose meaning is carried by colour, rule or position rather than by text.

### The authoring tools

Both scripts in `tools/` sit at the repo root rather than inside a skill: they read `docs/`, which never ships **with the skills**, so they are authoring equipment and belong to no one subject. (`docs/syllabus/` is tracked and does reach a clone; only `docs/references/` is ignored.) Each runs itself through `uv` with no install step, and `--help` is the authority on its flags — worth knowing that you reach for:

- `pdf_to_markdown.py --layout` for the wide Science outcome tables, whose three columns markitdown interleaves; `--out-dir` for whole documents.
- `parse_chinese_characters.py --write` to actually regenerate `chinese-characters.json`. The invariant checks below always run whatever flags you pass, and the script exits non-zero **without writing** when one fails, so a bad parse cannot land.

## Quote boundaries, don't paraphrase them

A **boundary** is a syllabus statement that an idea is *not required* at a level, and it is the most load-bearing content in the references. Each subject states its boundaries in its own idiom, which is the main reason the three skills are separate documents:

| Subject | How the boundary appears | Where |
|---|---|---|
| Science | prose "not required" statements, reproduced close to verbatim | collected under `Boundaries` in `science.md` |
| Math | range limits inside the learning outcomes | the `math-levels/` file for the level |
| English | the band at which an outcome begins | a **Not yet at this band** line closing each of the six Areas in `english.md` |
| Chinese | the grade at which an objective begins, per course | spans written `[CL 3-6 · HCL 3-6 · FCL 5-6]` in `chinese.md` |

Paraphrase loses the precision that makes a boundary usable. "The terms transparent/translucent/opaque are not required" tells you what to say instead. "Keep light simple at P4" does not. Where a boundary is quoted, carry the in-boundary phrasing beside it — *lets most light through* for *translucent*, *food-carrying tubes* for *phloem* — because the phrasing is what an adult reaching past the boundary actually needs.

**A boundary you inferred from absence is a different kind, and gets its own section.** `science.md` keeps `## Foundation outcomes that simply are not there` apart from its quoted `# Boundaries` precisely so the two cannot be confused: those entries are outcomes present on a Standard page with no counterpart on the matching Foundation page, and the file says in so many words that they are "listed separately rather than dressed up as syllabus quotations". They bind just as hard when setting a Foundation paper. Infer this way when you must, then segregate and disclaim it — never merge it into the verbatim list.

**When the source's formatting carries the meaning, say which evidence you used instead.** The Science syllabus marks Foundation exclusions by underlining, which text extraction drops, so `science.md` states outright that it read the per-topic outcome pages instead and names them. The reader can then audit your route, not just your conclusion.

**For Chinese, two conventions ride on the span notation.** A course **not named in a span does not carry that objective at all** — that is how "is X in or out for 基础华文" gets answered. And where HCL begins earlier than CL, that span is **bolded**: `[CL 5-6 · **HCL 4-6**]`. The bold is the only marker of where the courses diverge, so a reparse that re-emits plain spans drops the signal without changing a single character.

## Classroom practice is labelled, and its source is never named

Nothing outside `docs/syllabus/` may be cited as syllabus. Two references carry classroom practice instead, each distilled from a non-MOE PDF kept locally in `docs/references/` and never committed:

- `references/math-problem-sums.md` — the named concepts behind Singapore problem sums.
- `references/science-answering-techniques.md` with the topic files it routes to in `references/science-answering/` — the frames an open-ended Science answer is marked against.

Both are **tracked**, so a clone, an install and a release zip all carry them. What makes that safe is labelling, not absence, and it rests on four properties that any new such file must also have:

1. **It opens by disowning authority.** Literally `**This is not MOE syllabus.**`, then an account of what it actually is, then `math.md` or `science.md` named as the authority on what a level covers.
2. **It tells the agent not to quote it as MOE** — "apply it, but do not quote it as MOE". Disowning authority and forbidding attribution are two separate moves, and the second is the one that stops classroom wording reaching a parent as syllabus. The four template files make the same pair with `It is a **formatting convention, not MOE's**`.
3. **It names no source anywhere** — no title, no publisher, no page citation, not here, not in `README.md`, not in the reference. This is why the two documents go unnamed wherever they are described.
4. **It stands alone.** The source PDFs are not shipped, so everything needed to apply a concept or mark an answer is in the file itself. When you extend either file, the test is whether it still works for an agent that has only that file.

Where such a file's phrasing crosses a boundary — *elastic potential energy* and *stomata* are both excluded — it says so explicitly rather than carrying the term unmarked. The boundary wins over the classroom wording.

**The `(pNN)` marker rule runs the other way for MOE content.** A reference distilled from `docs/syllabus/` carries page markers densely — on the order of one every few lines in `science.md` and `english.md` — as provenance for anyone auditing against the source, and each `SKILL.md` tells the agent they record where a claim came from rather than pointing anywhere to follow. Keep them — Math, English and Chinese write them `(pNN)`, Science `[pNN]`, each consistent within its own files. It is the classroom-practice pair that carries none, and that asymmetry is the point.

Where a reference states something the PDFs do not, it is labelled in place — the Singapore maths heuristics in `references/math.md` are marked classroom practice rather than quoted syllabus, as are the CPA sequence and the bar model, which this edition of the Math syllabus never names, and the English composition marking criteria, which the 2020 EL syllabus does not contain in any form. Keep new additions to that standard: label it, or leave it out.

### Pointers to it stay conditional

Six pointers reach the two classroom-practice references — in `math.md`, `science.md`, the two `SKILL.md` files and the two `revision-guide-template.md` files — and every one is written as conditional even though the files currently ship: read the file when it ships, and otherwise fall back to the syllabus reference, which each pointer names. That way pulling a file back out of version control cannot leave a skill promising content it does not have, a bug this repo has already shipped once.

The hedge has a fixed wording, so grep for that rather than for the filenames:

```sh
grep -rn "when that file ships\|when it ships" $(git ls-files skills)
```

Grepping the filenames instead also matches the intra-cluster links — the router table in `science-answering-techniques.md`, the backlink atop each `science-answering/` topic file — and those are **unconditional by design**, because a cluster ships or does not ship as a unit. Adding hedges inside a cluster is the wrong repair. The two `paper-template.md` files name only `math.md` / `science.md` and are correctly not pointers either; leave them alone.

## Character data has invariants

`references/chinese-characters.json` holds the two 《欢乐伙伴》 character lists as course → semester → **lesson** → {识读字, 识写字}, each leaf a plain concatenated string of characters. A semester carries no aggregate of its own, so the lessons are the single source of truth. 华文 has 96 lessons, 高级华文 100. `tools/parse_chinese_characters.py --write` regenerates it and runs the checks below, refusing to write when one fails.

**Key on (semester, lesson), never on a lesson label alone.** Lesson numbering restarts each *year*, not each semester, so `第一课` names six different character sets — one in each of 一上, 二上, 三上, 四上, 五上, 六上 — and a second semester picks up mid-count (一下 opens at 第十一课, 六下 at 第七课). `chinese.md` states this; it is the likeliest way to read the data wrongly while appearing to succeed, and it is exactly where the reconstitution check's blindness to lesson boundaries bites.

The parse is **geometric, from the table's own ruling lines**, because the gap between the 识读字 and 识写字 columns collapses to a single space whenever the read column is full — whitespace splitting silently produces wrong but plausible data. The rules **shift from page to page**, so they are read per page: a hardcoded column boundary corrupts the later grades, which is the bug this data already suffered once.

Any reparse holds these four, the first three of which failed under earlier wrong column boundaries:

- Every character in a write list appears in some read list, with zero exceptions, in both courses.
- End-of-P6 totals land inside the syllabus's stated bands: 华文 1655 read / 1076 written, 高级华文 1815 / 1425.
- 华文 and 高级华文 read lists are set-identical through 四下 (1219 characters) and diverge from 五上.
- **Reconstitution**: a semester's lessons concatenated in document order byte-match the known-good per-semester data — `parse_chinese_characters.py --baseline <old.json> --check`, over all 48 lists. This is what proves a restructure lossless. It is also **blind to lesson boundaries**: characters shifted between two adjacent lessons still concatenate identically, so where a lesson starts and ends needs its own check against the source.

Check all four before trusting a reparse. Then update everything downstream of the JSON in the same commit: in `references/chinese.md`, the cumulative-by-semester table, the validation table, the lesson-numbers-by-year table and the prose sentence giving 96 and 100; in `README.md`, the four-check list. The counts and the lesson structure are restated in all of those, and nothing checks them against the JSON.

The per-grade spans on the Chapter 4 objectives hold two checks of their own, both of which the current data passes: an independent pixel sample of the page rendered at 3× agrees row for row, and 自评和互评 comes out as CL 5-6 · HCL 4-6, which is what the syllabus's own prose states.

A note on the character bands: the 《欢乐伙伴》 lists and the 2024 syllabus bands coincide only at end-of-P6. At the mid-stage checkpoints they diverge, and **in both directions** — end of P2, recognition runs under band (630 against 700-750) while the 华文 write list runs over it (368 against 300-350); end of P4, recognition is under again (1219 against 1300-1350). The bands are the standard's requirement, the lists are what the series actually teaches, and neither is a parse error. `references/chinese.md` records all three; quote whichever of the two a user is actually asking about, and say which it is.

## The skills are near-duplicates on purpose

**All three `SKILL.md` files run one skeleton**, each section specialised to its subject:

```
## 1. Fix the pitch
## 2. Load the syllabus        ← "Load the language" in the language skill
## 3. Respect the boundary
## 4. Work the mode            ← the four modes, as ### subsections
## Addressing the child        ← unnumbered, after the modes
## Currency
```

Frontmatter is exactly `name` and `description`, and the description follows one formula — scope and levels, then `Use when …` listing the four modes in the order section 4 gives them.

Two of those slots are not specialised at all, and they are the ones to watch:

- **`## Addressing the child` is byte-identical in all three files.** Pure duplication, no subject content. Edit it in one place and the other two are now wrong.
- **`## Currency` differs only in its opening edition sentence**, then shares its closing two sentences verbatim. This is the slot a syllabus rollover changes, so it is where an edition update lands — in the skill, and in `README.md`'s Sources table at the same time.

The four modes under step 4 are identically named in all three — **Tutor**, **Generate practice and papers**, **Mark and diagnose**, **Look up and plan**. Note that the phrase "four modes" is this file's vocabulary and `README.md`'s, never the skills' own: grep for a mode's name, not for "four modes".

**The templates are a second near-duplicate family.** `paper-template.md` and `revision-guide-template.md` exist in the Math and Science skills only — four files, two pairs, tracking each other more tightly than the `SKILL.md` files do: setting the subject name aside, the revision-guide pair diverges in exactly one heading (`2. Problem-Solving Strategy` against `2. Answering Frame`) and the paper pair in one (`Method Marking` against `Chain Marking`). Each pair also shares a closing self-check section whose argument is the same, that a guide whose own worked example needs a step its boundary warning rules out is the most convincing version of the error. The language skill deliberately has neither template, and says instead that neither syllabus prescribes a format.

So a behaviour change to one file is a decision about whether its counterparts need it too. Make that decision explicitly rather than by omission, and say in the commit which counterparts you considered.

### How a reference routes

A reference loads only when its subject is in play, and within a subject the pattern is **router → leaf**:

- The router carries everything not tied to one level or topic — `math.md` has how to teach it, marking conventions, calculator tags, the Standard/Foundation split and the progression chains; `science-answering-techniques.md` has the five moves, the boundary notes and the pitch.
- A leaf carries exactly one level pair or one topic, backlinks to its router, and repeats the provenance line — which edition it was quoted from, that the PDF does not ship, and that `(pNN)` records a page rather than pointing somewhere to follow. A leaf may be the only file an agent opens, so it restates that rather than relying on the router.
- A cross-level question is answered from the router alone.

The router's own table heads its first column `Open`, with a one-line "what's in it" cell per row, so the agent picks a leaf without opening any.

Split a reference into a subdirectory when it grows a per-level or per-topic axis. The directory takes the router's stem, the router stays outside it, and the leaf is named for the span it covers — level pairs for Math (`p1-p2.md`, then stream-suffixed `p5-p6-standard.md`), topic clusters for Science (`heat-and-matter.md`), lowercase and hyphenated either way. `SKILL.md` points only at the router.

Two exceptions already in place: `misconceptions.md` sits in `science-answering/` without being a topic, and `chinese-characters.json` is reached from both `SKILL.md` and `chinese.md` — the one non-Markdown, tool-generated reference, which is why it has invariants of its own.

## Editing conventions

- **A count restated in two files drifts, and nothing here checks it.** `math.md` enumerates the problem-sum concepts in prose while `math-problem-sums.md` carries one section each; "26 misconceptions" is asserted in four separate files; the character counts sit in three. When you add an item, grep the number and the list before committing — and prefer pointing at the authoritative file over restating its contents.
- **Changing a skill's wording or structure**: use the `writing-for-agents` skill. A `SKILL.md` is a document an agent consumes, so it is subject to that skill's own levers — progressive disclosure, single source of truth, positive phrasing over prohibition.
- **Scope**: subject-specific content, boundaries and marking conventions belong in the reference, which loads only when needed. A `SKILL.md` carries what every task in that subject needs — pitch, boundary discipline, the four modes — and nothing a single topic would use.
- **`skills/<name>/` is where a teacher skill lives**, the layout `npx skills add` installs from. `.claude/skills/<name>` and `.agents/skills/<name>` are symlinks into it, so both runtimes see the one copy — edit any of the three paths. Both runtime directories are **gitignored**, so those symlinks are not tracked and a fresh clone has none; the skills CLI restores them.
- **After adding or renaming a skill**, `npx skills add . --list` reads the repo the way an installer does and should print exactly the teacher skills, each with its description. Add the symlink from each runtime directory by hand if the CLI has not.
- **A push to `main` that touches `skills/` publishes a release** — `.github/workflows/release-skills.yml` zips each skill with its folder at the archive root and attaches all three to a `vYYYY.MM.DD-<short sha>` tag, so every release is a complete set and the `latest/download/<skill>.zip` URLs stay valid. Releasing needs nothing by hand; `gh workflow run release-skills.yml` re-releases the current `main` when a release is wanted without a skill edit.
- **`dist/` is ignored and is not release truth.** CI builds its own `dist/` from scratch; whatever sits there locally is a leftover from a hand-run and may be missing a skill entirely. Read the Releases page, not `dist/`.
- **Skills this repo consumes stay out of `skills/`** — `grill-me`, `handoff`, `writing-for-agents` sit in `.agents/skills/`, fetched from `mattpocock/skills` and pinned by hash in `skills-lock.json`. Leave them to the vendoring tool; hand-edits break the hash. `skills/` is what this repo publishes, so nothing vendored belongs there.
- **A new subject is a new skill**, with its own `skills/<name>/SKILL.md`, its own `references/` and a symlink from each runtime directory, rather than another reference bolted onto an existing one. The exception is a second language, which joins `primary-school-language-teacher` behind its subject-routing table.
