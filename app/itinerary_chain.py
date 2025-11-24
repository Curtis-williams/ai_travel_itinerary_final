import os
import json
from openai import OpenAI
from typing import Dict, Any
from dataclasses import dataclass, asdict

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))





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
    model_name = payload.get("model", payload.get("model_name", "gpt-4o-mini"))
    temperature = float(payload.get("temperature", 0.6))

    messages = build_messages(payload)

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=temperature,
    )

    content = response.choices[0].message.content

    try:
        data = json.loads(content)
    except Exception:
        data = {"summary": content}

    return data

