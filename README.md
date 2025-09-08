# 🎬 AI Movie Recommendation System

An **AI-powered movie recommendation system** built using **Content-Based Filtering + Semantic Search**.  
Users can enter any keyword (genre, movie name, director, actor, year, or even a short description), and the system recommends the most relevant movies with posters, ratings, and details.

🚀 Live Demo: [Click Here](https://your-username-movie-recommender.streamlit.app)  


---

## ✨ Features
- 🔎 **Smart Search**: Search by *genre, actor, director, year, or description*.
- 🧠 **AI Semantic Understanding**: Uses `sentence-transformers` for meaning-based matching.
- 🎭 **Content-Based Filtering**: Matches movies based on similarity of attributes.
- 🎨 **Clean UI**: Built with Streamlit, showing posters + IMDB details.
- ⚡ **Fast & Lightweight**: Dataset pre-processed and cached for quick results.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- [Streamlit] – Web app framework
- [Pandas] – Data handling
- [Scikit-learn] – Similarity computation
- [Sentence-Transformers] – Semantic embeddings
- **Dataset**: IMDb Movies Dataset (CSV with metadata like title, year, genre, director, stars, ratings)

---

## 📂 Project Structure
AI-movie-recommendation/
│── app.py # Streamlit app (UI + display)
│── utils/
│ └── recommendation.py # Core recommendation logic
│── data/
│ └── movies.csv # Movie dataset (IMDb metadata)
│── requirements.txt # Python dependencies
│── README.md # Project documentation


---


## Install dependencies:
pip install -r requirements.txt

---

## 🌐 Deployment :
This app is deployed on Streamlit Cloud.

---

## 📌 Future Improvements

- 🎥 Add trailer links (YouTube API).
- 🎭 Add collaborative filtering (user-based recommendations).
- 🌍 Expand dataset to include more global movies.
- 📱 Build mobile-friendly version.

---

## 👨‍💻 Author
- Aadarsh Jha
- Linkedin : www.linkedin.com/in/aadarshjha09
