#!/usr/bin/env python3
"""
update_markdown_image_references.py - Update Markdown image references

Part of Phyllux Technologies - Multi-Domain Phyllotactic Systems
Inventor: David Edward Sproule (@Phibronotchi)
License: MIT (code) / CC BY-SA 4.0 (documentation)
Repository: https://github.com/phibronotchi-beep/phyllux-superrepo

Updates Markdown files to show textless SVG images first, with labeled SVGs
available as links or alternates.

This tool only modifies Markdown files to update image references.
It does not modify any source code, legal documents, or IP claims.

Usage:
    python tools/update_markdown_image_references.py --root . --mode "inline-plus-link"
    python tools/update_markdown_image_references.py --root . --mode "inline-plus-link" --dry-run
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional


def find_markdown_files(root_dir: Path) -> List[Path]:
    """Recursively find all Markdown files in the directory tree."""
    md_files = []
    for md_path in root_dir.rglob('*.md'):
        # Skip temp directories, git, and tools
        path_str = str(md_path)
        if any(skip in path_str for skip in ['temp_old_images', '.git', 'tools/']):
            continue
        md_files.append(md_path)
    return sorted(md_files)


def find_svg_image_references(content: str) -> List[Tuple[int, str, str]]:
    """
    Find all SVG image references in Markdown content.
    
    Returns:
        List of tuples: (line_number, full_match, svg_path)
    """
    references = []
    
    # Pattern to match markdown image syntax: ![alt](path/to/image.svg)
    pattern = r'!\[([^\]]*)\]\(([^)]+\.svg)\)'
    
    for line_num, line in enumerate(content.split('\n'), 1):
        matches = re.finditer(pattern, line)
        for match in matches:
            alt_text = match.group(1)
            svg_path = match.group(2)
            references.append((line_num, match.group(0), svg_path, alt_text))
    
    return references


def resolve_image_path(svg_path: str, md_file: Path) -> Path:
    """
    Resolve relative image path to absolute Path.
    
    Handles:
    - Relative paths: ./images/foo.svg
    - Parent paths: ../images/foo.svg
    - Absolute paths from repo root: visuals/foo.svg
    """
    # If path starts with /, it's from repo root
    if svg_path.startswith('/'):
        # Assume repo root is where we're running from
        return Path(svg_path.lstrip('/'))
    
    # Otherwise, resolve relative to markdown file location
    md_dir = md_file.parent
    return (md_dir / svg_path).resolve()


def check_textless_exists(svg_path: Path, suffix: str = "-textless") -> Optional[Path]:
    """
    Check if a textless SVG version exists for the given SVG.
    
    Returns:
        Path to textless SVG if it exists, None otherwise
    """
    textless_path = svg_path.parent / f"{svg_path.stem}{suffix}.svg"
    if textless_path.exists():
        return textless_path
    return None


def get_relative_path(target: Path, from_file: Path) -> str:
    """Get relative path from markdown file to target file."""
    try:
        return str(Path(target).relative_to(from_file.parent))
    except ValueError:
        # If relative path fails, return absolute path
        return str(target)


def update_markdown_content(
    content: str,
    md_file: Path,
    mode: str = "inline-plus-link",
    suffix: str = "-textless",
    dry_run: bool = False
) -> Tuple[str, int]:
    """
    Update Markdown content to show textless images first.
    
    Args:
        content: Original Markdown content
        md_file: Path to the Markdown file
        mode: Update mode ("inline-plus-link" or "replace")
        suffix: Suffix used for textless images
        dry_run: If True, don't modify content
    
    Returns:
        Tuple of (updated_content, number_of_changes)
    """
    lines = content.split('\n')
    references = find_svg_image_references(content)
    
    if not references:
        return content, 0
    
    changes = 0
    offset = 0  # Track line offset as we insert lines
    
    for line_num, full_match, svg_path, alt_text in references:
        actual_line = line_num + offset - 1  # Convert to 0-based index
        
        # Resolve SVG path
        resolved_svg = resolve_image_path(svg_path, md_file)
        
        # Check if textless version exists
        textless_path = check_textless_exists(resolved_svg, suffix)
        
        if not textless_path:
            # No textless version, skip
            continue
        
        # Get relative paths
        rel_textless = get_relative_path(textless_path, md_file)
        rel_svg = get_relative_path(resolved_svg, md_file)
        
        # Determine new alt text
        if alt_text:
            textless_alt = f"{alt_text} (Textless)"
            svg_alt = f"{alt_text} (Labeled)"
        else:
            textless_alt = "Diagram (Textless)"
            svg_alt = "Diagram (Labeled)"
        
        if mode == "inline-plus-link":
            # Insert textless image, then link to labeled SVG
            new_lines = [
                f"![{textless_alt}]({rel_textless})",
                "",
                f"[View labeled version]({rel_svg})"
            ]
        elif mode == "replace":
            # Replace with textless only
            new_lines = [f"![{textless_alt}]({rel_textless})"]
        else:
            # Unknown mode, skip
            continue
        
        # Replace the line
        if not dry_run:
            # Remove old line and insert new lines
            lines.pop(actual_line)
            for i, new_line in enumerate(new_lines):
                lines.insert(actual_line + i, new_line)
            offset += len(new_lines) - 1
        
        changes += 1
    
    if dry_run:
        return content, changes
    else:
        return '\n'.join(lines), changes


def process_markdown_file(
    md_file: Path,
    mode: str = "inline-plus-link",
    suffix: str = "-textless",
    dry_run: bool = False
) -> bool:
    """
    Process a single Markdown file.
    
    Returns:
        True if file was modified (or would be in dry-run), False otherwise
    """
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[ERROR] Failed to read {md_file}: {e}")
        return False
    
    updated_content, changes = update_markdown_content(
        content,
        md_file,
        mode=mode,
        suffix=suffix,
        dry_run=dry_run
    )
    
    if changes == 0:
        return False
    
    if dry_run:
        print(f"[DRY-RUN] Would update {md_file} ({changes} change(s))")
        return True
    
    # Write updated content
    try:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"[OK] Updated {md_file} ({changes} change(s))")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to write {md_file}: {e}")
        return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Update Markdown files to show textless SVG images first",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Update all Markdown files
  python tools/update_markdown_image_references.py --root . --mode "inline-plus-link"
  
  # Dry run to see what would be changed
  python tools/update_markdown_image_references.py --root . --mode "inline-plus-link" --dry-run
        """
    )
    
    parser.add_argument(
        '--root',
        type=str,
        default='.',
        help='Root directory to scan for Markdown files (default: current directory)'
    )
    
    parser.add_argument(
        '--mode',
        type=str,
        default='inline-plus-link',
        choices=['inline-plus-link', 'replace'],
        help='Update mode: "inline-plus-link" shows textless inline with link to labeled, "replace" replaces with textless only (default: inline-plus-link)'
    )
    
    parser.add_argument(
        '--suffix',
        type=str,
        default='-textless',
        help='Suffix used for textless images (default: "-textless")'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print what would be changed without modifying files'
    )
    
    args = parser.parse_args()
    
    # Find all Markdown files
    root_dir = Path(args.root).resolve()
    if not root_dir.exists():
        print(f"[ERROR] Root directory does not exist: {root_dir}")
        sys.exit(1)
    
    print(f"Scanning for Markdown files in: {root_dir}")
    md_files = find_markdown_files(root_dir)
    print(f"Found {len(md_files)} Markdown files\n")
    
    if args.dry_run:
        print("[DRY-RUN MODE] No files will be modified\n")
    
    # Process each Markdown file
    updated_count = 0
    for md_file in md_files:
        if process_markdown_file(
            md_file,
            mode=args.mode,
            suffix=args.suffix,
            dry_run=args.dry_run
        ):
            updated_count += 1
    
    print(f"\n{'[DRY-RUN] Would update' if args.dry_run else 'Updated'} {updated_count}/{len(md_files)} Markdown files")


if __name__ == "__main__":
    main()
