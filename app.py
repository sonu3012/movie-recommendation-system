import streamlit as st
import pickle

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 2rem;
    }

    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        margin-bottom: 40px;
    }

    .movie-card {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(128,128,128,0.3);
        margin-bottom: 15px;
        text-align: center;
        min-height: 100px;
    }

    .movie-title {
        font-size: 20px;
        font-weight: bold;
    }

    .section-title {
        font-size: 28px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_resource
def load_data():

    movies = pickle.load(
        open("movie_list.pkl", "rb")
    )

    similarity = pickle.load(
        open("similarity.pkl", "rb")
    )

    return movies, similarity


movies, similarity = load_data()

# --------------------------------------------------
# RECOMMENDATION FUNCTION
# --------------------------------------------------

def recommend(movie):

    movie_index = movies[
        movies["title"] == movie
    ].index[0]

    distances = sorted(
        list(
            enumerate(
                similarity[movie_index]
            )
        ),
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
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Discover movies similar to your favorite films using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# MOVIE SELECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">🎥 Choose a Movie</div>',
    unsafe_allow_html=True
)

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

# --------------------------------------------------
# RECOMMEND BUTTON
# --------------------------------------------------

if st.button(
    "🍿 Recommend Movies",
    use_container_width=True
):

    recommendations = recommend(
        selected_movie
    )

    st.markdown(
        '<div class="section-title">'
        '🎬 Recommended Movies'
        '</div>',
        unsafe_allow_html=True
    )

    columns = st.columns(5)

    for i, movie in enumerate(recommendations):

        with columns[i]:

            st.markdown(
                f"""
                <div class="movie-card">

                <div class="movie-title">
                🎬 {movie}
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

# --------------------------------------------------
# ABOUT PROJECT
# --------------------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">'
    '📌 About This Project'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    """
    This project is a content-based Movie Recommendation System
    built using Python and Machine Learning.

    The system analyzes movie information and calculates similarity
    between movies using cosine similarity.

    When a user selects a movie, the system recommends five movies
    that are most similar to the selected movie.
    """
)

# --------------------------------------------------
# TECHNOLOGIES
# --------------------------------------------------

st.markdown(
    '<div class="section-title">'
    '🛠 Technologies Used'
    '</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🐍 Python")

with col2:
    st.info("🐼 Pandas")

with col3:
    st.info("🤖 Scikit-learn")

with col4:
    st.info("🎈 Streamlit")

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">'
    '⚙️ How It Works'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    """
    1. Movie data is collected and processed.
    2. Important movie features are combined.
    3. Features are converted into numerical vectors.
    4. Cosine similarity is calculated between movies.
    5. Similarity scores are stored.
    6. When the user selects a movie, the system finds the
       most similar movies.
    7. The top 5 movies are displayed.
    """
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "🎬 Movie Recommendation System | "
    "Built with Python, Machine Learning & Streamlit"
)

