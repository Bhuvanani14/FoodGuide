import json
import os
from typing import Dict, List, Tuple
import random

class MealPlanner:
    """Core meal planning logic"""
    
    def __init__(self):
        self.meals_db = self._load_meals_db()
        self.ingredients_db = self._load_ingredients_db()
        self.substitutions_db = self._load_substitutions_db()
    
    def _load_meals_db(self) -> Dict:
        """Load meals database"""
        return {
            "breakfast": [
                {"name": "Oatmeal with Berries", "ingredients": ["oats", "milk", "berries"], "calories": 350, "time": 15},
                {"name": "Scrambled Eggs & Toast", "ingredients": ["eggs", "bread", "butter"], "calories": 400, "time": 20},
                {"name": "Greek Yogurt Parfait", "ingredients": ["yogurt", "granola", "honey"], "calories": 300, "time": 5},
                {"name": "Smoothie Bowl", "ingredients": ["banana", "milk", "berries", "granola"], "calories": 380, "time": 10},
                {"name": "Pancakes", "ingredients": ["flour", "eggs", "milk", "syrup"], "calories": 450, "time": 25},
                {"name": "Avocado Toast", "ingredients": ["bread", "avocado", "eggs", "tomato"], "calories": 380, "time": 10},
            ],
            "lunch": [
                {"name": "Chicken Caesar Salad", "ingredients": ["chicken", "lettuce", "parmesan", "croutons"], "calories": 450, "time": 20},
                {"name": "Turkey Sandwich", "ingredients": ["turkey", "bread", "lettuce", "tomato"], "calories": 420, "time": 10},
                {"name": "Pasta Primavera", "ingredients": ["pasta", "broccoli", "peppers", "olive oil"], "calories": 480, "time": 30},
                {"name": "Buddha Bowl", "ingredients": ["quinoa", "chickpeas", "vegetables", "tahini"], "calories": 500, "time": 25},
                {"name": "Grilled Salmon", "ingredients": ["salmon", "rice", "asparagus", "lemon"], "calories": 520, "time": 35},
                {"name": "Veggie Wrap", "ingredients": ["tortilla", "hummus", "vegetables"], "calories": 380, "time": 15},
            ],
            "dinner": [
                {"name": "Spaghetti Bolognese", "ingredients": ["pasta", "beef", "tomato", "onion"], "calories": 600, "time": 45},
                {"name": "Grilled Chicken Breast", "ingredients": ["chicken", "broccoli", "potatoes"], "calories": 550, "time": 40},
                {"name": "Vegetable Stir Fry", "ingredients": ["vegetables", "soy sauce", "rice", "garlic"], "calories": 420, "time": 30},
                {"name": "Beef Tacos", "ingredients": ["beef", "tortillas", "lettuce", "cheese"], "calories": 580, "time": 25},
                {"name": "Baked Tilapia", "ingredients": ["tilapia", "lemon", "vegetables"], "calories": 480, "time": 35},
                {"name": "Mushroom Risotto", "ingredients": ["rice", "mushrooms", "parmesan", "wine"], "calories": 520, "time": 40},
            ]
        }
    
    def _load_ingredients_db(self) -> Dict:
        """Load ingredients database with prices"""
        return {
            "chicken": {"price": 8.99, "unit": "lb"},
            "beef": {"price": 12.99, "unit": "lb"},
            "salmon": {"price": 14.99, "unit": "lb"},
            "turkey": {"price": 9.99, "unit": "lb"},
            "eggs": {"price": 4.99, "unit": "dozen"},
            "oats": {"price": 3.99, "unit": "container"},
            "bread": {"price": 2.99, "unit": "loaf"},
            "milk": {"price": 3.49, "unit": "gallon"},
            "yogurt": {"price": 5.99, "unit": "container"},
            "berries": {"price": 4.99, "unit": "lb"},
            "lettuce": {"price": 2.49, "unit": "head"},
            "tomato": {"price": 1.99, "unit": "lb"},
            "pasta": {"price": 1.49, "unit": "box"},
            "rice": {"price": 2.49, "unit": "bag"},
            "vegetables": {"price": 3.99, "unit": "bag"},
            "cheese": {"price": 5.99, "unit": "container"},
        }
    
    def _load_substitutions_db(self) -> Dict:
        """Load food substitutions database"""
        return {
            "chicken": ["turkey", "tofu", "tempeh"],
            "beef": ["chicken", "turkey", "plant-based meat"],
            "eggs": ["tofu", "aquafaba", "applesauce"],
            "milk": ["almond milk", "oat milk", "coconut milk"],
            "butter": ["olive oil", "coconut oil", "applesauce"],
            "bread": ["whole wheat", "gluten-free", "lettuce wraps"],
            "pasta": ["whole wheat pasta", "rice noodles", "zucchini noodles"],
        }
    
    def generate_meal_plan(self, preferences: Dict) -> Dict:
        """Generate personalized meal plan"""
        meal_plan = {}
        preferences_diet = preferences.get('dietary_preferences', [])
        
        for meal_type in ['breakfast', 'lunch', 'dinner']:
            available_meals = self.meals_db.get(meal_type, [])
            selected_meal = random.choice(available_meals)
            meal_plan[meal_type] = selected_meal
        
        return meal_plan
    
    def get_grocery_list(self, meal_plan: Dict) -> List[Dict]:
        """Generate grocery list from meal plan"""
        grocery_list = {}
        
        for meal_type, meal in meal_plan.items():
            for ingredient in meal.get('ingredients', []):
                if ingredient in grocery_list:
                    grocery_list[ingredient]['quantity'] += 1
                else:
                    grocery_list[ingredient] = {
                        'name': ingredient,
                        'quantity': 1,
                        'unit': self.ingredients_db.get(ingredient, {}).get('unit', 'unit'),
                        'price': self.ingredients_db.get(ingredient, {}).get('price', 0),
                    }
        
        return list(grocery_list.values())
    
    def get_substitutions(self, ingredients: List[str]) -> Dict:
        """Get food substitutions for ingredients"""
        substitutions = {}
        
        for ingredient in ingredients:
            if ingredient in self.substitutions_db:
                substitutions[ingredient] = self.substitutions_db[ingredient]
            else:
                substitutions[ingredient] = []
        
        return substitutions
    
    def validate_preferences(self, preferences: Dict) -> Tuple[bool, str]:
        """Validate user preferences"""
        if not preferences.get('budget'):
            return False, "Budget is required"
        
        if preferences.get('budget') < 20:
            return False, "Budget must be at least $20"
        
        if not preferences.get('servings'):
            return False, "Number of servings is required"
        
        return True, "Preferences are valid"
