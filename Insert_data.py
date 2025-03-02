from datetime import date
import psycopg2

# Database connection parameters
DB_NAME = "Sportsdb"
DB_USER = "xxxxx"  # Change to your PostgreSQL username
DB_PASSWORD = "xxxxxxxx"  # Change to your actual password
DB_HOST = "localhost"
DB_PORT = "xxxxx"

try:
    # Establish database connection
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor = conn.cursor()

    today = date.today()

    # Insert Sample Teams
    teams_data = [
        ("Inter Miami", "MLS", "Gerardo Martino", "DRV PNK Stadium", "4-3-3"),
        ("Al Nassr", "Saudi Pro League", "Luís Castro", "Al-Awwal Park", "4-2-3-1"),
        ("Manchester City", "Premier League", "Pep Guardiola", "Etihad Stadium", "4-3-3"),
        ("Al Hilal", "Saudi Pro League", "Jorge Jesus", "King Fahd International Stadium", "4-2-3-1"),
        ("Liverpool", "Premier League", "Arne Slot", "Anfield", "4-3-3"),
        ("Real Madrid", "La Liga", "Carlo Ancelotti", "Santiago Bernabéu", "4-3-1-2"),
        ("Manchester City", "Premier League", "Pep Guardiola", "Etihad Stadium", "4-3-3"),
        ("FC Barcelona", "La Liga", "Xavi Hernandez", "Spotify Camp Nou", "4-3-3")
        ("Real Madrid", "La Liga", "Carlo Ancelotti", "Santiago Bernabéu", "4-3-1-2"),
        

    ]
    
    cursor.executemany(
        """
        INSERT INTO teams (name, league, coach, stadium, formation)
        VALUES (%s, %s, %s, %s, %s)
        """,
        teams_data
    )

    # ✅ Get Team IDs from DB
    cursor.execute("SELECT team_id, name FROM teams;")
    teams = {name: team_id for team_id, name in cursor.fetchall()}

    # Insert Sample Players
    players_data = [
        ("Lionel Messi", 36, "Forward", 1, "Argentina", "2025-06-30", "Left", 1.70, 72, 50.0, 2.5),
        ("Cristiano Ronaldo", 39, "Forward", 2, "Portugal", "2026-06-30", "Right", 1.87, 83, 40.0, 1.8),
        ("Kevin De Bruyne", 32, "Midfielder", 3, "Belgium", "2025-06-30", "Right", 1.81, 75, 85.0, 3.2),
        ("Neymar Jr.", 32, "Forward", 4, "Brazil", "2027-06-30", "Right", 1.75, 68, 70.0, 5.0),
        ("Virgil van Dijk", 32, "Defender", 5, "Netherlands", "2025-06-30", "Right", 1.93, 92, 60.0, 2.0),
        ("Kylian Mbappe", 25, "Forward", 6, "France", "2024-06-30", "Right", 1.78, 73, 180.0, 1.5),
        ("Erling Haaland", 23, "Forward", 7, "Norway", "2028-06-30", "Left", 1.94, 88, 200.0, 2.8),
        ("Pedri", 21, "Midfielder", 8, "Spain", "2026-06-30", "Right", 1.74, 64, 90.0, 3.0),
        ("Jude Bellingham", 20, "Midfielder", 9, "England", "2029-06-30", "Right", 1.86, 75, 150.0, 2.1),
        ("Trent Alexander-Arnold", 25, "Defender", 10, "England", "2025-06-30", "Right", 1.75, 69, 80.0, 3.5)
    ]
    
    cursor.executemany(
        """
        INSERT INTO players (name, age, position, team_id, nationality, contract_expiration, 
                             dominant_foot, height, weight, market_value, injury_prone_score)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        players_data
    )

      # ✅ Get Player IDs from DB
    cursor.execute("SELECT id, name FROM players;")
    players = {name: player_id for player_id, name in cursor.fetchall()}

    # Insert Matches Data
    matches_data = [
        (101, 1, 2, '2025-02-01', 'Etihad Stadium', 'Michael Oliver', 'Sunny'),
        (102, 3, 4, '2025-02-02', 'Parc des Princes', 'Clement Turpin', 'Cloudy'),
        (103, 5, 6, '2025-02-03', 'Anfield', 'Anthony Taylor', 'Rainy'),
        (104, 7, 8, '2025-02-04', 'Santiago Bernabéu', 'Jesús Gil Manzano', 'Windy'),
        (105, 9, 10, '2025-02-05', 'Camp Nou', 'Mateu Lahoz', 'Sunny'),
        (106, 2, 3, '2025-02-06', 'Old Trafford', 'Daniele Orsato', 'Snowy'),
        (107, 4, 5, '2025-02-07', 'Signal Iduna Park', 'Felix Brych', 'Rainy'),
        (108, 6, 7, '2025-02-08', 'Allianz Arena', 'Benoît Bastien', 'Cloudy'),
        (109, 8, 9, '2025-02-09', 'San Siro', 'Marco Guida', 'Sunny'),
        (110, 10, 1, '2025-02-10', 'Wembley Stadium', 'Szymon Marciniak', 'Windy'),
    ]

    cursor.executemany(
        """
        INSERT INTO matches (match_id, home_team_id, away_team_id, match_date, stadium, referee, weather)                 
        VALUES (%s, %s, %s, %s, %s, %s,%s)
        """,
        matches_data
    )

    #Insert game_Performance Data
    game_performance = [
        (1, 101, 61, 2, 2, 82.6, 3, 2, 7.6, 7.0),
        (2, 102, 63, 0, 1, 88.7, 2, 1, 4.0, 7.3),
        (3, 103, 89, 0, 2, 86.4, 1, 2, 6.7, 7.9),
        (4, 104, 72, 0, 1, 89.0, 2, 0, 4.2, 7.4),
        (5, 105, 80, 0, 1, 85.6, 1, 2, 6.7, 6.2),
        (6, 106, 70, 1, 1, 91.2, 2, 1, 5.5, 8.1),
        (7, 107, 88, 3, 2, 93.5, 1, 0, 3.8, 9.0),
        (8, 108, 75, 0, 1, 87.8, 2, 1, 6.0, 7.5),
        (9, 109, 82, 1, 2, 90.3, 1, 1, 5.1, 8.3),
        (10, 110, 77, 0, 3, 86.7, 2, 1, 4.5, 7.8),
    ]

    cursor.executemany(
        """
        INSERT INTO game_performance (player_id, match_id, minutes_played, goals, assists, pass_accuracy, tackles, interceptions, fatigue_score, player_rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, 
        game_performance
    )

        #Insert injury_history Data
    injury_history_data = [
        (1, '2024-12-10', 'Hamstring strain', 'Moderate', 21, 'Recovered'),
        (2, '2025-01-05', 'Ankle sprain', 'Minor', 10, 'Recovered'),
        (3, '2024-11-20', 'Knee ligament injury', 'Severe', 90, 'Recovering'),
        (4, '2024-12-15', 'Groin strain', 'Moderate', 28, 'Recovered'),
        (5, '2024-10-25', 'Fractured rib', 'Severe', 60, 'Recovered'),
        (6, '2025-01-02', 'Calf strain', 'Minor', 14, 'Recovered'),
        (7, '2024-09-30', 'ACL tear', 'Severe', 180, 'Recovering'),
        (8, '2025-01-10', 'Concussion', 'Moderate', 14, 'Recovered'),
        (9, '2024-11-05', 'Shoulder dislocation', 'Moderate', 35, 'Recovered'),
        (10, '2024-12-20', 'Hamstring tear', 'Severe', 75, 'Recovering'),
    ]

    cursor.executemany(
        """
        INSERT INTO injury_history (player_id, injury_date, injury_type, severity, recovery_time, recovery_status) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """, 
        injury_history_data
    ) 


    # Insert Biometric Data
    biometric_data = [
        (1, today, 65, 7.5, 85.0, 3.0, 2.5),  # Lionel Messi
        (2, today, 70, 6.0, 78.0, 4.5, 3.5),   # Cristiano Ronaldo
        (3, today, 62, 8.0, 90.0, 2.0, 2.0),  # Kevin De Bruyne
        (4, today, 68, 7.0, 80.0, 4.0, 3.0),  # Neymar Jr.
        (5, today, 60, 7.5, 88.0, 2.5, 1.5),  # Virgil van Dijk
        (6, today, 72, 6.5, 75.0, 5.0, 4.0),  # Kylian Mbappe
        (7, today, 64, 7.8, 92.0, 2.8, 2.2),  # Erling Haaland
        (8, today, 66, 8.5, 89.0, 1.8, 1.8),  # Pedri
        (9, today, 67, 8.0, 87.0, 2.2, 2.0),  # Jude Bellingham
        (10, today, 69, 7.2, 83.0, 3.5, 3.0)    # Trent Alexander-Arnold
         
    ]

    cursor.executemany(
        """
        INSERT INTO biometric_data (player_id, record_date, heart_rate, sleep_hours, hydration_level, fatigue_index, stress_level)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, 
        biometric_data
    ) 

      #Insert training_sessions  Data
    training_sessions_data = [
        (1, today, 90, "Strength", 8.5, 4.2),
        (2, today, 60, "Cardio", 6.0, 3.5),
        (3, today, 75, "Tactical", 7.2, 4.0),
        (4, today, 45, "Recovery", 4.5, 2.0),
        (5, today, 100, "Strength", 9.0, 5.5),
        (6, today, 80, "Cardio", 7.8, 4.8),
        (7, today, 90, "Tactical", 8.2, 5.0),
        (8, today, 50, "Recovery", 5.0, 2.2),
        (9, today, 110, "Strength", 9.5, 6.0),
        (10, today, 70, "Cardio", 6.5, 3.8)
    ]

    cursor.executemany(
        """
        INSERT INTO training_sessions (player_id, session_date, duration_minutes, training_type, workload, fatigue_level) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """, 
        training_sessions_data
    )      

     #Insert mental_performance  Data
    mental_performance_data = [
        (1, today, 6.1, 5.9, 6.2),
        (2, today, 8.8, 5.2, 7.3),
        (3, today, 8.0, 8.2, 7.4),
        (4, today, 6.4, 6.1, 5.6),
        (5, today, 6.7, 7.9, 8.4),
        (6, today, 7.5, 6.3, 7.1),
        (7, today, 9.1, 8.7, 8.9),
        (8, today, 6.2, 5.8, 7.0),
        (9, today, 7.8, 7.4, 8.1),
        (10, today, 7.0, 6.9, 7.3)
    ]

    cursor.executemany(
        """
        INSERT INTO mental_performance (player_id, record_date, confidence_level, focus_score, stress_management) 
        VALUES (%s, %s, %s, %s, %s)
        """, 
        mental_performance_data
    )      

    #Insert player_analytics  Data
    player_analytics_data = [
        (1, today, 1.26, 0.76, 4.9, 6.1),
        (2, today, 0.26, 0.16, 2.3, 2.3),
        (3, today, 1.18, 0.74, 5.4, 4.4),
        (4, today, 1.25, 0.77, 5.6, 4.2),
        (5, today, 0.75, 0.60, 6.7, 1.0),
        (6, today, 0.98, 0.45, 3.9, 5.8),
        (7, today, 1.42, 0.90, 7.2, 6.9),
        (8, today, 0.31, 0.22, 1.9, 2.4),
        (9, today, 1.10, 0.66, 5.3, 4.8),
        (10, today, 0.55, 0.33, 3.1, 3.5)
    ]

    cursor.executemany(
    """
    INSERT INTO player_analytics (player_id, record_date, expected_goals, expected_assists, defensive_contributions, attacking_contributions) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """, 
    player_analytics_data
    )
  



    # Commit transaction
    conn.commit()
    print("Sample Data Inserted Successfully!")

except psycopg2.Error as e:
    # Handle any database errors
    print(f"❌ Error: {e}")
    if conn:
        conn.rollback()  # Rollback in case of failure

finally:
    # Close cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed.")
