# AI Travel Itinerary Generator (LLM + Personalization)

Live Demo (Replit Deployment):  
👉 https://8876cc40-604c-49f4-a2f6-9ec1e60d9b32-00-w8z19ng1r46u.picard.replit.dev/

## 📌 Project Overview
This application generates personalized multi-day travel itineraries using:

- Flask (backend server)
- LangChain (prompt building + model handling)
- OpenAI API (gpt-4o-mini default)
- Custom Budget Estimator
- HTML/CSS UI

The system outputs a complete structured itinerary including:
- Daily plan (morning / afternoon / evening)
- Activity explanations
- Budget breakdown
- Travel tips
- JSON-format API output

## 🚀 Quickstart (Local Setup)

### 1. Clone or Download Repository

### 2. Install Dependencies

### 3. Set Your OpenAI API Key

Mac/Linux:

Windows CMD:

Open your browser at:  
👉 http://127.0.0.1:5000  

### 5. Use Live Cloud Version (No installation needed)
👉 https://8876cc40-604c-49f4-a2f6-9ec1e60d9b32-00-w8z19ng1r46u.picard.replit.dev/

## 🧠 Features & Functionality

### ✔ Personalized Itineraries  
Generated based on:
- Destination
- Dates
- Dietary needs
- Interests
- Budget style (tight / moderate / luxury)
- Hotel location
- Temperature (model creativity)
- Model selection (gpt-4o-mini, gpt-4.1, etc.)

### ✔ JSON Output  
A strict structured JSON format is returned internally.  
Fallback logic is included to handle malformed LLM responses.

### ✔ Budget Planner  
Automatically estimates:
- Lodging  
- Food  
- Activities  
- Transit  
- Per-day totals  

### ✔ Clean Web UI  
User fills out a form and receives a formatted multi-day itinerary.

## 📁 Project Structure

ai_travel_itinerary_final/
│
├── app/
│ ├── app.py # Flask web application
│ ├── itinerary_chain.py # LangChain wrapper + prompts
│ ├── budget.py # Budget estimator
│ ├── templates/index.html # Main UI
│ └── static/styles.css # Styling
│
├── evaluation/
│ ├── latency_vs_tokens.png # Simulated latency chart
│ └── cost_comparison.png # Simulated cost chart
│
├── presentation/
│ ├── storyboard.md
│ ├── checklist.md
│ └── recording_script.md
│
├── canvas_submission_checklist.md
├── requirements.txt
├── .replit
└── README.md

## 📊 Evaluation (Simulated)

Charts included for the presentation:

- **Latency vs Token Size** → `evaluation/latency_vs_tokens.png`
- **Cost Comparison** → `evaluation/cost_comparison.png`

These are simulated metrics provided for academic purposes.

## 📝 Notes

- Created as the **Final Project for CAP4630 – FAU (Fall 2025)**  
- Designed to be clean, extendable, and easy to run  
- Supports swapping models by editing `itinerary_chain.py`
- All files are included for Canvas submission:
  - Code
  - README
  - Presentation markdowns
  - Benchmark images

## 📣 Author  
**Curtis Williams**  
AI Travel Itinerary Generator — Final Project Submission  
2025
