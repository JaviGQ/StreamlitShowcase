import streamlit as st

st.title("A Counter and State Management")

if "counter" not in st.session_state:
    st.session_state.counter = 0

def increase_counter():
    st.session_state.counter += 1

def reset_counter():
    st.session_state.counter = 0

st.write(f"The current value of counter is {st.session_state.counter}.")

col1, col2 = st.columns(2)

with col1:
    st.button("Increase counter", on_click=increase_counter)

with col2:
    st.button("Reset counter", on_click=reset_counter)


