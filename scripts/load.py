import os
from sqlalchemy import create_engine

def load_data(df):

    try:
        db_password = os.getenv("DB_PASSWORD")

        engine = create_engine(
            f"postgresql+psycopg2://postgres:{db_password}@localhost:5432/data_pipeline_db"
        )

        df.to_sql(
            name="sales",
            con=engine,
            if_exists="replace",
            index=False
    )

        print("Data loaded into PostgreSQL successfully")

    except Exception as e:
        print("Error loading data:", e)