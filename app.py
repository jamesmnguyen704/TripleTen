import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header("Car Advertisement Data Analysis")

price_hist = px.histogram(df, x='price', nbins=50, title="Price Distribution")
st.plotly_chart(price_hist)

price_model_scatter = px.scatter(df, x='model_year', y='price', title="Price vs. Model Year")
st.plotly_chart(price_model_scatter)

if st.checkbox('Show Histogram of Odometer Readings'):
    odometer_hist = px.histogram(df, x='odometer', nbins=50, title="Odometer Readings Distribution")
    st.plotly_chart(odometer_hist)
