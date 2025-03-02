import psycopg2
import pandas as pd
from prefect import flow, task

# Database Connection Function with Error Handling
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="xxxxxxxx",
            user="postgres",
            password="xxxxxxxxxx",
            host="localhost",
            port="xxxxxx"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

# Extract Data
@task
def extract():
    conn = get_db_connection()
    if conn is None:
        return None  

    query = "SELECT player_id, name, age, position, height, weight, market_value FROM players;"
    df = pd.read_sql_query(query, conn)  
    conn.close()
    print("Extracted Data")
    return df

# Transform Data
@task
def transform(df):
    if df is None:
        return None  

    df["height"] = df["height"] * 100  
    df["weight"] = df["weight"] * 2.205  
    df["market_value"] = df["market_value"] * 1.1  
    print("Transformed Data")
    return df

# Load Data
@task
def load(df):
    if df is None:
        print("Skipping Load Step: No Data Available")
        return

    conn = get_db_connection()
    if conn is None:
        return  

    cursor = conn.cursor()

    # Create Table if Not Exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cleaned_players (
            player_id INT PRIMARY KEY REFERENCES players(player_id),
            name VARCHAR(100),
            age INT,
            position VARCHAR(50),
            height_cm FLOAT,
            weight_lbs FLOAT,
            market_value FLOAT
        );
    """)
    conn.commit()

    # Insert or Update Transformed Data
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO cleaned_players (player_id, name, age, position, height_cm, weight_lbs, market_value)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (player_id) 
            DO UPDATE SET 
                name = EXCLUDED.name,
                age = EXCLUDED.age,
                position = EXCLUDED.position,
                height_cm = EXCLUDED.height_cm,
                weight_lbs = EXCLUDED.weight_lbs,
                market_value = EXCLUDED.market_value;
        """, (row["player_id"], row["name"], row["age"], row["position"], row["height"], row["weight"], row["market_value"]))

    conn.commit()
    conn.close()
    print(" Loaded Data into Database")

# Prefect Flow (Manually Triggered)
@flow(name="ETL Pipeline")
def etl_pipeline():
    data = extract()
    transformed_data = transform.submit(data).result()  # Ensures correct task execution order
    load(transformed_data)


if __name__ == "__main__":
    etl_pipeline()
    print("ETL Pipeline Completed Successfully!")
