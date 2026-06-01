# Limbic Arc — Platform Assessment
## Leadership Edition

**Audience:** Limbic Arc leadership (ownership / executive team)
**Status:** Draft v0.1 — for discussion
**Date:** 2026-05-31
**Companion document:** *Technical Assessment (Draft v0.2)* — the detailed engineering analysis behind this summary.

> **A note on certainty.** This summary reflects what we observed in your systems and the materials shared. A few items still need confirmation with your teams and vendors; they're marked **[to confirm]**. Nothing here is a final decision — it's a basis for one.

---

## 1. The bottom line (read this if nothing else)

Limbic Arc runs on two good platforms: **Exigo** (the engine that runs your distributor network, ranks, and commissions) and **Fluid** (your modern online store). **Neither is the problem.** The problem is the **gap between them**, the **aging software** your customer and distributor websites are built on, and the fact that **you have no in-house technology team** to change any of it — so every update waits in your vendor's queue.

The practical effects you're already feeling:
- **Customers' payment information lives in two systems at once**, which makes subscriptions fragile and creates billing and compliance risk.
- **You can't ship changes quickly or cheaply** — even small ones depend on Exigo's priorities and timeline, not yours.
- **Customers see three different-looking websites and log in more than once**, which erodes trust and adds support load.
- **You're stuck playing defense** ("firefighting") instead of launching the features that would grow the business.

**Our recommendation:** modernize **gradually and safely**, one piece at a time — keep Exigo for what it's great at (commissions), let Fluid own payments and the store, and lift the few problem areas (payments, subscriptions, profile, family & friends, sign-up) out of the old software into modern, you-own-it building blocks. **The first step is small, low-risk, and starts paying off in weeks.** But it requires putting a delivery team in place — which is the single decision that unlocks everything else.

---

## 2. What we assessed

Your customer-facing site, your customer account area, your distributor (affiliate) back office, the connection between Exigo and Fluid, and the supporting concerns leadership cares about: **billing reliability, security, customer experience, speed of change, data/insights, and cost.** Your core Web App was out of scope except for one point: customers shouldn't have to log in repeatedly to reach it.

---

## 3. The five things that matter — and why

| # | What's happening | Why it matters to the business |
|---|------------------|-------------------------------|
| 1 | **Payment & subscription data is split** between Exigo and Fluid, with no single system in charge of "the card on file." | **Direct risk to revenue and customer trust.** Fragile subscriptions, billing inconsistencies, and a larger-than-necessary compliance (PCI) footprint. This is the #1 issue to fix. |
| 2 | **You depend on your vendor to change anything.** The websites are built on old, tightly-wound software only the vendor fully understands. | **You don't control your own speed or cost.** Simple changes are slow and expensive; your roadmap runs on someone else's calendar. |
| 3 | **Three different website experiences** and **repeated logins** across store, account, and affiliate areas. | **Brand and trust erosion**, lower conversion, more support tickets, a fragmented customer journey. |
| 4 | **Missing basics:** no proper access control (who can see/do what), no single sign-on, and analytics that *collect* data but don't yet *drive decisions*. | **Security and oversight gaps**, and decisions made without a clear view of business health. |
| 5 | **No in-house technology team.** | **The root cause of #2.** With no one to own the software, change is outsourced to the vendor by default. Nothing else improves durably until this is addressed. |

---

## 4. The payments issue, in plain terms (the one to act on first)

When a customer saves a credit card, it gets "tokenized" — turned into a secure reference. Today that happens in **both** Exigo and Fluid, and the two don't share a single source of truth for it. Two consequences:

- **Subscriptions become fragile and hard to reason about** — the kind of condition that leads to billing surprises and customer-service escalations.
- **Your compliance exposure is larger than it needs to be.** Because card handling happens in two places, more of your environment is subject to payment-security (PCI) obligations than necessary.

**The fix is well understood:** make **Fluid the single home for payment cards**, and ensure **Limbic Arc's own websites never handle raw card details at all** — which both removes the fragility and *shrinks* your compliance burden. *(Target state; current specifics [to confirm].)* This is the highest-value, most contained first project.

---

## 5. What this is costing you today

We're not putting a dollar figure on this yet (that needs your numbers), but the *form* of the cost is clear:

