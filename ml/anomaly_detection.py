import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
# Alert sensitivity mode
MODE = "production"  # change to "demo" for higher sensitivity

#  DATABASE SETTINGS (same as before)
DB_USER = "postgres"
DB_PASSWORD = "PassionateM707"
DB_NAME = "business_health_monitor"

DB_HOST = "localhost"
DB_PORT = "5432"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

#  Load data
query = """
SELECT
    date,
    revenue,
    orders,
    avg_latency,
    error_rate
FROM daily_kpis_full
ORDER BY date;
"""

df = pd.read_sql(query, engine)

#  Keep only numbers (ML rule)
features = df[["revenue", "orders", "avg_latency", "error_rate"]]

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

#  Train anomaly model
if MODE == "production":
    contamination = 0.1
else:
    contamination = 0.3

model = IsolationForest(
    n_estimators=100,
    contamination=contamination,
    random_state=42
)


df["anomaly_flag"] = model.fit_predict(features_scaled)

df["anomaly"] = df["anomaly_flag"].apply(lambda x: " Anomaly" if x == -1 else "Normal")

#  Show anomalies
print(df[["date", "revenue", "orders", "anomaly"]].tail(15))
#  Prepare table to save
output_df = df[
    ["date", "revenue", "orders", "avg_latency", "error_rate", "anomaly_flag", "anomaly"]
]

#  Save to PostgreSQL
output_df.to_sql(
    "daily_kpi_anomalies",
    engine,
    if_exists="replace",  # overwrites table if it exists
    index=False
)

print(" Anomaly table saved to database")
#  Prepare table to save
output_df = df[
    ["date", "revenue", "orders", "avg_latency", "error_rate", "anomaly_flag", "anomaly"]
]

#  Save to PostgreSQL
output_df.to_sql(
    "daily_kpi_anomalies",
    engine,
    if_exists="replace",  # overwrites table if it exists
    index=False
)

print(" Anomaly table saved to database")
