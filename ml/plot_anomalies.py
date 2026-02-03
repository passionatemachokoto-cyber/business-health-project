import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

#  Database settings
DB_USER = "postgres"
DB_PASSWORD = "PassionateM707"
DB_NAME = "business_health_monitor"

DB_HOST = "localhost"
DB_PORT = "5432"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

#  Load anomaly table
df = pd.read_sql("SELECT * FROM daily_kpi_anomalies ORDER BY date;", engine)

#  Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

#  Plot
plt.figure(figsize=(12,6))

# Normal points
normal = df[df['anomaly'] == "Normal"]
plt.scatter(normal['date'], normal['revenue'], color='blue', label='Normal')

# Anomalies
anomaly = df[df['anomaly'] == " Anomaly"]
plt.scatter(anomaly['date'], anomaly['revenue'], color='red', label='Anomaly', s=100)

plt.plot(df['date'], df['revenue'], color='gray', alpha=0.3)  # line for context
plt.title("Revenue with Anomalies Highlighted")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
