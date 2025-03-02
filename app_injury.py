from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import CORS

# Load Injury Prediction Model
injury_model = joblib.load("injury_prediction_model.pkl")

app = Flask(__name__)
CORS(app)

@app.route("/predict_injury", methods=["POST"])
def predict_injury():
    data = request.json
    try:
        # Extract Input Features
        features = pd.DataFrame([[
            float(data["sleep_hours"]),
            float(data["hydration_level"]),
            float(data["fatigue_index"]),
            float(data["stress_level"]),
            float(data["minutes_played"]),
            float(data["goals"]),
            float(data["assists"]),
            float(data["fatigue_score"])
        ]], columns=["sleep_hours", "hydration_level", "fatigue_index", "stress_level", 
                     "minutes_played", "goals", "assists", "fatigue_score"])

        # Make Prediction
        prediction = injury_model.predict(features)[0]

        return jsonify({"injury_risk": "High" if prediction == 1 else "Low"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
