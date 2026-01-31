# Phyllux Superrepo

**Meta-coordination and commercialization layer for the Phyllux ecosystem**

## What This Is

The Phyllux Superrepo is a navigation and deal-making brain that sits above three existing repositories:

- **[biomimetic-inventions-public](https://github.com/phibronotchi-beep/biomimetic-inventions-public)** - Public demonstrations and prior art for Phyllux Mesh, Wave, Vault, and Core technologies
- **[phyllux-framework](https://github.com/phibronotchi-beep/phyllux-framework)** - Four-tier ethical licensing model (Pioneer/Mission-Aligned/Commercial/Free) and governance
- **[phyllux-inventions-wip](https://github.com/phibronotchi-beep/phyllux-inventions-wip)** - 350 systematic technology fusions across 12+ categories

This superrepo does NOT duplicate code, weaken IP protections, or create new claims. Instead, it:

- **Maps opportunities** across 350 fusions by TAM, maturity, and feasibility
- **Supports PPA filing** with cross-repo evidence mapping and claim coordination
- **Generates partner briefs** using tier-specific templates aligned with the 4-tier licensing model
- **Tracks commercialization** from inquiry → brief → negotiation → close
- **Coordinates ecosystem** growth while preserving defensive IP posture

## What This Is NOT

- ❌ Not a code repository (references existing code via links)
- ❌ Not a place to create new IP claims (that's for the PPA)
- ❌ Not a replacement for the three existing repos
- ❌ Not public-facing (contains deal pipeline and strategy)

## Critical Timeline

- **Late January 2026:** PPA filing deadline
- **Mid-February 2026:** Treatment begins
- **90-Day Sprint:** Everything must be usable by one person with AI assistance

## Quick Navigation

### Immediate Priorities (This Week)
- 📋 [PPA Evidence Map](strategy/PPA_EVIDENCE_MAP.md) - Cross-repo evidence for USPTO filing
- 🎯 [Top 5 Commercial Lanes](strategy/TOP_5_LANES.md) - Highest-value opportunities
- 🤝 [Partner Target List](strategy/PARTNER_TARGET_LIST.md) - Specific organizations to contact
- ⚡ [Urgent Briefs](partnerships/briefs/) - Tier 1 partnership briefs (available on request)

### Daily Operations
- 🎛️ [Control Panel](CONTROL_PANEL.md) - Daily status and next actions
- ⚡ [Fast-Track Workflow](partnerships/FAST_TRACK_WORKFLOW.md) - Idea → sent brief in 24 hours

### Before Treatment
- 📖 [Handoff Guide](HANDOFF_GUIDE.md) - Instructions for trusted helper (what NOT to touch)

### Strategy & Analysis
- 📊 [Opportunity Matrix](strategy/OPPORTUNITY_MATRIX.md) - All 350 fusions scored
- 💰 [Revenue Model](strategy/REVENUE_MODEL.md) - Deal value estimation by tier
- 🏢 [Partnership Playbook](partnerships/PARTNERSHIP_PLAYBOOK.md) - How to engage partners

### Ecosystem & Governance
- 📎 [Ecosystem & Links](ECOSYSTEM_AND_LINKS.md) - All repo links, PHYLLUX-DOCS, and **official domains** (www.phyllux.org, www.phyllux.io, www.phyllux.com — *coming soon; we're working on it*)
- 🌟 [Vision](ecosystem/VISION.md) - Long-term ecosystem goals
- 🤖 [AI Collaboration Rules](ai-collaboration/CURSOR_RULES.md) - Safety guardrails
- ⚖️ [Governance Framework](ecosystem/GOVERNANCE_FRAMEWORK.md) - Decision-making structure

## Repository Roles

![Phyllux System Architecture](visuals/system_diagrams/phyllux-system-architecture.svg)

```
┌─────────────────────────────────────────────────────────────┐
│                   PHYLLUX SUPERREPO                         │
│         (Navigation + Commercialization Layer)              │
│                                                             │
│  • Opportunity scoring and prioritization                  │
│  • Partner brief generation and deal tracking              │
│  • PPA support and evidence coordination                   │
│  • Ecosystem orchestration and governance                  │
└─────────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   Framework   │  │    Public     │  │      WIP      │
│               │  │               │  │               │
│ • 4-tier      │  │ • Demos       │  │ • 350 fusions │
│   licensing   │  │ • Prior art   │  │ • Exploration │
│ • Governance  │  │ • Jan 7, 2026 │  │ • Maturity    │
│ • Templates   │  │   priority    │  │   pipeline    │
└───────────────┘  └───────────────┘  └───────────────┘
```

![Repository Relationships](visuals/system_diagrams/repository-relationships.svg)

## Installation

This repository contains documentation, scripts, and tools. No installation required for viewing documentation.

**For Python tools (analytics, textless SVG generation):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r analytics/requirements.txt
```

**Environment Setup:**
1. Copy `.env.example` to `.env`
2. Add your FAL API key (if using image generation tools)
3. Never commit `.env` to version control

## Usage

### Quick Start
1. Read [QUICK_START.md](QUICK_START.md) for 5-minute orientation
2. Check [CONTROL_PANEL.md](CONTROL_PANEL.md) for daily operations
3. Review [SYSTEM_CONTEXT.md](SYSTEM_CONTEXT.md) to understand ecosystem

### Common Workflows

**Generate Partner Brief:**
1. Review [FAST_TRACK_WORKFLOW.md](partnerships/FAST_TRACK_WORKFLOW.md)
2. Select appropriate tier template from `partnerships/briefs/`
3. Customize for partner and technology
4. Review and send

**Score Opportunities:**
1. Run `analytics/fusion_scorer.py` (when implemented)
2. Review `strategy/OPPORTUNITY_MATRIX.md`
3. Prioritize using `strategy/TOP_5_LANES.md`

**Generate Textless Diagrams:**
```bash
python tools/generate_textless_from_svg.py --root . --suffix "-textless"
python tools/update_markdown_image_references.py --root . --mode "inline-plus-link"
```

## Repository Structure

```
phyllux-superrepo/
├── README.md                 # This file
├── QUICK_START.md            # 5-minute orientation
├── CONTROL_PANEL.md          # Daily operations dashboard
├── strategy/                 # Strategic analysis and planning
├── partnerships/             # Partner engagement and deal tracking
├── architecture/             # System architecture documentation
├── workflows/                # Operational workflows
├── ecosystem/                # Ecosystem vision and governance
├── ai-collaboration/         # AI interaction guidelines
├── legal/                    # Legal and IP coordination
├── analytics/                # Analytics scripts (Python)
├── tools/                    # Utility scripts
└── visuals/                  # Visual assets (SVG diagrams)
```

See [NAVIGATION.md](NAVIGATION.md) for complete file map.

## Integration

This repository integrates with three other Phyllux repositories:

- **[biomimetic-inventions-public](https://github.com/phibronotchi-beep/biomimetic-inventions-public)** - References code and figures for technical validation
- **[phyllux-framework](https://github.com/phibronotchi-beep/phyllux-framework)** - Uses 4-tier licensing model and templates
- **[phyllux-inventions-wip](https://github.com/phibronotchi-beep/phyllux-inventions-wip)** - Scores 350 fusions for opportunities

See [SYSTEM_CONTEXT.md](SYSTEM_CONTEXT.md) for detailed integration mapping.

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Critical:** Never modify LICENSE, PRIOR_ART, PATENTS, or DISCLOSURE files. Always use qualified language.

## License

- **Code:** MIT License (see [LICENSE](LICENSE))
- **Documentation:** CC BY-SA 4.0
- **IP Notice:** All inventions remain proprietary. Prior art established January 7, 2026. PPA filing in progress (late January 2026).

## Contact

**David Edward Sproule**  
Independent Inventor | Phyllux Technologies  
Edmonton, Alberta, Canada  
**Email:** phibronotchi@gmail.com  
**GitHub:** [@phibronotchi-beep](https://github.com/phibronotchi-beep)  
**Twitter/X:** [@Phibronotchi](https://twitter.com/Phibronotchi)

---

## 🌿 Phyllux Ecosystem

This repository is part of the **Phyllux Technologies** ecosystem:

- **[biomimetic-inventions-public](https://github.com/phibronotchi-beep/biomimetic-inventions-public)** - Public demos & prior art
- **[phyllux-framework](https://github.com/phibronotchi-beep/phyllux-framework)** - Ethical IP framework
- **[phyllux-inventions-wip](https://github.com/phibronotchi-beep/phyllux-inventions-wip)** - 350 technology fusions

**Learn more:** [Phyllux Technologies](https://github.com/phibronotchi-beep)  
**Nature's 137.508° Innovation** | **Multi-Domain Phyllotactic Systems**

**Priority Date:** January 7, 2026

---

## Textless Diagram Workflow

This repository uses textless SVG versions of diagrams to avoid text-rendering issues in downstream tools and keep visuals clean. The textless images are shown first in Markdown documents, with labeled SVG versions available as links.

### Generating Textless Images

To generate textless SVG versions of all SVG diagrams:

```bash
python tools/generate_textless_from_svg.py --root . --suffix "-textless"
```

This will:
- Scan all SVG files recursively
- Remove all text elements (labels, titles, descriptions)
- Generate SVG files with the `-textless` suffix (e.g., `ecosystem-map-textless.svg`)

To preview what would be generated without creating files:

```bash
python tools/generate_textless_from_svg.py --root . --suffix "-textless" --dry-run
```

### Updating Markdown References

After generating textless images, update Markdown files to show textless images first:

```bash
python tools/update_markdown_image_references.py --root . --mode "inline-plus-link"
```

This will:
- Find all SVG image references in Markdown files
- For each SVG with a corresponding textless SVG, insert the textless image first
- Add a link to the labeled SVG version
- Preserve all existing alt text and surrounding content

To preview changes without modifying files:

```bash
python tools/update_markdown_image_references.py --root . --mode "inline-plus-link" --dry-run
```

**Note:** These tools only read SVG diagrams and write new image files, or modify Markdown image references. They do not modify any source code, legal documents, or IP claims.
