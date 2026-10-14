#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pymupdf"]
# ///
"""Parse the two 《欢乐伙伴》 character-list PDFs into per-lesson JSON.

Regenerates `skills/primary-school-language-teacher/references/chinese-characters.json`
as course -> semester -> lesson -> {识读字, 识写字}, and runs the invariant
checks that any reparse of this data has to pass.

    tools/parse_chinese_characters.py --check            # parse and verify only
    tools/parse_chinese_characters.py --write            # verify, then rewrite the JSON
    tools/parse_chinese_characters.py --baseline old.json --check

It reads `docs/syllabus/`, which never ships with the skills, so this is
authoring equipment that only runs on the authoring machine. The JSON it
produces is the artefact that ships.

Why the parse is geometric
--------------------------
Each page is one semester: a three-column table of lesson label · 识读字 ·
识写字. The gap between the read and write columns collapses to a single space
whenever the read column is full, so splitting extracted text on whitespace
yields wrong but entirely plausible data — the failure this file has already
suffered once. Instead the table's own ruling lines are read from
`page.get_drawings()` (four vertical rules: left edge, lesson|read, read|write,
right edge; the horizontal rules are the row boundaries) and every CJK glyph is
assigned to a cell by its own bbox.

The rule positions **shift from page to page** — the 华文 read|write rule is at
x=382.6 on pages 1-4 and 389.7 from page 5 on; lesson|read walks 162.9 → 169.9
→ 177.1 — so the rules are read per page. A hardcoded boundary silently
corrupts the later grades.

The page title and grade label sit above the first horizontal rule and so fall
outside the table. The first table row is the header (课次 / 识读字 / 识写字)
and is skipped by position: 识 occurs in the table body too, so the header
cannot be found by searching for it.
"""

from __future__ import annotations

import argparse
import bisect
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

import pymupdf

REPO = Path(__file__).resolve().parent.parent
TARGET = REPO / "skills/primary-school-language-teacher/references/chinese-characters.json"

PDFS = {
    "华文": REPO / "docs/syllabus/syllabus-primary-chinese-character-list.pdf",
    "高级华文": REPO / "docs/syllabus/syllabus-primary-chinese-character-list-higher.pdf",
}

SEMESTERS = ["一上", "一下", "二上", "二下", "三上", "三下",
             "四上", "四下", "五上", "五下", "六上", "六下"]

READ, WRITE = "识读字", "识写字"
CJK = re.compile(r"[一-鿿]")

# End-of-P6 cumulative distinct totals, and the P1-P4 shared-list size.
TOTALS = {"华文": (1655, 1076), "高级华文": (1815, 1425)}
SHARED_THROUGH_FOUR = 1219


def rules(page: pymupdf.Page) -> tuple[list[float], list[float]]:
    """The table's own ruling lines on this page: (vertical x, horizontal y).

    A rule reaches the page either as a zero-width line or as a hairline
    rectangle, so both shapes are collected.
    """
    vertical: set[float] = set()
    horizontal: set[float] = set()
    for drawing in page.get_drawings():
        for item in drawing["items"]:
            if item[0] == "l":
                p, q = item[1], item[2]
                if abs(p.x - q.x) < 0.6 and abs(p.y - q.y) > 20:
                    vertical.add(round(p.x, 1))
                if abs(p.y - q.y) < 0.6 and abs(p.x - q.x) > 20:
                    horizontal.add(round(p.y, 1))
            elif item[0] == "re":
                rect = item[1]
                if rect.width < 0.6 and rect.height > 20:
                    vertical.add(round(rect.x0, 1))
                if rect.height < 0.6 and rect.width > 20:
                    horizontal.add(round(rect.y0, 1))
    return sorted(vertical), sorted(horizontal)


def glyphs(page: pymupdf.Page) -> list[tuple[float, float, str]]:
    """Every CJK character on the page as (x, y, char), from its own bbox."""
    out = []
    for block in page.get_text("rawdict")["blocks"]:
        for line in block.get("lines", []):
            for span in line["spans"]:
                for char in span["chars"]:
                    if CJK.match(char["c"]):
                        out.append((char["bbox"][0], char["bbox"][1], char["c"]))
    return out


def parse_page(page: pymupdf.Page, where: str) -> OrderedDict:
    """One semester page -> lesson label -> {识读字, 识写字}, in document order."""
    vertical, horizontal = rules(page)
    if len(vertical) != 4:
        raise ValueError(f"{where}: expected 4 vertical rules, got {vertical}")
    if len(horizontal) < 3:
        raise ValueError(f"{where}: expected a header row plus lessons, got {horizontal}")

    cells: dict[tuple[int, int], list[tuple[float, float, str]]] = {}
    for x, y, char in glyphs(page):
        column = bisect.bisect_right(vertical, x) - 1
        row = bisect.bisect_right(horizontal, y) - 1
        if not 0 <= column <= 2:
            continue  # outside the table's left or right edge
        if not 0 <= row < len(horizontal) - 1:
            continue  # the page title and grade label, above the first rule
        cells.setdefault((row, column), []).append((y, x, char))

    def cell(row: int, column: int) -> str:
        # Reading order within a cell is top-to-bottom, then left-to-right.
        return "".join(c for _, _, c in sorted(cells.get((row, column), [])))

    header = [cell(0, i) for i in range(3)]
    if header != ["课次", READ, WRITE]:
        raise ValueError(f"{where}: first table row is not the header: {header}")

    lessons: OrderedDict[str, dict[str, str]] = OrderedDict()
    for row in range(1, len(horizontal) - 1):
        label = cell(row, 0)
        if not label:
            raise ValueError(f"{where}: row {row} has no lesson label")
        if label in lessons:
            raise ValueError(f"{where}: duplicate lesson label {label}")
        lessons[label] = {READ: cell(row, 1), WRITE: cell(row, 2)}
    return lessons


