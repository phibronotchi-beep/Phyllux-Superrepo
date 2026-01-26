# Handoff Guide

**Purpose:** Instructions for a trusted helper managing the Phyllux ecosystem during treatment (mid-February 2026+). Clear guidance on what they CAN do, what they MUST NOT do, and how to avoid damaging IP protections.

---

## ⚠️ CRITICAL: DO NOT TOUCH

**Under NO circumstances should your helper modify these:**

### In ANY Repository
- ❌ LICENSE files
- ❌ PRIOR_ART.md, PATENTS.md, DISCLOSURE.md files
- ❌ INVENTORSHIP_DECLARATION.md
- ❌ TIMESTAMP.md
- ❌ Any maturity tags (Conceptual, Simulated, Structural, etc.)
- ❌ Commit history or git tags
- ❌ Any file in legal/ directories

### In biomimetic-inventions-public
- ❌ Do NOT modify source code in PNM-public/, GAFAA-public/, PhiKey-public/
- ❌ Do NOT change any dates or version numbers
- ❌ Do NOT alter technical figures or diagrams
- ❌ Do NOT modify README.md files that establish prior art

### In phyllux-framework
- ❌ Do NOT change 4-tier licensing terms
- ❌ Do NOT modify TEMPLATE files
- ❌ Do NOT alter PHYLUX_SPINE.md or DISCLOSURE.md

### In phyllux-inventions-wip
- ❌ Do NOT change fusion page content or maturity tags
- ❌ Do NOT delete any fusion directories
- ❌ Do NOT modify Complete_Phyllux_Fusion_Matrix_Enriched.json

### In phyllux-superrepo
- ❌ Do NOT modify .cursor/rules (AI safety guardrails)
- ❌ Do NOT change REVENUE_MODEL.md tier definitions
- ❌ Do NOT alter PPA_EVIDENCE_MAP.md structure
- ❌ Do NOT delete or rename core files

---

## ✅ SAFE TO DO

**Your helper CAN safely:**

