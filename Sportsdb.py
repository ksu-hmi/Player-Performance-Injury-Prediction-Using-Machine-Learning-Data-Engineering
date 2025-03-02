import psycopg2

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="xxxxxx",
        user="xxxxxx",  # Change to your PostgreSQL username
        password="xxxxxxxx",  # Change to your actual password
        host="xxxxx",
        port="xxxxx"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = cursor.fetchall()

    print("✅ Tables in Database:", tables)

except Exception as e:
    print("❌ Error:", e)

finally:
    if conn:
        conn.close()