# System Context

**Purpose:** Understand how the three existing repositories relate to each other and to this superrepo. Essential reading before making changes or engaging partners.

---

## The Three Repositories

### 1. biomimetic-inventions-public
**GitHub:** https://github.com/phibronotchi-beep/biomimetic-inventions-public  
**Purpose:** Public demonstrations and prior art establishment  
**Priority Date:** January 7, 2026 (first commit)

**Contains:**
- **Phyllux Mesh (PNM-public/):** Neural interface electrode arrays using phyllotactic spacing
- **Phyllux Wave (GAFAA-public/):** Golden-angle fractal antenna arrays for communications
- **Phyllux Vault (PhiKey-public/):** Geometric security protocol exploration
- **Phyllux Core:** Integrated system documentation

**Key Characteristics:**
- All code is MIT licensed (permissive)
- All code is reproducible and timestamped
- Establishes prior art for PPA filing
- Public-facing (anyone can view, fork, use)
- Contains 25+ technical figures for PPA

**What It Does:**
- Demonstrates core technologies with working code
- Provides prior art defense against patent trolls
- Enables research collaboration (Tier 4 free access)
- Supports PPA filing with timestamped evidence

**What It Does NOT Do:**
- Does not contain IP claims (those are in the PPA)
- Does not contain commercial terms (those are in phyllux-framework)
- Does not contain fusion embodiments (those are in phyllux-inventions-wip)

---

### 2. phyllux-framework
**GitHub:** https://github.com/phibronotchi-beep/phyllux-framework  
**Purpose:** Governance, licensing, and ethical framework  
**Established:** January 20, 2026

**Contains:**
- **4-Tier Licensing Model:**
  - Tier 1: Pioneer (mission-critical, exclusive)
  - Tier 2: Mission-Aligned (non-exclusive, mission-driven)
  - Tier 3: Commercial (standard licensing)
  - Tier 4: Free (research, open source)
- **PHYLUX_SPINE.md:** Method spine documentation (137.508° golden angle)
- **DISCLOSURE.md:** Maturity framework and qualified language guidelines
- **TEMPLATE files:** Tier-specific licensing templates

**Key Characteristics:**
- Defines ethical boundaries and governance
- Establishes licensing structure (not legal contracts, but framework)
- Contains NO code (documentation only)
- Contains NO IP claims (references public repo for prior art)
- Public-facing (anyone can view)

