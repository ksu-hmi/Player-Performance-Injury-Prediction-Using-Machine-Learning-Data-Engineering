import psycopg2

try:
    conn = psycopg2.connect(
        dbname="xxxxxx",
        user="xxxxxxx",
        password="xxxxx",
        host="xxxxxxxx",
        port="xxxxxxx"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")  # Simple test query
    result = cursor.fetchone()
    print("✅ Successfully connected to PostgreSQL at:", result[0])

    conn.close()
except Exception as e:
    print("❌ Database connection error:", e)
