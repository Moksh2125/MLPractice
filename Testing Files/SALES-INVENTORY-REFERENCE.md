# Sales & Inventory Reference

What data exists, so you can ask real questions instead of guessing at column names — and a catalogue of growth/comparison/scope questions to run through Tracks B and C of [INTERN-TEST-PLAN.md](INTERN-TEST-PLAN.md).

## How outlets and periods scope every report

Every report needs two things settled before it runs, whether you say them or not: **which outlets** and **which period**. Testing how these get asked, defaulted and parsed is its own rich area.

**Outlets (scope):**
- By default a report runs on **one outlet** (the one open in billing, or the first by name) unless you ask for more.
- Say "all outlets", "every outlet", "outlet-wise", "compare outlets", "top outlets" (and similar) to get every outlet, or a breakdown across all of them.
- Name an outlet directly ("Adyar branch sales") and it's used without asking.
- On a large account, asking a vague question without saying which outlets triggers a clarifying question, with options all outlets, each head office, and individual outlets.
- Test: ask a vague question on a large multi-outlet test account and confirm you get asked; ask the same on a 1-outlet account and confirm you don't.

**Periods:**
- Nothing is defaulted silently — if you don't name a period, you're always asked, with quick options (Today, Yesterday, This week, Last week, This month so far, Last month, Last 7 days, Last 30 days) plus free text.
- Typed phrases it understands: "August", "1–15 Sep", "last quarter", "Q2 2025", "FY 2025-26", "month to date"/"MTD", "week to date"/"WTD", "year to date"/"YTD", "last 3 months", "last N days", a specific year ("in 2024").
- Weeks start **Monday**; the financial year starts **1 April**.
- Comparisons are two periods in one ask: "this week vs last week", "month on month", "compared to last year", "August vs last August". Both periods are matched by outlet and period, not by name.

Test ideas: every period phrase above, at least once; a comparison phrase combined with a specific outlet; a comparison across a financial-year boundary ("this FY vs last FY"); a nonsense phrase it should refuse rather than guess ("last umpteen days").

## Sales — what you can ask about

Two tables carry almost every sales question:

**Bill-level (one row per bill)** — totals, bill lists, day/hour/channel/payment breakdowns:

| Group | Columns you can reference in a question |
| --- | --- |
| Identity & outlet | invoice/bill number, restaurant (outlet) name, brand, virtual brand, city, state, area |
| Timing | bill date, hour of day, hour range (e.g. 11:00–12:00), day part (breakfast/lunch/snacks/dinner/late night) |
| Status | success / cancelled / complimentary (NC) / advanced, cancel reason, complimentary reason, cancelled by |
| Channel | online or offline, platform (Swiggy, Zomato, website…), order type (Dine In / Take Away / Home Delivery) |
| Money | before discount, discount, tax, after discount, final bill total, settled amount, waived off, round-off, packing charge, delivery charge, tip, service charge |
| Customer | name, phone, address, locality, GST number (B2B vs B2C) |
| People | billing staff, waiter/server/steward/captain |
| Other | guests/covers, table number, coupon code, print count (reprints), BOGO offer name |

**Item-level (one row per item line)** — item, category or group reports:

| Group | Columns you can reference in a question |
| --- | --- |
| Item | item name, category, group (Food/Beverage/Bar), variation (Half/Full), add-on, SAP code, item code, HSN code |
| Money | quantity, unit price, line amount, line discount, line tax, line total with tax |
| BOGO | BOGO offer id, bought vs free (get) item, BOGO price |
| Other | is taxable, special notes, item-level status |

Test ideas: ask for a column that sounds real but isn't (e.g. "sub-category" when only "category" exists); ask for something only available at item level while implying bill level (or the reverse) and see if it asks or gets it right; ask for a column masked for your test account (customer name/phone) and confirm it's masked, not blank or an error.

For the exhaustive column list on these and every other sales table, see [ALL-COLUMNS-SALES-INVENTORY.md](ALL-COLUMNS-SALES-INVENTORY.md).

## Sales — named metrics and the deliberately ambiguous terms

The system has an exact, named formula for common measures — asking for these by their everyday name should always give the right number:

