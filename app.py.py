import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('weather_model.pkl', 'rb'))

st.title("🌦️ Weather Forecast App")
st.write("Will it rain tomorrow? Let's find out!")

# Input widgets
MinTemp = st.number_input("Min Temperature")
MaxTemp = st.number_input("Max Temperature")
Rainfall = st.number_input("Rainfall")
Evaporation = st.number_input("Evaporation")
Sunshine = st.number_input("Sunshine")
Humidity9am = st.slider("Humidity 9am", 0, 100)
Humidity3pm = st.slider("Humidity 3pm", 0, 100)
Temp3pm = st.number_input("Temp at 3pm")

# You can add more inputs...

if st.button("Predict"):
    # Put inputs into a DataFrame
    input_data = pd.DataFrame([[MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, Humidity9am, Humidity3pm, Temp3pm]],
                              columns=['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
                                       'Humidity9am', 'Humidity3pm', 'Temp3pm'])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Yes! It will rain tomorrow ☔")
    else:
        st.info("Nope! No rain tomorrow ☀️")
