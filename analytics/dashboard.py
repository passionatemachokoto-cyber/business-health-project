import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Business Health Dashboard", layout="wide")

st.title(" Business Health Dashboard")

API_URL = "http://127.0.0.1:8000/revenue/alerts"

st.subheader("Revenue Forecast Alerts")

try:
    response = requests.get(API_URL)
    data = response.json()
    df = pd.DataFrame(data)

    if df.empty:
        st.info("No alerts found.")
    else:
        st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Could not connect to API: {e}")
