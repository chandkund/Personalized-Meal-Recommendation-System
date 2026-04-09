import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.recommend import get_meal_plan

# Page config
st.set_page_config(page_title="AI Meal Planner", layout="wide")

# Title
st.title("🍽️ AI Personalized Meal Planner")
st.markdown("### 🧠 Smart Nutrition-Based Indian Meal Recommendation System")

# Sidebar
st.sidebar.header("👤 Enter Your Details")

age = st.sidebar.slider("Age", 10, 60)
weight = st.sidebar.slider("Weight (kg)", 30, 120)
height = st.sidebar.slider("Height (cm)", 120, 200)
gender = st.sidebar.selectbox("Gender", ["male", "female"])
activity = st.sidebar.selectbox("Activity Level", ["low", "medium", "high"])
goal = st.sidebar.selectbox("Goal", ["weight_loss", "maintain", "weight_gain"])
diet = st.sidebar.selectbox("Diet Type", ["veg", "non-veg"])

# Button
if st.sidebar.button("🚀 Generate Meal Plan"):

    user = {
        "age": age,
        "weight": weight,
        "height": height,
        "gender": gender,
        "activity": activity,
        "goal": goal,
        "diet": diet
    }

    meals, calories = get_meal_plan(user)

    # Calories display
    st.subheader(f"🔥 Daily Calorie Requirement: {int(calories)} kcal")

    st.markdown("---")

    # Meal Cards
    st.subheader("🍛 Recommended Meals")

    cols = st.columns(3)

    for i, (_, meal) in enumerate(meals.iterrows()):
        with cols[i % 3]:
            st.markdown(f"""
            ### 🍴 {meal['meal_name']}

            **🔥 Calories:** {meal['calories']} kcal  
            **💪 Protein:** {meal['protein']} g  
            **🍞 Carbs:** {meal['carbs']} g  
            **🥑 Fat:** {meal['fat']} g  

            **🌾 Fibre:** {meal['fibre']} g  
            **🍬 Sugar:** {meal['sugar']} g  
            **🧂 Sodium:** {meal['sodium']} mg  

            **🦴 Calcium:** {meal['calcium']} mg  
            **🩸 Iron:** {meal['iron']} mg  
            **🍊 Vitamin C:** {meal['vitamin_c']} mg  
            """)

    st.markdown("---")

    # Charts
    st.subheader("📊 Nutrition Breakdown")

    st.bar_chart(meals[['protein', 'carbs', 'fat']])

    st.subheader("🧪 Micronutrients")

    st.bar_chart(meals[['calcium', 'iron', 'vitamin_c']])

    # Insight box
    st.info("💡 Recommendations are based on your calorie needs and full nutrition profile.")

    st.success("✅ Meal plan generated successfully!")