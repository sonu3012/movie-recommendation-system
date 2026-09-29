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
# CUSTOM CSS  (theme: velvet cinema + ticket stubs)
# Palette
#   Velvet   #170F14   page background
#   Curtain  #3A1420   glow / panels
#   Plum     #2A1822   surfaces
#   Marquee  #F0A93B   accent
#   Paper    #F3E6CB   ticket cards
#   Ink      #2B1B12   text on paper
# --------------------------------------------------

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,800&family=DM+Sans:wght@400;500;700&display=swap');

    :root {
        --velvet: #170F14;
        --curtain: #3A1420;
        --plum: #2A1822;
        --marquee: #F0A93B;
        --marquee-soft: #F7C873;
        --paper: #F3E6CB;
        --ink: #2B1B12;
        --text: #EFE4D2;
        --muted: #B9A99A;
        --line: rgba(240, 169, 59, 0.28);
    }

    /* ---------- Base ---------- */

    html, body, [class*="css"], .stApp {
        font-family: 'DM Sans', sans-serif;
        color: var(--text);
    }

    .stApp {
        background:
            radial-gradient(1100px 420px at 50% -120px, var(--curtain) 0%, transparent 70%),
            var(--velvet);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    p, li, label, span {
        color: var(--text);
    }

    hr {
        border: none;
        border-top: 1px dashed var(--line);
        margin: 2.5rem 0 1rem 0;
    }

    /* ---------- Header ---------- */

    .title {
        text-align: center;
        font-family: 'Fraunces', serif;
        font-size: 52px;
        font-weight: 800;
        letter-spacing: -0.5px;
        line-height: 1.1;
        color: var(--paper);
        text-shadow: 0 0 28px rgba(240, 169, 59, 0.35);
        margin-bottom: 12px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: var(--muted);
        max-width: 640px;
        margin: 0 auto 44px auto;
        line-height: 1.6;
    }

    .section-title {
        font-family: 'Fraunces', serif;
        font-size: 28px;
        font-weight: 600;
        color: var(--paper);
        margin-top: 34px;
        margin-bottom: 18px;
        padding-left: 14px;
        border-left: 4px solid var(--marquee);
    }

    /* ---------- Select box ---------- */

    [data-testid="stSelectbox"] label p {
        color: var(--muted);
        font-size: 15px;
        font-weight: 500;
    }

    div[data-baseweb="select"] > div {
        background-color: var(--plum);
        border: 1px solid var(--line);
        border-radius: 12px;
        min-height: 52px;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    div[data-baseweb="select"] > div:hover,
    div[data-baseweb="select"] > div:focus-within {
        border-color: var(--marquee);
        box-shadow: 0 0 0 3px rgba(240, 169, 59, 0.18);
    }

    div[data-baseweb="select"] * {
        color: var(--text);
    }

    div[data-baseweb="select"] svg {
        fill: var(--marquee);
    }

    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] [role="listbox"] {
        background-color: var(--plum);
    }

    div[data-baseweb="popover"] li {
        color: var(--text);
        background-color: var(--plum);
    }

    div[data-baseweb="popover"] li:hover,
    div[data-baseweb="popover"] li[aria-selected="true"] {
        background-color: var(--curtain);
        color: var(--marquee-soft);
    }

    /* ---------- Button ---------- */

    .stButton > button {
        background: linear-gradient(135deg, var(--marquee-soft), var(--marquee));
        color: var(--ink);
        font-family: 'DM Sans', sans-serif;
        font-size: 17px;
        font-weight: 700;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        box-shadow: 0 8px 22px rgba(240, 169, 59, 0.25);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .stButton > button p {
        color: var(--ink);
        font-weight: 700;
    }

    .stButton > button:hover {
        color: var(--ink);
        border: none;
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(240, 169, 59, 0.38);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    .stButton > button:focus-visible {
        outline: 3px solid var(--paper);
        outline-offset: 2px;
    }

    /* ---------- Recommendation cards (ticket stubs) ---------- */

    .movie-card {
        position: relative;
        padding: 22px 26px;
        border-radius: 12px;
        margin-bottom: 15px;
        text-align: center;
        min-height: 130px;
        display: flex;
        align-items: center;
        justify-content: center;
        background:
            radial-gradient(circle at 0% 50%, var(--velvet) 0 11px, transparent 12px),
            radial-gradient(circle at 100% 50%, var(--velvet) 0 11px, transparent 12px),
            var(--paper);
        box-shadow: 0 10px 26px rgba(0, 0, 0, 0.45);
        transition: transform 0.2s ease;
    }

    .movie-card::before {
        content: "";
        position: absolute;
        top: 10px;
        bottom: 10px;
        left: 22px;
        right: 22px;
        border: 1px dashed rgba(43, 27, 18, 0.28);
        border-radius: 8px;
        pointer-events: none;
    }

    .movie-card:hover {
        transform: translateY(-4px) rotate(-0.6deg);
    }

    .movie-title {
        position: relative;
        font-family: 'Fraunces', serif;
        font-size: 19px;
        font-weight: 800;
        line-height: 1.3;
        color: var(--ink);
    }

    /* ---------- Info boxes (technologies) ---------- */

    [data-testid="stAlert"] {
        background-color: var(--plum);
        border: 1px solid var(--line);
        border-left: 4px solid var(--marquee);
        border-radius: 12px;
    }

    [data-testid="stAlert"] * {
        color: var(--text);
        font-weight: 500;
    }

    /* ---------- About / How it works text ---------- */

    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        line-height: 1.75;
        font-size: 16px;
    }

    [data-testid="stMarkdownContainer"] ol {
        padding-left: 1.4rem;
    }

    [data-testid="stMarkdownContainer"] li::marker {
        color: var(--marquee);
        font-weight: 700;
    }

    /* ---------- Footer ---------- */

    [data-testid="stCaptionContainer"] {
        text-align: center;
    }

    [data-testid="stCaptionContainer"] p {
        color: var(--muted);
        font-size: 14px;
    }

    /* ---------- Small screens ---------- */

    @media (max-width: 640px) {
        .title { font-size: 34px; }
        .subtitle { font-size: 16px; }
        .section-title { font-size: 23px; }
    }

    @media (prefers-reduced-motion: reduce) {
        .movie-card, .stButton > button { transition: none; }
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

