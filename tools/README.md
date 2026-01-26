# Tools Directory

This directory contains utility scripts for maintaining the Phyllux Superrepo.

## Image Generation Tools

### `generate_textless_from_svg.py`

Generates textless SVG versions of SVG diagrams by removing all text elements while preserving visual structure. No external dependencies required.

**Usage:**
```bash
# Generate all textless images
python tools/generate_textless_from_svg.py --root . --suffix "-textless"

# Dry run to preview
python tools/generate_textless_from_svg.py --root . --suffix "-textless" --dry-run
```

**What it does:**
- Recursively scans for `.svg` files
- Removes `<text>`, `<tspan>`, `<title>`, `<desc>` elements
- Removes text-related attributes (`aria-label`, `alt`, `data-label`, etc.)
- Preserves all shapes, paths, and visual structure
- Generates SVG files with naming pattern: `original-name-textless.svg`

**Safety:**
- Only reads SVG files and writes new SVG files
- Does not modify existing SVG files
- Does not touch source code, legal documents, or IP claims

### `update_markdown_image_references.py`

Updates Markdown files to show textless SVG images first, with labeled SVG versions available as links.

**Usage:**
```bash
# Update all Markdown files
python tools/update_markdown_image_references.py --root . --mode "inline-plus-link"

# Dry run to preview changes
python tools/update_markdown_image_references.py --root . --mode "inline-plus-link" --dry-run
```

**Modes:**
- `inline-plus-link` (default): Shows textless image inline, with link to labeled SVG
- `replace`: Replaces SVG reference with textless image only

**What it does:**
- Scans all Markdown files recursively
- Finds SVG image references: `![Alt text](path/to/image.svg)`
- Checks if corresponding textless SVG exists (e.g., `image-textless.svg`)
- Updates Markdown to show textless image first
- Adds link to labeled SVG version
- Preserves all alt text and surrounding content

**Example transformation:**

Before:
```markdown
Here is the Phyllux ecosystem:

![Ecosystem Map](visuals/ecosystem/ecosystem-map.svg)
```

After:
```markdown
Here is the Phyllux ecosystem:

![Ecosystem Map (Textless)](visuals/ecosystem/ecosystem-map-textless.svg)

[View labeled version](visuals/ecosystem/ecosystem-map.svg)
```

**Safety:**
- Only modifies Markdown files
- Does not delete or move SVG files
- Does not touch non-Markdown files
- Idempotent: running multiple times produces the same result
- Preserves all surrounding text and structure

## Workflow

1. **Generate textless images:**
   ```bash
   python tools/generate_textless_from_svg.py --root . --suffix "-textless"
   ```

2. **Update Markdown references:**
   ```bash
   python tools/update_markdown_image_references.py --root . --mode "inline-plus-link"
   ```

3. **Verify changes:**
   - Check that textless SVGs were created
   - Review Markdown files to ensure images display correctly
   - Test that labeled SVG links work

## Notes

- Textless images are used to avoid text-rendering issues in downstream tools
- Labeled SVG versions remain available for detailed viewing
- All tools support `--dry-run` mode for safe previewing
- Tools are designed to be idempotent and safe to run multiple times
