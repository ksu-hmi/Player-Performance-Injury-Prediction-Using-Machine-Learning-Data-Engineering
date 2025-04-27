import pandas as pd
from sqlalchemy import create_engine
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database Connection Details
DATABASE_URL = "xxxxxxxxxxxxxxxxxxxxxxx"  # Update with actual connection string

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# SQL Query to extract game performance data
query = """
SELECT player_id, name, minutes_played, goals, assists, pass_accuracy, fatigue_score, player_rating
FROM game_performance
WHERE player_rating IS NOT NULL;
"""

try:
    # Extract Game Performance Data
    logger.info("Connecting to the database and executing query...")
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    
    logger.info("Data extracted successfully!")
    
    # Check for missing values and log the count
    missing_data = df.isnull().sum().sum()
    if missing_data > 0:
        logger.warning(f"There are {missing_data} missing values in the data_

