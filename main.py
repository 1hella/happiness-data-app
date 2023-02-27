import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")

data1_header = st.selectbox("Select the data for the X-axis", ("GDP", "Generosity", "Happiness"))
data2_header = st.selectbox("Select the data for the Y-axis", ("GDP", "Generosity", "Happiness"))

st.subheader(f"{data1_header} and {data2_header}")

df = pd.read_csv('happy.csv')
data1 = df[data1_header.lower()]
data2 = df[data2_header.lower()]

figure = px.scatter(df, x=data1, y=data2, hover_data=['country'], labels={"x": data1_header, "y": data2_header})
st.plotly_chart(figure)