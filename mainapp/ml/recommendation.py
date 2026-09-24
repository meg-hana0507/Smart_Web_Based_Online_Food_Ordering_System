import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from mainapp.models import OrderItem


def get_recommendations(user_id):
    """
    Returns list of recommended food IDs for a given user
    """

    # Get user-food purchase data
    data = OrderItem.objects.values(
        'order__user_id',
        'food_id'
    )

    df = pd.DataFrame(list(data))

    # If no orders exist
    if df.empty:
        return []

    # Rename column
    df.rename(columns={'order__user_id': 'user_id'}, inplace=True)

    # Create user-food matrix
    user_food_matrix = pd.crosstab(
        df['user_id'],
        df['food_id']
    )

    # User not found
    if user_id not in user_food_matrix.index:
        return []

    # Calculate similarity
    similarity = cosine_similarity(user_food_matrix)

    similarity_df = pd.DataFrame(
        similarity,
        index=user_food_matrix.index,
        columns=user_food_matrix.index
    )

    # Get top similar users
    similar_users = similarity_df[user_id].sort_values(
        ascending=False
    )[1:4]

    recommended_foods = set()

    for sim_user in similar_users.index:
        foods = df[df['user_id'] == sim_user]['food_id'].tolist()
        recommended_foods.update(foods)

    # Remove foods already ordered by current user
    user_foods = set(
        df[df['user_id'] == user_id]['food_id']
    )

    recommended_foods = recommended_foods - user_foods

    return list(recommended_foods)