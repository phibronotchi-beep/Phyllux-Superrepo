# biomimetic-inventions-public Repository

**GitHub:** https://github.com/phibronotchi-beep/biomimetic-inventions-public  
**Purpose:** Public demonstrations and prior art establishment  
**Priority Date:** January 7, 2026 (first commit)

---

## Overview

This repository contains public, reproducible code demonstrations of four core Phyllux technologies. It serves three critical functions:

1. **Prior Art Establishment:** Timestamped public disclosure establishes defensive prior art
2. **Technical Validation:** Working code demonstrates feasibility and reproducibility
3. **Research Collaboration:** MIT-licensed code enables Tier 4 (Free) research access

---

## Core Technologies

![Mesh Applications](visuals/technologies/mesh-applications.svg)

### 1. Phyllux Mesh (PNM-public/)
**Phyllotactic Neural Meshing** - Electrode arrays for neural interfaces

**Key Features:**
- 121-electrode phyllotactic layout (signature configuration)
- Non-periodic spacing designed to minimize crosstalk
- Fibonacci-based element counts (13, 21, 34, 55, 89, 121, 144, etc.)
- 3D electrode arrays with depth variation

**Applications:**
- Brain-computer interfaces (BCIs)
- Neuroprosthetics
- Neural recording systems
- Brain mapping

**Evidence for PPA:**
- Figure 1: 121-electrode layout
- Figure 5: Crosstalk minimization analysis
- Figure 9: Signal-to-noise ratio improvement
- Figure 11: 3D depth variation
- Figure 14: Spatial sampling uniformity

**Code Location:**
- `PNM-public/src/pnm_public/` - Core implementation
- `PNM-public/examples/` - Demonstration scripts
- `PNM-public/images/` - Technical figures

---

![Wave Applications](visuals/technologies/wave-applications.svg)

### 2. Phyllux Wave (GAFAA-public/)
**Golden-Angle Fractal Antenna Arrays** - Non-periodic antenna arrays

**Key Features:**
- Golden angle (137.508°) spiral element placement
- Scalable from 10 to 10,000+ elements
- Non-periodic layout may reduce grating lobes
- Array factor analysis for radiation patterns

**Applications:**
- Satellite constellations (Starlink-class)
- 5G/6G base stations
- Phased array radar
- Terahertz communication

**Evidence for PPA:**
- Figure 3: 3D spiral antenna layout
- Figure 7: Array factor analysis
- Figure 12: Mutual coupling reduction
- Figure 15: Frequency response (1-10 GHz)
- Figure 18: Scalability demonstration

**Code Location:**
- `golden-angle-antenna-GAFAA-public/src/gafaa_public/` - Core implementation
- `golden-angle-antenna-GAFAA-public/examples/` - Demonstration scripts
- `golden-angle-antenna-GAFAA-public/images/` - Technical figures

---

![Vault Applications](visuals/technologies/vault-applications.svg)

### 3. Phyllux Vault (PhiKey-public/)
**Geometric Security Protocol** - Cryptographic key derivation using geometric structures

**Key Features:**
- Golden ratio lattice structures
- Geometric path traversal for key derivation
- Multi-dimensional lattice visualization
- Key space entropy analysis

**Applications:**
- Post-quantum cryptography exploration
- Geometric security research
- Zero-knowledge proof systems
- Blockchain security

**Evidence for PPA:**
- Figure 2: Golden ratio lattice structure
- Figure 6: Geometric path traversal
- Figure 10: Multi-dimensional lattice
- Figure 13: Key space entropy

**Code Location:**
- `PhiKey-public/src/phikey_public/` - Core implementation
- `PhiKey-public/examples/` - Demonstration scripts
- `PhiKey-public/images/` - Technical figures

**Note:** This is conceptual exploration, NOT production-grade cryptography.

---

![Core Integration](visuals/technologies/core-integration.svg)

### 4. Phyllux Core
**High-Performance Computational Integration** - Unified system combining Wave + Mesh + Vault

**Key Features:**
- Integrated system documentation
- Cross-domain application of 137.508° method spine
- Shared geometric framework

**Applications:**
- Integrated systems requiring multiple Phyllux technologies
- Energy-efficient computing
- Parallel processing optimization

**Evidence for PPA:**
- Integrated system diagrams
- Cross-domain method spine documentation

---

## Method Spine (137.508° Golden Angle)

**The Unifying Principle:**

All four technologies share a common geometric parameter: the golden angle (approximately 137.508°), derived from the golden ratio (φ ≈ 1.618).

