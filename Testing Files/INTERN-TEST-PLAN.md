# Report & Dashboard Reliability — Intern Test Plan

_28 Sep 2026_

Hunt for two things above all: **inconsistency** (identical input passing once and failing another time) and **corrupted or wrong output** in reports, dashboards and uploads — across weird file formats, odd wording, and scale. Test only on **qa** or **staging**, never production.

## How to test safely

- Test only on **qa** or **staging** (ask for the login link and a test account) — **never production**. Both environments run the same model and warehouse guardrails as production, so anything you find there is real.
- Sign in with the test/staff account you're given. Don't use your own Petpooja account or a real customer's account.
- Never type a real customer's name, phone number or email into a test upload or a chat question — use the sample data you're given, or made-up names.
- If a report ever shows what looks like another restaurant's data, or you can reach a screen/organization you weren't given access to, **stop immediately** and report it as Critical — don't keep poking at it to confirm.
- Every report and chat has a trace id on its detail page (`Admin → Reports`, or the chat itself) — always grab it before you move on. It's the only way anyone can find your exact run afterwards.

## How to report a bug

One entry per finding, even a small one — five interns each skipping "small" bugs is how a real pattern gets missed. Put every entry in the shared tracker.

| Field | What to put |
| --- | --- |
| Trace ID | From the report/chat detail page |
| Track & test ID | e.g. "Track A — A7" |
| What you did | The exact question you typed, or the file you uploaded (attach it) |
| Expected | What should have happened |
| Actual | What happened, verbatim error text included |
| Reproducible? | Tried again — same result every time, different result each time, or only happened once |
| Severity | Critical / High / Medium / Low — see the guide near the end |
| Evidence | Screenshot, and the expanded "▶ SQL" text on any failed try if there is one |

**Inconsistent results are the most valuable finding you can hand back.** If the exact same file or question passes once and fails another time, that's not a "flaky" annoyance to shrug off — file it, mark Reproducible as "different result each time," and attach every trace id, not just the failing one.

## Track A — Upload & format stress (Excel/CSV)

Build each file yourself (a few real-looking rows is enough) and upload it as a report format. Ask a normal question against it, and separately try naming it directly ("build the report from this upload"). Note whether the app's read of the file matches what you actually put in it.

| ID | Build this file | What to check for |
| --- | --- | --- |
| A1 | 200+ columns, only 10 rows | Are all columns picked up, or does it silently cut off partway? |
| A2 | 1–2 columns, 50,000+ rows | Does the row cap kick in cleanly, or does it hang/time out/half-read? |
| A3 | Merged cells across the header row | Does the header get read correctly, or do merged cells break column alignment? |
| A4 | Two header rows — a title row above the real column headers | Does it use row 2 as headers, or mistake row 1 for data/headers? |
| A5 | A totals/summary row mixed into the middle of the data, not just at the end | Does it get treated as a real data row and thrown into the numbers? |
| A6 | 3–4 blank rows before the header starts | Is the real header still found? |
| A7 | Several sheets, only one of them relevant, one sheet hidden | Does it pick the right sheet? Does the hidden sheet get read at all? |
| A8 | One column with text and numbers mixed row to row | Read as text, as numbers, or does it break? |
| A9 | One date column with 3 different formats mixed in (`12/01/2025`, `2025-01-12`, `12-Jan-25`) | Are all rows read as the same date column, or do some silently become text? |
| A10 | Currency values with symbols and separators (`₹1,23,456.00`) | Read as a number, or as text because of the symbol/commas? |
| A11 | A percentage column written as `12%` in some rows and `0.12` in others | Consistent interpretation, or mixed? |
| A12 | Scattered blank cells in an otherwise-required column | Handled gracefully, or does one gap break the whole column? |
| A13 | Two columns with the exact same header name | Which one wins, or does it error out clearly? |
| A14 | Column headers in Hindi, emoji, or with stray symbols (`Sales ($)#`) | Read correctly, or mis-parsed/dropped? |
| A15 | A column named exactly like a real metric ("Total Sales") but holding something unrelated | Does the model confuse it with the real metric? |
| A16 | A cell holding a live formula (`=SUM(A1:A5)`) instead of a value | Read as the computed value, the formula text, or does it break? |
| A17 | A cell holding a spreadsheet error (`#REF!`, `#N/A`, `#DIV/0!`) | Handled as blank/skip, or does it corrupt the read? |
| A18 | One cell with a very long value — a full paragraph of text | Truncated cleanly, or does it break formatting/the model's reading of the rest of the file? |
| A19 | A CSV saved with a UTF-8 BOM, and a separate one saved in a non-UTF-8 encoding | Both readable, or does one produce garbled characters? |
| A20 | A CSV with inconsistent quoting/delimiters (a comma inside an unquoted text field) | Rows still align, or does everything shift by a column? |
| A21 | A file right at the upload size limit | Clean success or a clean, clear failure — never a silent partial read |
| A22 | A corrupted or password-protected `.xlsx` | A clear error message, never a hang or a generic 500 |
| A23 | The exact same file from an earlier test, re-uploaded and re-run 5 times | This is Track C's method applied here — see below. Any difference between runs is a bug on its own |

