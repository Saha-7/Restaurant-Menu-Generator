import streamlit as st

st.title("Restaurant name Generator")

st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Mexican", "American", "Thai","Chinese"))