| Ask for | What it computes |
| --- | --- |
| Net sales / after discount | Bill value minus discount, before tax |
| Billed / final bill amount | Discount, tax, packing, delivery, service charge all applied |
| Settled amount | What was actually received, after any waive-off |
| Discount | Discount given (not the discount %, reason or name) |
| Tax / GST | Tax charged (not the rate, or split by CGST/SGST) |
| Tax by name (CGST, SGST, IGST…) | One amount per tax type |
| Taxable / non-taxable sales | Item amount on lines with/without tax |
| Quantity sold | Units sold |
| Number of bills / orders | Distinct bill count |
| Unique customers | Distinct customers by phone number |
| BOGO discount, BOGO bought/free quantity | Buy-one-get-one offer breakdowns |
| Complimentary (NC) amount | Bill total of complimentary bills only |
| Modified bills | Bills changed after being printed |
| Customer spend | What a customer paid — for top/repeat-customer questions |

**On purpose ambiguous — these should make the system ask, not guess:**

| Word | Why it's ambiguous | What it should do |
| --- | --- | --- |
| "Total" / "Sales" / "Sale amount" | Could mean billed total, settled, after discount, before discount, or after-discount-plus-tax | Ask which one, the first time; remember your answer after that |
| "Net Sale" | Could mean after-discount, or settled-minus-tax | Ask, the first time |
| "My Amount" | Could mean before discount, billed total, settled, or before-discount-minus-waived-off | Has a default (before discount) — confirm it's used silently, without asking |
| "Order Type" | Could mean the channel (Swiggy/Zomato/…), Dine In/Take Away/Delivery only, online/offline, or the four-way split | Ask, the first time |
| "Covers" / "Persons" / "Pax" | Could count only bills with a guest count entered, treat every bill as at least 1, or use 1 for non-dine-in | Ask, the first time |

Test idea: ask "total sales yesterday" as your very first question in a fresh chat and confirm you get asked which "Total" is meant; answer it; ask "total sales today" right after and confirm it does **not** ask again.

## Inventory — what you can ask about

Inventory tracks raw materials moving in and out of stock. Every movement has a **type**:

| Type code | Meaning |
| --- | --- |
| PU | Purchase (goods received from a supplier) |
| IT | Internal transfer (in or out, between outlets/kitchens) |
| MS | Manual stock (a correction — excess on the inward side, shortage on the outward side) |
| SR | Sale return (raw material received back) |
| WA | Wastage |
| PR | Purchase return (sent back to a supplier) |
| SL | Dispatch (a central kitchen sending stock to a restaurant — not a POS sale) |

Columns and concepts you can ask about:

| Group | What's there |
| --- | --- |
| Raw material | Name, category, sub-category, unit of measure (Kg, GMS, Pcs…) |
| Stock levels | Opening stock, closing stock (system), current/live stock, physical stock (not stored — entered by the restaurant) |
| Purchasing | Purchase value, purchase quantity (consumption or purchase units), supplier/vendor name, supplier GST number, payments made to suppliers |
| Purchase orders | Requested quantity, PO count, PO status (pending approval, approved, sent, cancelled…) |
| Consumption | POS consumption (theoretical, from recipes), consumption cost at 15-day or 90-day average price |
| Wastage & returns | Wastage quantity/value, purchase returns |
| Batches | Batch number, manufacturing/expiry dates, stock expiring within 30 days, expired stock still held |
| Recipes | Which raw materials and quantities go into a menu item |

Test ideas: ask about a raw material name that doesn't exist in the test data; ask for "stock" alone (ambiguous — system closing stock, or current live stock?); ask for wastage without saying qty/value/amount (ambiguous too).

## Inventory — named metrics

