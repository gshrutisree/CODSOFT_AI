movies = {
    'Vincenzo': ['action', 'thriller', 'sci-fi'],
    'True beauty': ['comedy', 'romance'],
    'Extradinary you': ['drama', 'romance'],
    'My name': ['action', 'adventure'],
    'All of us are dead': ['zombie', 'thriller'],
    'Reply 1988': ['comedy', 'drama'],
    'Goblin': ['adventure', 'fantasy'],
    'Squid game': ['sci-fi', 'adventure'],
    
}

def calculate_overlap(user_input, movie_features):
    
    return len(set(movie_features) & set(user_input.split()))

def recommend_movie(user_input, movies_data):
    
    best_match = None
    max_overlap = 0

    for movie, features in movies_data.items():
        overlap = calculate_overlap(user_input, features)
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = movie

    return best_match
    
user_input = input("Enter your favorite genre: ")

# Get the recommended movie
recommended_movie = recommend_movie(user_input, movies)

if recommended_movie:
    print(f"Recommended movie for you: {recommended_movie}")
else:
    print("Sorry, no recommendations found.")