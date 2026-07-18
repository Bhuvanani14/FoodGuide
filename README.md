# 🍽️ FoodGuide AI - Meal Planner

A Flask-based AI-powered meal planning application with an interactive glassmorphism UI. Generate personalized meal plans, grocery lists, food substitutions, and budget analysis in real-time.

**GitHub**: https://github.com/Bhuvanani14/FoodGuide  
**Cloud Project**: tidy-node-494313-j1  
**Deployment Status**: Ready to Deploy to Cloud Run

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

### Local Development

**Prerequisites**: Python 3.11+, pip, Git

**Installation**:
```bash
# Clone repository
git clone https://github.com/Bhuvanani14/FoodGuide.git
cd FoodGuide

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python run.py
```

**Access**: http://localhost:5000

### ☁️ Cloud Deployment (Google Cloud Run)

**Prerequisites**: 
- Billing enabled on project `tidy-node-494313-j1`
- gcloud CLI installed and authenticated

**Deploy**:
```bash
# Automatic deployment
chmod +x deploy-cloud-run.sh
./deploy-cloud-run.sh

# Get service URL
gcloud run services describe foodguide-ai-meal-planner \
  --platform managed --region us-central1 \
  --format 'value(status.url)'
```

📖 **Detailed Cloud Deployment Guide**: See [CLOUD_DEPLOYMENT.md](CLOUD_DEPLOYMENT.md)

## 📖 How to Use

1. **Enter Your Preferences**
   - Budget ($20 minimum)
   - Servings (1-12)
   - Dietary preference
   - Cooking time

2. **Generate Meal Plan**
   - View breakfast, lunch & dinner suggestions
   - See ingredients with quantities & prices
   - Analyze total cost

3. **Optimize & Explore**
   - Generate alternatives for variety
   - Optimize to fit budget
   - Check food substitutions

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
pyth� Supported Browsers

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome
- [ ] Nutritional information display
- [ ] Recipe details and cooking instructions
- [ ] Grocery store price comparison
- [ ] Dietary restriction compliance checking
- [ ] Export to shopping lists/PDFs
- [ ] Roadmap

- **� API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/generate-meal-plan` | POST | Generate meal plan with budget |
| `/api/optimize-budget` | POST | Optimize costs |
| `/api/budget-recommendation` | POST | Get budget tips |
| `/api/alternative-meals` | POST | Generate alternatives |
| `/health` | GET | Health check |

## 📄 License

MIT License - see LICENSE file for details

## 🤝 Contributing

1. Fork the repo
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push branch (`git push origin feature/amazing`)
5. Open Pull Request

## 📧 Support

- Issues: [GitHub Issues](https://github.com/Bhuvanani14/FoodGuide/issues)
- Questions: Create a discussion or issue
- Feedback: Always welcome!

---

**Made with ❤️ by [Bhuvanani14](https://github.com/Bhuvanani14)**  
**Repository**: https://github.com/Bhuvanani14/FoodGuide  
**Cloud Project**: tidy-node-494313-j1