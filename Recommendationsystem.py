
user_ratings = {
    'User1': {'Movie1': 4, 'Movie2': 5, 'Movie3': 3},
    'User2': {'Movie1': 5, 'Movie4': 4, 'Movie5': 2},
    'User3': {'Movie2': 3, 'Movie4': 5, 'Movie6': 4},
    
}
def calculate_similarity(user1, user2):
    common_movies = set(user1.keys()) & set(user2.keys())
    if not common_movies:
        return 0  
    union_movies = set(user1.keys()) | set(user2.keys())
    similarity = len(common_movies) / len(union_movies)
    return similarity


def get_recommendations(target_user):
    recommendations = {}
    for user, ratings in user_ratings.items():
        if user == target_user:
            continue  
        similarity = calculate_similarity(user_ratings[target_user], ratings)
        for movie, rating in ratings.items():
            if movie not in user_ratings[target_user]:
                if movie not in recommendations:
                    recommendations[movie] = 0
                recommendations[movie] += similarity * rating
  
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return sorted_recommendations


target_user = 'User1'
recommended_movies = get_recommendations(target_user)

top_n = 5
print(f"Top {top_n} movie recommendations for {target_user}:")
for movie, score in recommended_movies[:top_n]:
    print(f"Movie: {movie}, Score: {score}")
