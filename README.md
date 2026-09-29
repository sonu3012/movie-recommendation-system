# 🎬 Movie Recommendation System

A Machine Learning based **Movie Recommendation System** that recommends movies similar to a user's selected movie using **content-based filtering and cosine similarity**.

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-recommendation-system-dxz8fqsdfsbas5hjuwh2qu.streamlit.app/)

**Live Application:**
https://movie-recommendation-system-dxz8fqsdfsbas5hjuwh2qu.streamlit.app/

## 📌 Project Overview

The Movie Recommendation System helps users discover movies similar to a movie they already like.

The system uses movie metadata to calculate similarity between movies. When a user selects a movie, the recommendation engine identifies the most similar movies and displays the top 5 recommendations.

## 🎯 Objective

The main objective of this project is to build and deploy a practical Machine Learning recommendation system that can:

* Process movie information
* Calculate similarity between movies
* Recommend similar movies
* Provide an interactive web interface
* Deploy the ML application online

## 🧠 Recommendation Approach

This project uses **Content-Based Filtering**.

The system compares the characteristics/features associated with movies and calculates their similarity.

The recommendation process is:

```text
Movie Dataset
     ↓
Data Preprocessing
     ↓
Feature Processing
     ↓
Feature Vectors
     ↓
Cosine Similarity
     ↓
Similarity Matrix
     ↓
Top Similar Movies
     ↓
Streamlit Application
```

## 📊 How It Works

### 1. Data Processing

Movie data is processed using Python and Pandas.

### 2. Feature Representation

Relevant movie information is converted into a representation that can be compared mathematically.

### 3. Similarity Calculation

The system uses **Cosine Similarity** to determine how similar two movies are.

### 4. Recommendation

When a user selects a movie:

```text
Selected Movie
      ↓
Find Movie Index
      ↓
Retrieve Similarity Scores
      ↓
Sort Similar Movies
      ↓
Select Top 5
      ↓
Display Recommendations
```

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Jupyter Notebook
* Git
* GitHub

## ✨ Features

* 🎬 Movie selection
* 🤖 Machine Learning based recommendations
* 🔎 Content-based filtering
* 📊 Cosine similarity
* ⚡ Fast recommendation lookup
* 🖥 Interactive Streamlit interface
* ☁️ Online deployment

## 📂 Project Structure

```text
Movie_Recommendation_Deployment/
│
├── app.py
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md
```

## 💻 Run the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/sonu3012/movie-recommendation-system.git
```

### Step 2: Open the project

```bash
cd movie-recommendation-system
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Streamlit

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 📦 Requirements

The project uses the following Python packages:

```text
streamlit
pandas
numpy
scikit-learn
```

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud** and connected to the GitHub repository.

Every update pushed to the repository can be reflected in the deployed application.

## 🔗 Project Links

**GitHub:**
https://github.com/sonu3012/movie-recommendation-system

**Live Demo:**
https://movie-recommendation-system-dxz8fqsdfsbas5hjuwh2qu.streamlit.app/

## 📈 Future Improvements

Possible future improvements include:

* Movie posters
* Movie descriptions
* Genre filtering
* Search functionality
* Rating information
* Movie trailers
* Personalized user recommendations
* Improved recommendation algorithms
* More advanced recommendation techniques

## 👨‍💻 Author

**Sonu Kumar Ray**

B.Tech – Artificial Intelligence & Data Science

GitHub: https://github.com/sonu3012

## ⭐ Project

If you find this project useful, feel free to explore the repository and try the live application.


📊 How It Works
1. Data Processing

Movie data is processed using Python and Pandas.

2. Feature Representation

Relevant movie information is converted into a numerical representation that can be compared mathematically.

3. Similarity Calculation

The system uses Cosine Similarity to determine how similar two movies are.

4. Recommendation

When a user selects a movie:

Selected Movie
      ↓
Find Movie Index
      ↓
Retrieve Similarity Scores
      ↓
Sort Similar Movies
      ↓
Select Top 5
      ↓
Display Recommendations
✨ Features
🎬 Movie selection
🤖 Machine Learning based recommendations
🔎 Content-based filtering
📊 Cosine similarity
⚡ Fast recommendation lookup
🖥 Interactive Streamlit interface
☁️ Online deployment
🛠 Technologies Used
Python
Pandas
NumPy
Scikit-learn
Streamlit
Jupyter Notebook
Git
GitHub
Git LFS


📂 Project Structure
Movie_Recommendation_Deployment/
│
├── app.py
├── movie_list.pkl
├── similarity.pkl
├── requirements.txt
├── .gitignore
├── .gitattributes
└── README.md


