import pandas as pd

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print(movies.head())
print(ratings.head())

print(movies.shape)
print(ratings.shape)

print(movies.info())
print(ratings.info())

print(movies.isnull().sum())
print(ratings.isnull().sum())

print(ratings['userId'].nunique())
print(ratings["rating"].mean())

df = pd.merge(movies, ratings, on="movieId")
print("\nTop 10 most rated movies ")


top_movies = df.groupby("title")['rating'].count().sort_values(ascending=False).head(10)
print(top_movies)

movie_ratings = df.groupby('title')['rating'].agg(['mean', 'count'])
top_rated = movie_ratings[movie_ratings['count'] >= 50]
top_rated = top_rated.sort_values('mean', ascending=False).head(10)
print(top_rated)

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

movie_matrix = df.pivot_table(index='userId', columns='title', values='rating')
movie_matrix = movie_matrix.fillna(0)
print(movie_matrix.shape)

movie_similarity = cosine_similarity(movie_matrix.T)
similarity_df = pd.DataFrame(movie_similarity, index=movie_matrix.columns, columns=movie_matrix.columns)
print(similarity_df.shape)

def recommend_movies(movie_title, n=5):
    if movie_title not in similarity_df.columns:
        return "Movie not found!"
    similar_movies = similarity_df[movie_title].sort_values(ascending=False)[1:n+1]
    return similar_movies

print("\n=== Movies similar to Toy Story ===")
print(recommend_movies("Toy Story (1995)"))

print("\n=== Movies similar to Matrix ===")
print(recommend_movies("Matrix, The (1999)"))