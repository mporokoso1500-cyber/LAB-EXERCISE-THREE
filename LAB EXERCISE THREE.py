def main():
    favorite_movies = ["The First Blood", "The Expendables", "Full Metal Jacket"]
    print("Initial list of movies:", favorite_movies)

    new_movie = input("\nEnter a new movie to add: ")
    favorite_movies.append(new_movie)
    print(f"'{new_movie}' has been added.")

    movie_to_remove = input("\nEnter a movie to remove: ")
    if movie_to_remove in favorite_movies:
        favorite_movies.remove(movie_to_remove)
        print(f"'{movie_to_remove}' has been removed.")
    else:
        print(f"'{movie_to_remove}' was not found in the list.")
    favorite_movies.sort()
    print("\nFinal sorted list of movies:", favorite_movies)


if __name__ == "__main__":
    main()

