#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["markitdown[pdf]==0.1.8", "pypdf>=5"]
# ///
"""Extract a syllabus PDF to Markdown, page by page, via markitdown.

Every chunk of output carries the page it came from, so a reference can cite
the page a claim was read on.

    pdf_to_markdown.py --outline docs/syllabus/syllabus-primary-math.pdf
    pdf_to_markdown.py --pages 29-40 docs/syllabus/syllabus-primary-math.pdf
    pdf_to_markdown.py --out-dir out docs/syllabus/*.pdf

markitdown recovers headings and simple tables well. It reads the wide
multi-column tables of the Science syllabus as interleaved prose, so for those
pages pass --layout, which windows and labels the same way over
`pdftotext -layout`. The 《欢乐伙伴》 character lists need neither: they are
parsed from x-coordinates (`pdftotext -bbox-layout`) — see README.md.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from markitdown import MarkItDown
from pypdf import PdfReader, PdfWriter

PAGE_MARKER = "<!-- {name} p{page} -->"


def parse_pages(spec: str, total: int) -> list[int]:
    """Turn "3", "29-40", "1,5,9-11" into a sorted list of 1-based page numbers."""
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        match = re.fullmatch(r"(\d+)(?:-(\d+))?", part)
        if not match:
            raise ValueError(f"cannot read page spec {part!r}")
        first = int(match.group(1))
        last = int(match.group(2) or first)
        if first < 1 or last < first:
            raise ValueError(f"page range {part!r} is backwards or starts below 1")
        pages.update(range(first, min(last, total) + 1))
    if not pages:
        raise ValueError(f"page spec {spec!r} selects nothing")
    return sorted(pages)


BOILERPLATE = re.compile(r"^(?:[ivxlcdm\d.\s|-]+|page\s*\|?\s*\d+|official\s*\(open\))$", re.I)


def page_map(reader: PdfReader) -> list[str]:
    """First real line of each page — the finding aid these PDFs lack bookmarks for."""
    per_page: list[list[str]] = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        per_page.append([line.strip() for line in text.splitlines() if line.strip()])

    # Running headers and footers repeat across pages; they are never the heading.
    # Digits are blanked first, so a footer carrying its own page number still
    # counts as the same line on every page.
    def key(line: str) -> str:
        return re.sub(r"\d+", "#", line)

    seen: dict[str, int] = {}
    for lines in per_page:
        for line in {key(line) for line in lines}:
            seen[line] = seen.get(line, 0) + 1
    repeated = max(2, len(per_page) // 3)

    out = []
    for number, lines in enumerate(per_page, start=1):
        heads = [
            line
            for line in lines
            if not BOILERPLATE.match(line) and seen.get(key(line), 0) < repeated
        ][:2]
        out.append(f"  p{number}: {' · '.join(heads)[:90] or '(no text)'}")
    return out


def outline(path: Path) -> str:
    """Page count plus bookmarks, or a per-page map when the PDF has none."""
    reader = PdfReader(str(path))
    lines = [f"{path.name}: {len(reader.pages)} pages"]
    bookmarks: list[str] = []

    def walk(items, depth: int = 0) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item, depth + 1)
                continue
            try:
                page = reader.get_destination_page_number(item) + 1
            except Exception:
                page = None
            where = f"p{page}" if page else "?"
            bookmarks.append(f"{'  ' * depth}- {item.title.strip()} ({where})")

    try:
        walk(reader.outline)
    except Exception:
        bookmarks = []
    lines.extend(bookmarks or page_map(reader))
    return "\n".join(lines)


def convert(converter: MarkItDown, reader: PdfReader, page: int, workdir: Path) -> str:
    """Convert a single page, which is what pins output to a page number."""
    writer = PdfWriter()
    writer.add_page(reader.pages[page - 1])
    slice_path = workdir / f"p{page}.pdf"
    with slice_path.open("wb") as handle:
        writer.write(handle)
    try:
        return converter.convert(str(slice_path)).text_content.strip()
    finally:
        slice_path.unlink(missing_ok=True)


def convert_layout(path: Path, page: int) -> str:
    """One page through `pdftotext -layout`, which keeps columns apart."""
    binary = shutil.which("pdftotext")
    if binary is None:
        raise RuntimeError("--layout needs pdftotext (brew install poppler)")
    result = subprocess.run(
        [binary, "-layout", "-f", str(page), "-l", str(page), str(path), "-"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pdftotext failed: {result.stderr.strip()}")
    return result.stdout.strip()


def extract(path: Path, pages: list[int] | None, markers: bool, layout: bool) -> str:
    reader = PdfReader(str(path))
    selected = pages or list(range(1, len(reader.pages) + 1))
    converter = None if layout else MarkItDown(enable_plugins=False)
    chunks: list[str] = []
    with tempfile.TemporaryDirectory() as workdir:
        for page in selected:
            if converter is None:
                text = convert_layout(path, page)
            else:
                text = convert(converter, reader, page, Path(workdir))
            if not text:
                continue
            if markers:
                text = PAGE_MARKER.format(name=path.stem, page=page) + "\n\n" + text
            chunks.append(text)
    return "\n\n".join(chunks) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract syllabus PDFs to page-attributed Markdown."
    )
    parser.add_argument("pdfs", nargs="+", type=Path, help="PDF files to extract")
    parser.add_argument(
        "--pages",
        help='page window, 1-based: "3", "29-40", "1,5,9-11" (default: all)',
    )
    parser.add_argument(
        "--outline",
        action="store_true",
        help="print a page map (bookmarks, or each page's first line) and stop",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        help="write <stem>.md per PDF here instead of to stdout",
    )
    parser.add_argument(
        "--layout",
        action="store_true",
        help="extract via pdftotext -layout instead, for wide multi-column tables",
    )
    parser.add_argument(
        "--no-page-markers",
        action="store_true",
        help="omit the <!-- name pN --> comments",
    )
    args = parser.parse_args()

    if args.pages and len(args.pdfs) > 1:
        parser.error("--pages applies to one PDF at a time")

    status = 0
    for path in args.pdfs:
        if not path.is_file():
            print(f"{path}: not a file", file=sys.stderr)
            status = 1
            continue
        try:
            if args.outline:
                print(outline(path))
                continue
            pages = None
            if args.pages:
                total = len(PdfReader(str(path)).pages)
                pages = parse_pages(args.pages, total)
            markdown = extract(path, pages, not args.no_page_markers, args.layout)
        except Exception as exc:
            print(f"{path}: {exc}", file=sys.stderr)
            status = 1
            continue
        if args.out_dir:
            args.out_dir.mkdir(parents=True, exist_ok=True)
            target = args.out_dir / f"{path.stem}.md"
            target.write_text(markdown, encoding="utf-8")
            print(f"{path.name} -> {target}", file=sys.stderr)
        else:
            sys.stdout.write(markdown)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
