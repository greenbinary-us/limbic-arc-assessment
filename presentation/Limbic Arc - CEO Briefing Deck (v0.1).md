# Limbic Arc — Platform Assessment
## CEO Briefing — Slide Deck Script

**Purpose:** Build a PowerPoint from this document. Each numbered section below is **one slide**.
**Audience:** Limbic Arc leadership — non-technical; the CEO is the decision-maker.
**Companion:** the detailed *Technical Assessment (v0.4)*.

**How to read each slide section:**
- **On slide** = the few words/visuals to put on the slide (keep it sparse).
- **Image** = drop in the named picture from the `images/` folder (already sized 16:9).
- **Say** = speaker notes / talk track (not shown on the slide).

> A note on certainty: a few specifics still need confirmation with your teams and vendors. Those are marked **[to confirm]**. Nothing here is a final decision — it's a basis for one.

**Suggested length:** ~17 slides, ~20–25 minutes with discussion.

---

## SLIDE 1 — Title

**On slide:**
- **Limbic Arc — Platform Assessment**
- A plain-language briefing for leadership
- *Date · Prepared for the leadership team*

**Image:** *(optional — use a solid brand color or the title layout in the .pptx)*

**Say:** This is the leadership view of a deeper technical assessment. I'll keep it in plain business terms: what's working, what's at risk, what it's costing you, and what I recommend you do — in what order. There's one decision at the end that unlocks everything else.

---

## SLIDE 2 — The bottom line (read this if nothing else)

**On slide:**
- You run on **two good platforms** — **Exigo** (distributor network, ranks, commissions) and **Fluid** (your modern online store). **Neither is the problem.**
- The problem is the **gap between them**, the **aging software** your websites are built on, and having **no in-house tech team** to change any of it.
- **Recommendation:** modernize **gradually and safely**, one piece at a time. The first step is **small, low-risk, and starts paying off in weeks.**

**Say:** If you remember one slide, this is it. Your two core platforms are good choices — keep them. What hurts you is the seam between them, the old website code, and the fact that every change waits in a vendor's queue because you have no one in-house to own it. The fix is *not* a risky rewrite — it's a gradual, reversible modernization. But it requires one decision: putting a team in place. We'll come back to that.

---

## SLIDE 3 — What we looked at

**On slide:**
- Your **customer-facing site**, **customer account area**, and **distributor (affiliate) back office**
- The **connection between Exigo and Fluid**
- The concerns leadership cares about: **billing reliability, security, customer experience, speed of change, and insights**
- *Out of scope:* your core Web App — except that customers shouldn't have to **log in repeatedly** to reach it

**Say:** We assessed the surfaces your customers and distributors actually touch, plus the plumbing between your two platforms, through a leadership lens — reliability, risk, experience, speed, cost. Your core product Web App was out of scope, with one exception we'll flag: people shouldn't have to log in over and over to get to it.

---

## SLIDE 4 — How it works today

**On slide:**
- Three separate websites on top of two systems that don't share **one source of truth**

**Image:** `images/current-state.png`

**Say:** Here's the shape of things today. A customer or distributor crosses three different-looking websites — your modern Fluid store, the white-themed Exigo account area, and the green-themed Exigo back office — and logs in more than once along the way. Underneath, the *same information* — profile, subscriptions, and the payment card — lives in **two systems at once**, with no single one in charge. The red item, the card stored in two places, is the sharpest edge. We'll dig into that in a moment.

---

## SLIDE 5 — The five things that matter

**On slide (table):**

| # | What's happening | Why it matters to the business |
|---|---|---|
| 1 | **Payment & subscription data is split** between Exigo and Fluid; no single "card on file." | **Direct risk to revenue & trust** — fragile subscriptions, billing inconsistencies, extra compliance cost. **#1 to fix.** |
| 2 | **You depend on your vendor to change anything** (old, tightly-wound website software). | **You don't control your own speed or cost.** Your roadmap runs on someone else's calendar. |
| 3 | **Three different website experiences** and **repeated logins**. | **Brand & trust erosion**, lower conversion, more support tickets. |
| 4 | **Missing basics:** no proper access control, no single sign-on, analytics that don't yet drive decisions. | **Security & oversight gaps**; decisions made without a clear view. |
| 5 | **No in-house technology team.** | **The root cause of #2.** Nothing improves durably until this is addressed. |

