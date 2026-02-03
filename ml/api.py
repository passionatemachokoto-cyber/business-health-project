from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Business Health API")

@app.get("/revenue/alerts")
def get_revenue_alerts():
    df = pd.read_csv("ml/revenue_forecast_with_alerts.csv")
    alerts = df[df["status"] != "Normal"]
    return alerts.to_dict(orient="records")
