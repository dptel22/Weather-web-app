import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast app")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data for view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)


figure = px.line(x=, y=, labels={"x": "Date" , "y": "Temperature"})
st.plotly_chart()




