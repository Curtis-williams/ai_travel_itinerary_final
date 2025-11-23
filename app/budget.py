from typing import Dict, Any

DEFAULT_COSTS = {
    "lodging_per_night": {"tight": 80, "moderate": 160, "luxury": 320},
    "food_per_day": {"tight": 30, "moderate": 60, "luxury": 120},
    "activities_per_day": {"tight": 20, "moderate": 50, "luxury": 120},
    "transit_per_day": {"tight": 10, "moderate": 20, "luxury": 50},
}

def estimate_budget(days: int, party_size: int, budget_level: str) -> Dict[str, Any]:
    level = budget_level if budget_level in DEFAULT_COSTS["lodging_per_night"] else "moderate"
    lodging = DEFAULT_COSTS["lodging_per_night"][level] * max(days-1, 1)  # nights ~= days-1
    food = DEFAULT_COSTS["food_per_day"][level] * days * party_size
    activities = DEFAULT_COSTS["activities_per_day"][level] * days * party_size
    transit = DEFAULT_COSTS["transit_per_day"][level] * days * party_size
    total = lodging + food + activities + transit
    return {
        "breakdown": {
            "lodging": lodging,
            "food": food,
            "activities": activities,
            "transit": transit
        },
        "total": total,
        "per_person_per_day": total / (party_size * days)
    }
