# CLAUDE.md — Auto Job Applier (LinkedIn)
> **Self-updating knowledge base.** Every agent that works in this project MUST read this file fully at the start. When you learn something new — a preference, a correction, a workflow, a fact about Harsha's setup — write it into the relevant section below before ending the session. Future agents depend on this file. Do not rely on memory alone.

---

## 🤖 Agent Instructions (READ FIRST)

**At session start:**
1. Read this entire file.
2. Check the `Learned Facts` and `Corrections & Preferences` sections for anything relevant to the current task.

**During / at session end — write back if you learned:**
- A new preference or workflow Harsha mentioned
- A correction to something in this file
- A config change that was made
- A problem encountered and how it was solved
- Anything that would help the next agent avoid repeating a mistake

**How to write back:**
- Add to the appropriate section below.
- Use the format: `- [YYYY-MM-DD] Your note here.`
- Update existing entries instead of duplicating if it's the same topic.
- Keep entries concise — one line if possible.

---

## Project Overview

LinkedIn Easy Apply automation bot for Harsha Vardhan Yellela.
- Repo: https://github.com/GodsScion/Auto_job_applier_linkedIn
- Configured for: harsha.yellela@gmail.com
- Platform: Linux (Arch), running locally

---

## How to Run

```bash
# Main bot (applies to jobs):
cd /home/har5ha/Desktop/Auto_job_applier_linkedIn
python runAiBot.py

# Flask dashboard (optional UI):
python app.py
# Then open http://localhost:5000
```

---

## Config Files (all in `config/`)

| File | Purpose |
|------|---------|
| `personals.py` | Name, phone, address, EEO demographics |
| `secrets.py` | LinkedIn credentials, AI provider/key |
| `questions.py` | Resume path, experience, visa, salary, cover letter |
| `search.py` | Job search terms, filters, blacklists |
| `settings.py` | Browser behavior, safe mode, stealth |

---

## Current Configuration Snapshot

> **Agents: update this section when config changes are made.**

- **AI Provider:** DeepSeek (deepseek-reasoner / R1 model)
- **Search Terms:** AI Engineer, ML Engineer, AI Automation Engineer, Backend Engineer, Software Engineer, LLM Engineer, AI Agent Developer
- **Location:** United States
- **Experience Filter:** Entry level, Associate, Mid-Senior level
- **Work Type:** Remote + Hybrid
- **Salary Target:** $110,000 USD
- **Visa:** Yes (F-1 OPT → H-1B sponsorship needed)
- **Safe Mode:** True | **Stealth Mode:** True | **Background:** False (visible)
- **Pause Before Submit:** True (review each application before submitting)
- **Resume Path:** `D:\Desktop\resume\resumes\Harsha_Yellela_AI-Automation-Engineer.pdf`

### Credentials Status
- `config/secrets.py` → `password` and `llm_api_key` must be filled before running
- DeepSeek API key: https://platform.deepseek.com/

### Blacklists
- **Keywords:** US Citizen, Security Clearance, .NET, PHP, Ruby
- **Companies:** Crossover, Staffing, Outsourcing firms

---

## Output Files

- Applied jobs: `all excels/all_applied_applications_history.csv`
- Failed jobs: `all excels/all_failed_applications_history.csv`
- Logs: `logs/`

---

## Learned Facts

> Things agents have discovered about how this project actually works in practice.
> Format: `- [YYYY-MM-DD] Fact.`

- [2026-03-16] Project runs on Linux (Arch), not Windows — `cd` path in run instructions updated accordingly.
- [2026-03-16] User wants CLAUDE.md to be self-updating: agents must write learnings back here at end of session.
- [2026-03-16] Resumes are at `/home/har5ha/Desktop/resume/resumes/`. Role-to-resume mapping is in `config/questions.py` → `resume_by_role` dict. Bot auto-selects the right resume per search term and re-uploads at each term switch.

---

## Corrections & Preferences

> Harsha's explicit corrections, preferences, and things agents got wrong before.
> Format: `- [YYYY-MM-DD] What was wrong / what Harsha prefers instead.`

*(none yet — agents: add here when Harsha corrects you or states a preference)*

---

## Solved Problems

> Bugs, blockers, or issues encountered and how they were resolved.
> Format: `- [YYYY-MM-DD] Problem → Solution.`

- [2026-03-19] ChromeDriver version mismatch → `modules/open_chrome.py` line 39 has `version_main` hardcoded. Must match installed Chrome version. Currently set to 146. Check `chrome://settings/help` for current Chrome version and update this value if it breaks again (error: `This version of ChromeDriver only supports Chrome version X`).
- [2026-03-16] DeepSeek 402 (Insufficient Balance) causes ALL subsequent jobs to fail: API error is silently swallowed as `{"error": ...}` dict, questions go unanswered, Submit never appears. Fixed by detecting balance/auth errors in skill extraction and setting `aiClient = None` immediately so the bot falls back to non-AI answering instead of cascading 155 failures. Top up balance at https://platform.deepseek.com/ to restore AI.
- [2026-03-16] Bot crashes when stuck in form loop: `discard_job()` pressed ESC but `wait_span_click('Discard')` silently failed → modal overlay stayed open → next job click intercepted by overlay → session died. Fixed by adding JS force-close fallback in `discard_job()` after the Discard click fails.
- [2026-03-18] 10 failed jobs due to `APITimeoutError`: DeepSeek reasoner model is slow, default 30s timeout not enough. Increased to 90s in `modules/ai/deepseekConnections.py` line ~78. If timeouts persist, top up balance or switch to `deepseek-chat` (faster/cheaper).
- [2026-03-18] Stats board showed blank numbers despite correct code: root cause was `tk.StringVar.textvariable` bindings not updating reliably across threads on Linux/Arch. Fixed by replacing ALL StringVar usage with direct `label.config(text=...)` calls in `refresh()`. Also changed font from `"Segoe UI"` (Windows-only) to `"DejaVu Sans"` (available on Arch). Stats board also changed to show last 5 applied jobs (title · company · age) instead of just 1.
- [2026-03-18] AI had poor context for answering form questions: `user_information_all` in `config/questions.py` was a short summary. Fixed by loading full `personal_details.md` + first 4000 chars of `projects.md` from `/home/har5ha/Desktop/resume/references/` at bot startup in `runAiBot.py`, overriding the imported `user_information_all`.

---

## Workflow Notes

> How Harsha likes to work with this bot. Habits, rituals, sequences.

- `pause_before_submit = True` — bot pauses before each submit for manual review
- `pause_at_failed_question = True` — bot pauses if it can't answer a question
- First run: keep `run_in_background = False` so Chrome is visible
- After confirming it works: optionally set `run_non_stop = True` for hands-off operation
