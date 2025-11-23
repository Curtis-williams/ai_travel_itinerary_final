# Demo Recording Script (≈10 minutes)

**Presenter:** Curtis Williams
**Project:** AI Travel Itinerary Generator (LLM + Personalization)
**Date:** 2025-11-11

## 0:00–0:30 — Title
- Slide: Title
- Line: "Hi, I'm Curtis Williams. This is the AI Travel Itinerary Generator: LLM + personalization."

## 0:30–1:30 — Objectives
- Slide: Objectives
- Line: "Goal: generate day-by-day travel plans from destination + interests, with budget awareness and diet."

## 1:30–3:00 — System & Pipeline
- Slide: System Overview → Architecture & Methodology
- Show pipeline diagram (pipeline_diagram.png)
- Line: "Flask UI → Prompt Builder → OpenAI via LangChain → JSON → Budget module."

## 3:00–6:00 — Live App Demo
- Switch to app (localhost:5000)
- Input: Destination 'Tokyo'; Interests 'coffee, design, hiking'; Days 3; Budget 'moderate'; Diet 'vegetarian'; Party=2; Temperature 0.6.
- Click **Generate Plan**.
- Narrate returned itinerary structure (morning/afternoon/evening) and the budget breakdown.
- Call the API: `POST /api/itinerary` with the same payload (show JSON result).

## 6:00–7:30 — Prompt Engineering
- Slide: Prompt Engineering
- Line: "System prompt enforces structure + authenticity; user prompt slots variables. JSON output reduces glue code."

## 7:30–8:30 — Results
- Slides: Latency vs Tokens; Cost Comparison
- Lines: "We simulated token ranges and temperatures; tradeoff between speed and richness; prompt structure reduces parse errors."

## 8:30–9:20 — Findings & Limitations
- Slide: Key Findings; Limitations
- Lines: "Personalization knobs visibly change outputs; limitations: no real-time data; approximate budget; potential hallucinations."

## 9:20–10:00 — Next Steps & Conclusion
- Slide: Next Steps; Conclusion
- Line: "Add POI retrieval, maps, live pricing; this compact LLM app delivers useful personalized plans."
