# Movie Recommendation System

## Description
<<<<<<< HEAD
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
=======
This project implements a movie recommendation system based on content-based filtering. It uses movie metadata 'overview' and 'genres' to find similar movies. The core idea is to transform the textual features of movies into numerical representations using TF-IDF and Count Vectorizer and then calculate cosine similarity between them to suggest movies.


## Process flow
- **Data Upload**: Load the movie dataset into a pandas DataFrame so the metadata and text are ready for analysis.
- **Text Cleaning/preprocess**: Handle missing values,convert the text to lowercase, remove punctuation, and normalize the movie descriptions.
- **Tokenization and Stopword Removal**: Split the text into words and remove common stopwords that do not add much meaning.
- **Lemmatization**: Reduce words to their root form so similar terms are represented consistently 
- **Feature Creation**: Combine the cleaned movie text into a single feature column for each movie.
- **Vectorization**: Convert the processed text into numerical vectors using TF-IDF or Bag-of-Words.
- **Similarity Calculation**: Compute cosine similarity between the selected movie and all other movies to measure likeness between movies.
- **Recommendation Selection**: Rank the movies by similarity score and select the top matches. Lets the user choose the NLP approach TF-IDF OR Bag of Words from the Streamlit UI before generating recommendations.
- **Output**: Return the recommended movie titles along with their similarity scores and matching keywords.
- **UI Display**: Show the final recommendations in the Streamlit app for the user.

 **Install Dependencies**:
    create virtual environment
    Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
or
```bash
pip install pandas scikit-learn nltk streamlit
>>>>>>> 108f257 (update)
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

<<<<<<< HEAD
## Usage
1.  **Load Data**: The `movies_metadata.csv` file 
2.  **Run Cells**: Execute the notebook cells sequentially to perform data loading, preprocessing, TF-IDF vectorization, and similarity matrix creation.
3.  **Recommendations**: Use the `recommend(movie_title, n)` or `recommend_and_scores(movie_title, n)` functions by passing a movie title and the number of recommendations desired.
4.  **Streamlit UI**:open url shown on terminal after run app.py ,select movie from drop down list ,click on `recommend and score` button to display similar movies along with their similarity score percent and matching keywords

## Data Source
The dataset used is `movies_metadata.csv`
=======

## Usage
1. **Load Data**: Load movies dataset
2. **Run Cells**: Execute the notebook cells sequentially to perform data loading, preprocessing, and similarity matrix creation.
3. **Recommendations**: Use the `recommend(movie_title, n)` or `recommend_and_scores(movie_title, n)` functions by passing a movie title and the number of recommendations desired.
4. **Streamlit UI**: Open the URL shown in the terminal after running `app.py`, then select a movie, choose the NLP method (`TF-IDF` or `Bag of Words`) from sidebar, and click the `Recommend and score` button to display similar movies along with their similarity score percent and matching keywords.

## TF-IDF and Bag of Words

### TF-IDF 
TF-IDF is a way to turn words into numbers so a computer can compare movie descriptions.
- Formula: TF × IDF
    - **TF(Term Frequency)** = word frequency in a movie description  or (number of times term appears in a document/total no of terms in document)
    - **IDF(Inverse Document Frequency)** = log(total movies / movies containing the word) or total number of documents in dataset/number of documents containing term

- It gives more weight to distinctive words.
- It reduces the effect of common words.

- So a word gets a high TF-IDF score when it appears many times in one movie description but is not common in the whole dataset. This helps the system focus on words that are more meaningful for that movie.

### Bag of Words
- Bag of Words also turns text into numbers, but it only counts words. It does not check whether a word is common or rare across the whole dataset.

- In the current implementation, both methods follow the same pipeline: movie text is converted into a numeric matrix and cosine similarity is used to find the closest movies. The only difference is the vectorizer used in the text-to-number step. `TfidfVectorizer` gives words a weighted importance, whereas `CountVectorizer` uses raw word counts.
>>>>>>> 108f257 (update)

## Technologies Used
- Python
- Pandas (for data manipulation)
<<<<<<< HEAD
- NumPy (for numerical operations)
- NLTK (for natural language processing tasks like tokenization, stop word removal, and lemmatization)
- Scikit-learn (for TF-IDF vectorization and cosine similarity calculation)
=======
- NLTK (for natural language processing tasks like tokenization, stop word removal, and lemmatization)
- Scikit-learn (for TF-IDF vectorization , Count Vectorizer and cosine similarity calculation)
>>>>>>> 108f257 (update)
- Streamlit

## Saved Files
- `df.pkl`: df after preprocessing (used for storing the cleaned movie data).
- `indices.pkl`:Pandas Series mapping movie titles to their indices (used for quickly finding a movie's index).
- `movies.pkl`:TF-IDF vectorizer (used for storing the fitted TF-IDF model).
- `movies_matrix.pkl`:TF-IDF matrix (used for storing the numerical representation of movie features).
<<<<<<< HEAD
=======
- `movies_matrix_bow.pkl`: Bag-of-Words matrix (used for storing the word-count representation of movie text for similarity matching).
- `movies_bow.pkl`: Bag-of-Words vectorizer (used for storing the fitted word-count model for movie descriptions).
>>>>>>> 108f257 (update)