| Ask for | What it computes |
| --- | --- |
| Opening stock | Stock at the start of the period (previous day's closing) |
| Purchase quantity / purchase value | Goods received as purchases, in quantity or value |
| Closing stock (system) | System-calculated closing stock at period end |
| Current / live stock | Stock balance right now (not a past date) |
| Wastage quantity / value / amount | Raw material wasted, in three framings (qty, value at cost, or with tax) |
| Purchase returns | Quantity returned to suppliers |
| Internal transfer in / out | Stock moved between outlets or kitchens |
| POS consumption | Theoretical raw material usage from recipes |
| Raw material cost | Consumption cost at 15-day or 90-day average purchase price |
| Requested qty (PO) | Quantity requested on purchase orders |
| Stock expiring within 30 days / expired stock held | Batch-level expiry tracking |
| Paid to suppliers | Amount actually paid against purchases |

**On purpose ambiguous:**

| Word | Why it's ambiguous |
| --- | --- |
| "Stock" alone | System closing stock, or current live stock? |
| "Wastage" alone | Quantity, cost value, or amount with tax? |
| "Internal transfer" alone | In, or out? |
| "Raw material cost" | 90-day average, 15-day average, or the stored POS consumption cost? |

Test idea: ask for "wastage this month" and confirm it asks (or uses a sensible, stated default) rather than picking one silently and never saying which.

## Growth, comparison and average questions to test

This is where Track B (wording) should spend the most time — comparisons touch date-splitting, matching logic and rounding all at once.

| ID | Ask this | What it's testing |
| --- | --- | --- |
| G1 | "Sales this month vs last month" (MoM) | Two adjacent calendar months, correctly matched |
| G2 | "Sales this August vs last August" (YoY) | Same month, a year apart |
| G3 | "This week vs last week" (WoW) | Monday-start weeks |
| G4 | "Yesterday vs the day before" (DoD) | Single-day comparison |
| G5 | "This quarter vs last quarter" | Calendar quarters (Jan–Mar, Apr–Jun…) |
| G6 | "This financial year vs last financial year" | FY boundaries (1 April–1 April), not calendar years |
| G7 | "Last 7 days vs the 7 days before that" | A rolling window compared to the window right before it |
| G8 | "Average daily sales this month" | Ambiguous by design — over days that had bills, or every calendar day? Should ask, not guess |
| G9 | "Month on month growth for the last 6 months" | Several consecutive comparisons in one answer, not just two periods |
| G10 | "% change in sales vs last month" | Correct % change formula, including when the earlier period is zero (should show 0%, never an error) |
| G11 | "Compare Adyar outlet vs Besant Nagar outlet, this month" | A comparison that splits by outlet, not by time |
| G12 | "Sales by day for this month" (a pivot) | Every day of the month present, even days with zero sales |
| G13 | "Growth in net sales after discount, month on month" | A comparison combined with an ambiguous term — does it ask once and apply the answer to both periods? |
| G14 | "This month to date vs last month to date" (MTD vs MTD) | Partial-month comparisons, matched on the same number of elapsed days |
| G15 | "Sales trend for the last 12 months" | A long run of periods, not just two |

## More test ideas beyond uploads

**Scope combinations:**
- A single named outlet, all outlets, and a head-office group — same question, three different scopes.
- A question that implies a comparison across outlets ("which outlet did best this month") rather than across time.
- The largest test organization available (most outlets) with "all outlets" — does it stay fast and correct, or degrade?
- As staff, view a customer's data (if your test account can) and confirm the same scope rules apply there too.

**Cross-domain:**
- One question that needs both sales and inventory together (e.g. "food cost as a % of sales this month").
- A question naming a sales term and an inventory term in the same sentence, and seeing which table it reasons from.

**Ranking & shares:**
- "Top 10 items by quantity sold" — confirm ties are broken consistently (by amount, then name).
- "Items with zero sales this month" — a report that should return absences, not just non-zero rows.
- "Each item's % share of total sales" — confirm shares are computed before any Top-N cut, not after.

**Editing & drill-down (today's newest feature):**
- Ask for a change to a report or dashboard from the **main chat**, and separately through the **report's own editor** — for the same request, confirm both give the same result.
- Ask to add a widget to an existing dashboard from chat.
- Ask a small follow-up question about a report that's just a plain question, not an edit ("why is Tuesday so low") — confirm it answers in words, not by silently changing the report.

**Deliberately impossible or out of scope:**
- A metric that isn't in either metrics book at all ("customer lifetime value", "employee turnover").
- A request for something outside sales/inventory entirely ("what's the weather").
- Both should fail clearly and say what's wrong — never guess an answer that looks plausible but is invented.
