import pandas as pd
from prophet import Prophet
from sqlalchemy import create_engine
import plotly.express as px

# -----------------------------
# Database connection
# -----------------------------
DB_USER = "postgres"
DB_PASSWORD = "PassionateM707"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "business_health_monitor"

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# -----------------------------
# Load daily revenue
# -----------------------------
query = """
SELECT date, revenue
FROM daily_kpis
ORDER BY date
"""
df = pd.read_sql(query, engine)
df = df.rename(columns={"date": "ds", "revenue": "y"})
# Ensure ds is datetime
df["ds"] = pd.to_datetime(df["ds"])

# -----------------------------
# Train model
# -----------------------------
model = Prophet()
model.fit(df)

# -----------------------------
# Forecast next 7 days
# -----------------------------
future = model.make_future_dataframe(periods=7)

forecast = model.predict(future)   # 👈 THIS LINE MUST EXIST
forecast["ds"] = pd.to_datetime(forecast["ds"])
# -----------------------------
# Plot forecast
# -----------------------------
fig = px.line(
    forecast,
    x="ds",
    y=["yhat", "yhat_lower", "yhat_upper"],
    title="Revenue Forecast with Confidence Intervals"
)
fig.show()

# -----------------------------
# Compare actual vs forecast
# -----------------------------
merged = pd.merge(
    df,
    forecast[["ds", "yhat_lower", "yhat", "yhat_upper"]],
    on="ds",
    how="left"
)
# Create alert flag
merged["alert"] = merged["y"] < merged["yhat_lower"]

# Create business-friendly status
merged["status"] = merged["alert"].apply(
    lambda x: "ALERT" if x else "Normal"
)

merged["forecast_alert"] = merged["y"] < merged["yhat_lower"]
merged["status"] = merged["alert"].apply(
    lambda x: "ALERT" if x else "Normal"
)
# Add alert severity (business-friendly)
def severity(row):
    if row["alert"] and row["y"] < row["yhat_lower"] * 0.5:
        return "HIGH"
    elif row["alert"]:
        return "MEDIUM"
    else:
        return "NONE"

merged["severity"] = merged.apply(severity, axis=1)

alerts = merged[merged["forecast_alert"] == True]

print("\n FORECAST DEVIATION ALERTS ")
if alerts.empty:
    print("No revenue alerts. Performance is within expected range.")
else:
    print(alerts[["ds", "y", "yhat_lower", "yhat"]])
# Save forecast + alerts for API
output = merged.copy()

output.rename(columns={
    "ds": "date",
    "y": "revenue"
}, inplace=True)

output[["date", "revenue", "status", "severity"]].to_csv(

    "ml/revenue_forecast_with_alerts.csv",
    index=False
)

print("Saved ml/revenue_forecast_with_alerts.csv")
