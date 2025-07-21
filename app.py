# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("boston_model.pkl")

st.title("🏠 Boston Housing Price Prediction")

st.write("Enter values to predict the house price (MEDV):")

# Collect user input
CRIM = st.number_input("Crime Rate (CRIM)", 0.0, 100.0, 0.1)
ZN = st.number_input("Residential Land Zone (ZN)", 0.0, 100.0, 0.0)
INDUS = st.number_input("Non-retail business (INDUS)", 0.0, 30.0, 0.0)
CHAS = st.selectbox("Bounds Charles River (CHAS)", [0, 1])
NOX = st.number_input("Nitric Oxide Concentration (NOX)", 0.0, 1.0, 0.5)
RM = st.number_input("Average Rooms (RM)", 0.0, 10.0, 6.0)
AGE = st.number_input("Proportion of Old Units (AGE)", 0.0, 100.0, 50.0)
DIS = st.number_input("Distance to Employment Centers (DIS)", 0.0, 20.0, 5.0)
RAD = st.number_input("Accessibility to Highways (RAD)", 1.0, 24.0, 1.0)
TAX = st.number_input("Tax Rate (TAX)", 100.0, 800.0, 300.0)
PTRATIO = st.number_input("Pupil-Teacher Ratio (PTRATIO)", 10.0, 30.0, 15.0)
B = st.number_input("Proportion of Black Residents (B)", 0.0, 400.0, 350.0)
LSTAT = st.number_input("% Lower Status Population (LSTAT)", 0.0, 40.0, 12.0)

if st.button("Predict"):
    features = [[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]]
    prediction = model.predict(features)
    st.success(f"🏡 Predicted House Price (MEDV): ${prediction[0]*1000:.2f}")
