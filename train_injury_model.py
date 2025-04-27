import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


df = pd.read_csv("injury_prediction_data.csv")


X = df.drop(columns=["player_id", "injury_risk"])
y = df["injury_risk"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, max_depth=10, min_samples_split=5, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Random Forest Injury Prediction Model Trained! Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))


joblib.dump(model, "injury_prediction_model.pkl")
print(" Injury Prediction Model Saved!")
