import pickle
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

# Load files
indices = pickle.load(open("indices.pkl", "rb"))
df = pd.read_pickle("df.pkl")


movies_vectorizer = pickle.load(open("movies.pkl", "rb"))
movies_matrix = pickle.load(open("movies_matrix.pkl", "rb"))
bow_vectorizer = pickle.load(open("movies_bow.pkl", "rb"))
bow_matrix = pickle.load(open("movies_matrix_bow.pkl", "rb"))




def recommend_and_scores(movie: str, method: str , n: int = 10):
    if movie not in indices:
        return pd.DataFrame()

    if method == "bag_of_words":
        vectorizer, movies_matrix_selected = bow_vectorizer, bow_matrix
    else:
        vectorizer = movies_vectorizer
        movies_matrix_selected = movies_matrix

    idx = indices[movie]

    # Compute similarity scores
    similarity_scores = cosine_similarity(
        movies_matrix_selected[idx],
        movies_matrix_selected,
    ).flatten()

    # Get top matches excluding the movie itself
    similar_indices = similarity_scores.argsort()[::-1][1:n + 1]

    # Create a DataFrame with titles and their respective scores
    recommendations = pd.DataFrame(
        {
            "title": df["title"].iloc[similar_indices].values,
            "similarity_score": similarity_scores[similar_indices] * 100,
        }
    )

    return recommendations, vectorizer, movies_matrix_selected


# Explain keywords

def explain_similarity(movie_a: str, movie_b: str, vectorizer, movies_matrix, n: int = 5):
    idx1 = indices[movie_a]
    idx2 = indices[movie_b]

    vec1 = movies_matrix[idx1].toarray().flatten()
    vec2 = movies_matrix[idx2].toarray().flatten()

    # Element-wise multiplication to get highest similarity keywords
    similarity = vec1 * vec2
    top_indices = similarity.argsort()[::-1][:n]
    feature_names = vectorizer.get_feature_names_out()

    return [feature_names[i] for i in top_indices]


# Sidebar to explain project flow
st.sidebar.title("Project Flow")
st.sidebar.markdown(
    """
    1. Load movie metadata from the saved dataframe.
    2. Choose the NLP method: TF-IDF or Bag of Words.
    3. Convert movie text into a numeric matrix.
    4. Compute cosine similarity between movies.
    5. Show the most similar movie recommendations.
    """
)

st.sidebar.markdown("---")
st.sidebar.subheader("NLP Technique")
st.sidebar.markdown(
    """
    **TF-IDF**
    - Measures how important a word is in one movie description compared with the whole dataset.
    - Formula: TF × IDF
    - TF(Term Frequency) = word frequency in a movie description  or (number of times term appears in a document/total no of terms in document)
    - IDF(Inverse Document Frequency) = log(total movies / movies containing the word) or total number of documents in dataset/number of documents containing term

    **Bag of Words**
    - Counts how many times each word appears in a movie description.
    - It does not weight rare or important words differently.
    - Converts text (sentence, paragraph, or document) into a collection of words
    """
)

st.sidebar.markdown("---")
st.sidebar.subheader("NLP Method")

method = st.sidebar.selectbox(
    "Choose NLP method",
    options=["tfidf", "bag_of_words"],
    index=0,
    format_func=lambda method_name: "TF-IDF" if method_name == "tfidf" else "Bag of Words",
)

# Title
st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar movie recommendations.")

movie_list = df["title"].values
selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend and score"):
    recommendations, vectorizer, movies_matrix = recommend_and_scores(
        selected_movie,
        method=method,
        n=5,
    )

    st.subheader("Recommended Movies")

    for _, row in recommendations.iterrows():
        st.write(f"🎬 {row['title']}")
        st.write(f"{row['similarity_score']:.2f}% match")

        keywords = explain_similarity(
            selected_movie,
            row["title"],
            vectorizer,
            movies_matrix,
        )

        with st.expander("Why recommended? Similar keywords"):
            st.write(", ".join(keywords))

        st.divider()