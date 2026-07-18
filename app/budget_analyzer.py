from typing import Dict, List, Tuple

class BudgetAnalyzer:
    """Budget analysis and feasibility logic"""
    
    def __init__(self):
        self.price_multiplier = 1.15  # 15% markup for processing/waste
    
    def calculate_total_cost(self, grocery_list: List[Dict]) -> float:
        """Calculate total cost of grocery list"""
        total = 0.0
        for item in grocery_list:
            item_cost = item.get('price', 0) * item.get('quantity', 1)
            total += item_cost * self.price_multiplier
        
        return round(total, 2)
    
    def check_budget_feasibility(self, total_cost: float, budget: float) -> Dict:
        """Check if meal plan fits within budget"""
        feasible = total_cost <= budget
        remaining = budget - total_cost
        percentage = (total_cost / budget * 100) if budget > 0 else 0
        
        return {
            'feasible': feasible,
            'total_cost': total_cost,
            'budget': budget,
            'remaining': round(remaining, 2),
            'percentage_used': round(percentage, 2),
            'status': 'Within Budget' if feasible else 'Over Budget'
        }
    
    def optimize_meal_plan(self, grocery_list: List[Dict], target_budget: float) -> Tuple[List[Dict], float]:
        """Optimize meal plan to fit within budget"""
        total_cost = self.calculate_total_cost(grocery_list)
        
        if total_cost <= target_budget:
            return grocery_list, total_cost
        
        # Sort by price per unit and reduce quantities
        sorted_list = sorted(grocery_list, key=lambda x: x.get('price', 0), reverse=True)
        
        for item in sorted_list:
            if total_cost <= target_budget:
                break
            
            # Reduce quantity by 1 if possible
            if item['quantity'] > 1:
                item['quantity'] -= 1
                total_cost = self.calculate_total_cost(sorted_list)
        
        return sorted_list, round(total_cost, 2)
    
    def calculate_cost_per_serving(self, total_cost: float, servings: int) -> float:
        """Calculate cost per serving"""
        if servings <= 0:
            return 0
        
        return round(total_cost / servings, 2)
    
    def get_budget_recommendation(self, total_cost: float, servings: int) -> Dict:
        """Get budget recommendations"""
        cost_per_serving = self.calculate_cost_per_serving(total_cost, servings)
        
        return {
            'total_cost': total_cost,
            'cost_per_serving': cost_per_serving,
            'servings': servings,
            'recommendation': self._get_recommendation(cost_per_serving)
        }
    
    def _get_recommendation(self, cost_per_serving: float) -> str:
        """Generate budget recommendation message"""
        if cost_per_serving < 3:
            return "Budget-friendly option"
        elif cost_per_serving < 5:
            return "Moderate cost option"
        elif cost_per_serving < 8:
            return "Premium option"
        else:
            return "Luxury option"
    
    def compare_alternatives(self, alternatives: List[Dict]) -> Dict:
        """Compare costs of different meal alternatives"""
        comparison = []
        
        for alt in alternatives:
            cost = self.calculate_total_cost(alt.get('grocery_list', []))
            comparison.append({
                'name': alt.get('name'),
                'cost': cost,
                'feasible': cost <= alt.get('budget', float('inf'))
            })
        
        # Sort by cost
        comparison.sort(key=lambda x: x['cost'])
        
        return {
            'comparison': comparison,
            'cheapest': comparison[0] if comparison else None,
            'average_cost': sum(c['cost'] for c in comparison) / len(comparison) if comparison else 0
        }
