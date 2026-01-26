# Interface Contracts

**Purpose:** Define integration contracts between system components and repositories.

**Last Updated:** January 25, 2026

---

## Repository Contracts

### biomimetic-inventions-public → Other Repos

**Contract:**
- Provides: Code implementations, technical figures, prior art dates
- Receives: References, links, citations
- Never: Modified by other repos (read-only)

**Interface:**
- GitHub URLs for code references
- Figure IDs for PPA evidence
- Commit hashes for prior art dates

---

### phyllux-framework → Other Repos

**Contract:**
- Provides: Licensing framework, maturity definitions, method spine documentation
- Receives: Applications of framework, maturity tags, method spine usage
- Never: Modified by other repos (read-only)

**Interface:**
- Tier definitions for briefs
- Maturity framework for fusions
- Method spine documentation

---

### phyllux-inventions-wip → Other Repos

**Contract:**
- Provides: Fusion embodiments, maturity tags, technical diagrams
- Receives: Opportunity scoring, brief generation, commercial tracking
- Never: Modified by superrepo (read-only)

**Interface:**
- JSON data for scoring
- Fusion IDs for briefs
- Maturity tags for prioritization

---

### phyllux-superrepo → All Repos

**Contract:**
- Provides: Opportunity scoring, brief generation, deal tracking
- Receives: Code, frameworks, fusions (read-only)
- Never: Modifies source repos (read-only only)

**Interface:**
- GitHub URLs for references
- JSON data for scoring
- Templates for briefs

---

## Integration Rules

**Read-Only Principle:**
- Superrepo never modifies source repos
- All references via URLs or read-only data
- Maintains clear separation of concerns

**Qualified Language:**
- All descriptions use qualified language
- No absolute performance claims
- Maturity framework applied consistently

**Prior Art Protection:**
- All repos reference prior art dates consistently
- No modifications to LICENSE, PRIOR_ART, PATENTS, DISCLOSURE files
- Defensive publication strategy maintained

---

## Related Documents

- [PHYLUX_SYSTEM_MAP.md](PHYLUX_SYSTEM_MAP.md) - System architecture
- [MODULE_CATALOG.md](MODULE_CATALOG.md) - Component catalog
- [../SYSTEM_CONTEXT.md](../SYSTEM_CONTEXT.md) - Repository relationships

---

**Last Updated:** January 25, 2026