**Mathematical Relationship:**
- Golden ratio: φ = (1 + √5) / 2 ≈ 1.618
- Golden angle: 360° / φ² ≈ 137.508°
- Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 121, 144, ...

**Implementation:**
- Present in all code implementations
- Used for element spacing and layout
- Provides non-periodic advantages over regular grids

---

## Repository Structure

```
biomimetic-inventions-public/
├── PNM-public/                    # Phyllux Mesh
│   ├── src/pnm_public/
│   ├── examples/
│   └── images/
├── golden-angle-antenna-GAFAA-public/  # Phyllux Wave
│   ├── src/gafaa_public/
│   ├── examples/
│   └── images/
├── PhiKey-public/                 # Phyllux Vault
│   ├── src/phikey_public/
│   ├── examples/
│   └── images/
├── INTEGRATED_SYSTEM.md           # Phyllux Core
├── README.md
└── LICENSE (MIT)
```

---

## Licensing

**Code:** MIT License (permissive, allows commercial use)  
**Documentation:** CC BY-SA 4.0  
**IP Notice:** All inventions remain proprietary; code is for demonstration and prior art only

**Why MIT for Code:**
- Enables research collaboration (Tier 4 free access)
- Establishes prior art (public disclosure)
- Allows reproducibility (validates technical claims)
- Does NOT weaken IP (inventions are separate from code)

---

## Prior Art Timeline

| Date | Event | Evidence |
|------|-------|----------|
| January 7, 2026 | First commit | Git commit hash, GitHub timestamp |
| January 7, 2026 | Public repository created | GitHub repository creation date |
| [Ongoing] | Code updates and improvements | Git commit history |

**All commits are:**
- Signed by David Edward Sproule
- Timestamped by GitHub
- Publicly visible (defensive publication)

---

## Key Files for PPA

**Technical Figures (25 total):**
- Located in `*/images/` directories
- SVG format for vector graphics
- PNG format for analysis plots
- Referenced in PPA_EVIDENCE_MAP.md

**Code Examples:**
- All in `*/examples/` directories
- Reproducible (no proprietary dependencies)
- Well-documented with docstrings
- Demonstrate core algorithms

**Core Implementation:**
- All in `*/src/*_public/` directories
- Modular design
- Clear separation of concerns
- MIT licensed

---

## Integration with Other Repos

**phyllux-framework:**
- References this repo for technical implementations
- Uses this repo's prior art dates
- Links to code for Tier 4 (Free) access

**phyllux-inventions-wip:**
- References this repo for core technology implementations
- Embodiments build on code from this repo
- Uses qualified language when referencing capabilities

**phyllux-superrepo (this repo):**
- Maps evidence from this repo to PPA claims
- References code for partner briefs
- Uses figures for PPA filing

---

## Usage Guidelines

### For Researchers (Tier 4 - Free)
- ✅ Full access to all code
- ✅ Can fork, modify, and use for research
- ✅ Must maintain MIT license
- ✅ Attribution required

### For Partners (Tiers 1-3)
- ✅ Can review code for technical validation
- ✅ Can reference code in discussions
- ✅ Licensing terms negotiated separately
- ❌ Cannot use code commercially without license

### For Patent Examiners
- ✅ All code is prior art as of January 7, 2026
- ✅ All figures support PPA claims
- ✅ Code demonstrates reproducibility
- ✅ Method spine (137.508°) is clearly implemented

---

## Critical Constraints

**DO NOT:**
- ❌ Modify LICENSE file (MIT must remain)
- ❌ Change commit dates or history
- ❌ Remove or alter prior art timestamps
- ❌ Add absolute performance claims
- ❌ Remove qualified language ("may", "designed to")

**DO:**
- ✅ Add new examples and demonstrations
- ✅ Improve code quality and documentation
- ✅ Add new technical figures
- ✅ Maintain MIT license for code
- ✅ Use qualified language

---

## Related Documents

- [phyllux-framework.md](phyllux-framework.md) - Licensing framework
- [phyllux-inventions-wip.md](phyllux-inventions-wip.md) - Fusion embodiments
- [../strategy/PPA_EVIDENCE_MAP.md](../strategy/PPA_EVIDENCE_MAP.md) - PPA evidence mapping
- [../architecture/METHOD_SPINE_INTEGRATION.md](../architecture/METHOD_SPINE_INTEGRATION.md) - Method spine details

---

**Last Updated:** January 25, 2026