- **Time and energy** spent firefighting instead of serving customers or building features.
- **Slow, expensive changes** — every enhancement carries a vendor-queue tax.
- **Risk** concentrated in billing and compliance, where mistakes are costly and visible.
- **Opportunity cost** — the features that would differentiate Limbic Arc aren't getting built.
- **Strategic exposure** — today, if you ever wanted to change platforms, the custom website code couldn't come with you. You don't own your own destiny.

---

## 6. What "good" looks like

- **One source of truth** for each thing that matters: Exigo owns commissions and profiles, Fluid owns payments and the store, and the connection between them is reliable and monitored.
- **You own your software**, running in your own cloud account — changeable on *your* timeline, not a vendor's.
- **One consistent, modern experience** with a single login across store, account, and affiliate.
- **Decisions driven by data** — a clear dashboard of business health (subscribers, churn, retention, field/distributor activity).
- **On offense** — able to launch new ideas quickly (a targeted promotion, a birthday discount, a UX refresh) instead of filing a vendor ticket and waiting.

---

## 7. The recommended path — gradual, safe, reversible

We do **not** recommend a risky "big rewrite." We recommend a proven, incremental approach: **keep everything running, and modernize one area at a time**, retiring the old software piece by piece. Each step stands on its own and leaves you better off — there's an **exit ramp at every phase**.

| Phase | What leadership gets out of it |
|-------|-------------------------------|
| **0 — Get capability in place & stop the bleeding** | A team that can actually make changes; early protective wins on billing and compliance. **Small, fixed, low-commitment first step.** |
| **1 — Foundations** | Your own secure cloud, proper access control, single sign-on, and the ability to ship safely. |
| **2 — Payments & subscriptions** | The #1 fix: one home for cards, reduced compliance burden, reliable subscriptions. |
| **3 — Profile & family/friends** | Clean, flexible customer data — unlocks promotions, segmentation, personalization. |
| **4 — Unified sign-up & modern experience** | One consistent, modern, single-login experience across the journey. |
| **5 — Insights & AI** | Decision-ready dashboards and the first customer-facing AI features — moving you onto offense. |

**Why this order:** stop the riskiest/most expensive bleeding first (payments, vendor lock-in), build the foundation, then modernize the experience, then innovate.

---

## 8. How fast could we move on new ideas? (a useful test)

You raised some "what if" ideas. They're a good measure of progress, because they're hard *today* and become easy *after* the modernization:

| Idea | Today | After modernization |
|------|-------|---------------------|
| Show a banner to a specific group on all logged-in pages | Hard / vendor-dependent | Easy |
| Modernize the Contact Us page | Vendor change request | Quick |
| Match a modern look-and-feel everywhere | Very hard (three systems) | Achievable, phased |
| Let users personalize their dashboard | Not possible today | Feasible |
| Give Family & Friends a 5% birthday discount | Hard (data split across systems) | Straightforward |

**The point:** every one of these depends on the *same* handful of fixes in the roadmap. The investment pays off across all of them, not just one.

---

## 9. The one decision that unlocks everything

Because there's **no in-house team today**, someone has to do this work. There are three ways to staff it:

- **Build** — hire your own team (most control, but 3–6 months before real progress).
- **Partner** — bring in an experienced firm (fastest start, expertise on day one).
- **Hybrid** — start with a partner and grow your own team over time (fast start *and* you end up owning the capability).

**For where Limbic Arc is today — no team, real urgency on billing, and a desire to eventually own this — a partner-led start that transitions to hybrid is the most sensible.** Whichever you choose, the key is to **decide soon**: this choice gates the entire roadmap.

---

## 10. What we need from leadership

1. **Direction on staffing** — build, partner, or hybrid (Section 9).
2. **Go-ahead for a small Phase 0** — a short, fixed-scope first step that delivers the integration map, early billing/compliance protections, and a sized plan for the rest. Low risk, fast value.
3. **A few confirmations** so we can finalize specifics **[to confirm]:** current card-handling/compliance setup, how your subscriptions are split between Exigo and Fluid, what your store platform (Fluid) supports via its connections, and the exact boundary of the Web App.

---

## 11. Closing

Limbic Arc has the right two platforms and a real business. What's missing is **ownership of the layer in between** and **the capability to change it.** The path forward is low-risk and incremental, the first step is small, and the payoff — lower risk, faster delivery, a better customer experience, and the freedom to innovate — is substantial. The sooner the staffing decision is made, the sooner the firefighting stops.

*Detailed technical analysis, source-of-truth model, security findings, and the full phased plan are in the companion Technical Assessment (v0.2).*
