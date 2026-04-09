import pandas as pd


def load_raw_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None


def clean_columns(df):
    # Clean column names
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(".", "", regex=False)
    )

    # 🔥 Convert numeric columns properly
    numeric_cols = [
        'calories_(kcal)',
        'carbohydrates_(g)',
        'protein_(g)',
        'fats_(g)',
        'free_sugar_(g)',
        'fibre_(g)',
        'sodium_(mg)',
        'calcium_(mg)',
        'iron_(mg)',
        'vitamin_c_(mg)',
        'folate_(µg)'
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(",", "")
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove invalid rows
    df.dropna(inplace=True)

    return df


def select_columns(df):
    return df[
        [
            'dish_name',
            'calories_(kcal)',
            'carbohydrates_(g)',
            'protein_(g)',
            'fats_(g)',
            'free_sugar_(g)',
            'fibre_(g)',
            'sodium_(mg)',
            'calcium_(mg)',
            'iron_(mg)',
            'vitamin_c_(mg)',
            'folate_(µg)'
        ]
    ]


def rename_columns(df):
    return df.rename(columns={
        'dish_name': 'meal_name',
        'calories_(kcal)': 'calories',
        'carbohydrates_(g)': 'carbs',
        'protein_(g)': 'protein',
        'fats_(g)': 'fat',
        'free_sugar_(g)': 'sugar',
        'fibre_(g)': 'fibre',
        'sodium_(mg)': 'sodium',
        'calcium_(mg)': 'calcium',
        'iron_(mg)': 'iron',
        'vitamin_c_(mg)': 'vitamin_c',
        'folate_(µg)': 'folate'
    })


def assign_diet(food):
    food = str(food).lower()
    non_veg_items = ['chicken', 'egg', 'fish', 'mutton', 'beef', 'prawn']

    if any(item in food for item in non_veg_items):
        return "non-veg"
    return "veg"


def feature_engineering(df):
    # Diet type
    df['diet_type'] = df['meal_name'].apply(assign_diet)

    # Category (based on calories)
    def assign_category(calories):
        if calories < 300:
            return "Breakfast"
        elif calories < 600:
            return "Lunch"
        else:
            return "Dinner"

    df['category'] = df['calories'].apply(assign_category)

    return df


def save_processed_data(df, path):
    df.to_csv(path, index=False)


def run_pipeline(input_path, output_path):
    df = load_raw_data(input_path)

    if df is None:
        return

    df = clean_columns(df)
    df = select_columns(df)
    df = rename_columns(df)        # ✅ IMPORTANT ORDER
    df = feature_engineering(df)   # ✅ AFTER rename

    save_processed_data(df, output_path)

    print("✅ Dataset Ready!")