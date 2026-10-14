# primary-school-teacher

Three agent skills that know the Singapore Ministry of Education primary school syllabus — **Mathematics**, **Science**, and the two languages, **English and Chinese** — and use it to tutor a child, set practice and papers, mark work, and answer syllabus questions.

| Skill | Covers |
|---|---|
| `primary-school-math-teacher` | Mathematics P1-P6, Standard and Foundation |
| `primary-school-science-teacher` | Science P3-P6, Standard and Foundation |
| `primary-school-language-teacher` | English P1-P6 by band; Chinese 华文 / 高级华文 / 基础华文 |

One skill fires per subject, so a Math question never pays for the Science boundaries or the Chinese character tables. English and Chinese share a skill because they share a shape — outcomes that spiral by band or grade rather than a per-level topic list — and route to one reference apiece.

## Install

```sh
npx skills add shadowandy/primary-school-teacher
```

That offers all three; `--skill primary-school-math-teacher` takes one, and `--list` prints what the
repo carries without installing. The CLI symlinks into each agent directory it finds, so a skill
installed once is visible to every runtime on the machine.

Each skill is also published as its own zip on every update, for a runtime that installs from an
archive rather than from a repo:

```sh
curl -LO https://github.com/shadowandy/primary-school-teacher/releases/latest/download/primary-school-math-teacher.zip
```

