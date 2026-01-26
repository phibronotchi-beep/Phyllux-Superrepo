# Contributing to Phyllux Superrepo

Thank you for your interest in contributing to the Phyllux ecosystem! This document provides guidelines for contributing to this repository.

## Overview

The Phyllux Superrepo is a meta-coordination and commercialization layer. It does NOT contain source code implementations (those are in `biomimetic-inventions-public`). Instead, it focuses on:

- Opportunity scoring and prioritization
- Partner brief generation
- Deal pipeline management
- PPA filing support
- Ecosystem coordination

## How to Contribute

### Reporting Issues

If you find a bug, broken link, or have a suggestion:

1. Check if an issue already exists
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce (if applicable)
   - Expected vs actual behavior
   - Relevant file paths

### Documentation Improvements

We welcome improvements to:
- README clarity
- Code comments and docstrings
- Workflow documentation
- Cross-repo integration guides

**Guidelines:**
- Use qualified language ("may", "designed to", "simulations suggest")
- Maintain consistency with ecosystem terminology
- Link to other Phyllux repos where relevant
- Include examples where helpful

### Code Contributions

**Analytics Scripts:**
- All scripts in `analytics/` are functional stubs
- Implement TODO items following existing patterns
- Add docstrings to all functions
- Include error handling
- Test with sample data

**Tools:**
- Tools in `tools/` are production-ready
- Follow existing code style
- Add tests if adding new functionality
- Document usage in `tools/README.md`

### Critical Constraints

**DO NOT MODIFY:**
- LICENSE files
- PRIOR_ART.md, PATENTS.md, DISCLOSURE.md files
- Maturity tags in referenced repos
- Legal/IP documentation
- `.cursor/rules` (AI safety guardrails)

**ALWAYS USE:**
- Qualified language (no absolute claims)
- Consistent terminology (Phyllux, not SOLARIS)
- Proper attribution
- Cross-repo links where relevant

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/phibronotchi-beep/phyllux-superrepo.git
   cd phyllux-superrepo
   ```

2. **Set up Python environment (for analytics/tools):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r analytics/requirements.txt
   ```

3. **Test tools:**
   ```bash
   python tools/generate_textless_from_svg.py --root . --suffix "-textless" --dry-run
   python tools/update_markdown_image_references.py --root . --mode "inline-plus-link" --dry-run
   ```

## Code Style

**Python:**
- Follow PEP 8
- Use type hints where appropriate
- Document all functions with docstrings
- Use snake_case for variables/functions
- Use UPPER_CASE for constants

**Markdown:**
- Use proper heading hierarchy
- Include table of contents for files >150 lines
- Use code blocks with syntax highlighting
- Include alt text for images

## Pull Request Process

1. **Create a branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes:**
   - Follow code style guidelines
   - Update documentation as needed
   - Test your changes

3. **Commit your changes:**
   ```bash
   git commit -m "docs: improve README clarity"
   ```
   Use conventional commit prefixes:
   - `docs:` - Documentation changes
   - `fix:` - Bug fixes
   - `feat:` - New features
   - `refactor:` - Code refactoring
   - `chore:` - Maintenance tasks

4. **Push and create PR:**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a pull request on GitHub.

5. **PR Review:**
   - All PRs require review
   - Address feedback promptly
   - Ensure all checks pass

## Questions?

- **Email:** phibronotchi@gmail.com
- **GitHub:** @phibronotchi-beep
- **Twitter/X:** @Phibronotchi

## License

By contributing, you agree that your contributions will be licensed under the same license as the repository (MIT for code, CC BY-SA 4.0 for documentation).

---

**Thank you for contributing to the Phyllux ecosystem!** 🌿
