import streamlit as st
import datetime

st.title("My first Web App for HCI")
st.header("Human-Computer Interaction")
st.subheader("Javier Gil")

st.divider()

st.write("Registration Form")

current_year = datetime.datetime.now().year
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
year_of_birth = st.number_input("Year of Birth",
                                min_value=1900,
                                max_value=2025,
                                step=1)
start_year_at_FIU = st.number_input("Start Year at FIU",
                                min_value=1965,
                                max_value=2025,
                                step=1)

age = current_year - year_of_birth
years_at_FIU = current_year - start_year_at_FIU

if first_name and last_name and year_of_birth and age and years_at_FIU:
    st.success(f"Hi {first_name} {last_name}! You are {age} years old!"
               f" You have been at FIU for {years_at_FIU} years.")
else:
    st.info("Please fill out the form.")