## Track B — Wording & phrasing stress (chat questions)

Ask these as real chat questions (new chat each time unless the test says otherwise). Check the answer is right, not just that it answered — compare numbers against what you'd expect from the data.

| ID | Ask this | Why it's a good stress test |
| --- | --- | --- |
| B1 | "How's business" | Extremely vague — does it ask a sensible clarifying question, or guess wrong silently? |
| B2 | One question asking for 8 different metrics across 3 periods and 2 comparisons at once | Overloaded — does it handle all of it correctly, or quietly drop half the request? |
| B3 | Ask for sales by outlet, then immediately reply "no I meant purchase, not sales" | Mid-chat correction — does it actually switch, or blend the two? |
| B4 | "Give me revenue" (when more than one revenue-like metric exists) | Ambiguous term — does it ask which one, or pick one silently? |
| B5 | "gimme sales fr yesterday n compare to last wk pls" | Typos and shorthand — does it still parse correctly? |
| B6 | A question mixing Hindi and English (Hinglish) | Does it understand it, or misread the mixed terms? |
| B7 | A question naming a column or metric that doesn't exist in the data | Does it say so clearly, or hallucinate an answer anyway? |
| B8 | A nonsensical date range — end date before start date, or "last 400 days" | A clear error, not a wrong silent answer |
| B9 | An outlet name that's misspelled or doesn't exist | Does it say it can't find that outlet, or silently return data for a different one? |
| B10 | One long, run-on question — a full paragraph with several asks buried in it | Does it get all of it, or only the first sentence? |
| B11 | The exact same question asked 5 times in a row in the same chat | Same answer every time? (This is Track C's method — see below) |
| B12 | A follow-up question asked while the previous report is still generating | Does the first one finish correctly, or does it get corrupted/cancelled by the second? |
| B13 | Ask for a change to a report from the main chat ("make the bars a table instead"), then make the same change through the report's own editor | Both paths should produce the same result — this is a brand new feature, worth extra attention |
| B14 | Ask for something the system can't do ("predict next month's sales") | Does it fail gracefully and say so, rather than making something up? |
| B15 | The same question in ALL CAPS, and again in all lowercase with no punctuation | No difference in the answer |

## Track C — Consistency & repeat testing

This is the single most valuable track. We already know identical input can pass once and fail another time — this track is about finding how often, and on what.

1. Pick 5 files from Track A and 5 questions from Track B (mix easy and weird ones).
2. Run each one exactly **5 times**, spread across the test day — not back to back. A few minutes apart is enough; also try once first thing in the morning and once at the end of the day.
3. Log pass/fail for every single run in the tracker, with its trace id — not just a final "3/5 passed."
4. Anything that flips between pass and fail on identical input is filed immediately as **Inconsistent**, with every trace id attached (the passing ones too — they matter for comparison).
5. Once a day, reopen 2–3 reports you (or a teammate) made the day before, and confirm they still open and still refresh correctly. A report that worked yesterday and is now broken today, with nothing about the input changed, is its own kind of bug — file it as Inconsistent too, and note in the report that nothing about the input changed since it last worked.

## Track D — Scale & stress

| ID | Do this | What to check for |
| --- | --- | --- |
| D1 | Upload a file right at the maximum size/row limit | A clean success or a clean, immediate failure — never a silent partial read or a long hang |
| D2 | Ask for a report over the longest date range the UI allows (several years) | Correct numbers, reasonable time, no truncation without saying so |
| D3 | Ask for "all outlets" on the largest test organization available | Doesn't time out or silently drop outlets |
| D4 | Build (or find) a dashboard with the most tiles you can, then refresh all of them at once | All tiles finish correctly; none get stuck "running" forever |
| D5 | Open 5+ chats or reports in different browser tabs and generate in all of them at the same time | Each finishes with its own correct result — none get mixed up with another tab's |
| D6 | Send 10 follow-up questions in one chat back to back, without waiting for each to finish | Every one eventually gets a correct, separate answer — none get lost or answered out of order |
| D7 | Ask one question that needs several data areas at once (sales + purchase + inventory + staff, all in one report) | Correct across all areas, not just the first one it reaches |

## Track E — Cancel, refresh, sharing and demo mode

| ID | Do this | What to check for |
| --- | --- | --- |
| E1 | Stop/cancel a report mid-generation, at different stages (while it says "writing the query" vs "running the query") | It actually stops — doesn't keep running in the background or keep billing after you've left the page |
| E2 | Refresh an existing report, then cancel the refresh partway through | The report's last good data stays intact; the cancelled refresh doesn't half-overwrite it |
| E3 | Deliberately fail a report (e.g. a bad upload), then hit retry | Retry reuses your original question/upload — doesn't start over from nothing |
| E4 | Share a report or dashboard as view-only to a second test account | The viewer truly can't edit, and can't see more than what was shared |
| E5 | Use "view as a user" (demo) mode as a staff account | You land in a real, working view of that user's data, and exiting demo cleanly returns you to staff |
| E6 | Sign in with Google, then trigger a billing sign-in in the same browser (or the reverse order) | Only one session should be active — the earlier one should be signed out, not silently left valid alongside the new one |

## Severity guide

| Severity | Example from this system |
| --- | --- |
| Critical | Data from one restaurant appears in another's report or dashboard; you can reach another organization's data or sign in as someone else |
| High | A report fails **every time** with the exact same input (not just sometimes); numbers are visibly wrong compared to the source file/data; a cancelled or stopped run keeps running (and billing) in the background |
| Medium | A report fails **sometimes** and succeeds other times with identical input (this is what Track C is built to catch); an upload is misread in a way nobody would expect, but the error is visible — not silent |
| Low | Slow but eventually correct; a confusing but non-blocking message; a cosmetic formatting issue |

When in doubt, file it and mark the severity as your best guess — don't sit on a finding because you're not sure how bad it is.

## Daily process & assignment

| Intern | Primary track | Also helps with |
| --- | --- | --- |
| 1 | Track A — uploads & formats | Track C repeats on their own Track A cases |
| 2 | Track B — wording & phrasing | Track C repeats on their own Track B cases |
| 3 | Track D — scale & stress | Track E |
| 4 | Track E — cancel/refresh/sharing/demo | Track D |

Track C (consistency) isn't a separate person's job — everyone runs their own cases through it. It's the whole point of this plan.

**Daily rhythm:**
- Start of day: a 5-minute standup — what you're testing today, anything still open from yesterday.
- Log every result the same day, not from memory the next morning.
- End of day: reopen 2–3 of yesterday's reports (Track C, step 5) before starting anything new.

**Done when:** every test ID across Tracks A, B, D and E has been run at least once, the Track C repeat-5 protocol has been applied to at least 10 cases per person, and every finding is logged with a trace id and severity. Aim for two weeks; check in earlier if Critical or High findings pile up.

---

See also: [SALES-INVENTORY-REFERENCE.md](SALES-INVENTORY-REFERENCE.md) (what to ask about, and a growth/comparison question catalogue) and [ALL-COLUMNS-SALES-INVENTORY.md](ALL-COLUMNS-SALES-INVENTORY.md) (the complete column list, table by table).
