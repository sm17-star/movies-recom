import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.feature_extraction.text import TfidfVectorizer

# Load files
movies_matrix = pickle.load(open('movies_matrix.pkl','rb'))
indices = pickle.load(open('indices.pkl','rb'))
df = pd.read_pickle('df.pkl')
movies = pickle.load(open('movies.pkl','rb'))


def recommend_and_scores(movie, n=5):
    if movie not in indices:
        return pd.DataFrame()

    idx = indices[movie]

    # Compute similarity scores
    similarity_scores = cosine_similarity(
        movies_matrix[idx],
        movies_matrix
    ).flatten()

    # Get top matches excluding the movie itself
    similar_indices = similarity_scores.argsort()[::-1][1:n+1]

    # Create a DataFrame with titles and their respective scores
    recommendations = pd.DataFrame({
        'title': df['title'].iloc[similar_indices].values,
        'similarity_score': similarity_scores[similar_indices]*100
    })

    return recommendations


#Explain keywords 

feature_names = movies.get_feature_names_out()

def explain_similarity(m1,m2,n=5):
    idx1 = indices[m1]
    idx2 = indices[m2]
    vec1 = movies_matrix[idx1].toarray().flatten()# [0.2,0.9,0.7,0.6.....]
    vec2 = movies_matrix[idx2].toarray().flatten() # [0.7,0.1,0.9,0.5,0.4,0.2......]
    
    #elemnent wise multiplication to get highest similarity keywords
    similarity=vec1*vec2
    top_indices = similarity.argsort()[::-1][:n]
 
    words=[]
    for i in top_indices:
        words.append(feature_names[i])
    return words



# Title
st.title("🎬 Movie Recommendation System")

# Subtitle
st.write("Select a movie and get similar movie recommendations.")

# Dropdown
movie_list = df['title'].values

selected_movie = st.selectbox(
    "Choose a movie",
    movie_list
)

# Button
if st.button("Recommend and score"):

    recommendations = recommend_and_scores(selected_movie)

    st.subheader("Recommended Movies")

    for i,rows in recommendations.iterrows():
        st.write(f"🎬 {rows['title']}")
        st.write(f"{rows['similarity_score']:.2f}%  match")

        keywords=explain_similarity(selected_movie,rows['title'])
     
        with st.expander("Why recommended? there are similar keys"):
                st.write(" , ".join(keywords))
        
        st.divider()