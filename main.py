import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast app")
place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data for view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if filtered_data:  # Check if data was returned
            if option == "Temperature":
                # Convert Kelvin to Celsius
                temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
                dates = [dict["dt_txt"] for dict in filtered_data]
                figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
                st.plotly_chart(figure)

            if option == "Sky":
                images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                          "Rain": "images/rain.png", "Snow": "images/snow.png"}

                sky_conditions = [dict["weather"][0]['main'] for dict in filtered_data]
                image_paths = [images[condition] for condition in sky_conditions]
                st.image(image_paths, width=115)
        else:
            st.error("No data found. Please check the city name.")

    except Exception as e:
        st.error(f"Error: {str(e)}. Please check the city name and try again.")