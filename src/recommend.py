from src.preprocessing import load_raw_data, clean_columns, select_columns, feature_engineering, rename_columns
from src.feature_engineering import calculate_bmr, calculate_calories, adjust_calories_for_goal
from src.model import recommend_meals


def get_meal_plan(user_input):
    
    # Load processed data
    df = load_raw_data("data/meals.csv")
    
    # Filter by diet
    df = df[df['diet_type'] == user_input['diet']]
    
    # Calculate calories
    bmr = calculate_bmr(
        user_input['weight'],
        user_input['height'],
        user_input['age'],
        user_input['gender']
    )
    
    calories = calculate_calories(bmr, user_input['activity'])
    final_calories = adjust_calories_for_goal(calories, user_input['goal'])
    
    # Per meal target
    per_meal = final_calories / 3
    
    user_features = [
    per_meal,   # calories
    20,         # protein
    30,         # carbs
    10,         # fat
    5,          # fibre
    5,          # sugar
    500,        # sodium
    100,        # calcium
    10,         # iron
    20,         # vitamin C
    100         # folate
]
    
    meals = recommend_meals(df, user_features)
    
    return meals, final_calories