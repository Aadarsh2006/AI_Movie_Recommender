import pandas as pd
import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import os

# Load embedding model (semantic meaning)
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text


def load_data():
    path = os.path.join("data", "movies.csv")   # relative path
    movies = pd.read_csv(path)

    # Clean key columns
    for col in ['Series_Title','Genre','Director','Star1','Star2','Star3','Star4','Overview']:
        movies[col] = movies[col].fillna('').apply(clean_text)

    # Combine stars
    movies['Stars'] = movies['Star1'] + ' ' + movies['Star2'] + ' ' + movies['Star3'] + ' ' + movies['Star4']

    # Precompute embeddings for semantic matching (title + overview)
    movies['semantic_text'] = movies['Series_Title'] + " " + movies['Overview']
    movies['embedding'] = list(model.encode(movies['semantic_text'].tolist(), convert_to_numpy=True))
    
    return movies

def recommend_movies(user_input, movies, top_n=5):
    user_input = clean_text(user_input)

    # Split into keywords
    keywords = user_input.split()

    # Compute semantic embedding of user input
    user_emb = model.encode([user_input], convert_to_numpy=True)

    # Similarity scores
    semantic_scores = cosine_similarity(user_emb, np.vstack(movies['embedding']))[0]

    # Structured feature matching (boost)
    title_match = movies['Series_Title'].apply(lambda x: any(kw in x for kw in keywords)).astype(int)
    genre_match = movies['Genre'].apply(lambda x: any(kw in x for kw in keywords)).astype(int)
    director_match = movies['Director'].apply(lambda x: any(kw in x for kw in keywords)).astype(int)
    stars_match = movies['Stars'].apply(lambda x: any(kw in x for kw in keywords)).astype(int)

    # Weighted score
    final_score = (5*title_match + 4*genre_match + 3*director_match +
                   2*stars_match + 1*semantic_scores)

    # Get top N movies
    top_indices = final_score.argsort()[-top_n:][::-1]
    recommended = movies.iloc[top_indices][['Series_Title','Released_Year','Genre','Director','IMDB_Rating','Poster_Link']]

    return recommended

