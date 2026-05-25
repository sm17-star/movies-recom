# Movie Recommendation System

## Description
This project implements a movie recommendation system based on content-based filtering. It uses movie metadata 'overview' and 'genres' to find similar movies. The core idea is to transform the textual features of movies into numerical representations using TF-IDF and then calculate cosine similarity between them to suggest movies.

## Features
- **Data Loading and Preprocessing**: Loads movie metadata, handles missing values, and processes text data.
- **Text Vectorization**: Utilizes TF-IDF to convert movie overview and genres into a numerical matrix.
- **Lemmatization**: Reduces words to their base or root form for better feature representation.
- **Similarity Calculation**: Employs cosine similarity to measure the likeness between movies.
- **Recommendation Engine**: Provides movie recommendations based on user input, returning a list of similar movie titles and another function that returns movie titles along with their similarity scores.
- **UI**:Streamlit webapp

## Installation
To run this notebook, you'll need to install the following Python libraries:

```bash
pip install pandas numpy scikit-learn nltk
```

Also download NLTK data:
```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```
To run streamlit application:
```bash
streamlit run app.py
```

## Usage
1.  **Load Data**: The `movies_metadata.csv` file 
2.  **Run Cells**: Execute the notebook cells sequentially to perform data loading, preprocessing, TF-IDF vectorization, and similarity matrix creation.
3.  **Recommendations**: Use the `recommend(movie_title, n)` or `recommend_and_scores(movie_title, n)` functions by passing a movie title and the number of recommendations desired.
4.  **Streamlit UI**:open url shown on terminal after run app.py ,select movie from drop down list ,click on `recommend and score` button to display similar movies along with their similarity score percent and matching keywords

## Data Source
The dataset used is `movies_metadata.csv`

## Technologies Used
- Python
- Pandas (for data manipulation)
- NumPy (for numerical operations)
- NLTK (for natural language processing tasks like tokenization, stop word removal, and lemmatization)
- Scikit-learn (for TF-IDF vectorization and cosine similarity calculation)
- Streamlit

## Saved Files
- `df.pkl`: df after preprocessing (used for storing the cleaned movie data).
- `indices.pkl`:Pandas Series mapping movie titles to their indices (used for quickly finding a movie's index).
- `movies.pkl`:TF-IDF vectorizer (used for storing the fitted TF-IDF model).
- `movies_matrix.pkl`:TF-IDF matrix (used for storing the numerical representation of movie features).
