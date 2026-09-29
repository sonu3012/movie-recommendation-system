import streamlit as st
import pickle


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


# --------------------------------------------------
# Load Saved Movie Data and Similarity Matrix
# --------------------------------------------------

@st.cache_resource
def load_data():

    movies = pickle.load(open("movie_list.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))

    return movies, similarity


movies, similarity = load_data()


# --------------------------------------------------
# Recommendation Function
# --------------------------------------------------

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


# --------------------------------------------------
# User Interface
# --------------------------------------------------

st.title("🎬 Movie Recommendation System")

st.write(
    "Select a movie and discover movies similar to it."
)


# --------------------------------------------------
# Movie Selection
# --------------------------------------------------

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "🎥 Select a movie",
    movie_list
)


# --------------------------------------------------
# Recommendation Button
# --------------------------------------------------

if st.button("🍿 Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader("🎬 Recommended Movies")

    for movie in recommendations:

        st.write("👉", movie)

        