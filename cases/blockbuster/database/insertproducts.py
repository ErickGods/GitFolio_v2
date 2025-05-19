import requests
import pyodbc

API_KEY = 'YOUR_TMDB_API_KEY'
URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=en-US&page=1'

response = requests.get(URL)
movies = response.json().get('results', [])

# SQL Server connection
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=YOUR_SERVER;DATABASE=YOUR_DB;UID=USER;PWD=PWD')
cursor = conn.cursor()

for movie in movies:
    title = movie['title']
    genre = 'Unknown'  # you can fetch genres from another endpoint
    duration = 120  # placeholder (real duration needs separate call)
    rating = 'PG-13'  # placeholder or use certification endpoint
    year = movie['release_date'][:4]
    stock = 10
    sale_price = 19.90
    rental_price = (sale_price/3)
    is_active = 1

    cursor.execute("""
        INSERT INTO BB_Products (Title, Type, Genre, DurationMinutes, Rating,
                                 ReleaseYear, Stock, SalePrice, RentalPrice, IsActive)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (title, 'Movie', genre, duration, rating, int(year), stock, sale_price, rental_price, is_active))

conn.commit()
cursor.close()
conn.close()
