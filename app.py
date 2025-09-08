import streamlit as st
from utils.recommendation import load_data, recommend_movies

# ----------------- Load Dataset -----------------
st.set_page_config(page_title="AI Movie Recommendation System", layout="centered")
st.title("🎬 AI Movie Recommendation System")
st.write("Enter any keyword (genre, actor, director, movie name, year, or even a description) and get accurate movie recommendations!")

# Load movies once
@st.cache_resource
def load_all():
    return load_data()

movies = load_all()

# ----------------- User Input -----------------
user_input = st.text_input("Enter keyword:", "")

if st.button("Get Recommendations"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a keyword first!")
    else:
        with st.spinner("🔍 Finding best matches..."):
            recommended = recommend_movies(user_input, movies, top_n=5)

        if recommended.empty:
            st.info("No movies found matching your keyword.")
        else:
            st.success(f"🎯 Recommended Movies for **'{user_input}'**:")
            
            for _, row in recommended.iterrows():
                col1, col2 = st.columns([1, 3])
                with col1:
                    if row['Poster_Link'] != '':
                        st.image(row['Poster_Link'], width=150)
                with col2:
                    st.markdown(f"### {row['Series_Title'].title()} ({row['Released_Year']})")
                    st.write(f"**Genre:** {row['Genre'].title()}")
                    st.write(f"**Director:** {row['Director'].title()}")
                    st.write(f"**IMDB Rating:** ⭐ {row['IMDB_Rating']}")
                st.write("---")