**Say:** Five issues — but they're not five separate problems. Number 5, having no in-house team, is the upstream cause of most of the others: with no one to own the software, change is outsourced by default. We'll take each in turn, starting with the one that touches revenue most directly.

---

## SLIDE 6 — The #1 risk: one card, stored in two places

**On slide:**
- When a customer saves a card, it gets "tokenized" (turned into a secure reference)
- Today that happens in **both** Exigo and Fluid — with **no single owner**

**Image:** `images/payments-split.png`

**Say:** When someone saves a credit card, it's turned into a secure token. Today that happens in *both* systems, and the two tokens aren't interchangeable — so "the card is on file in both" does **not** mean the billing is consistent. That's the root of fragile subscriptions, billing surprises that become support escalations, and a larger compliance footprint than you need. This is the highest-value thing to fix, and it's contained — a great first project.

---

## SLIDE 7 — The fix: one secure home for cards

**On slide:**
- Make **Fluid** the single home for payment cards
- Keep card details **off Limbic Arc's own websites entirely** *(target — to confirm)*
- Result: reliable subscriptions **+** a smaller compliance burden

**Image:** `images/payments-target.png`

**Say:** The fix is well understood. Cards live in one place — Fluid's secure vault. Your own websites never touch raw card details; the secure form is hosted by Fluid and simply shown on the page. Exigo still gets the billing events it needs for commissions — but not the card data. That removes the fragility *and* shrinks your compliance obligations at the same time. **[to confirm]** the exact current card-handling setup, but the direction is clear and high-value.

---

## SLIDE 8 — You don't control your own speed

**On slide:**
- Your customer and distributor websites are built on **old software only the vendor fully understands**
- Even **small changes** are slow and expensive — and wait in the vendor's queue
- You don't set your own **timeline or cost**

**Say:** Your websites are built on an aging starter-kit that came with Exigo — it was meant to bootstrap onto Exigo's own flows, not to be a long-term product platform. Presentation, business rules, and data access are all tangled together, with thin documentation, so any change needs vendor know-how. The practical effect: simple changes are slow and expensive, and your roadmap runs on the vendor's priorities, not yours. This is why you feel stuck "firefighting."

---

## SLIDE 9 — Three websites, three logins

**On slide:**
- Same brand — but customers cross **three separate experiences** and **sign in again** at each boundary

**Image:** `images/three-experiences.png`

**Say:** These are your actual screens. Three different looks — modern store, white account area, green back office — and a login at each boundary. For a customer, that fragmentation reads as "is this even the same company?" It erodes trust, lowers conversion, and adds support load. It's not a cosmetic issue — it's the visible surface of the split underneath.

---

## SLIDE 10 — The missing basics

**On slide:**
- **No proper access control** — who can see and do what isn't clearly defined
- **No single sign-on** — more passwords, inconsistent security
- **Analytics that collect data but don't yet drive decisions** (you have dashboards, not direction)

**Say:** A few foundations that most platforms take for granted are missing. There's no role-based access control, so the system can't cleanly separate what a customer, a distributor, an admin, or support is allowed to do — that's a security and oversight gap. There's no single sign-on, which is both a customer annoyance and a security liability. And your analytics capture plenty of data but don't yet answer "how healthy is the business right now." None of these caused the architecture gap, but they make every fix slower and riskier.

---

## SLIDE 11 — The root cause: no in-house technology team

**On slide:**
- You work through capable **vendors**, but have **no technical counterpart of your own**
- So there's **no one to own the code** or direct the vendors — and change waits in their queue
- **This is the upstream cause.** Architecture alone won't fix it.

**Say:** This is the one that sits underneath the others. You have good vendors, but no technical representation on *your* side — no one whose job is to own the code and steer the vendors. That's exactly why you're locked into the vendor queue and stuck reacting. Better architecture helps, but it can't substitute for having someone on your side to drive it. Which is why the staffing decision — coming up — gates everything.

---

## SLIDE 12 — What "good" looks like

**On slide:**
- Keep Exigo and Fluid for what they're best at — and **own the layer in between**

**Image:** `images/target-architecture.png`

**Say:** Here's the target. One modern experience with a single login on top. Underneath, a small set of building blocks — payments, subscriptions, profile, family & friends, sign-up — that *you* own and can change on your timeline. And beneath those, Exigo and Fluid kept for what they do best: Exigo runs the network and commissions, Fluid runs the store and payments. The key idea: this is **not** "replace Exigo" or "replace Fluid." It's owning the few pieces in the middle so changes stop waiting in a queue.

