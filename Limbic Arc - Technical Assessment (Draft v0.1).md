# Limbic Arc — Integration & Platform Technical Assessment

**Status:** Initial draft (v0.1) — for review and iteration
**Date:** 2026-05-31
**Prepared by:** Integration assessment
**Source material:** `Write up.txt`, `inconsistent user experience/` screenshots, vendor documentation (Exigo, Fluid), and assessor analysis

> **Confidence & verification note.** Findings below are tagged with confidence levels — **HIGH** (directly observed in screenshots/write-up or vendor-documented), **MEDIUM** (strongly implied by the evidence and standard for this class of system), **LOW / ASSUMPTION** (inferred, needs confirmation with the Limbic Arc / Exigo teams). Items marked **[VERIFY]** are claims to validate before acting. This is a draft; nothing here should be treated as a final architectural decision.

---

## 1. Executive Summary

Limbic Arc runs a direct-selling (MLM) business on two primary platforms: **Exigo** as the MLM/commission engine and back office, and **Fluid (fluid.app)** as the modern e-commerce/shopping experience. Exigo is a strong commission and genealogy engine; Fluid is a strong storefront and rep-enablement app. The problem is not either platform individually — it is the **seam between them**, and the legacy **Exigo .NET boilerplate** that the customer-facing and distributor-facing web properties are still built on.

The system today exhibits four compounding issues:

1. **Split source of truth.** Profiles, subscriptions, and especially **payment tokenization** live in *both* Exigo and Fluid with no single authority. This has already produced **double-charging incidents** from token mismatches — the most severe, customer-trust-damaging symptom in the assessment.
2. **Tightly-coupled legacy front end.** The customer admin and distributor back office are forked from Exigo's .NET boilerplate, with no front-end/back-end separation, thin documentation, and a hard dependency on Exigo for any change. Velocity and cost of change are dictated by Exigo's queue, not Limbic Arc's roadmap.
3. **Fragmented, inconsistent user experience.** At least three distinct visual identities are live at once (modern Fluid, white-header Exigo admin, green-header Exigo affiliate). Users also re-authenticate when crossing system boundaries.
4. **Missing platform foundations.** No role-based access control (RBAC) on the sites, limited administrative tooling, no defined CI/CD discipline, and analytics that capture data but don't yet drive decisions. The team is in reactive "firefighting" mode rather than building.

**Headline recommendation:** Adopt a **Strangler Fig** modernization strategy — incrementally extract the bottleneck domains (Profile, Payments/Tokenization, Subscriptions, Family & Friends, Signup/Upgrade) out of the Exigo boilerplate into independently deployable, API-fronted services, with an explicit, enforced **source-of-truth contract** per domain. Keep Exigo as the system of record for *commissions and genealogy* (what it is best at), let Fluid own *commerce and tokenization* (what it is best at), and stop retrofitting Exigo for things it was never designed to do.

---

## 2. Scope & Methodology

**In scope:** Customer-facing landing/subscription site, customer admin, distributor (affiliate) admin/back office, the Exigo↔Fluid integration seam, subscriptions, payments/tokenization, profile, family & friends, data/analytics, and platform concerns (hosting, observability, CI/CD, security/RBAC, AI enablement).

**Explicitly out of scope:** The Web App itself — *except* the single touchpoint that users should not have to re-authenticate to reach it (SSO).

---

## 3. Current-State System Inventory

| # | System | Platform / Stack | Primary Role | Source-of-truth today |
|---|--------|------------------|--------------|------------------------|
| 1 | **Landing / subscription site** (limbicarc.com) | Fluid (modern) | Marketing, plan discovery, subscribe/checkout | Fluid for new commerce |
| 2 | **Customer Admin** | Exigo .NET boilerplate (white-header theme) | Account info, subscription mgmt, card update, Pet InfoBoost, Family & Friends | Exigo (tokenizes card in Exigo) |
| 3 | **Distributor / Affiliate Admin (Back Office)** | Exigo .NET boilerplate (green-header theme) | Genealogy, title advancement, commissions, affiliate onboarding, tax info | Exigo |
| 4 | **MLM / Commission Engine** | Exigo | Genealogy, volume, commission calculation & payout | Exigo (correct) |
| 5 | **Web App** | (out of scope, SSO touchpoint only) | Core product experience | — |
| 6 | **Data / Analytics** | Google Analytics + Power BI | Reporting | Split across sources |

