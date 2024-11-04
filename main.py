import langchain_helper as lch
import streamlit as st

#website tilte
st.title("Pet Name Generator")

#sidebar inputfields 

#user inputs the animal type
user_animal_type = st.sidebar.selectbox("What is your pet?", ["Dog", "Cat", "Cow", "Hamster"])

#user inputs the pet color based on the animal type
if user_animal_type == "Cat":
    user_pet_color = st.sidebar.text_area(label="What is your pet's color?", max_chars=100)

if user_animal_type == "Dog":
    user_pet_color = st.sidebar.text_area(label="What is your pet's color?", max_chars=100)

if user_animal_type == "Cow":
    user_pet_color = st.sidebar.text_area(label="What is your pet's color?", max_chars=100)

if user_animal_type == "Hamster":
    user_pet_color = st.sidebar.text_area(label="What is your pet's color?", max_chars=100)

#user inputs the amount of names to be generated
pet_name_amount = st.sidebar.text_input(label="How many pet names do you want?")

#showing output if user inputs the amount of names to be generated
if pet_name_amount:
    response = lch.generate_pet_name(user_animal_type, user_pet_color, pet_name_amount) #calling the function
    st.text(response['pet_name']) #showing the pet names

    #footer
    st.markdown("---")
    st.write("Developed by: duttaturja")
    st.write("[GitHub](https://github.com/duttaturja) [Facebook](https://www.facebook.com/turja.dutta.313/) [Instagram](https://www.instagram.com/duttaturja)")

#developed by: duttaturja 
# [GitHub](https://github.com/duttaturja) 
# [Facebook](https://www.facebook.com/turja.dutta.313/) 
# [Instagram](https://www.instagram.com/duttaturja)   