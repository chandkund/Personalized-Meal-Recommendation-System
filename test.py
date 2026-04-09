from src.recommend import get_meal_plan

user = {
    "age": 25,
    "weight": 70,
    "height": 170,
    "gender": "male",
    "activity": "medium",
    "goal": "weight_loss",
    "diet": "veg"
}

meals, calories = get_meal_plan(user)

print("Calories:", calories)
print(meals)