**Confidence:** HIGH for systems 1–4 (directly evidenced). System 5 per write-up.

### 3.1 Visual / UX evidence (from screenshots)

The screenshot set demonstrates **three concurrent design languages**, which is the visible surface of the deeper architectural split:

- **Modern Fluid theme** — gradient hero ("Join The Movement"), "What's Included / $99" subscription page with a slide-in checkout drawer, modern Contact Us. *(images 3, 4/5, 6.1)*
- **Exigo Customer Admin, white header** — "Account Information", "Pet InfoBoost Program" upsell with inline pricing/charge logic. *(images 1, 5.1)*
- **Exigo Affiliate/Distributor, green header** — "Affiliate Information / Your Enroller", the distributor dashboard with "Title Advancement", compensation plan, news widgets, and an older green "Contact us" page. *(images 2, 6, 7)*

A user moving from "subscribe" (Fluid) → "manage my account" (Exigo customer) → "affiliate opportunity / back office" (Exigo distributor) crosses **three different-looking applications**, and (per write-up) **logs in more than once** along the way.

---

## 4. Root-Cause Analysis (the "why", not just the "what")

The individual complaints in the write-up are symptoms of a small number of root causes. Naming them keeps the recommendations honest.

**Root cause A — Exigo boilerplate was never meant to be a long-term product surface.**
Exigo's strength is the commission/genealogy engine and its data architecture (200+ APIs, replicated data, SOC 2 Type II). The .NET boilerplate "replicated site" code ships to *bootstrap* a customer onto Exigo's own commerce/replicated-site flows — it is a starter kit, not a product platform. Limbic Arc has retrofitted it to do things (custom subscriptions, third-party commerce, Family & Friends, Pet InfoBoost upsells) it was not designed for. *(Confidence: HIGH — consistent with vendor positioning and the write-up.)*

**Root cause B — No separation of concerns in the legacy front end.**
The customer and distributor sites have no front-end/back-end boundary; presentation, business logic, and Exigo data access are interleaved. Combined with thin documentation, this means **every change requires Exigo tribal knowledge**, so Limbic Arc cannot move without Exigo, and Exigo's priority queue sets Limbic Arc's release timeline. *(Confidence: HIGH — stated in write-up; classic tightly-coupled-legacy signature.)*

**Root cause C — No designated source of truth per domain.**
Because two platforms (Exigo, Fluid) each independently believe they own profile/subscription/payment data, the same business object exists in two places with divergent state. This is the direct mechanism behind tokenization conflicts and double-charges. *(Confidence: HIGH.)*

**Root cause D — Missing platform engineering foundations.**
No RBAC, limited admin tooling, no CI/CD discipline, reactive observability. These don't cause the architecture problem but they *amplify* it: every fix is slow, risky, and hard to verify, which is what keeps the team in firefighting mode. *(Confidence: HIGH.)*

> **Key reframing:** This is not "replace Exigo" and it is not "replace Fluid." It is **"own the seam and the surfaces."** Extract the contested domains into Limbic-Arc-owned services with clear contracts to each platform.

---

## 5. Deep Dive — Subscriptions & Payment Tokenization (the #1 risk)

The write-up correctly identifies **subscriptions as the main problem area**, and tokenization as the sharpest edge. This deserves its own treatment because it is the only issue actively causing **financial harm and customer-trust loss** (double charges).

### 5.1 What's happening (failure model)

