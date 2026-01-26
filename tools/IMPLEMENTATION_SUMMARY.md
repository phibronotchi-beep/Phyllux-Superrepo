# Textless Image Workflow - Implementation Summary

## Overview

Two tools have been implemented to support textless diagram workflow:

1. **`generate_textless_from_svg.py`** - Generates textless PNG versions of SVG diagrams
2. **`update_markdown_image_references.py`** - Updates Markdown files to show textless images first

## Implementation Details

### 1. Textless Image Generator

**File:** `tools/generate_textless_from_svg.py`

**Features:**
- Recursively scans repository for `.svg` files
- Parses SVG XML using `xml.etree.ElementTree`
- Removes all text elements:
  - `<text>` and `<tspan>` elements
  - `<title>` and `<desc>` elements
  - Text-related attributes (`aria-label`, `alt`, `data-label`, `data-title`, etc.)
- Preserves all visual structure (shapes, paths, circles, rectangles, lines)
- Renders to PNG using `cairosvg`
- Generates files with naming pattern: `original-name-textless.png`

**CLI Options:**
- `--root` - Root directory to scan (default: current directory)
- `--suffix` - Suffix to add before extension (default: "-textless")
- `--format` - Output format (default: "png", only PNG supported)
- `--dry-run` - Preview mode without creating files

**Dependencies:**
- `cairosvg` - For SVG to PNG conversion (install with: `pip install cairosvg`)

**Safety:**
- Only reads SVG files and writes new PNG files
- Does not modify existing SVG files
- Does not touch source code, legal documents, or IP claims
- Skips temp directories and git folders

### 2. Markdown Reference Updater

**File:** `tools/update_markdown_image_references.py`

**Features:**
- Recursively scans repository for `.md` files
- Finds SVG image references: `![Alt text](path/to/image.svg)`
- Checks if corresponding textless PNG exists
- Updates Markdown to show textless image first
- Adds link to labeled SVG version
- Preserves all alt text and surrounding content

**Update Modes:**
- `inline-plus-link` (default): Shows textless image inline, with link to labeled SVG
- `replace`: Replaces SVG reference with textless image only

**CLI Options:**
- `--root` - Root directory to scan (default: current directory)
- `--mode` - Update mode: "inline-plus-link" or "replace" (default: "inline-plus-link")
- `--suffix` - Suffix used for textless images (default: "-textless")
- `--dry-run` - Preview mode without modifying files

**Safety:**
- Only modifies Markdown files
- Does not delete or move SVG files
- Does not touch non-Markdown files
- Idempotent: running multiple times produces the same result
- Preserves all surrounding text and structure

## Usage Workflow

### Step 1: Generate Textless Images

```bash
# Install dependencies first
pip install cairosvg

# Generate all textless PNGs
python tools/generate_textless_from_svg.py --root . --suffix "-textless" --format png

# Or preview first
python tools/generate_textless_from_svg.py --root . --suffix "-textless" --format png --dry-run
```

### Step 2: Update Markdown References

```bash
# Update all Markdown files
python tools/update_markdown_image_references.py --root . --mode "inline-plus-link"

# Or preview first
python tools/update_markdown_image_references.py --root . --mode "inline-plus-link" --dry-run
```

## Example Transformation

**Before:**
```markdown
Here is the Phyllux ecosystem:

![Ecosystem Map](visuals/ecosystem/ecosystem-map.svg)
```

**After:**
```markdown
Here is the Phyllux ecosystem:

![Ecosystem Map (Textless)](visuals/ecosystem/ecosystem-map-textless.png)

[View labeled version](visuals/ecosystem/ecosystem-map.svg)
```

## Files Created

- `tools/generate_textless_from_svg.py` - Textless image generator
- `tools/update_markdown_image_references.py` - Markdown updater
- `tools/README.md` - Detailed tool documentation
- `tools/requirements.txt` - Python dependencies
- `tools/IMPLEMENTATION_SUMMARY.md` - This file

## Documentation Updates

- `README.md` - Added "Textless Diagram Workflow" section
- `tools/README.md` - Complete tool documentation

## Testing

Both tools support `--dry-run` mode for safe testing:

```bash
# Test textless generation
python tools/generate_textless_from_svg.py --root . --suffix "-textless" --format png --dry-run

# Test Markdown updates
python tools/update_markdown_image_references.py --root . --mode "inline-plus-link" --dry-run
```

## Notes

- Textless images avoid text-rendering issues in downstream tools
- Labeled SVG versions remain available for detailed viewing
- All tools are idempotent and safe to run multiple times
- Tools only modify image files and Markdown references
- No source code, legal documents, or IP claims are modified
