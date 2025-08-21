import streamlit as st

st.title("Restaurant name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Italian", "Mexican", "American", "Thai","Chinese"))

def generate_restaurant_name_items(cuisine):
    return{
        'restaurant_name': 'Curry Delight',
        'menu_items': 'Samosa, Butter Chicken',
    }

if cuisine:
    response = generate_restaurant_name_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-", item)