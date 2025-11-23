import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from .itinerary_chain import run_itinerary_llm
from .budget import estimate_budget

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/itinerary", methods=["POST"])
def api_itinerary():
    payload = request.get_json(force=True)
    data = run_itinerary_llm(payload)
    # Add budget estimate
    days = int(payload.get("days", 3))
    party_size = int(payload.get("party_size", 1))
    budget_level = payload.get("budget", "moderate")
    budget = estimate_budget(days, party_size, budget_level)
    return jsonify({"itinerary": data, "budget": budget})

@app.route("/plan", methods=["POST"])
def plan():
    form = request.form
    payload = {
        "name": form.get("name","Traveler"),
        "destination": form["destination"],
        "dates": form.get("dates",""),
        "interests": form.get("interests",""),
        "budget": form.get("budget","moderate"),
        "party_size": int(form.get("party_size","1")),
        "diet": form.get("diet",""),
        "hotel_area": form.get("hotel_area",""),
        "days": int(form.get("days","3")),
        "model_name": form.get("model_name","gpt-4o-mini"),
        "temperature": float(form.get("temperature","0.6"))
    }
    data = run_itinerary_llm(payload)
    budget = estimate_budget(payload["days"], payload["party_size"], payload["budget"])
    return render_template("index.html", result=data, budget=budget, form_payload=payload)

if __name__ == "__main__":
    app.run(debug=True)