---

## SLIDE 13 — Who owns what

**On slide:**
- **One source of truth** for each thing — everyone else just gets a copy

**Image:** `images/source-of-truth.png`

**Say:** "Good" depends on one simple rule: exactly one system is in charge of each thing. Exigo owns the network, ranks, commissions, and the master profile record. Fluid owns payments, subscriptions, and the store. Family & Friends becomes a clean new service so perks like a birthday discount become easy. And the rule that makes it stick: no website is ever allowed to write to a system that doesn't own that data. That single discipline prevents the entire class of "split data" problems you have today.

---

## SLIDE 14 — The recommended path

**On slide:**
- **No risky "big rewrite."** Modernize one area at a time
- **Exit ramp at every phase** — each step stands on its own

**Image:** `images/roadmap.png`

**Say:** We do not recommend a big-bang rewrite. We recommend a proven, incremental path. Step 1 — get a team in place and stop the cheap-to-stop bleeding — gates everything after it. Step 2 builds the foundations. Step 3 is the #1 payments fix. Then clean customer data, then a unified modern experience, then insights and AI to go on offense. The order is deliberate: reduce the riskiest, most expensive bleeding first, then build, then modernize, then innovate. Every phase leaves you better off, and there's an exit ramp at each one.

---

## SLIDE 15 — The one decision that unlocks everything

**On slide:**
- There's **no in-house team today** — so someone has to do the work
- Three ways to staff it: **Build · Partner · Hybrid**

**Image:** `images/staffing.png`

**Say:** Everything in the roadmap assumes a team exists to execute it — so the gating decision is how you staff it. Build your own team: most control, but three to six months before real progress. Bring in an experienced partner: fastest start, expertise on day one. Or hybrid: start with a partner and grow your own team over time — fast start *and* you end up owning the capability. I'm not pushing one here — the important point is that this choice gates the whole roadmap, so *deciding soon* matters more than which option you pick.

---

## SLIDE 16 — What we'd need from leadership

**On slide:**
1. **Direction on staffing** — build, partner, or hybrid
2. **Go-ahead for a small first step** — fixed-scope, low-risk: an integration map, early billing/compliance protections, and a sized plan for the rest
3. **A few confirmations** so we can finalize specifics **[to confirm]**

**Say:** Three things. First, a direction on staffing — that's the gate. Second, a green light for a small, fixed-scope first step that delivers a clear map of your systems, some early protections on billing and compliance, and a properly sized plan for everything after — low risk, fast value. Third, a handful of confirmations: your current card-handling and compliance setup, how subscriptions split between Exigo and Fluid, what Fluid supports through its connections, and the exact boundary of the Web App.

---

## SLIDE 17 — Closing

**On slide:**
- The right two platforms. A real business. What's missing is **ownership of the layer in between** — and the **capability to change it.**
- The path is **low-risk and incremental**, the first step is **small**, and the payoff is **lower risk, faster delivery, a better experience, and the freedom to innovate.**
- **The sooner the staffing decision is made, the sooner the firefighting stops.**

**Say:** To close: you've got the right platforms and a real business. What's missing is ownership of the layer in between and the capability to change it. The path forward is low-risk and incremental, the first step is small, and the payoff is substantial. The single most valuable thing you can do is make the staffing decision — because that's what turns this from a plan into progress. Happy to take questions.

---

## Appendix — image inventory

| Slide | Image file | What it shows |
|---|---|---|
| 4 | `images/current-state.png` | Three websites on two systems; data duplicated; card in two places |
| 6 | `images/payments-split.png` | The #1 risk — one card tokenized in both Exigo and Fluid |
| 7 | `images/payments-target.png` | The fix — Fluid as the single card vault; sites out of PCI scope |
| 9 | `images/three-experiences.png` | The three live websites (real screenshots) and three logins |
| 12 | `images/target-architecture.png` | Owned building-block layer between one experience and the two engines |
| 13 | `images/source-of-truth.png` | Who owns what — one source of truth per domain |
| 14 | `images/roadmap.png` | The six-phase gradual modernization path |
| 15 | `images/staffing.png` | Build vs. Partner vs. Hybrid (neutral) |

*All images are 16:9 (2560×1440 px) and drop directly onto a standard widescreen slide.*
