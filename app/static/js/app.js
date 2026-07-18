// State management
const appState = {
    currentMealPlan: null,
    currentGroceryList: null,
    currentBudget: null,
    currentPreferences: null
};

// DOM Elements
const preferenceForm = document.getElementById('preferenceForm');
const resultsPanel = document.getElementById('resultsPanel');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const regenerateBtn = document.getElementById('regenerateBtn');
const optimizeBtn = document.getElementById('optimizeBtn');
const restartBtn = document.getElementById('restartBtn');

// Event Listeners
preferenceForm.addEventListener('submit', handleGenerateMealPlan);
regenerateBtn.addEventListener('click', handleRegenerateMealPlan);
optimizeBtn.addEventListener('click', handleOptimizeBudget);
restartBtn.addEventListener('click', resetForm);

// Main Functions
async function handleGenerateMealPlan(e) {
    e.preventDefault();
    
    const preferences = {
        budget: parseFloat(document.getElementById('budget').value),
        servings: parseInt(document.getElementById('servings').value),
        dietary_preferences: document.getElementById('dietary').value,
        cooking_time: document.getElementById('time').value
    };
    
    appState.currentPreferences = preferences;
    
    // Validate preferences
    if (preferences.budget < 20) {
        showError('Budget must be at least $20');
        return;
    }
    
    if (preferences.servings < 1 || preferences.servings > 12) {
        showError('Servings must be between 1 and 12');
        return;
    }
    
    showLoading(true);
    hideError();
    
    try {
        const response = await fetch('/api/generate-meal-plan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(preferences)
        });
        
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Failed to generate meal plan');
        }
        
        const data = await response.json();
        appState.currentMealPlan = data.meal_plan;
        appState.currentGroceryList = data.grocery_list;
        appState.currentBudget = data.budget_info;
        
        displayMealPlan(data);
        displayGroceryList(data.grocery_list);
        displayBudgetInfo(data.budget_info, preferences.servings);
        displaySubstitutions(data.substitutions);
        
        showLoading(false);
        resultsPanel.style.display = 'block';
        
        // Scroll to results
        setTimeout(() => {
            resultsPanel.scrollIntoView({ behavior: 'smooth' });
        }, 300);
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message);
        showLoading(false);
    }
}

async function handleRegenerateMealPlan() {
    if (!appState.currentPreferences) return;
    
    showLoading(true);
    hideError();
    
    try {
        const response = await fetch('/api/generate-meal-plan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(appState.currentPreferences)
        });
        
        const data = await response.json();
        appState.currentMealPlan = data.meal_plan;
        appState.currentGroceryList = data.grocery_list;
        appState.currentBudget = data.budget_info;
        
        displayMealPlan(data);
        displayGroceryList(data.grocery_list);
        displayBudgetInfo(data.budget_info, appState.currentPreferences.servings);
        displaySubstitutions(data.substitutions);
        
        showLoading(false);
        showMessage('✅ Alternative meal plan generated!');
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message);
        showLoading(false);
    }
}

async function handleOptimizeBudget() {
    if (!appState.currentGroceryList || !appState.currentBudget) return;
    
    showLoading(true);
    hideError();
    
    try {
        const response = await fetch('/api/optimize-budget', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                grocery_list: appState.currentGroceryList,
                budget: appState.currentPreferences.budget
            })
        });
        
        const data = await response.json();
        appState.currentGroceryList = data.optimized_list;
        appState.currentBudget = data.budget_info;
        
        displayGroceryList(data.optimized_list);
        displayBudgetInfo(data.budget_info, appState.currentPreferences.servings);
        
        showLoading(false);
        showMessage('⚡ Meal plan optimized to fit your budget!');
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message);
        showLoading(false);
    }
}

// Display Functions
function displayMealPlan(data) {
    const mealPlan = data.meal_plan;
    
    // Breakfast
    document.getElementById('breakfastMeal').textContent = mealPlan.breakfast.name;
    document.getElementById('breakfastTime').textContent = `⏱️ ${mealPlan.breakfast.time} minutes`;
    
    // Lunch
    document.getElementById('lunchMeal').textContent = mealPlan.lunch.name;
    document.getElementById('lunchTime').textContent = `⏱️ ${mealPlan.lunch.time} minutes`;
    
    // Dinner
    document.getElementById('dinnerMeal').textContent = mealPlan.dinner.name;
    document.getElementById('dinnerTime').textContent = `⏱️ ${mealPlan.dinner.time} minutes`;
}

function displayGroceryList(groceryList) {
    const tbody = document.getElementById('groceryTableBody');
    tbody.innerHTML = '';
    
    groceryList.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.quantity}</td>
            <td>${item.unit}</td>
            <td>$${(item.price * item.quantity).toFixed(2)}</td>
        `;
        tbody.appendChild(row);
    });
}

function displayBudgetInfo(budgetInfo, servings) {
    const totalCost = budgetInfo.total_cost;
    const costPerServing = (totalCost / servings).toFixed(2);
    
    document.getElementById('totalCost').textContent = `$${totalCost.toFixed(2)}`;
    document.getElementById('userBudget').textContent = `$${budgetInfo.budget.toFixed(2)}`;
    document.getElementById('costPerServing').textContent = `$${costPerServing}`;
    
    const remainingElement = document.getElementById('remainingBudget');
    const remaining = budgetInfo.remaining;
    remainingElement.querySelector('.stat-value').textContent = `$${remaining.toFixed(2)}`;
    
    // Update budget status
    const statusElement = document.getElementById('budgetStatus');
    const messageElement = document.getElementById('budgetMessage');
    const progressElement = document.getElementById('budgetProgress');
    
    const percentage = Math.min(budgetInfo.percentage_used, 100);
    progressElement.style.width = percentage + '%';
    
    if (budgetInfo.feasible) {
        messageElement.textContent = `✅ ${budgetInfo.status} - You'll save $${remaining.toFixed(2)}`;
        progressElement.classList.remove('danger');
    } else {
        messageElement.textContent = `⚠️ ${budgetInfo.status} - Over by $${Math.abs(remaining).toFixed(2)}`;
        progressElement.classList.add('danger');
    }
}

function displaySubstitutions(substitutions) {
    const container = document.getElementById('substitutionsList');
    container.innerHTML = '';
    
    Object.entries(substitutions).forEach(([ingredient, alternatives]) => {
        if (alternatives.length > 0) {
            const div = document.createElement('div');
            div.className = 'substitution-item';
            div.innerHTML = `
                <strong>${capitalizeFirst(ingredient)}</strong>
                <p>Try: ${alternatives.join(', ')}</p>
            `;
            container.appendChild(div);
        }
    });
}

// Utility Functions
function capitalizeFirst(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

function showLoading(show) {
    loadingSpinner.style.display = show ? 'flex' : 'none';
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
}

function hideError() {
    errorMessage.style.display = 'none';
}

function showMessage(message) {
    // Simple notification (can be enhanced)
    console.log(message);
}

function resetForm() {
    preferenceForm.reset();
    resultsPanel.style.display = 'none';
    appState.currentMealPlan = null;
    appState.currentGroceryList = null;
    appState.currentBudget = null;
    appState.currentPreferences = null;
    hideError();
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Initialize
console.log('🍽️ Meal Planner AI loaded successfully!');