The archive unpacks to `primary-school-math-teacher/SKILL.md` and its `references/`. Those
`latest/download/` URLs always serve the current release, and
[Releases](https://github.com/shadowandy/primary-school-teacher/releases) keeps every earlier one.

## Layout

```
skills/
  primary-school-math-teacher/
    SKILL.md                              # pitch discipline, range limits, the four modes
    references/
      math.md                             # router: how to teach, marking, calculator tags, cross-level
      math-levels/
        p1-p2.md                          # content by level: P1, P2
        p3-p4.md                          # content by level: P3, P4
        p5-p6-standard.md                 # content by level: P5, P6 Standard
        p5-p6-foundation.md               # content by level: P5, P6 Foundation
      math-problem-sums.md                # the named problem-sum concepts, K-C-A, worked examples
      paper-template.md                   # house format for a practice/exam paper + marking scheme
      revision-guide-template.md          # house format for topical notes / a revision guide
  primary-school-science-teacher/
    SKILL.md                              # pitch discipline, the prose boundaries, the four modes
    references/
      science.md                          # topics by theme P3-P6, "not required" boundaries
      science-answering-techniques.md     # router: the five moves, boundary notes, pitch
      science-answering/
        heat-and-matter.md                # frames: heat, evaporation/condensation, states of matter
        energy-forces-and-electricity.md  # frames: light, electricity, forces, energy
        living-things.md                  # frames: plant reproduction, photosynthesis, digestion, circulation
        environment.md                    # frames: food webs, adaptation, man's impact
        misconceptions.md                 # the 26 named misconceptions, in topic order
      paper-template.md                   # house format for a practice/exam paper + marking scheme
      revision-guide-template.md          # house format for topical notes / a revision guide
  primary-school-language-teacher/
    SKILL.md                              # pitch discipline, subject routing, the four modes
    references/
      english.md                          # six Areas of Language Learning, by band
      chinese.md                          # 华文 / 高级华文 / 基础华文, unit model, objectives
      chinese-characters.json             # per-lesson 识读字 / 识写字, both courses
tools/
  pdf_to_markdown.py                      # docs/ PDF -> page-labelled Markdown, via markitdown
  parse_chinese_characters.py             # the two 《欢乐伙伴》 PDFs -> chinese-characters.json, checked
docs/
  syllabus/                               # the source MOE syllabus PDFs
  references/                             # the two non-MOE classroom-practice PDFs
```

`skills/<name>/` is the canonical copy — the layout `npx skills add` installs from. `.claude/skills/<name>` and `.agents/skills/<name>` symlink into it, so this repo's own agents see all three while there is still one file to edit.

Both scripts in `tools/` sit at the repo root rather than in a skill: they read `docs/`, which never ships, so they are authoring equipment and belong to no one subject.

All three skills are **model-invoked**: each fires on its own when a primary-level teaching, setting, marking or lookup task in its subject comes up, and each can also be called by name.

## Design

Two ideas carry all three skills, and each `SKILL.md` states them in its own subject's terms.

**Pitch.** Every task begins by fixing the level (P1-P6) and the stream — Math and Science split Standard/Foundation at P5-P6; Chinese runs three separate courses; English is banded P1-2 / P3-4 / P5-6. Nothing else can be right until this is.

**Boundary.** The syllabuses state what is *not required* at each level, and this is where a well-meaning adult most reliably goes above-level — explaining P4 light with "translucent", or P5 plant transport with "phloem", both of which the syllabus explicitly excludes. Each subject states its boundaries differently, which is the main reason the skills are separate documents: Science states them in prose and the reference collects every one verbatim, Math sets them as range limits inside the learning outcomes, and the two languages set them as the level at which an outcome begins. A question that cannot be solved without crossing a boundary is above-level and belongs out of the paper.

Within a skill, a reference is still loaded only when it is needed: an English task does not pay for the Chinese character tables, and a Science task pays for one topic's answer frames rather than all five.

## Reading the sources

`tools/pdf_to_markdown.py` extracts a PDF in `docs/` to Markdown through
[markitdown](https://github.com/microsoft/markitdown). It runs itself through `uv` — no install
step — and needs no argument but a path:

```sh
T=tools/pdf_to_markdown.py
$T --outline docs/syllabus/syllabus-primary-science.pdf     # page count, then one line per page
$T --pages 39-44 docs/syllabus/syllabus-primary-science.pdf --layout
$T --out-dir build docs/syllabus/*.pdf                     # whole documents, one .md each
```

None of these PDFs carry bookmarks, so `--outline` prints a page map instead: the first real line
of each page, with running headers and footers filtered out. That is how you find the window to
read — `p39: Diversity of Living and Non-Living Things … (P3)`.

Extraction is page by page, and each page's output is prefixed `<!-- <stem> pN -->`, so anything
quoted into a reference can cite the page it was read on.

markitdown recovers headings and ordinary tables well. It reads the Science syllabus's wide
three-column outcome tables as interleaved prose, so `--layout` extracts those pages through
`pdftotext -layout` instead, windowed and labelled the same way.

## Sources

Distilled from the PDFs in `docs/`:

| Subject | Document | Edition |
|---|---|---|
| Mathematics | Mathematics Syllabus Primary One to Six | 2021 P1 cohort, updated Oct 2025 |
| Science | Primary Science Syllabus | current |
| English | English Language Syllabus 2020 (Primary) | 2020 |
| Chinese | 《小学华文课程标准2024》 | 2024 P1 cohort |
| Chinese characters | 《欢乐伙伴》生字表 — 华文 and 高级华文 | per-lesson lists |

### How the character lists were extracted, and how they were checked

The two character-list PDFs are three-column tables (lesson · 识读字 · 识写字), one semester per page. Splitting on whitespace fails, because the gap between the read and write columns collapses to a single space whenever the read column is full. They are parsed instead from **the table's own ruling lines** (PyMuPDF `page.get_drawings()`): the vertical rules give the column boundaries and the horizontal rules the rows, and each glyph's own bounding box (`page.get_text("rawdict")`) places it in a cell.

The rule positions **shift from page to page** — the 华文 read|write rule is at x=382.6 on pages 1-4 and 389.7 from page 5 on, and lesson|read walks 162.9 → 169.9 → 177.1 — so the rules are read per page. A hardcoded column boundary silently corrupts the later grades, which is the bug this data suffered once. `tools/parse_chinese_characters.py` does all of this: it regenerates the JSON lesson by lesson, runs the checks below, and refuses to write if any of them fail.

Four independent checks say the parse is sound:

- **Every character in a write list appears in some read list** — zero exceptions across both courses. A child recognises a character before being asked to write it, so this is what the data should look like, and it is the check that caught two earlier wrong column boundaries.
- **End-of-P6 totals land inside the syllabus's own stated bands**: 华文 1655 recognised / 1076 written against bands of 1600-1700 and 1000-1100; 高级华文 1815 / 1425 against 1800-1900 and 1400-1500.
- **华文 and 高级华文 recognition lists are set-identical through P4** (1219 characters), diverging only from 五上. Through the foundation-building stage HCL asks for more *writing* of the same characters — 960 against 736 — not more reading.
- **Each semester reconstitutes**: concatenating a semester's lessons in document order byte-matches the earlier, already-verified per-semester data, for all 48 lists (2 courses × 12 semesters × 2 columns). That is what proved the move to per-lesson lists lossless. It says nothing about where the lesson boundaries fall, so those were checked separately against the source.

### One known gap

《小学华文课程标准2024》 marks the grade at which each individual objective begins using **colour shading** in its tables, which plain text extraction drops. It is recoverable all the same: the shading is a vector fill path per course colour, and mapping each shaded cell to the grade-header glyph centres gives every objective its span. `references/chinese.md` carries them as `[CL 3-6 · HCL 3-6 · FCL 5-6]`, cross-checked against an independent pixel sample and against the one span the syllabus also states in prose.

What the language skill does not carry is MOE's 语言能力描述, the level-by-level proficiency descriptors the objectives were graded against. That is a separate publication, it is not in this repo, and `references/chinese.md` says so rather than approximating it.

Separately, the 2021 Math syllabus names Pólya's four steps and "the use of heuristics" but does not enumerate a heuristics list, and names no problem-sum concepts at all. The common Singapore heuristics are in `references/math.md` and the concepts in `references/math-problem-sums.md`, both labelled as classroom practice rather than quoted syllabus.

## Currency

MOE revises syllabuses on a cycle and schools phase them in by cohort. Each skill is told that when a user's own material disagrees with a reference, their material is the better evidence about the cohort in front of them.
