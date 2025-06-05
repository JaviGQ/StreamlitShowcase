import streamlit as st

st.title("Temperature Converter")

def convertFtoC(temp):
    return (float(temp) - 32.0 ) *  5.0/9.0

def convertCtoF(temp):
    return (float(temp) * 9.0/5.0) + 32.0

temp_input = st.slider("Enter a temperature value",
                             min_value=-100.0,
                             max_value=200.0,
                             value=32.0)

conv_type = st.radio("Type of conversion", options=[
    "Fahrenheit to Celsius",
    "Celsius to Fahrenheit",
])
if conv_type == "Fahrenheit to Celsius":
    output = convertFtoC(temp_input)
    st.metric(label="Converted Temperature in Celcius", value=f"{output:.2f}")
elif conv_type == "Celsius to Fahrenheit":
    output = convertCtoF(temp_input)
    st.metric(label="Converted Temperature in Fahrenheit", value=f"{output:.2f}")


if "history" not in st.session_state:
    st.session_state.history = []

st.session_state.history.insert(0,(temp_input, conv_type, output))

print(st.session_state.history)

st.subheader("Conversion History")
for i, (temp, conv_type, output) in enumerate(st.session_state.history):
    st.write(f"{i}. {temp} ({conv_type})->{output:.2f}")