- Subscriptions exist **partly in Exigo, partly in Fluid**. Card tokenization happens in **both** — a customer updating their card in the Exigo customer admin tokenizes in *Exigo*; a Fluid checkout tokenizes in *Fluid*.
- There is **no authoritative mapping** between the Exigo payment token and the Fluid payment token for the same customer/card.
- When a recurring charge runs, the billing initiator (Exigo autoship and/or Fluid subscription) charges against *its* token. If both think they own the subscription, or if a card update propagated to only one side, the customer can be **charged twice** or charged on a **stale token**. *(Confidence: MEDIUM-HIGH — this is the standard mechanism for the symptom described; exact trigger conditions are [VERIFY] with billing logs.)*

### 5.2 Why "tokenize everywhere" is the trap

PCI tokens are **gateway/processor-scoped** — an Exigo token and a Fluid token are not interchangeable even for the *same* card, because they may reference different merchant accounts/processors. So "the card is on file in both systems" does **not** mean "billing is consistent." Reconciling by card number is also a PCI anti-pattern. The only durable fix is **one tokenization authority**.

### 5.3 Target state (recommended)

1. **Fluid is the single tokenization authority and recurring-billing processor of record** (matches the stated desired state). All card capture/update — including the flows currently in Exigo customer admin — route to Fluid's vault.
2. The **Exigo customer-admin "update card" screen must stop tokenizing in Exigo.** Either (a) embed/redirect to Fluid's hosted card capture, or (b) call a Limbic-Arc Payments service that proxies to Fluid. Until this is done, the dichotomy and the double-charge risk persist. *(This is the single highest-value fix.)*
3. **Subscription state has one owner (Fluid, target).** Exigo should receive subscription/payment *events* (for volume/commission purposes) rather than independently initiating billing.
4. **Idempotency + a billing reconciliation ledger.** Every recurring charge carries an idempotency key tied to `(subscription_id, billing_period)`. A daily reconciliation job compares Exigo-side and Fluid-side charge records and **alerts on any duplicate or orphaned charge** before the customer notices. *(This is the safety net during the long migration window the write-up anticipates.)*

### 5.4 Reality check — the dichotomy will persist during migration

The write-up is right that dual tokenization "will continue for a long time." That makes the **reconciliation ledger and duplicate-charge alerting non-optional** as a near-term, defensive control — it is cheaper and faster than the full migration and directly stops the bleeding. **Recommend treating it as a Phase 0 quick win.**

---

## 6. Source-of-Truth Model (expanded from the write-up table)

The write-up's table is the right instrument. Expanded with ownership rationale, integration direction, and a migration note:

| Domain | Current state | Target SoT | Why | Sync direction (target) |
|--------|---------------|-----------|-----|--------------------------|
| **Profile / Identity** | Mixed (Exigo + Fluid) | **Exigo** (or dedicated Profile service — see note) | Identity must be singular; Exigo holds genealogy keyed to the person | Profile svc → Fluid (push), Exigo authoritative |
| **Payin / Tokenization** | Mixed (Exigo + Fluid) | **Fluid** | One PCI vault, one processor of record; stops double-charge | Card capture → Fluid only |
| **Commission payouts** | Exigo | **Exigo** | Core competency; do not move | Exigo authoritative |
| **Family & Friends** | Exigo extended (retrofit) | **Separate service** | Retrofit is brittle; cross-cuts profile + subscription + entitlement | F&F svc ↔ Exigo + Fluid |
| **Subscriptions** | Mixed | **Fluid** | Commerce/recurring billing is Fluid's strength | Fluid → Exigo (events for volume) |

**Note on Profile [DECISION NEEDED]:** The write-up lists Profile's desired SoT as **Exigo**, while §5 (recommendations) proposes *extracting profile into a separate application with APIs*. These are reconcilable but should be stated explicitly: a **Profile service** can be the *API surface and integration hub* while **Exigo remains the system of record** behind it (the service is a facade + cache + event publisher, not a competing database). Recommend documenting it this way to avoid creating a *fourth* place identity lives. *(Confidence: MEDIUM — this is an architecture decision the team should ratify.)*

**Governance rule to adopt:** *Exactly one* system may be the writer/owner for each domain. Every other system is a read-replica/subscriber that receives changes via events or sync. No screen anywhere may write to a non-owning system. This single rule, enforced, prevents the entire class of "mixed" bugs.

