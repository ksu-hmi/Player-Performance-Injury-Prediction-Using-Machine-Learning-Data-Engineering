import joblib
import pandas as pd

# Load Trained Model
model = joblib.load("player_performance_model.pkl")


new_player = pd.DataFrame({
    "player_name": ["Haaland"], 
    "minutes_played": [90],
    "goals": [5],
    "assists": [3],
    "pass_accuracy": [90],
    "fatigue_score": [9]
})


print("\n🔹 New Player Stats:")
print(new_player)


if "player_name" in new_player.columns:
    new_player_for_prediction = new_player.drop(columns=["player_name"])
else:
    new_player_for_prediction = new_player


predicted_rating = model.predict(new_player_for_prediction)[0]


print(f"\nPredicted Player Rating for {new_player['player_name'][0]}: {predicted_rating:.2f}")
