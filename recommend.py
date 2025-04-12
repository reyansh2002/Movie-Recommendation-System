import sqlite3

def recommend_by_genre(genre):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    query = f"""
    SELECT m.title, m.genres,
           ROUND(AVG(r.rating), 2) AS avg_rating,
           COUNT(r.rating) AS num_ratings
    FROM movies m
    JOIN ratings r ON m.movieId = r.movieId
    WHERE m.genres LIKE '%{genre}%'
    GROUP BY m.movieId
    HAVING num_ratings >= 5
    ORDER BY avg_rating DESC, num_ratings DESC
    LIMIT 20
    """

    results = cursor.execute(query).fetchall()
    conn.close()
    return results


def recommend_by_rating(threshold):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    query = f"""
    SELECT m.title, m.genres,
           ROUND(AVG(r.rating), 2) AS avg_rating,
           COUNT(r.rating) AS num_ratings
    FROM movies m
    JOIN ratings r ON m.movieId = r.movieId
    GROUP BY m.movieId
    HAVING avg_rating >= {threshold} AND num_ratings >= 5
    ORDER BY avg_rating DESC, num_ratings DESC
    LIMIT 20
    """

    results = cursor.execute(query).fetchall()
    conn.close()
    return results


def recommend_by_keyword(keyword):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    query = f"""
    SELECT m.title, m.genres,
           ROUND(AVG(r.rating), 2) AS avg_rating,
           COUNT(r.rating) AS num_ratings
    FROM movies m
    JOIN ratings r ON m.movieId = r.movieId
    WHERE m.title LIKE '%{keyword}%'
    GROUP BY m.movieId
    HAVING num_ratings >= 5
    ORDER BY avg_rating DESC, num_ratings DESC
    LIMIT 20
    """

    results = cursor.execute(query).fetchall()
    conn.close()
    return results


# MAIN MENU
if __name__ == "__main__":
    print("\n🎬 Welcome to the Movie Recommender!")
    print("Choose an option:")
    print("1. Recommend by Genre")
    print("2. Recommend by Rating Threshold")
    print("3. Recommend by Keyword")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        genre = input("Enter a genre (e.g., Action, Comedy, Horror): ")
        movies = recommend_by_genre(genre)

    elif choice == "2":
        try:
            rating = float(input("Enter minimum rating (e.g., 4.0): "))
            movies = recommend_by_rating(rating)
        except ValueError:
            print("❌ Invalid rating value.")
            movies = []

    elif choice == "3":
        keyword = input("Enter a keyword in the title (e.g., Avengers, Love): ")
        movies = recommend_by_keyword(keyword)

    else:
        print("❌ Invalid choice.")
        movies = []

    # Display results
    if movies:
        print("\n🎥 Recommended Movies:")
        for title, genres, avg_rating, count in movies:
            print(f"- {title} ({genres}) → ⭐ {avg_rating} from {count} ratings")
    else:
        print("\nNo matching movies found.")