---

## 7. Target Architecture & Recommendations

### 7.1 Strategy: Strangler Fig, not big-bang rewrite

Incrementally route specific capabilities away from the Exigo boilerplate to new Limbic-Arc-owned services behind a stable API/facade, retiring boilerplate code domain-by-domain. This preserves the working commission engine, contains risk, and lets the team demonstrate value early. *(Confidence: HIGH — appropriate pattern for tightly-coupled legacy with a strong core engine.)*

### 7.2 Extracted services (matches & extends the write-up's recommendations)

The write-up's five extractions are sound. Sequenced by **value × urgency**:

1. **Payments / Tokenization service** *(do first — financial risk)* — Fronts Fluid's vault; becomes the *only* path for card capture/update; replaces the Exigo-side tokenization in customer admin.
2. **Subscriptions service** *(second — main problem area)* — Owns subscription lifecycle on Fluid; publishes events to Exigo for volume/commission.
3. **Profile service** *(third — unblocks everything)* — Single identity API in front of Exigo-as-record; the SSO and RBAC anchor.
4. **Family & Friends service** *(fourth)* — Removes the brittle Exigo retrofit; models entitlements/relationships cleanly (this is what makes "Pet InfoBoost free for active F&F" and "birthday discount" tractable — see §11).
5. **Signup / Upgrade flow application** *(fifth, but partly enabled by 1–4)* — Unified, modern enrollment + upgrade across customer and affiliate, built on the services above.

**Architectural guardrails for the new services (assessor additions):**
- **API-first, contract-tested** boundaries (e.g., OpenAPI; consumer-driven contract tests so Exigo/Fluid schema drift is caught in CI, not production).
- **Event-driven sync** with an outbox pattern + idempotent consumers — this is how you make 2-way sync (which Fluid advertises) reliable instead of a race condition.
- **Anti-corruption layer** in each service so Exigo's and Fluid's data models don't leak into Limbic Arc's domain.
- **Front-end/back-end separation** — new surfaces are a thin modern web front end calling these APIs, *not* more coupled .NET boilerplate. This is what finally breaks the Exigo-dependency for changes.

### 7.3 Cross-cutting platform foundations (the write-up's other asks)

| Concern | Current | Recommendation | Confidence |
|--------|---------|----------------|-----------|
| **Identity / SSO** | Re-login across systems | Central IdP (e.g., OIDC) so customer/affiliate session carries into the Web App and across surfaces — directly fixes the out-of-scope touchpoint | HIGH |
| **RBAC** | None on the sites | Role/claim model at the IdP + per-service authorization; admin vs. customer vs. affiliate vs. support roles | HIGH |
| **Hosting** | Shared/unclear | Dedicated cloud subscription/tenant for Limbic Arc (isolation, cost attribution, blast-radius control) — matches write-up | HIGH |
| **Observability** | Limited / reactive | Datadog (per write-up) — but specifically: distributed tracing across the Exigo↔Fluid seam, **billing reconciliation dashboards & duplicate-charge alerts**, synthetic checks on checkout/card-update | HIGH |
| **CI/CD** | Not defined | Establish branch strategy, automated build/test gates, IaC, and progressive deploys; **enforce the test-first discipline** as the team builds new services | HIGH |
| **Analytics** | GA + Power BI (capture only) | Define **business-health metrics** (see §9) and a semantic layer; move from "we have dashboards" to "dashboards drive decisions" | MEDIUM |

---

## 8. Security & Compliance Findings (assessor additions)

These were under-emphasized in the write-up and matter for an MLM/payments business:

