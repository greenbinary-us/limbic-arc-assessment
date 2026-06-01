# Limbic Arc — Technical Assessment · Verification Items

Items extracted from the assessment that must be validated with the Limbic Arc, Exigo, and Fluid teams before acting. (Previously inline `[VERIFY]` tags in the main document.)

| # | Item | Where it applies | Needed to |
|---|------|------------------|-----------|
| V1 | Exact downstream billing effects of split tokenization — confirm against actual billing records. | §6.1 Deep Dive (fragmentation) | Quantify the payment risk and target the reconciliation control. |
| V2 | Current state of card handling on Limbic Arc surfaces — confirm whether/where Limbic Arc sites currently collect card data. | §6.3 (target: no card data / out of PCI scope) | Confirm the gap between current and target PCI posture. |
| V3 | Merchant account(s) and current PCI SAQ level across Exigo and Fluid. | §6.3 / §9 Security | Size the PCI-scope-reduction work and confirm SAQ-A feasibility. |
| V4 | Fluid API capabilities — hosted card capture, subscription events, and 2-way sync. | §8.2 guardrails / Roadmap Phase 3 | Gate the Payments & Subscriptions extraction design. |
| V5 | Subscription volume split between Exigo and Fluid (which subscriptions, and what % of volume/revenue each holds). | Roadmap Phase 3 (migration plan) | Size and sequence the subscription migration. |
| V6 | Web App scope boundary — confirm SSO is the only integration touchpoint. | §2 Scope | Confirm the out-of-scope boundary. |

*Resolve these as part of Phase 1 (discovery / integration mapping); each gates a specific downstream decision.*
