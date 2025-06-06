import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit import color_picker

st.set_page_config(page_title="Dashboard",
                   layout="wide",
                   page_icon=":bar_chart:")

st.title("Water Quality Data Dashboard")
st.subheader("Visualization Tool for Biscayne Bay")

uploaded_image = st.sidebar.file_uploader("Upload a CSV dataset")
st.sidebar.info("If no CSV file it uploaded, a default one will be used for visualization.")

if uploaded_image is not None:
    df = pd.read_csv(uploaded_image)
    #st.dataframe(df)

else:
    df = pd.read_csv("datasets/biscayne_bay_dataset_oct_2022.csv")

scatterPlot, linePlot, maps, threeDPlot, tables = st.tabs([
    "Scatter Chart",
    "Line Chart",
    "Maps",
    "3D Chart",
    "Tables"
])

with scatterPlot:
    st.subheader("Scatter Chart for Water Quality Parameters")
    fig1 = px.scatter(
        df,
        x="Temperature (C)",
        y="Total Water Column (m)",
        title="Temperature (C) vs. Total Water Column (m)",
        color="ODO (mg/L)"
    )

    st.plotly_chart(fig1)

with linePlot:
    st.subheader("Line Chart for Water Quality Parameters")

    col1, col2 = st.columns([2,5])
    with col1:
        color=st.color_picker("Choose a color", "#081E3F")
        parameter=st.selectbox("Choose a parameter", options=["", "Total Water Column (m)", "Temperature (C)", "pH", "ODO (mg/L)"])

    with col2:

        fig2 = px.line(
            df,
            x=df.index,
            y=parameter,
            title=f"{parameter} over time"
        )
        fig2.update_traces(line_color=color)
        st.plotly_chart(fig2)

with maps:
    st.subheader("Map for Water Quality Parameters")
    fig3 = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        zoom=17,
        mapbox_style="open-street-map",
        color="Temperature (C)",
        hover_data=df
    )
    st.plotly_chart(fig3)

with threeDPlot:
    st.subheader("3D Chart for Water Quality Parameters")
    fig4 = px.scatter_3d(
        df,
        x="longitude",
        y="latitude",
        z="Total Water Column (m)",
        color="Temperature (C)",
    )
    fig4.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig4)

with tables:
    st.subheader("Raw Data")
    st.dataframe(df)
    st.divider()
    st.subheader("Summary Statistics")
    st.write(df.describe())