**What It Does:**
- Provides licensing framework for partnerships
- Establishes ethical boundaries (what we won't license)
- Documents method spine (unifying principle)
- Provides templates for partner engagement

**What It Does NOT Do:**
- Does not contain actual code implementations
- Does not make IP claims (references biomimetic-inventions-public)
- Does not contain commercial terms (those are negotiated per deal)
- Does not contain fusion embodiments (those are in phyllux-inventions-wip)

---

### 3. phyllux-inventions-wip
**GitHub:** https://github.com/phibronotchi-beep/phyllux-inventions-wip  
**Purpose:** 350 systematic technology fusions across 12+ categories  
**Established:** January 25, 2026

**Contains:**
- **350 Fusion Pages:** Each combining one core Phyllux tech with one emerging technology
- **Complete_Phyllux_Fusion_Matrix_Enriched.json:** Structured data of all fusions
- **Categories:** Biological (65), Quantum (40), AI/ML (35), Materials (30), Energy (30), Communications (30), etc.
- **Maturity Tags:** Conceptual, Derived, Simulated, Structural, Candidate

**Key Characteristics:**
- Uses qualified language ("may", "designed to", "simulations suggest")
- Maturity framework prevents overclaiming
- Each fusion has technical diagrams (SVG)
- Cross-references to public repo for implementations
- Public-facing (anyone can view)

**What It Does:**
- Documents 350 potential applications
- Provides embodiment examples for PPA
- Shows breadth of method spine applicability
- Enables opportunity scoring and prioritization

**What It Does NOT Do:**
- Does not contain working code (references biomimetic-inventions-public)
- Does not make absolute performance claims
- Does not contain licensing terms (those are in phyllux-framework)
- Does not contain commercial strategy (that's in this superrepo)

---

## The Superrepo (This Repository)

**Purpose:** Meta-coordination and commercialization layer

**What It Does:**
- **Maps opportunities** across 350 fusions (scoring, prioritization)
- **Supports PPA filing** (evidence mapping, claim coordination)
- **Generates partner briefs** (tier-specific templates)
- **Tracks commercialization** (deal pipeline, conversations)
- **Coordinates ecosystem** (governance, contributor paths)

**What It Does NOT Do:**
- Does NOT duplicate code (references via GitHub URLs)
- Does NOT create new IP claims (that's for the PPA)
- Does NOT modify the three existing repos (read-only references)
- Does NOT contain legal contracts (those are negotiated per deal)

**Key Characteristics:**
- Contains deal pipeline (confidential, in partnerships/pipeline/)
- Contains strategy documents (not public-facing)
- Contains analytics scripts (read-only, don't modify source repos)
- References existing repos via URLs, never duplicates

---

## How They Work Together

```
┌─────────────────────────────────────────────────────────────┐
│              PHYLLUX SUPERREPO (This Repo)                  │
│         Navigation + Commercialization + Strategy            │
│                                                             │
│  • Scores 350 fusions → prioritizes opportunities          │
│  • Maps evidence → supports PPA filing                     │
│  • Generates briefs → engages partners                      │
│  • Tracks deals → manages pipeline                          │
└─────────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│   Framework   │  │    Public     │  │      WIP       │
│               │  │               │  │               │
│ • 4-tier      │  │ • Demos       │  │ • 350 fusions │
│   licensing   │  │ • Prior art   │  │ • Embodiments │
│ • Governance  │  │ • Code        │  │ • Maturity    │
│ • Templates   │  │ • Figures    │  │ • Diagrams    │
└───────────────┘  └───────────────┘  └───────────────┘
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                    ┌──────▼──────┐
                    │ Method Spine │
                    │ 137.508°     │
                    │ Golden Angle │
                    └──────────────┘
```

### Example: Partner Engagement Flow

1. **Superrepo identifies opportunity:**
   - Fusion 234 (Phyllux Mesh + BCIs) scores high in OPPORTUNITY_MATRIX.md
   - Tier 1 BCI identified in PARTNER_TARGET_LIST.md
   - Tier 1 (Pioneer) selected based on mission alignment

2. **Superrepo generates brief:**
   - Uses _template_pioneer.md from partnerships/briefs/
   - References biomimetic-inventions-public/PNM-public/ for technical details
   - References phyllux-framework for licensing framework
   - References phyllux-inventions-wip Fusion 234 for embodiment

3. **Partner reviews:**
   - Views public code in biomimetic-inventions-public
   - Reviews licensing framework in phyllux-framework
   - Sees embodiment in phyllux-inventions-wip
   - Receives brief from superrepo (deal-specific)

4. **Negotiation:**
   - Terms based on phyllux-framework tier structure
   - Technical validation using biomimetic-inventions-public code
   - Embodiment details from phyllux-inventions-wip
   - Deal tracked in superrepo partnerships/pipeline/

---

## Critical Boundaries

### What Each Repo Owns

**biomimetic-inventions-public:**
- Code implementations
- Technical figures
- Prior art dates
- Public demonstrations

**phyllux-framework:**
- Licensing framework
- Governance structure
- Ethical boundaries
- Method spine documentation

**phyllux-inventions-wip:**
- Fusion embodiments
- Maturity assessments
- Technical diagrams
- Qualified language examples

**phyllux-superrepo (this repo):**
- Opportunity scoring
- Partner briefs
- Deal pipeline
- Commercial strategy

### What NO Repo Should Do

- ❌ Make absolute performance claims (use qualified language)
- ❌ Modify LICENSE, PRIOR_ART, PATENTS, DISCLOSURE files
- ❌ Duplicate code across repos (reference via URLs)
- ❌ Create conflicting IP claims
- ❌ Weaken defensive IP posture

---

## Integration Points

### Method Spine (137.508° Golden Angle)

**Present in all repos:**
- biomimetic-inventions-public: Implementation in code
- phyllux-framework: Documented in PHYLUX_SPINE.md
- phyllux-inventions-wip: Applied across 350 fusions
- phyllux-superrepo: Referenced in briefs and strategy

**This is the unifying principle** that connects all technologies and embodiments.

### Maturity Framework

**Defined in phyllux-framework/DISCLOSURE.md:**
- Conceptual (1-2/10)
- Derived (3-4/10)
- Simulated (5-6/10)
- Structural (7-8/10)
- Candidate (9-10/10)

**Applied in phyllux-inventions-wip:**
- Each fusion tagged with maturity level
- Prevents overclaiming immature work

**Used in phyllux-superrepo:**
- Maturity influences opportunity scoring
- Higher maturity = higher commercial priority

### Qualified Language

**Required in all repos:**
- "may provide"
- "designed to"
- "simulations suggest"
- "could enable"
- "appears to"

**Never use:**
- "guarantees"
- "proven"
- "definitely"
- Absolute performance claims

---

## Repository Access Patterns

### Public Access (Anyone)
- biomimetic-inventions-public: Full access (MIT license)
- phyllux-framework: Full access (CC BY-SA 4.0)
- phyllux-inventions-wip: Full access (view only)
- phyllux-superrepo: Public files only (pipeline/ is confidential)

### Partner Access (During Negotiation)
- All public repos: Full access
- phyllux-superrepo: Selected briefs and strategy docs
- phyllux-superrepo/pipeline/: Confidential, not shared

### Internal Access (David + AI)
- All repos: Full access
- phyllux-superrepo/pipeline/: Full access for deal tracking
- Analytics scripts: Can read all repos, never modify

---

## Common Questions

### "Where do I add new code?"
→ biomimetic-inventions-public (if it's a demo/prior art)  
→ Never in superrepo (this repo doesn't contain code)

### "Where do I document a new fusion?"
→ phyllux-inventions-wip (create new fusion page)  
→ Then reference it in superrepo OPPORTUNITY_MATRIX.md

### "Where do I track a partner conversation?"
→ phyllux-superrepo/partnerships/pipeline/active_conversations.md  
→ Never in other repos (they're public)

### "Where do I update licensing terms?"
→ phyllux-framework (framework only, not contracts)  
→ Never modify LICENSE files in any repo

### "Where do I add PPA evidence?"
→ phyllux-superrepo/strategy/PPA_EVIDENCE_MAP.md  
→ References evidence in biomimetic-inventions-public

---

## Related Documents

- [repos/_integration_map.md](repos/_integration_map.md) - Detailed integration mapping
- [architecture/PHYLUX_SYSTEM_MAP.md](architecture/PHYLUX_SYSTEM_MAP.md) - System architecture
- [architecture/METHOD_SPINE_INTEGRATION.md](architecture/METHOD_SPINE_INTEGRATION.md) - Method spine details

---

**Last Updated:** January 25, 2026
