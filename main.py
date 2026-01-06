import streamlit as st
from generator import generator_func

st.sidebar.title("Choose your writing style!")

tone = "Thriller, Comedy, Drama, Romance, Horror, Fantasy, Science Fiction, Mystery, Adventure, Tragedy, Action Thriller, Psychological Thriller, Dark Comedy, Satire, Paranormal Romance, Historical Fiction, Dystopian, Utopian, Cyberpunk, Steampunk, Space Opera, Gothic Horror, Supernatural Mystery, Crime Fiction, Political Drama, Slice of Life, Coming-of-Age, Epic Fantasy, Magical Realism, Post-Apocalyptic, Techno-Thriller, Urban Fantasy, Mythological Retelling".split(",")

tone_of_story = st.sidebar.selectbox("Choose your writing tone", options=tone)

st.title("Daily Story Writer!")

# ---- FORM START ----
with st.form("story_form"):
    story_input = st.text_area("Write a story", height=200)
    submitted = st.form_submit_button("Generate Story")

# ---- FORM END ----

if submitted:
    st.write(generator_func(story_input, tone_of_story))
