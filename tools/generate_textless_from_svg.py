#!/usr/bin/env python3
"""
Textless SVG Generator (no Cairo required)

This tool only reads SVG diagrams and writes new SVG files.
It does not modify any source code, legal documents, or IP claims.

Recursively scans for SVG files and generates textless SVG versions by:
- Removing all text elements (<text>, <tspan>, <title>, <desc>)
- Removing text-related attributes (aria-label, alt, data-label, etc.)
- Preserving all shapes and visual structure

Usage:
    python tools/generate_textless_from_svg.py --root . --suffix "-textless"
    python tools/generate_textless_from_svg.py --root . --suffix "-textless" --dry-run
"""

import argparse
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

TEXT_ATTRS = [
    "aria-label",
    "alt",
    "data-label",
    "data-title",
    "aria-labelledby",
    "aria-describedby",
]


def remove_text_elements(root: ET.Element) -> None:
    """Recursively remove all text-bearing elements from SVG."""
    def process_element(elem: ET.Element, parent: ET.Element | None = None) -> None:
        # Strip text-related attributes
        for attr in TEXT_ATTRS:
            if attr in elem.attrib:
                del elem.attrib[attr]

        # Get tag name without namespace
        tag_name = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
        should_remove = tag_name in {"text", "tspan", "title", "desc"}

        # Copy children before mutating
        children = list(elem)
        for child in children:
            process_element(child, elem)

        if should_remove and parent is not None:
            parent.remove(elem)

    # Process children of root
    for child in list(root):
        process_element(child, root)

    # Final pass for title/desc directly under root
    for child in list(root):
        tag_name = child.tag.split("}")[-1] if "}" in child.tag else child.tag
        if tag_name in {"title", "desc"}:
            root.remove(child)


def make_textless_svg(svg_path: Path, suffix: str = "-textless") -> Path:
    """Create a textless SVG next to the original and return its path."""
    try:
        tree = ET.parse(svg_path)
    except ET.ParseError as e:
        raise ValueError(f"Failed to parse SVG {svg_path}: {e}") from e

    root = tree.getroot()
    remove_text_elements(root)

    out_path = svg_path.with_name(svg_path.stem + suffix + svg_path.suffix)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    return out_path


def iter_svg_files(root: Path):
    """Yield SVG files under root, skipping .git and temp_old_images."""
    for path in root.rglob("*.svg"):
        if ".git" in path.parts or "temp_old_images" in path.parts:
            continue
        yield path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate textless SVG versions of SVG diagrams (no Cairo required)",
    )
    parser.add_argument(
        "--root",
        type=str,
        default=".",
        help="Root directory to scan for SVG files (default: current directory)",
    )
    parser.add_argument(
        "--suffix",
        type=str,
        default="-textless",
        help='Suffix to add before .svg (default: "-textless")',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be generated without creating files",
    )

    args = parser.parse_args()

    root_dir = Path(args.root).resolve()
    if not root_dir.exists():
        print(f"[ERROR] Root directory does not exist: {root_dir}")
        sys.exit(1)

    print(f"Scanning for SVG files in: {root_dir}")
    svg_files = list(iter_svg_files(root_dir))
    print(f"Found {len(svg_files)} SVG files\n")

    if args.dry_run:
        print("[DRY-RUN MODE] No files will be created\n")

    success_count = 0
    for svg_path in svg_files:
        out_path = svg_path.with_name(svg_path.stem + args.suffix + svg_path.suffix)
        if out_path.exists():
            print(f"[skip] {out_path} already exists")
            success_count += 1
            continue

        if args.dry_run:
            print(f"[dry-run] would create {out_path}")
            success_count += 1
        else:
            try:
                created = make_textless_svg(svg_path, suffix=args.suffix)
                print(f"[ok] created {created}")
                success_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to process {svg_path}: {e}")

    print(
        f"\n{'[DRY-RUN] Would create' if args.dry_run else 'Created'} "
        f"{success_count}/{len(svg_files)} textless SVGs"
    )


if __name__ == "__main__":
    main()
