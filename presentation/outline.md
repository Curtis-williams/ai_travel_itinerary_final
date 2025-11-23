# AI Travel Itinerary Generator (LLM + Personalization)

## Objectives
- Build a generative system that converts destination + interests into a day-by-day itinerary
- Personalize recommendations (diet, budget, party size, hotel area)
- Provide transparent budget estimates and API access

## System Description (Data + Models)
- Inputs: destination, dates, interests, party size, diet, budget
- Model: OpenAI chat model via LangChain (prompt-engineered JSON output)
- Personalization: slot-filling & style guides conditioned on user profile
- Optional retrieval of local POIs (e.g., places APIs) — abstracted for demo

## Methodology / Pipeline
- Form -> Payload -> Prompt template (system + user) -> LLM JSON
- Parse JSON -> Render itinerary (morning/afternoon/evening)
- Budget module estimates costs (lodging/food/activities/transit)
- Expose both UI and REST endpoint

## Prompt Engineering
- System prompt enforces structure + tone + constraints
- User prompt slots: destination, days, interests, budget, diet, party size, hotel area
- Guidance for free vs. premium options; transit-first when tight

## Demo (Screenshots)
- Show form, results cards, budget widget
- Show API call to /api/itinerary returning JSON

## Results (Simulated Benchmarks)
- Latency vs. tokens chart (gpt-4o-mini vs. gpt-4.1, 128–4k tokens)
- Cost comparison per itinerary (temperature 0.3–0.9)
- A/B prompts: structured JSON prompt reduces post-parse errors

## Findings
- Structured prompts + JSON export reduce glue-code and retries
- Small “style knobs” (budget, diet) yield visible, controllable changes

## Limitations
- No live booking or real-time hours; dependent on model knowledge
- Hallucinations if not grounded with retrieval/API lookups

## Next Steps
- Add retrieval (POI search, hours, price levels)
- Caching + re-ranking + deduping similar activities
- Cost-aware decoding (token ceiling + prompt compression)

## Conclusion
- A compact LLM app can deliver high perceived value with thoughtful prompts and light personalization.
