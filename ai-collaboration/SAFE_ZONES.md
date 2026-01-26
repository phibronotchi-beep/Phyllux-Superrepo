# Safe Zones

**Purpose:** Clearly defined areas where AI can safely make modifications without risking IP damage.

**Last Updated:** January 25, 2026

---

## Safe Modification Zones

![Safe Zones Map](visuals/ai-collaboration/safe-zones-map.svg)

### phyllux-superrepo Only

**Safe to Modify:**
- CONTROL_PANEL.md (daily status updates)
- partnerships/pipeline/active_conversations.md (conversation tracking)
- partnerships/pipeline/proposals_sent.md (proposal logging)
- partnerships/pipeline/closed_deals.md (deal tracking)
- OPPORTUNITY_MATRIX.md (scoring updates, using analytics scripts)
- Partner briefs in partnerships/briefs/ (using templates)
- Analytics script outputs

**Never Modify:**
- .cursor/rules (AI safety guardrails)
- REVENUE_MODEL.md tier definitions
- PPA_EVIDENCE_MAP.md structure
- Core documentation files

---

## Read-Only Zones

**All Source Repos (biomimetic-inventions-public, phyllux-framework, phyllux-inventions-wip):**
- Read-only access only
- Reference via URLs
- Never modify directly

---

## Related Documents

- [CURSOR_RULES.md](CURSOR_RULES.md) - AI safety guardrails
- [QUALITY_GATES.md](QUALITY_GATES.md) - Quality checks

---

**Last Updated:** January 25, 2026
