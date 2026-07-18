# AI Meal Planning Microapp

A Flask-based AI-powered meal planning application with an interactive glassmorphism UI. The app generates personalized meal plans (breakfast, lunch, dinner), grocery lists, food substitutions, and budget feasibility analysis.

## Project Structure

- **app/**: Flask application package
  - `__init__.py`: Application factory
  - `routes.py`: API endpoints
  - `meal_planner.py`: Meal planning logic
  - `budget_analyzer.py`: Budget analysis logic
- **templates/**: HTML templates with glassmorphism effects
- **static/**: CSS and JavaScript assets
- **data/**: JSON files for meal and ingredient databases
- **run.py**: Application entry point
- **config.py**: Configuration settings
- **requirements.txt**: Python dependencies

## Setup Instructions

1. Install dependencies: `pip install -r requirements.txt`
2. Set environment variables: Create a `.env` file with `OPENAI_API_KEY`
3. Run the app: `python run.py`
4. Open browser: `http://localhost:5000`

## Features

- Interactive meal plan generator
- Grocery list creation with quantities
- Smart food substitutions based on preferences
- Budget feasibility analysis
- Glassmorphism UI with smooth animations
- Real-time calculations

## Technologies

- Flask (Backend)
- Python (Logic)
- HTML5, CSS3 (Frontend)
- JavaScript (Interactivity)
- OpenAI API (AI suggestions)
