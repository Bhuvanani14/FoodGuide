from flask import Blueprint, render_template, request, jsonify
from app.meal_planner import MealPlanner
from app.budget_analyzer import BudgetAnalyzer

main_bp = Blueprint('main', __name__)
meal_planner = MealPlanner()
budget_analyzer = BudgetAnalyzer()

@main_bp.route('/')
def index():
    """Render main application page"""
    return render_template('index.html')

@main_bp.route('/api/generate-meal-plan', methods=['POST'])
def generate_meal_plan():
    """Generate personalized meal plan"""
    try:
        data = request.get_json()
        
        # Validate preferences
        is_valid, message = meal_planner.validate_preferences(data)
        if not is_valid:
            return jsonify({'error': message}), 400
        
        # Generate meal plan
        meal_plan = meal_planner.generate_meal_plan(data)
        
        # Get grocery list
        grocery_list = meal_planner.get_grocery_list(meal_plan)
        
        # Calculate costs
        total_cost = budget_analyzer.calculate_total_cost(grocery_list)
        budget_info = budget_analyzer.check_budget_feasibility(total_cost, data['budget'])
        
        # Get substitutions
        ingredient_names = [item['name'] for item in grocery_list]
        substitutions = meal_planner.get_substitutions(ingredient_names)
        
        return jsonify({
            'success': True,
            'meal_plan': meal_plan,
            'grocery_list': grocery_list,
            'budget_info': budget_info,
            'substitutions': substitutions,
            'cost_per_serving': budget_analyzer.calculate_cost_per_serving(total_cost, data['servings'])
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/optimize-budget', methods=['POST'])
def optimize_budget():
    """Optimize meal plan to fit within budget"""
    try:
        data = request.get_json()
        grocery_list = data.get('grocery_list', [])
        target_budget = data.get('budget', 0)
        
        optimized_list, total_cost = budget_analyzer.optimize_meal_plan(
            grocery_list, 
            target_budget
        )
        
        budget_info = budget_analyzer.check_budget_feasibility(
            total_cost, 
            target_budget
        )
        
        return jsonify({
            'success': True,
            'optimized_list': optimized_list,
            'total_cost': total_cost,
            'budget_info': budget_info
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/budget-recommendation', methods=['POST'])
def get_budget_recommendation():
    """Get budget recommendations"""
    try:
        data = request.get_json()
        grocery_list = data.get('grocery_list', [])
        servings = data.get('servings', 1)
        
        total_cost = budget_analyzer.calculate_total_cost(grocery_list)
        recommendation = budget_analyzer.get_budget_recommendation(total_cost, servings)
        
        return jsonify({
            'success': True,
            'recommendation': recommendation
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/alternative-meals', methods=['POST'])
def get_alternative_meals():
    """Get alternative meal combinations"""
    try:
        data = request.get_json()
        
        alternatives = []
        for i in range(3):
            alt_meal_plan = meal_planner.generate_meal_plan(data)
            alt_grocery_list = meal_planner.get_grocery_list(alt_meal_plan)
            alt_cost = budget_analyzer.calculate_total_cost(alt_grocery_list)
            
            alternatives.append({
                'name': f'Option {i+1}',
                'meal_plan': alt_meal_plan,
                'grocery_list': alt_grocery_list,
                'cost': alt_cost
            })
        
        return jsonify({
            'success': True,
            'alternatives': alternatives
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})
