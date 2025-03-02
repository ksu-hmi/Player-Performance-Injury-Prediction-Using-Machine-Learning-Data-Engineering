import streamlit as st
import requests

st.title("🏥 Player Injury Prediction")

# User Inputs
sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, step=0.5)
hydration_level = st.number_input("Hydration Level (%)", min_value=0, max_value=100)
fatigue_index = st.slider("Fatigue Index", 0, 10)
stress_level = st.slider("Stress Level", 0, 10)
minutes_played = st.number_input("Minutes Played", min_value=0, max_value=120)
goals = st.number_input("Goals", min_value=0, max_value=10)
assists = st.number_input("Assists", min_value=0, max_value=10)
fatigue_score = st.slider("Fatigue Score", 0, 10)

# Predict Button
if st.button("Predict Injury Risk"):
    data = {
        "sleep_hours": sleep_hours,
        "hydration_level": hydration_level,
        "fatigue_index": fatigue_index,
        "stress_level": stress_level,
        "minutes_played": minutes_played,
        "goals": goals,
        "assists": assists,
        "fatigue_score": fatigue_score
    }
    response = requests.post("http://127.0.0.1:5000/predict_injury", json=data)
    result = response.json()

    # Display Prediction
    if "injury_risk" in result:
        st.warning(f"⚠️ Injury Risk: {result['injury_risk']}")
    else:
        st.error("⚠️ Error in prediction")
