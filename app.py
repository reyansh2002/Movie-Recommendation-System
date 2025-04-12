import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = 'movies.db'

# Query helper
def run_query(query):
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(query, conn)

st.title("🎬 Movie Recommendation System")
st.subheader("Powered by SQLite + Streamlit")

option = st.sidebar.radio("Choose a search option:", [
    "🔍 Search by Genre",
    "⭐ Filter by Rating",
    "🔑 Search by Keyword"
])

if option == "🔍 Search by Genre":
    genre = st.text_input("Enter Genre (e.g., Action, Comedy, Horror):", "Action")
    if st.button("Get Recommendations"):
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
        results = run_query(query)
        st.dataframe(results)

elif option == "⭐ Filter by Rating":
    rating = st.slider("Select minimum average rating:", 0.0, 5.0, 4.0)
    if st.button("Get High Rated Movies"):
        query = f"""
        SELECT m.title, m.genres,
               ROUND(AVG(r.rating), 2) AS avg_rating,
               COUNT(r.rating) AS num_ratings
        FROM movies m
        JOIN ratings r ON m.movieId = r.movieId
        GROUP BY m.movieId
        HAVING avg_rating >= {rating} AND num_ratings >= 5
        ORDER BY avg_rating DESC, num_ratings DESC
        LIMIT 20
        """
        results = run_query(query)
        st.dataframe(results)

elif option == "🔑 Search by Keyword":
    keyword = st.text_input("Enter a word from the movie title:", "Love")
    if st.button("Search"):
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
        results = run_query(query)
        st.dataframe(results)
