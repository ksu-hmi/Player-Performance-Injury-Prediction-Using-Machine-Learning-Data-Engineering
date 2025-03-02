import psycopg2

# Database connection parameters
DB_HOST = "localhost"
DB_NAME = "xxxxxxxx"
DB_USER = "postgres"
DB_PASSWORD = "xxxxxxx"

conn = None  

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()

    # Delete dependent records first
    cursor.execute("DELETE FROM cleaned_players;")
    
    # Now delete from players
    cursor.execute("DELETE FROM players;")

    # Commit the transaction
    conn.commit()
    print("All records deleted successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection only if it was successfully created
    if conn is not None:
        cursor.close()
        conn.close()
        print("Database connection closed.")
