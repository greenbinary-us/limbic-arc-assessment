# Limbic Arc — Technical Assessment · Appendix

Sections moved out of the main assessment: Data & Analytics, Open Questions & Status, and Sources.

---

## A. Data & Analytics

The write-up asks "what are we doing with analytics?" and "what metrics determine business health?", and notes GA + Power BI are underused.

- **Define the business-health metric set first**, then instrument. Candidates for a subscription MLM:
  - **Revenue/retention:** MRR, churn / involuntary churn (failed payments), reactivation, LTV, ARPU.
  - **Billing integrity:** failed-charge / dunning rate, token-mismatch / reconciliation-exception count (ties to the payments deep dive).
  - **Field health (MLM-specific):** active distributors, rank-advancement velocity, enroller activity, genealogy depth/width, F&F attach rate.
  - **Commerce:** checkout conversion, subscription attach (e.g., Pet InfoBoost), AOV.
- **Unify the data.** Profile/subscription/payment split across Exigo + Fluid means analytics are stitched manually. A modest data pipeline into a single warehouse (the extracted services publishing events makes this natural) turns Power BI from "reports a few sources" into "single source for decisions."

---

## B. Open Questions & Status

| # | Question | Status / Answer |
|---|----------|-----------------|
| B.1 | Payment/billing behavior at the tokenization seam | Resolved for this draft — framing reduced to "tokenization happens in multiple places with no single authority." |
| B.2 | Profile source of truth | Resolved — Exigo. The Profile service is a facade; Exigo remains the record. |
| B.3 | Card data on Limbic Arc sites / PCI scope | Target (unverified): Limbic Arc sites should collect no credit-card info and be out of PCI scope. (See Verification Items V2/V3.) |
| B.4 | Merchant account(s) & current PCI SAQ level | Yet to be verified. (See Verification Items V3.) |
| B.5 | Replicated-site usage | Clarified: low usage = low functionality, but used by all users. On the critical path; cannot be retired as low-priority. |
| B.6 | Fluid API surface (hosted capture, subscription events, 2-way sync) | To be confirmed. Gates Phase 3 design. (See Verification Items V4.) |
| B.7 | Delivery capability | Confirmed: Limbic Arc works through vendors with no technical representation of its own. Phase 1 must put technical representation in place (team and/or integration partner). |
| B.8 | Web App scope boundary (SSO-only?) | To be confirmed. (See Verification Items V6.) |

---

## C. Sources

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
