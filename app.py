import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model (local file for Streamlit Cloud)
model = joblib.load('best_electricity_model.joblib')

st.set_page_config(page_title="Electricity Usage Predictor", page_icon="⚡")
st.title("🏠 Home Energy Consumption Estimator")
st.write("Enter home details below to predict monthly electricity usage:")

# Input fields
num_rooms = st.number_input("Number of rooms", 1, 10, 3)
num_people = st.number_input("Number of people", 1, 20, 4)
housearea = st.number_input("House area (sq ft)", 200, 3000, 800)
is_ac = st.selectbox("Has AC?", [0, 1])
is_tv = st.selectbox("Has TV?", [0, 1])
is_flat = st.selectbox("Is Flat?", [0, 1])
num_children = st.number_input("Number of children", 0, 10, 2)
is_urban = st.selectbox("Urban area?", [0, 1])
amount_paid = st.number_input("Last month bill (₹)", 100, 5000, 800)

# Predict button
if st.button("🔮 Predict Usage"):
    # Build dataframe with correct column names as expected by the model
    input_df = pd.DataFrame([{
        "num_rooms": num_rooms,
        "num_people": num_people,
        "housearea": housearea,
        "is_ac": is_ac,
        "is_tv": is_tv,
        "is_flat": is_flat,
        "num_children": num_children,
        "is_urban": is_urban,
        "amount_paid": amount_paid
    }])

    # Predict using the trained model
    prediction = model.predict(input_df)

    st.success(f"Estimated Monthly Electricity Usage: {prediction[0]:.2f} units ⚡")
