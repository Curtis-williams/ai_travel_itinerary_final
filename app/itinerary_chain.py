import os
from typing import Dict, Any
from dataclasses import dataclass, asdict

# Using OpenAI via langchain_openai if desired; plain SDK also works.
try:
    from langchain_openai import ChatOpenAI
except Exception:
    ChatOpenAI = None

SYSTEM_PROMPT = """You are a meticulous travel-planning assistant.
Return concise, well-structured itineraries with local authenticity,
grouped by Day 1/2/3 with morning/afternoon/evening, addresses or neighborhoods,
approx costs, and travel times (short text). Respect dietary restrictions.
When budget is 'tight', prefer free/low-cost options and public transit.
When budget is 'luxury', include premium dining and unique experiences.
"""

USER_PROMPT = """Create a {days}-day itinerary for {name} in {destination} on {dates}.
Interests: {interests}.
Budget: {budget}. Party size: {party_size}.
Dietary: {diet}.
Hotel location (if known): {hotel_area}. Return JSON with keys:
- 'summary' (str)
- 'days' (list of day objects; each has 'date' (if available), 'morning', 'afternoon', 'evening', each an array of items: name, why, rough_cost, address/area)
- 'tips' (array of concise tips)
"""

@dataclass
class TravelerProfile:
    name: str = "Traveler"
    home_city: str = ""
    preferences: str = ""
    diet: str = ""
    party_size: int = 1

def build_messages(payload: Dict[str, Any]) -> list:
    days = payload.get("days", 3)
    msg = USER_PROMPT.format(
        days=days,
        name=payload.get("name", "Traveler"),
        destination=payload["destination"],
        dates=payload.get("dates", "upcoming dates"),
        interests=payload.get("interests", "general sightseeing"),
        budget=payload.get("budget", "moderate"),
        party_size=payload.get("party_size", 1),
        diet=payload.get("diet", "none"),
        hotel_area=payload.get("hotel_area", "not specified"),
    )
    return [{"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": msg}]

def run_itinerary_llm(payload: Dict[str, Any]) -> Dict[str, Any]:
    # In production, prefer ChatOpenAI with model param (e.g., gpt-4o-mini)
    model_name = payload.get("model_name", "gpt-4o-mini")
    temperature = float(payload.get("temperature", 0.6))

    if ChatOpenAI is None:
        # Fallback stub (for environments without langchain). Returns a toy response.
        return {
            "summary": f"Sample {payload.get('days', 3)}-day plan for {payload['destination']} based on interests: {payload.get('interests','')}",
            "days": [
                {"date": "Day 1", "morning": [{"name":"Walking tour","why":"Orientation","rough_cost":"$0-20","area":"Old Town"}],
                 "afternoon":[{"name":"Museum","why":"Culture","rough_cost":"$15","area":"Downtown"}],
                 "evening":[{"name":"Local bistro","why":"Cuisine","rough_cost":"$25-40","area":"Riverside"}]},
                {"date": "Day 2", "morning": [{"name":"Market visit","why":"Local foods","rough_cost":"$0-10","area":"Central Market"}],
                 "afternoon":[{"name":"Park & viewpoints","why":"Scenery","rough_cost":"Free","area":"City Park"}],
                 "evening":[{"name":"Street food crawl","why":"Authentic eats","rough_cost":"$15-25","area":"Night Market"}]},
                {"date": "Day 3", "morning": [{"name":"Bike ride","why":"Active explore","rough_cost":"$10-20","area":"Waterfront"}],
                 "afternoon":[{"name":"Art district","why":"Galleries","rough_cost":"Free-$10","area":"Arts Quarter"}],
                 "evening":[{"name":"Rooftop view","why":"Sunset","rough_cost":"$10-20","area":"High Street"}]}
            ],
            "tips": ["Buy transit card", "Reserve popular restaurants", "Check opening hours"]
        }

    llm = ChatOpenAI(model=model_name, temperature=temperature)
    messages = build_messages(payload)
    resp = llm.invoke(messages)
    # Expecting JSON in the reply; attempt to parse, else wrap as summary-only.
    try:
        import json
        data = json.loads(resp.content)
        return data
    except Exception:
        return {"summary": resp.content, "days": [], "tips": []}
