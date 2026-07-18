# AI Meal Planner - Smart Cooking Assistant

A Flask-based AI-powered meal planning application with an interactive glassmorphism UI. Generate personalized meal plans, grocery lists, food substitutions, and budget analysis in real-time.

## 🎯 Features

- **🍽️ Personalized Meal Plans**: Generates breakfast, lunch, and dinner combinations
- **🛒 Smart Grocery List**: Auto-generates shopping lists with quantities and prices
- **💵 Budget Analysis**: Real-time budget feasibility checks and cost per serving
- **🔄 Food Substitutions**: Suggests alternative ingredients based on dietary preferences
- **⚡ Budget Optimization**: Automatically adjusts meal plans to fit your budget
- **✨ Glassmorphism UI**: Modern, interactive interface with smooth animations
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile

## 🛠️ Technologies

- **Backend**: Flask, Python
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Glassmorphism design with backdrop filters
- **API**: RESTful endpoints for meal planning logic

## 📋 Project Structure

```
.
├── app/
│   ├── __init__.py           # Flask application factory
│   ├── routes.py             # API endpoints
│   ├── meal_planner.py       # Meal planning logic
│   ├── budget_analyzer.py    # Budget analysis logic
│   ├── templates/
│   │   └── index.html        # Main application template
│   └── static/
│       ├── css/
│       │   └── style.css     # Glassmorphism styling
│       └── js/
│           └── app.js        # Interactive frontend logic
├── .github/
│   └── copilot-instructions.md
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── run.py                    # Application entry point
└── README.md                 # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd path/to/meal-planner
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables (optional)**
   ```bash
   # Create a .env file in the root directory
   FLASK_ENV=development
   OPENAI_API_KEY=your_api_key_here  # Optional for future AI features
   ```

5. **Run the application**
   ```bash
   python run.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000`

## 📖 How to Use

1. **Enter Your Preferences**
   - Set your daily budget (minimum $20)
   - Enter number of servings (1-12)
   - Choose dietary preference (vegetarian, vegan, etc.)
   - Select cooking time preference

2. **Generate Meal Plan**
   - Click "Generate Meal Plan" button
   - View personalized breakfast, lunch, and dinner suggestions
   - See complete grocery list with prices

3. **Review Budget Analysis**
   - Check total cost vs. your budget
   - See cost per serving
   - View remaining budget

4. **Explore Alternatives**
   - Use "Generate Alternative" to get different meal combinations
   - Click "Optimize for Budget" to reduce costs
   - View food substitutions for each ingredient

## 🎨 Glassmorphism Design Features

- **Backdrop Blur**: Semi-transparent panels with blur effect
- **Glass Effect**: Layered translucent cards
- **Gradient Backgrounds**: Smooth color transitions
- **Smooth Animations**: Floating background, hover effects, transitions
- **Modern Color Palette**: Indigo, purple, and slate tones
- **Interactive Elements**: Glowing buttons and borders on interaction

## 💻 API Endpoints

### POST `/api/generate-meal-plan`
Generates a complete meal plan with grocery list and budget analysis.

**Request:**
```json
{
  "budget": 50,
  "servings": 2,
  "dietary_preferences": "vegetarian",
  "cooking_time": "quick"
}
```

**Response:**
```json
{
  "success": true,
  "meal_plan": { ... },
  "grocery_list": [ ... ],
  "budget_info": { ... },
  "substitutions": { ... }
}
```

### POST `/api/optimize-budget`
Optimizes meal plan to fit within budget.

### POST `/api/budget-recommendation`
Gets budget recommendations and tips.

### POST `/api/alternative-meals`
Generates alternative meal combinations.

## 🔧 Configuration

Edit `config.py` to adjust:
- Debug mode
- Secret key
- Environment-specific settings

## 📦 Dependencies

- **Flask==2.3.2**: Web framework
- **python-dotenv==1.0.0**: Environment variable management
- **openai==0.27.8**: OpenAI API (optional)
- **requests==2.31.0**: HTTP library

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Glassmorphism Design](https://glassmorphism.com/)
- [CSS Backdrop Filter](https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter)

## 🐛 Troubleshooting

### Port 5000 already in use
```bash
# Use a different port
python -c "from app import create_app; app = create_app(); app.run(port=5001)"
```

### Module not found errors
Ensure virtual environment is activated and all packages are installed:
```bash
pip install -r requirements.txt
```

### CSS not loading
Clear browser cache or do a hard refresh (Ctrl+Shift+R on Windows/Linux, Cmd+Shift+R on Mac)

## 🚀 Future Enhancements

- [ ] Integration with OpenAI API for AI-powered meal suggestions
- [ ] User authentication and saved meal plans
- [ ] Nutritional information display
- [ ] Recipe details and cooking instructions
- [ ] Grocery store price comparison
- [ ] Dietary restriction compliance checking
- [ ] Export to shopping lists/PDFs
- [ ] Mobile app version

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 💡 Tips

- Start with a small budget to test the optimization feature
- Try different dietary preferences to see varied meal plans
- Use the glassmorphic cards to explore multiple alternatives
- Check the browser console for debugging information

---

**Made with ❤️ for home chefs and meal planning enthusiasts**
