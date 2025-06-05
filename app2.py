import streamlit as st

st.set_page_config(page_title="Registration",
                   layout="centered",
                   initial_sidebar_state="expanded",
                   page_icon="<3")

st.title("Party Registration")
st.subheader("Come celebrate my bday party!")

st.divider()

st.sidebar.title("Contact")
st.sidebar.subheader("We want to hear from you!")

contact_option = st.sidebar.selectbox(
    "How would you like to be contacted?", options=["", "email", "call", "text"])

if contact_option:
    st.sidebar.success(f"We will be {contact_option}ing you!")

st.sidebar.divider()

with st.form("Registration", clear_on_submit=True):
    name = st.text_input("What is your name?", placeholder="First and Last Name")
    age = st.number_input("How old are you?", min_value=21, step=1)
    email = st.text_input("What is your email?", placeholder="name@fiu.edu")
    major = st.selectbox("What is your major?", options=["", "CS", "Data Science and AI", "IT", "CyberSecurity", "Other"])
    level = st.selectbox("What is your level?", options=["", "Undergraduate", "Master's", "PhD"])
    subscribe = st.checkbox("Subscribe to learn more about our events", value=False)
    submit = st.form_submit_button("Submit")
    if submit:
        st.success(f"Thank you, you have been successfully registered!")
    else:
        st.info("Are you interested in registering?")