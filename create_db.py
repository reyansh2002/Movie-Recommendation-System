import pandas as pd
import sqlite3

# Load data
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Clean genres (replace '|' with ', ')
movies['genres'] = movies['genres'].str.replace('|', ', ')

# Connect to SQLite
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Drop old tables
cursor.execute("DROP TABLE IF EXISTS movies")
cursor.execute("DROP TABLE IF EXISTS ratings")

# Create movies table
cursor.execute("""
CREATE TABLE movies (
    movieId INTEGER PRIMARY KEY,
    title TEXT,
    genres TEXT
)
""")

# Create ratings table
cursor.execute("""
CREATE TABLE ratings (
    userId INTEGER,
    movieId INTEGER,
    rating REAL,
    FOREIGN KEY(movieId) REFERENCES movies(movieId)
)
""")

# Load data
movies.to_sql('movies', conn, if_exists='append', index=False)
ratings.to_sql('ratings', conn, if_exists='append', index=False)

# Close
print("✅ Database created with movies and ratings.")
conn.close()
