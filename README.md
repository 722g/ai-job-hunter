# Primo — AI Job Hunter 🚀

> Upload your CV. Get matched jobs, cover letters, and interview answers — powered by Claude AI.

**Live demo:** [primo-zm8k.onrender.com](https://primo-zm8k.onrender.com)

---

## What it does

Primo reads your CV (PDF or DOCX), extracts your skills and experience, matches you with relevant jobs, and uses the Anthropic Claude API to generate:

- **Personalized cover letters** tailored to each job
- **Interview answers** for any application question
- **Job matches** based on your actual CV content

Supports 4 languages: English, German, Russian, Polish.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, Flask, Gunicorn |
| AI | Anthropic Claude API (claude-sonnet-4-6) |
| CV Parsing | pdfplumber, python-docx |
| Session | flask-session (filesystem) |
| Deployment | Render.com |

---

## Features

- CV upload (PDF/DOCX) with skill and experience extraction
- AI-generated cover letters tailored per job  
- AI-generated interview answers
- Rate limiting: 3 AI requests per user per day
- Multi-language support (EN, DE, RU, PL)

---

## Built by

**722** — [github.com/722g](https://github.com/722g) · [linkedin.com/in/gigi-simonishvili](https://linkedin.com/in/gigi-simonishvili)

---

*Powered by Claude AI*
