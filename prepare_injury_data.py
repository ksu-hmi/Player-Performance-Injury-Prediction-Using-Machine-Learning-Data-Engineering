import psycopg2
import pandas as pd

# Connect to Database
conn = psycopg2.connect(
    dbname="xxxxx",
    user="postgres",
    password="xxxxxx",
    host="xxxxxxx",
    port="5432"
)

# Extract Biometric and Injury Data
query = """
    SELECT b.player_id, b.sleep_hours, b.hydration_level, b.fatigue_index, b.stress_level, 
           p.minutes_played, p.goals, p.assists, p.fatigue_score, 
           i.injury_id IS NOT NULL AS injury_risk
    FROM biometric_data b
    JOIN game_performance p ON b.player_id = p.player_id
    LEFT JOIN injury_history i ON b.player_id = i.player_id;
"""
df = pd.read_sql(query, conn)
conn.close()

# Handle Missing Values
df.fillna(0, inplace=True)

# Save Processed Data
df.to_csv("injury_prediction_data.csv", index=False)

print("Injury Prediction Data Prepared!")