def parse() -> OrderedDict:
    data: OrderedDict[str, OrderedDict] = OrderedDict()
    for course, path in PDFS.items():
        if not path.is_file():
            raise SystemExit(f"{path}: not found — docs/ stays on the authoring machine")
        doc = pymupdf.open(path)
        if len(doc) != len(SEMESTERS):
            raise ValueError(f"{path.name}: {len(doc)} pages, expected {len(SEMESTERS)}")
        data[course] = OrderedDict(
            (semester, parse_page(doc[index], f"{course} {semester}"))
            for index, semester in enumerate(SEMESTERS)
        )
    return data


def semester_string(data, course: str, semester: str, column: str) -> str:
    """A semester's list, derived by concatenating its lessons in order."""
    return "".join(lesson[column] for lesson in data[course][semester].values())


def cumulative(data, course: str, column: str, through: str | None = None) -> OrderedDict:
    """Distinct characters up to and including `through`, in first-seen order."""
    seen: OrderedDict[str, None] = OrderedDict()
    for semester in SEMESTERS:
        for char in semester_string(data, course, semester, column):
            seen.setdefault(char, None)
        if semester == through:
            break
    return seen


def check(data, baseline: Path | None) -> bool:
    ok = True

    def report(passed: bool, line: str) -> None:
        nonlocal ok
        ok = ok and passed
        print(f"{'PASS' if passed else 'FAIL'}  {line}", file=sys.stderr)

    if baseline is not None:
        old = json.loads(baseline.read_text(encoding="utf-8"))
        bad = [
            f"{course} {semester} {column}"
            for course in PDFS
            for semester in SEMESTERS
            for column in (READ, WRITE)
            if semester_string(data, course, semester, column) != old[course][semester][column]
        ]
        report(
            not bad,
            f"reconstitution: 48 semester lists rebuild byte-identically from lessons"
            + (f" — mismatches: {', '.join(bad)}" if bad else ""),
        )

    for course in PDFS:
        read = cumulative(data, course, READ)
        write = cumulative(data, course, WRITE)
        stray = sorted(set(write) - set(read))
        report(not stray, f"{course}: every written character is also read"
                          + (f" — stray: {''.join(stray)}" if stray else ""))
        expected = TOTALS[course]
        report(
            (len(read), len(write)) == expected,
            f"{course}: end-of-P6 totals {len(read)} read / {len(write)} written "
            f"(expected {expected[0]} / {expected[1]})",
        )

    low = set(cumulative(data, "华文", READ, through="四下"))
    high = set(cumulative(data, "高级华文", READ, through="四下"))
    report(
        low == high and len(low) == SHARED_THROUGH_FOUR,
        f"read lists set-identical through 四下: {len(low)} vs {len(high)} "
        f"(expected {SHARED_THROUGH_FOUR} each)",
    )
    five_low = set(cumulative(data, "华文", READ, through="五上"))
    five_high = set(cumulative(data, "高级华文", READ, through="五上"))
    report(five_low != five_high, "read lists diverge from 五上")

    empty = [
        f"{course} {semester} {lesson}"
        for course in PDFS
        for semester in SEMESTERS
        for lesson, cells in data[course][semester].items()
        if not cells[WRITE]
    ]
    if empty:
        print(f"NOTE  lessons with an empty 识写字 list: {', '.join(empty)}", file=sys.stderr)
    for course in PDFS:
        count = sum(len(data[course][semester]) for semester in SEMESTERS)
        print(f"NOTE  {course}: {count} lessons across {len(SEMESTERS)} semesters", file=sys.stderr)
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Parse the 《欢乐伙伴》 character lists into per-lesson JSON."
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help=f"rewrite {TARGET.relative_to(REPO)} (only if every check passes)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="run the invariant checks (implied by --write)",
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        help="a per-semester JSON to check exact reconstitution against",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="write the JSON here instead of to the reference path",
    )
    args = parser.parse_args()

    data = parse()
    payload = json.dumps(data, ensure_ascii=False, indent=1)

    # The checks always run: wrong-but-plausible data is this file's failure
    # mode, so nothing is written that has not just been verified.
    if not check(data, args.baseline):
        print("checks failed — not writing", file=sys.stderr)
        return 1

    if args.out:
        args.out.write_text(payload, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    elif args.write:
        TARGET.write_text(payload, encoding="utf-8")
        print(f"wrote {TARGET}", file=sys.stderr)
    elif not (args.check or args.baseline):
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