- **No RBAC = authorization gap.** Without roles, any authenticated user may reach functions they shouldn't; support/admin actions aren't separated. **HIGH priority.** *(Confidence: HIGH — stated absence.)*
- **PCI scope is currently larger than it should be.** Tokenizing in Exigo *and* Fluid means **two** environments are in PCI scope. Consolidating tokenization to Fluid (hosted fields/redirect) shrinks Limbic Arc's PCI footprint and is a compliance *and* risk win. **[VERIFY]** current PCI SAQ level and who holds the merchant account(s). *(Confidence: MEDIUM-HIGH.)*
- **Single-sign-on absence** is both UX and security debt (more credential surfaces, inconsistent session/MFA policy).
- **Audit trail.** With multiple writers to profile/subscription/payment, there is likely no unified audit log of "who changed what, where." Needed for dispute/double-charge investigations. **[VERIFY].**
- **Vendor lock-in / exit risk.** The write-up's point is well taken: boilerplate code is non-portable if Limbic Arc ever leaves Exigo. The extracted-services architecture *is* the mitigation — it makes the engine replaceable behind a stable contract.

---

## 9. Data & Analytics (assessor additions)

The write-up asks two open questions — *"what are we doing with analytics?"* and *"what metrics determine business health?"* — and notes GA + Power BI are underused. Recommendations:

- **Define the business-health metric set first**, then instrument. Candidate North-Star + supporting metrics for a subscription MLM:
  - **Revenue/retention:** MRR, churn / involuntary churn (failed payments!), reactivation, LTV, ARPU.
  - **Billing integrity (new, ties to §5):** duplicate-charge rate, failed-charge/dunning rate, token-mismatch incidents — *these should be a standing dashboard given the double-charge history.*
  - **Field health (MLM-specific):** active distributors, rank advancement velocity, enroller activity, genealogy depth/width, F&F attach rate.
  - **Commerce:** checkout conversion, subscription attach (e.g., Pet InfoBoost), AOV.
- **Unify the data.** Profile/subscription/payment split across Exigo + Fluid means analytics are stitched manually. A modest **data pipeline into a single warehouse** (the extracted services publishing events makes this natural) turns Power BI from "reports a few sources" into "single source for decisions."
- *(Confidence: MEDIUM — exact KPIs to be agreed with the business.)*

---

## 10. AI Enablement (from "defense" to "offense")

The write-up's framing — *playing defense when we should be on offense* — is correct, and the architecture work is the prerequisite. AI features are hard to ship on coupled boilerplate; they're easy on clean APIs + unified data. Once §7 is underway:

- **Internal / developer velocity (defense → neutral):** AI-assisted development to reduce firefighting; automated triage of support/billing issues using the reconciliation data.
- **Customer-facing (offense):** AI-curated InfoBoost recommendations ("Custom InfoBoost Creation" is already a product hook — see image 4), churn-risk prediction with proactive save offers, distributor coaching/"next best action" (Fluid already has an AI assistant, "Catchups", to integrate with rather than rebuild).
- **Guardrail:** AI features should consume the *Profile/Subscription/Payments APIs*, never the legacy boilerplate directly — otherwise they inherit the coupling. *(Confidence: MEDIUM — opportunity framing, not committed scope.)*

---

## 11. "What If" Scenarios — Mapped to the Target Architecture

The write-up's escalating use cases are an excellent litmus test. Here's *why each is hard today* and *what makes it easy after extraction* — this is the concrete payoff of the recommendations.

| Use case | Hard today because… | Enabled by… | Difficulty (post-extraction) |
|----------|---------------------|-------------|------------------------------|
| **Common banner for a user group on all logged-in pages** | No shared layout/component across the 3 surfaces; no group/segment concept; no RBAC/segmentation | Shared front-end shell + Profile/segment service + feature-flag/targeting | Low |
| **Modernize Contact Us to match Fluid** | Page lives in Exigo green-theme boilerplate; change needs Exigo | Move surface to modern front end calling APIs | Low–Med |
| **Match modern UX site-wide** | Three coupled apps, no design system, Exigo dependency | Design system + progressive surface migration (Strangler Fig) | Med–High |
| **User-customizable theme / movable widgets / saved prefs** | No user-preference store; no componentized front end | Profile/preferences service + component-based UI | High |
| **5% F&F birthday discount** | F&F is an Exigo retrofit; discount engine + DOB + billing all split across Exigo/Fluid | F&F service (entitlements) + Subscriptions/Payments service (promo applied at billing in Fluid) + event on birthday | Med–High |

