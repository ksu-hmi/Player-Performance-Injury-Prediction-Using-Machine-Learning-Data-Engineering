from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

# Load Trained Model
model = joblib.load("player_performance_model.pkl")

# Initialize Flask App
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Updated CORS settings

@app.route("/")
def home():
    return jsonify({"message": "Player Performance Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json 
    try:
        # Extract input features
        minutes_played = float(data["minutes_played"])
        goals = int(data["goals"])
        assists = int(data["assists"])
        pass_accuracy = float(data["pass_accuracy"])
        fatigue_score = float(data["fatigue_score"])

        # Create DataFrame for prediction
        features = pd.DataFrame([[minutes_played, goals, assists, pass_accuracy, fatigue_score]],
                                columns=["minutes_played", "goals", "assists", "pass_accuracy", "fatigue_score"])

        # Make prediction
        prediction = model.predict(features)[0]

        return jsonify({"predicted_rating": round(prediction, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)

