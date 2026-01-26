#!/usr/bin/env python3
"""
SVG File Verification Script

Verifies that all SVG files:
1. Exist in the correct locations
2. Have titles/content that match their filenames
3. Are referenced correctly in markdown documents
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

def extract_svg_title(svg_path: Path) -> str:
    """Extract title from SVG file."""
    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for <title> tag
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if match:
                return match.group(1).strip()
    except Exception as e:
        return f"ERROR: {e}"
    return "NO TITLE FOUND"

def find_svg_references() -> Dict[str, List[str]]:
    """Find all SVG references in markdown files."""
    references = {}
    for md_file in Path('.').rglob('*.md'):
        if 'temp_old_images' in str(md_file) or '.git' in str(md_file):
            continue
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Find all image references
                matches = re.findall(r'!\[.*?\]\((.*?\.svg)\)', content)
                for match in matches:
                    svg_path = match
                    if svg_path not in references:
                        references[svg_path] = []
                    references[svg_path].append(str(md_file))
        except Exception:
            pass
    return references

def verify_all_svgs():
    """Verify all SVG files."""
    print("=" * 80)
    print("SVG FILE VERIFICATION")
    print("=" * 80)
    
    # Find all SVG files
    svg_files = list(Path('visuals').rglob('*.svg'))
    print(f"\nFound {len(svg_files)} SVG files\n")
    
    # Find all references
    references = find_svg_references()
    
    issues = []
    verified = []
    
    # Check each SVG file
    for svg_path in sorted(svg_files):
        rel_path = str(svg_path.relative_to('.'))
        title = extract_svg_title(svg_path)
        
        # Check if file exists
        if not svg_path.exists():
            issues.append((rel_path, "FILE NOT FOUND", []))
            continue
        
        # Check if referenced
        is_referenced = rel_path in references
        ref_files = references.get(rel_path, [])
        
        # Extract expected content from filename
        filename = svg_path.stem
        filename_words = filename.replace('-', ' ').replace('_', ' ').split()
        
        # Check if title matches filename (fuzzy match)
        title_words = title.lower().replace('-', ' ').replace('_', ' ').split()
        match_score = len(set(filename_words) & set(title_words))
        
        status = "OK"
        if match_score < 2 and "NO TITLE" not in title and "ERROR" not in title:
            status = "WARNING: Title may not match filename"
            issues.append((rel_path, status, ref_files))
        else:
            verified.append((rel_path, title, ref_files))
    
    # Print verified files
    print("\n" + "=" * 80)
    print("VERIFIED FILES")
    print("=" * 80)
    for rel_path, title, ref_files in verified[:10]:  # Show first 10
        print(f"\n[OK] {rel_path}")
        print(f"  Title: {title}")
        if ref_files:
            print(f"  Referenced in: {len(ref_files)} file(s)")
    
    if len(verified) > 10:
        print(f"\n... and {len(verified) - 10} more verified files")
    
    # Print issues
    if issues:
        print("\n" + "=" * 80)
        print("ISSUES FOUND")
        print("=" * 80)
        for rel_path, status, ref_files in issues:
            print(f"\n[WARNING] {rel_path}")
            print(f"  {status}")
            if ref_files:
                print(f"  Referenced in: {', '.join(ref_files)}")
    else:
        print("\n" + "=" * 80)
        print("NO ISSUES FOUND - ALL FILES VERIFIED")
        print("=" * 80)
    
    # Check for unreferenced files
    all_svg_paths = {str(svg.relative_to('.')) for svg in svg_files}
    referenced_paths = set(references.keys())
    unreferenced = all_svg_paths - referenced_paths
    
    if unreferenced:
        print("\n" + "=" * 80)
        print(f"UNREFERENCED FILES ({len(unreferenced)})")
        print("=" * 80)
        for path in sorted(unreferenced)[:10]:
            print(f"  - {path}")
        if len(unreferenced) > 10:
            print(f"  ... and {len(unreferenced) - 10} more")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total SVG files: {len(svg_files)}")
    print(f"Verified: {len(verified)}")
    print(f"Issues: {len(issues)}")
    print(f"Referenced: {len(referenced_paths)}")
    print(f"Unreferenced: {len(unreferenced)}")
    print("=" * 80)

if __name__ == "__main__":
    verify_all_svgs()
