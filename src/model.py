from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def recommend_meals(df, user_features):

    features = df[
        [
            'calories', 'protein', 'carbs', 'fat',
            'fibre', 'sugar', 'sodium',
            'calcium', 'iron', 'vitamin_c', 'folate'
        ]
    ]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    user_df = pd.DataFrame([user_features], columns=features.columns)
    user_vector = scaler.transform(user_df)

    similarity = cosine_similarity(user_vector, scaled_features)

    df['score'] = similarity[0]

    return df.sort_values(by='score', ascending=False).head(6)