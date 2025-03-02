import streamlit as st
import requests

st.title("Player Performance Prediction")

# User Inputs
minutes_played = st.number_input("Minutes Played", min_value=0, max_value=120, step=1)
goals = st.number_input("Goals Scored", min_value=0, max_value=10, step=1)
assists = st.number_input("Assists", min_value=0, max_value=10, step=1)
pass_accuracy = st.slider("Pass Accuracy (%)", 0.0, 100.0, 85.0)
fatigue_score = st.slider("Fatigue Score", 0, 10, 5)

# Predict Button
if st.button("Predict Player Rating"):
    # Send Data to API
    data = {
        "minutes_played": minutes_played,
        "goals": goals,
        "assists": assists,
        "pass_accuracy": pass_accuracy,
        "fatigue_score": fatigue_score
    }
    response = requests.post("http://127.0.0.1:5000/predict", json=data)
    result = response.json()

    # Display Prediction
    if "predicted_rating" in result:
        st.success(f"Predicted Player Rating: {result['predicted_rating']}")
    else:
        st.error("Error in prediction")
