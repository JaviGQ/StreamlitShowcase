import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

st.set_page_config(
    page_title = "App 5 - Showcase",
    page_icon = ":bar_chart:",
    layout = "centered",
)

st.title("Informative App for Final Presentation")
st.sidebar.subheader("Use the checkboxes below to explore features.")

with st.sidebar.expander("Contact Us"):
    st.write("Any feedback or ideas?")
    st.text_input("Your email address")
    st.text_area("Message")
    st.button("Send")

tab1, tab2, tab3 = st.tabs(["Basic Plots", "Sliders", "Media Widgets"])

with tab1:
    if st.checkbox("Show some basic plots"):
        df = pd.DataFrame(np.random.rand(20, 3), columns=["A", "B", "C"])
        st.dataframe(df)
        st.line_chart(df)

with tab2:
        if st.checkbox("Enable Sliders"):
            age = st.slider("How old are you?", 18, 130, 25)
            value_range = st.slider("Select a numeric range",
                                    0., 200., (25., 75.))
            time_range = st.slider("Select a time range",
                                   value=(time(8, 45), time(17,45)))

with tab3:
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded image", use_container_width=True)

    camera_input = st.camera_input("Try it out!")
    if camera_input:
        st.image(camera_input, caption="Captured Image", use_container_width=True)

    st.video("https://www.youtube.com/watch?v=8K_rHzVCgEU")
    st.caption("20,000 Diamong Tree")