### In phyllux-superrepo ONLY
- ✅ Update CONTROL_PANEL.md daily status
- ✅ Add entries to partnerships/pipeline/active_conversations.md
- ✅ Log proposals in partnerships/pipeline/proposals_sent.md
- ✅ Add new rows to OPPORTUNITY_MATRIX.md (using analytics scripts)
- ✅ Create new partner briefs in partnerships/briefs/ (using templates)
- ✅ Run analytics scripts (they're read-only by design)
- ✅ Update PARTNER_TARGET_LIST.md with new contacts

### Communication
- ✅ Reply to partner inquiries with "David is unavailable until [date], I'll forward this to him"
- ✅ Schedule follow-up calls for post-treatment
- ✅ Send pre-approved briefs that are marked "✅ Ready to send"
- ✅ Thank partners for their interest and set expectations

### Administrative
- ✅ Track incoming emails and tag for follow-up
- ✅ Update deal pipeline with conversation notes
- ✅ Run scheduled analytics scripts (if automated)
- ✅ Monitor for urgent time-sensitive opportunities

---

## 🎯 PRIMARY RESPONSIBILITIES

### 1. Monitor Incoming Inquiries

**Where to check:**
- Email: phibronotchi@gmail.com
- GitHub issues (if any opened)
- Social media DMs (@Phibronotchi)

**What to do:**
1. Log inquiry in partnerships/pipeline/active_conversations.md
2. Send acknowledgment: "Thank you for your interest. David is unavailable until [date]. I'll ensure he receives this and follows up when he returns."
3. If clearly aligned with a tier, note that in the log
4. Do NOT negotiate terms or make commitments

### 2. Send Pre-Approved Briefs (If Marked Ready)

**Pre-approved briefs:**
- partnerships/briefs/_URGENT_neuralink_mesh.md (if marked ✅ Ready)
- partnerships/briefs/_URGENT_spacex_wave.md (if marked ✅ Ready)

**How to send:**
1. Convert markdown to PDF or clean email format
2. Include standard intro: "On behalf of David Edward Sproule, inventor of Phyllux technologies..."
3. Attach brief as PDF
4. Include links to phyllux-framework and biomimetic-inventions-public
5. Set expectation: "David will be available for follow-up discussions in [month]"
6. Log in partnerships/pipeline/proposals_sent.md

### 3. Update Status Tracking

**Weekly updates to CONTROL_PANEL.md:**
- Update "Active Conversations" table
- Note any new inquiries
- Flag any urgent/time-sensitive items
- Update "This Week's Goals" completion status

**DO NOT:**
- Change priority rankings
- Modify tier classifications
- Alter deal value estimates

### 4. Run Scheduled Analytics (If Comfortable)

**Safe to run:**
```bash
cd analytics/
python fusion_scorer.py --output ../strategy/OPPORTUNITY_MATRIX.md
python maturity_tracker.py --output ../strategy/MATURITY_DASHBOARD.md
```

**Never run:**
- Scripts that modify source repos
- Scripts that change legal/IP files
- Custom scripts not in analytics/

---

## 🚨 EMERGENCY PROTOCOLS

### If Someone Wants to Sign a Deal

**Response:**
"Thank you for your interest in moving forward. David will be available starting [date] to discuss terms. In the meantime, I'm happy to schedule a call for [date range]."

**DO NOT:**
- Negotiate terms
- Agree to any timeline
- Commit to exclusivity
- Sign anything

**DO:**
- Log the interest with as much detail as possible
- Schedule a tentative call post-treatment
- Send them to phyllux-framework to review tier structure

### If Someone Asks About IP/Patents

**Response:**
"Phyllux technologies are protected through public prior art (established January 7, 2026) and a provisional patent application filed in January 2026. For specific legal questions, I recommend reviewing our public repositories and David will be available to discuss in detail starting [date]."

**DO NOT:**
- Discuss patent strategy
- Share PPA contents (if filed)
- Make claims about patent strength
- Discuss competitive landscape

### If Someone Wants Exclusive Rights

**Response:**
"Exclusivity is negotiable on a case-by-case basis and depends on tier alignment, deal structure, and mission fit. David will need to be directly involved in those discussions. He'll be available starting [date]."

**DO NOT:**
- Grant exclusivity
- Discuss exclusivity terms
- Commit to any specific arrangement

### If Technical Questions Come Up

**Response:**
"For technical details, please see our public demonstrations at github.com/phibronotchi-beep/biomimetic-inventions-public. For deeper technical discussions, David will be available starting [date]."

**DO:**
- Point to public repos
- Share published demos and figures
- Offer to schedule technical deep-dive post-treatment

**DO NOT:**
- Try to answer technical questions beyond what's public
- Share unpublished technical details
- Make performance claims

---

## 📞 COMMUNICATION TEMPLATES

### Acknowledgment Email

```
Subject: Re: [Their Subject] - Phyllux Partnership Inquiry

Dear [Name],

Thank you for your interest in Phyllux technologies. I'm writing on behalf of David Edward Sproule, the inventor.

David is currently unavailable due to a scheduled medical treatment and will return to full availability in [month]. I've logged your inquiry and will ensure David receives it as a priority when he returns.

In the meantime, you can learn more about Phyllux technologies and our licensing model here:
- Framework & Licensing: https://github.com/phibronotchi-beep/phyllux-framework
- Public Demonstrations: https://github.com/phibronotchi-beep/biomimetic-inventions-public

If you'd like to schedule a conversation for [date range], please let me know and I'll coordinate with David upon his return.

Best regards,
[Your Name]
On behalf of David Edward Sproule
Phyllux Technologies
```

### Follow-Up Scheduling

```
Subject: Scheduling Phyllux Partnership Discussion - [Partner Name]

Dear [Name],

David is now available for follow-up discussions regarding [technology/partnership]. 

Based on your inquiry from [date], we believe this aligns with our [Pioneer/Mission-Aligned/Commercial/Research] tier. Would you be available for a 30-minute call during [date range]?

We can discuss:
- Technical validation and feasibility
- Licensing terms and collaboration structure
- Timeline and next steps

Please let me know your availability.

Best regards,
[Your Name] or David Edward Sproule
```

---

## 📊 WEEKLY CHECKLIST

**Every Monday:**
- [ ] Check email for new inquiries
- [ ] Update CONTROL_PANEL.md with current status
- [ ] Review partnerships/pipeline/active_conversations.md
- [ ] Flag any urgent items for post-treatment follow-up

**Every Friday:**
- [ ] Summarize week's activity in a brief note
- [ ] Update "This Week's Goals" completion
- [ ] Note any time-sensitive opportunities
- [ ] Prepare next week's plan (if applicable)

---

## 🎓 LEARNING RESOURCES

**To understand the ecosystem:**
1. Read phyllux-framework README: 4-tier licensing model
2. Read biomimetic-inventions-public README: What the technologies are
3. Read SYSTEM_CONTEXT.md in this repo: How repos relate
4. Read TOP_5_LANES.md: Priority opportunities

**To understand what NOT to touch:**
1. Read .cursor/rules in this repo: AI safety guardrails
2. Read DISCLOSURE.md in phyllux-framework: Maturity levels and qualified language
3. Read PHYLUX_SPINE.md in phyllux-framework: Method spine and IP boundaries

---

## 📞 WHEN IN DOUBT

**Golden Rules:**
1. **Don't modify:** If you're not sure, don't change it
2. **Don't commit:** If you're not sure, don't make legal/business commitments
3. **Don't delete:** Never delete files, repos, or conversations
4. **Do document:** Log everything in partnerships/pipeline/
5. **Do communicate:** Acknowledge inquiries, set expectations, schedule for later

**Contact David (Emergency Only):**
- If someone demands immediate legal action
- If someone threatens IP infringement claims
- If a major partnership opportunity has a hard deadline that can't wait

**Otherwise:**
- Log it, acknowledge it, schedule for post-treatment

---

## 🙏 THANK YOU

Your help during this time is invaluable. By following these guidelines, you're protecting years of work and ensuring the Phyllux ecosystem emerges strong post-treatment.

**Remember:** The goal is to keep things stable and moving forward, not to close deals or make decisions. David will handle strategy and negotiations when he returns.

**You're doing great by simply:**
- Monitoring inquiries
- Logging activity
- Setting expectations
- Protecting the IP

That's all that's needed. Thank you.

---

**Last Updated:** [Date]  
**Helper Name:** [If applicable]  
**David's Expected Return:** [Date]
