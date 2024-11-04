import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

user_animal_type = st.sidebar.selectbox("What is your pet?", ["Dog", "Cat", "Cow", "Hamster"])

if user_animal_type == "Cat":
    user_pet_color = st.sidebar.text_area(label="What is your pet's color?", max_chars=100)

if user_animal_type == "Dog":
    user_pet_color = st.sidebar.text_area(label="What is your pet's color?", max_chars=100)

if user_animal_type == "Cow":
    user_pet_color = st.sidebar.text_area(label="What is your pet's color?", max_chars=100)

if user_animal_type == "Hamster":
    user_pet_color = st.sidebar.text_area(label="What is your pet's color?", max_chars=100)

pet_name_amount = st.sidebar.text_input(label="How many pet names do you want?")

if pet_name_amount and user_pet_color:
    response = lch.generate_pet_name(user_animal_type, user_pet_color, pet_name_amount)
    st.text(response['pet_name'])