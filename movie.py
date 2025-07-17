import streamlit as st 
from tmdb import get_movie

st.title("Movie App 🎬")

# Fix background color
st.markdown("""
    <style>
    .stApp { background-color: #1A5276; }
    .movie-text { color: #FFFFFF !important; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

movie_name = st.text_input("Enter a movie name...")

if st.button("Fetch details..."):
    details = get_movie(movie_name)
    if details and 'Title' in details:
        year = details.get('Year', 'N/A')
        rating = details.get('imdbRating', 'N/A')
        rated = details.get('Rated', 'N/A')
        runtime = details.get('Runtime', 'N/A')
        plot = details.get('Plot', 'N/A')

        st.markdown(f"<p class='movie-text'>Title: {details['Title']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='movie-text'>Year: {year}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='movie-text'>Rating: {rating}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='movie-text'>Rated: {rated}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='movie-text'>Runtime: {runtime}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='movie-text'>Plot: {plot}</p>", unsafe_allow_html=True)
    else:
        st.error("Movie not found! Please check the title.")
