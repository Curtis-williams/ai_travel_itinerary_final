# AI Travel Itinerary Generator (LLM + Personalization)

**Stack:** Flask · LangChain · OpenAI API  
**Concepts:** Generative AI, Prompt Engineering, Personalization, Budgeting

## Quickstart
1. **Clone/Unzip** this project.
2. **Install deps:** `pip install -r requirements.txt`
3. **Set API key:** `export OPENAI_API_KEY="sk-..."` (Windows: `set OPENAI_API_KEY=...`)
4. **Run:** `python app/app.py` then open http://127.0.0.1:5000
5. Optional production: `gunicorn -w 2 -b 0.0.0.0:8000 app.app:app`

## What it does
- Takes **destination**, **dates**, **interests**, **budget**, and **dietary needs**.
- Generates a **3- or 5-day itinerary** with morning/afternoon/evening blocks.
- Personalizes suggestions based on user profile (saved in a simple JSON store).
- Adds a **budget planner** that estimates cost per day (lodging, food, activities, transit) and totals.
- Exposes a simple **JSON API** at `/api/itinerary` for programmatic access.

## Files
- `app/app.py` — Flask routes and server
- `app/itinerary_chain.py` — LangChain prompt and call wrapper
- `app/budget.py` — Budget estimator
- `app/templates/index.html` — UI form + results
- `app/static/styles.css` — Styling
- `requirements.txt` — Dependencies
- `evaluation/` — Simulated charts for latency and cost
- `presentation/` — Slide outline (Markdown) you can paste into PowerPoint/Slides

## Evaluation (simulated)
See `evaluation/latency_vs_tokens.png` and `evaluation/cost_comparison.png` for quick, *simulated* benchmarks to include in the presentation.

## Notes
- This app is designed as a **capstone demo**: clean, minimal, and easy to extend.
- Swap in different models by editing `itinerary_chain.py` (e.g., gpt-4o-mini vs. gpt-4.1).

(c) 2025-11-11 — Prepared for CAP 4630 presentation.
