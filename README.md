<div align="center">

# 🎬 Movie Recommendation System

### Discover your next favourite movie with Machine Learning

A **content-based recommendation engine** that suggests movies similar to the one you love, powered by **cosine similarity** and served through an interactive **Streamlit** web app.

<br>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movie-recommendation-system-dxz8fqsdfsbas5hjuwh2qu.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

[🚀 Live Demo](#-live-demo) · [🧠 How It Works](#-how-it-works) · [✨ Features](#-features) · [💻 Run Locally](#-run-locally) · [📈 Roadmap](#-roadmap)

</div>

---

## 🚀 Live Demo

| | |
|---|---|
| **🌐 Live Application** | 👉 **[Try the Movie Recommender](https://movie-recommendation-system-dxz8fqsdfsbas5hjuwh2qu.streamlit.app/)** |
| **📦 GitHub Repository** | [sonu3012/movie-recommendation-system](https://github.com/sonu3012/movie-recommendation-system) |

> Pick a movie, and the app instantly returns the **top 5 most similar movies**.

<!-- Add a screenshot or GIF of the app here -->
<!-- ![App Preview](./assets/preview.png) -->

---

## 📌 Overview

The **Movie Recommendation System** helps users discover movies similar to ones they already enjoy. It analyses movie metadata, measures how alike movies are, and surfaces the closest matches through a clean web interface.

### 🎯 Objectives

- 🎞️ Process and prepare movie information
- 📐 Calculate similarity between movies
- 🤖 Recommend similar movies accurately
- 🖥️ Provide an interactive web interface
- ☁️ Deploy the ML application online

---

## 🧠 How It Works

This project uses **Content-Based Filtering**: it compares the characteristics of movies and recommends the ones that are most alike.

### 🔄 Pipeline

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

### 📊 Step by Step

| Step | What happens |
|---|---|
| **1. Data Processing** | Movie data is cleaned and prepared using **Python** and **Pandas** |
| **2. Feature Representation** | Relevant movie information is converted into a **numerical representation** that can be compared mathematically |
| **3. Similarity Calculation** | **Cosine Similarity** measures how similar any two movies are |
| **4. Recommendation** | The most similar movies to the user's selection are returned |

### 🎬 Recommendation Flow

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

---

## ✨ Features

- 🎬 **Movie selection** from a list
- 🤖 **ML-powered** recommendations
- 🔎 **Content-based filtering**
- 📊 **Cosine similarity** engine
- ⚡ **Fast lookup** using a precomputed similarity matrix
- 🖥️ **Interactive Streamlit interface**
- ☁️ **Live online deployment**

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Web App** | Streamlit |
| **Development** | Jupyter Notebook |
| **Version Control** | Git, GitHub, Git LFS |
| **Deployment** | Streamlit Community Cloud |

---

## 📂 Project Structure

```text
Movie_Recommendation_Deployment/
│
├── app.py               # Streamlit application
├── movie_list.pkl       # Processed movie data
├── similarity.pkl       # Precomputed similarity matrix
├── requirements.txt     # Python dependencies
├── .gitignore
├── .gitattributes       # Git LFS configuration
└── README.md
```

---

## 💻 Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sonu3012/movie-recommendation-system.git
```

### 2️⃣ Open the project
```bash
cd movie-recommendation-system
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the app
```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

> 📦 **Note:** Large `.pkl` files are stored with **Git LFS**. Run `git lfs install` before cloning if the files don't download correctly.

### 📋 Requirements

```text
streamlit
pandas
numpy
scikit-learn
```

---

## 🌐 Deployment

The app is deployed on **Streamlit Community Cloud** and connected directly to this GitHub repository. Every update pushed to the repository can be reflected in the live application automatically.

---

## 📈 Roadmap

- [ ] 🖼️ Movie posters
- [ ] 📝 Movie descriptions
- [ ] 🎭 Genre filtering
- [ ] 🔍 Search functionality
- [ ] ⭐ Rating information
- [ ] 🎥 Movie trailers
- [ ] 👤 Personalized user recommendations
- [ ] 🧪 Improved recommendation algorithms
- [ ] 🚀 More advanced recommendation techniques

---

## 👨‍💻 Author

<div align="center">

**Sonu Kumar Ray**
B.Tech — Artificial Intelligence & Data Science

[![GitHub](https://img.shields.io/badge/GitHub-sonu3012-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sonu3012)

</div>

---

<div align="center">

### ⭐ If you found this project useful, give it a star!

**[Try the Live App](https://movie-recommendation-system-dxz8fqsdfsbas5hjuwh2qu.streamlit.app/)** · **[View Repository](https://github.com/sonu3012/movie-recommendation-system)**

</div>
