import pandas as pd
from sqlalchemy import create_engine

# Database Connection Details
DATABASE_URL = "xxxxxxxxxxxxxxxxxxxxxxx"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Extract Game Performance Data
query = """
SELECT player_id, name, minutes_played, goals, assists, pass_accuracy, fatigue_score, player_rating
FROM game_performance
WHERE player_rating IS NOT NULL;
"""

# Use SQLAlchemy engine with pandas
with engine.connect() as conn:
    df = pd.read_sql(query, conn)

# Drop Missing Values
df.dropna(inplace=True)

# Save Processed Data for ML
df.to_csv("player_performance_data.csv", index=False)

print("Player Performance Data Prepared!")
