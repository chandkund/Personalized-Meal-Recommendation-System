def calculate_bmr(weight, height, age, gender):
    gender = gender.lower()
    
    if gender == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "female":
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("Gender must be 'male' or 'female'")


def calculate_calories(bmr, activity_level):
    activity_map = {
        "low": 1.2,
        "medium": 1.55,
        "high": 1.9
    }
    
    if activity_level not in activity_map:
        raise ValueError("Invalid activity level")
    
    return bmr * activity_map[activity_level]


def adjust_calories_for_goal(calories, goal):
    if goal == "weight_loss":
        return calories - 300
    elif goal == "weight_gain":
        return calories + 300
    elif goal == "maintain":
        return calories
    else:
        raise ValueError("Invalid goal")