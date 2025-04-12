
# 🎬 Movie Recommendation System

This is a simple and interactive **Movie Recommendation System** built using **Streamlit** for the front-end interface and **SQLite** for the backend database. The app allows users to search for movies based on genre, rating threshold, or keywords in the title.

---

## 📁 Project Structure

```
├── app.py              # Streamlit app for user interaction
├── recommend.py        # Command-line based recommendation script
├── create_db.py        # Script to generate the SQLite database from CSV files
├── movies.csv          # Dataset containing movie details
├── ratings.csv         # Dataset containing user ratings
├── movies.db           # SQLite database with movies and ratings
```

---

## ⚙️ Features

- 🔍 **Search by Genre** – Find top-rated movies in your favorite genre.
- ⭐ **Filter by Rating** – Discover highly-rated films above a given threshold.
- 🔑 **Search by Keyword** – Look for movies using words in their titles.
- 📊 **Minimum 5 Ratings Filter** – Ensures reliability by filtering out movies with very few reviews.

---

## 🛠️ Setup Instructions

1. **Install Dependencies**  
   Ensure Python is installed. Then run:
   ```bash
   pip install streamlit pandas
   ```

2. **Prepare the Database**
   - Place `movies.csv` and `ratings.csv` in the same directory.
   - Run the script to generate the database:
     ```bash
     python create_db.py
     ```

3. **Launch the Streamlit App**
   ```bash
   streamlit run app.py
   ```

4. **Or Use CLI Recommender**
   ```bash
   python recommend.py
   ```

---

## 📊 Sample Datasets

- `movies.csv`: Contains movie ID, title, and genres.
- `ratings.csv`: Contains user ratings for each movie.

---

## 📦 Requirements

- Python 3.7+
- `streamlit`
- `pandas`
- `sqlite3` (comes with Python)

---

## 🧠 Behind the Scenes

The app uses SQL queries to:
- Join the `movies` and `ratings` tables
- Calculate average ratings and rating counts
- Filter results based on user inputs

---

## 📸 Screenshot

### Genre
![image alt](https://github.com/reyansh2002/Movie-Recommendation-System/blob/main/output/Streamlit%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%20Beta%2012-04-2025%2020_04_10.png)


### Rating
![image alt](https://github.com/reyansh2002/Movie-Recommendation-System/blob/main/output/Streamlit%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%20Beta%2012-04-2025%2020_04_47.png)


### keyword
![image alt](https://github.com/reyansh2002/Movie-Recommendation-System/blob/main/output/Streamlit%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%20Beta%2012-04-2025%2020_05_25.png)

---

