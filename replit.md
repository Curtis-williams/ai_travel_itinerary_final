# AI Travel Itinerary Generator

## Overview
A Flask-based web application that generates personalized travel itineraries using OpenAI's language models and LangChain. The app creates detailed 3-5 day travel plans based on user preferences including destination, interests, budget, dietary needs, and party size.

## Tech Stack
- **Backend**: Python 3.11, Flask
- **AI/ML**: OpenAI API (via LangChain)
- **Libraries**: LangChain, langchain-openai, python-dotenv
- **Deployment**: Gunicorn (production)

## Project Structure
```
.
├── app/
│   ├── app.py              # Main Flask application
│   ├── itinerary_chain.py  # LangChain integration for itinerary generation
│   ├── budget.py           # Budget estimation logic
│   ├── templates/
│   │   └── index.html      # Frontend form and results display
│   └── static/
│       └── styles.css      # CSS styling
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore file
└── replit.md              # This file
```

## Recent Changes (2025-11-23)
1. **Replit Environment Setup**: 
   - Installed Python 3.11 and all required dependencies
   - Fixed import structure to work with Replit environment
   - Changed relative imports to absolute imports with sys.path modification
   
2. **Flask Configuration**:
   - Updated Flask app to bind to 0.0.0.0:5000 for proper Replit preview functionality
   - Configured workflow to run Flask development server
   
3. **Deployment Configuration**:
   - Set up autoscale deployment with Gunicorn
   - Production command: `gunicorn --bind=0.0.0.0:5000 --reuse-port app.app:app`

4. **Environment Setup**:
   - Created .gitignore for Python project
   - OpenAI integration identified (requires OPENAI_API_KEY)

## Configuration

### Required Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required for AI-powered itinerary generation)

### Setting Up the API Key
To use this application, you need to provide your OpenAI API key:
1. Click on the "Secrets" tab in Replit
2. Add a new secret with key `OPENAI_API_KEY` and your API key as the value

## Features
1. **Personalized Itineraries**: Generate custom travel plans based on:
   - Destination and travel dates
   - Personal interests (museums, hiking, food, etc.)
   - Budget level (tight, moderate, luxury)
   - Party size
   - Dietary restrictions
   - Preferred hotel area

2. **Budget Planning**: Automatic cost estimation including:
   - Lodging costs
   - Food expenses
   - Activities budget
   - Transit costs
   - Per-person per-day breakdown

3. **Day-by-Day Schedule**: Structured itineraries with:
   - Morning, afternoon, and evening activities
   - Location details and neighborhoods
   - Cost estimates for each activity
   - Travel tips and recommendations

4. **API Access**: JSON API endpoint at `/api/itinerary` for programmatic access

## API Endpoints
- `GET /` - Main web interface
- `POST /plan` - Generate itinerary from web form
- `POST /api/itinerary` - JSON API for programmatic access

## Model Options
- Default: gpt-4o-mini (cost-effective)
- Configurable via form: Support for other OpenAI models
- Temperature control: 0.0 (deterministic) to 2.0 (creative)

## Development
- Development server runs on port 5000
- Debug mode enabled for development
- Hot reload enabled with Flask development server

## Production Deployment
- Uses Gunicorn WSGI server
- Autoscale deployment type (scales based on traffic)
- Binds to 0.0.0.0:5000 for Replit deployment

## Notes
- The app includes fallback logic if LangChain is unavailable (returns sample itinerary)
- Budget estimates are based on configurable defaults in `budget.py`
- All prompts are defined in `itinerary_chain.py` and can be customized
