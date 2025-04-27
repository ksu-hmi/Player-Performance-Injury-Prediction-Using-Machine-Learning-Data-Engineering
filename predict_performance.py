import joblib
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load Trained Model
model = joblib.load("player_performance_model.pkl")

# Define New Player Data
new_player = pd.DataFrame({
    "player_name": ["Haaland"], 
    "minutes_played": [90],
    "goals": [5],
    "assists": [3],
    "pass_accuracy": [90],
    "fatigue_score": [9]
})

# Log New Player Data
logging.info(f"New player data: {new_player}")

# Drop player_name column if it exists
if "player_name" in new_player.columns:
    new_player_for_prediction = new_player.drop(columns=["player_name"])
else:
    new_player_for_prediction = new_player

# Input Validation: Check if all columns are in the expected range
def validate_input(player_data):
    try:
        if not (0 <= player_data["minutes_played"].iloc[0] <= 120):
            raise ValueError("Minutes played must be between 0 and 120.")
        if not (0 <= player_data["goals"].iloc[0] <= 10):
            raise ValueError("Goals must be between 0 and 10.")
        if not (0 <= player_data["assists"].iloc[0] <= 10):
            raise ValueError("Assists must be between 0 and 10.")
        if not (0 <= player_data["pass_accuracy"].iloc[0] <= 100):
            raise ValueError("Pass accuracy must be between 0 and 100.")
        if not (0 <= player_data["fatigue_score"].iloc[0] <= 10):
            raise ValueError("Fatigue score must be between 0 and 10.")
    except ValueError as e:
        logging.error(f"Input validation error: {e}")
        return False
    return True

# Validate the new player's data before prediction
if validate_input(new_player_for_prediction):
    # Make prediction
    predicted_rating = model.predict(new_player_for_prediction)
    logging.info(f"Predicted rating for {new_player['player_name'].iloc[0]}: {predicted_rating[0]}")
    print(f"\n🔹 {new_player['player_name'].iloc[0]} Prediction: {predicted_rating[0]}")
else:
    print("🔸 Invalid player data. Please check the input values.")



predicted_rating = model.predict(new_player_for_prediction)[0]


print(f"\nPredicted Player Rating for {new_player['player_name'][0]}: {predicted_rating:.2f}")
