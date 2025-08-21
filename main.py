import streamlit as st
import langChainHelper

st.title("Restaurant name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Mexican", "American", "Thai","Chinese"))



if cuisine:
    response = langChainHelper.generate_restaurant_name_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-", item)