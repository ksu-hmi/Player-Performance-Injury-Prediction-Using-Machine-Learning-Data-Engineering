import psycopg2
import pandas as pd

# Database Connection
conn = psycopg2.connect(
    dbname="xxxxxxx",
    user="xxxxxxx",
    password="xxxxx",
    host="localhost",
    port="xxxx"
)

# Extract Players Data
query = "SELECT player_id, name, age, position, height, weight, market_value FROM players;"
df = pd.read_sql(query, conn)
conn.close()

# Data Cleaning
df["height"] = df["height"] * 100  # Convert height from meters to cm
df["weight"] = df["weight"] * 2.205  # Convert weight from kg to lbs
df["market_value"] = df["market_value"] * 1.1  # Increase value by 10% (adjustments)

# Display Cleaned Data
print(df)