**Insight:** every "even harder" case collapses to *the same four missing capabilities* — a **profile/preferences store, a clean F&F entitlement model, a single billing/promo authority, and a componentized front end**. That is exactly what §7 builds. The roadmap pays for itself across all of these, not just one.

---

## 12. Suggested Phasing / Roadmap (draft — to refine with the team)

> Sequenced to **stop financial bleeding first, unblock velocity second, modernize experience third.** Durations are placeholders **[VERIFY/SIZE]**.

- **Phase 0 — Stop the bleeding (weeks).** Billing reconciliation ledger + duplicate-charge alerting (Datadog); audit logging on payment/subscription writes; freeze *new* Exigo-side tokenization where avoidable. *Defensive, cheap, high ROI.*
- **Phase 1 — Foundations.** Dedicated cloud subscription; CI/CD + test-first discipline; central IdP/SSO + RBAC skeleton; observability/tracing across the seam.
- **Phase 2 — Payments & Subscriptions extraction.** Consolidate tokenization to Fluid; Payments service; Subscriptions service; retire Exigo-side card capture. *(Resolves the #1 problem.)*
- **Phase 3 — Profile & Family/Friends extraction.** Profile API (Exigo-as-record), F&F entitlement service. *(Unblocks segmentation, banners, birthday discount, prefs.)*
- **Phase 4 — Unified Signup/Upgrade + UX modernization.** Modern front-end shell + design system; migrate surfaces off green/white Exigo boilerplate; SSO into Web App.
- **Phase 5 — Analytics & AI offense.** Unified warehouse + business-health dashboards; first customer-facing AI features.

---

## 13. Open Questions & Assumptions (to resolve before finalizing)

1. **[VERIFY]** Exact double-charge trigger conditions — pull billing logs for affected accounts; is it card-update propagation, dual-initiation, or retry/dunning?
2. **[DECISION]** Profile SoT — Exigo-as-record behind a Profile service, vs. a standalone profile datastore. (Recommend the former.)
3. **[VERIFY]** Merchant account(s) and PCI SAQ scope across Exigo and Fluid.
4. **[VERIFY]** Which subscriptions are in Exigo vs. Fluid today, and what % of volume/revenue each represents (sizes the migration).
5. **[VERIFY]** Replicated-site usage — write-up says "very low"; confirm so it can be deprioritized/retired.
6. **[VERIFY]** Fluid's API surface for tokenization/subscriptions/2-way sync — confirm it supports the events and hosted card capture the target design assumes.
7. **[CONFIRM]** Team capacity, in-house .NET vs. modern-stack skills, and appetite for the phasing above.
8. **[CLARIFY]** Web App scope boundary — confirm SSO is the only integration touchpoint expected.

---

## 14. Sources

- Exigo platform, APIs, replicated sites, data architecture, SOC 2 Type II:
  - [Exigo — Enterprise MLM Software](https://www.exigo.com/)
  - [Exigo Platform: Enterprise Direct Selling PaaS (SOC 2 Type II)](https://www.exigo.com/exigo-platform/)
  - [Exigo MLM Software — Real-Time Commissions & Genealogy](https://www.exigo.com/mlm-software/)
  - [MLM Shopping Platforms / Replicated Websites — Exigo](https://www.exigo.com/resources/blog/mlm-shopping-platforms-the-engine-behind-scalable-direct-selling/)
  - [Custom Exigo API Development & Integration — Sunrise Integration](https://www.sunriseintegration.com/pages/platforms/exigo)
- Fluid platform (bolts onto existing back office, 2-way sync, commerce/CRM, AI "Catchups"):
  - [fluid.app](https://www.fluid.app/)
  - [Fluid — Platform](https://www.fluid.app/home/page/platform)
- Internal: `Write up.txt`; `inconsistent user experience/` screenshots (1–7).

---

*End of draft v0.1. Next iteration should fold in answers to §13, right-size §12, and (if available) confirm Fluid/Exigo API capabilities against vendor docs or a technical contact.*
