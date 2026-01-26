# Fast-Track Workflow

**Purpose:** Generate and send a partner brief in 24 hours. Streamlined process for urgent opportunities.

**Last Updated:** January 25, 2026

---

![Fast-Track Workflow](visuals/flow_diagrams/fast-track-workflow.svg)

## 24-Hour Workflow

![Fast-Track Workflow](visuals/flow_diagrams/fast-track-workflow.svg)

### Hour 1-2: Opportunity Identification

**Tasks:**
1. Identify partner and technology
2. Determine tier (1-4)
3. Review PARTNER_TARGET_LIST.md
4. Check OPPORTUNITY_MATRIX.md for scoring
5. Review TOP_5_LANES.md for context

**Output:**
- Partner name
- Technology (Phyllux tech + application)
- Tier assignment
- Fusion ID (if applicable)

---

### Hour 3-4: Brief Generation

**Tasks:**
1. Select tier template:
   - Tier 1: _template_pioneer.md
   - Tier 2: _template_mission.md
   - Tier 3: _template_commercial.md
   - Tier 4: _template_research.md
2. Run analytics/brief_generator.py (optional, for initial draft)
3. Customize for partner:
   - Partner name
   - Technology details
   - Mission alignment (if Tier 2)
   - Market opportunity
4. Add technical validation data:
   - Link to public code
   - Reference figures
   - Include simulation results
5. Review for qualified language:
   - Use "may", "designed to", "simulations suggest"
   - Remove absolute claims
   - Check maturity tags

**Output:**
- Customized brief (markdown)
- Ready for review

---

### Hour 5-6: Review and Refinement

**Tasks:**
1. Review brief for:
   - Accuracy
   - Qualified language
   - Mission alignment (if Tier 2)
   - Technical correctness
   - Professional tone
2. Add missing information:
   - Additional technical details
   - Market context
   - Partner-specific content
3. Final proofread:
   - Grammar and spelling
   - Formatting
   - Links and references

**Output:**
- Finalized brief
- Marked as "✅ Ready to send"

---

### Hour 7-8: Preparation

**Tasks:**
1. Convert to PDF (if needed)
2. Prepare email:
   - Subject line
   - Brief introduction
   - Brief attachment
   - Links to public repos
3. Identify contact:
   - Research partner contacts
   - Find appropriate email
   - Verify contact information
4. Log in pipeline:
   - partnerships/pipeline/active_conversations.md
   - Note tier, technology, status
   - Set follow-up date

**Output:**
- Email ready to send
- Brief attached
- Pipeline logged

---

### Hour 9-24: Send and Follow-Up Planning

**Tasks:**
1. Send email:
   - Professional tone
   - Clear subject line
   - Brief introduction
   - Brief attachment
   - Links to public repos
2. Log in pipeline:
   - partnerships/pipeline/proposals_sent.md
   - Note send date
   - Set follow-up date
3. Plan follow-up:
   - Tier 1: 2 weeks
   - Tier 2: 3 weeks
   - Tier 3: 4 weeks
   - Tier 4: As needed
4. Update CONTROL_PANEL.md:
   - Note brief sent
   - Update partner brief status
   - Plan next actions

**Output:**
- Brief sent
- Pipeline updated
- Follow-up scheduled

---

## Quick Reference

### Tier Templates
- Tier 1: partnerships/briefs/_template_pioneer.md
- Tier 2: partnerships/briefs/_template_mission.md
- Tier 3: partnerships/briefs/_template_commercial.md
- Tier 4: partnerships/briefs/_template_research.md

### Automation Tools
- analytics/brief_generator.py - Generate initial draft
- analytics/fusion_scorer.py - Score opportunities
- analytics/deal_value_estimator.py - Estimate deal value

### Pipeline Files
- partnerships/pipeline/active_conversations.md - Track conversations
- partnerships/pipeline/proposals_sent.md - Log proposals
- partnerships/pipeline/closed_deals.md - Track closed deals

---

## Common Issues and Solutions

### Issue: Missing Technical Validation Data

**Solution:**
- Reference public code (biomimetic-inventions-public)
- Link to technical figures
- Include simulation results
- Note maturity level

---

### Issue: Uncertain Tier Assignment

**Solution:**
- Review phyllux-framework for tier definitions
- Consider mission alignment
- Review PARTNER_TARGET_LIST.md for examples
- When in doubt, start with Tier 3 (Commercial)

---

### Issue: Missing Partner Contact

**Solution:**
- Research partner's website
- Use LinkedIn for contact research
- Check industry directories
- Use general contact if specific contact unavailable

---

### Issue: Brief Too Generic

**Solution:**
- Customize for partner's mission/needs
- Add partner-specific context
- Include relevant market data
- Reference partner's work/products

---

## Quality Checklist

Before sending, verify:

- [ ] Partner name correct
- [ ] Technology correctly identified
- [ ] Tier assignment appropriate
- [ ] Qualified language used throughout
- [ ] Technical validation data included
- [ ] Links to public repos included
- [ ] Mission alignment emphasized (if Tier 2)
- [ ] Professional tone maintained
- [ ] Grammar and spelling checked
- [ ] Pipeline logged
- [ ] Follow-up date set

---

## Related Documents

- [TIER_ENGAGEMENT_GUIDE.md](TIER_ENGAGEMENT_GUIDE.md) - Tier-specific approach
- [PARTNERSHIP_PLAYBOOK.md](PARTNERSHIP_PLAYBOOK.md) - Comprehensive guide
- [briefs/](briefs/) - Brief templates
- [../strategy/PARTNER_TARGET_LIST.md](../strategy/PARTNER_TARGET_LIST.md) - Partner organizations

---

**Last Updated:** January 25, 2026
