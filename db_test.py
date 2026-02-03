from sqlalchemy import create_engine
import pandas as pd


DB_USER = "postgres"
DB_PASSWORD = "PassionateM707"
DB_NAME = "business_health_monitor"

DB_HOST = "localhost"
DB_PORT = "5432"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

query = "SELECT * FROM daily_ops LIMIT 5;"

df = pd.read_sql(query, engine)

print(df)

