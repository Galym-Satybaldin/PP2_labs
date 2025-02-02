def compute_average_imdb(movies):
    total = 0
    for movie in movies:
        total += movie["imdb"]
    return total / len(movies)

# Create an empty list to hold the movies.
movies = []

# Ask the user for the number of movies.
num_movies = int(input("How many movies do you want to enter? "))

# Get the details for each movie.
for i in range(num_movies):
    print("\nEnter details for movie", i + 1)
    name = input("Movie name: ")
    imdb = float(input("IMDB score: "))
    category = input("Category: ")
    # Create a dictionary for the movie and add it to the list.
    movie = {"name": name, "imdb": imdb, "category": category}
    movies.append(movie)

# Compute and print the average IMDB score.
average = compute_average_imdb(movies)
print("\nAverage IMDB score:", average)
