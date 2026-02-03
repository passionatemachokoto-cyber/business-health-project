 Business Health Monitoring System

An end-to-end data analytics and machine learning project that monitors business performance, detects anomalies, and forecasts revenue trends using real-world data engineering and ML practices.



Project Overview

This project simulates a **Business Health Monitoring System** used by data teams to track revenue, operational performance, and early warning signals.

It combines:
- SQL-based data modeling
- Python analytics
- Machine learning forecasting
- Anomaly detection
- API and dashboard integration

The system answers key business questions such as:
- Is revenue behaving normally?
- Are there unusual drops or spikes that need attention?
- What does future revenue look like?
- Are operational metrics degrading?

Project Architecture
business-health-project/
│
├── analytics/ # Data analysis & visualisation
│ └── dashboard.py # Streamlit dashboard
│
├── ml/ # Machine learning & alerts
│ ├── forecast_revenue.py
│ ├── api.py
│ └── revenue_forecast_with_alerts.csv
│
├── Data Base/ # SQL tables & views
│
├── venv/ # Python virtual environment
│
└── README.md



 
 Data Layer (SQL)
Core Tables
- fact_sales – transactional sales data
- fact_ops_events – operational metrics (latency, error rate)

Derived Tables
- daily_kpis – daily revenue & order metrics
- daily_ops – daily operational aggregates
- daily_kpis_full – joined business + ops KPIs

These tables simulate how analytics teams build business-ready datasets from raw facts.


 Machine Learning Layer

Revenue Forecasting
- Uses Facebook Prophet
- Models daily revenue trends
- Produces prediction intervals (`yhat_lower`, `yhat_upper`)

 Anomaly Detection
- Compares actual revenue vs forecast bounds
- Flags deviations outside business tolerance
- Assigns:
  - `Normal`
  - `Warning`
  - `Critical`

 Outputs
- Forecast plots
- Alert tables
- CSV used by downstream services



 API Layer

A lightweight FastAPI service exposes:
- Revenue alerts
- Forecast data for dashboards

This simulates how ML outputs are consumed by other systems.



 Dashboard (Streamlit)

The Streamlit app provides:
- Revenue trend visualisation
- Anomaly highlighting
- Business-friendly KPIs

This mirrors how non-technical stakeholders consume analytics.

---

 Tech Stack

- Python (pandas, Prophet, FastAPI, Streamlit)
- PostgreSQL (SQL modeling)
- Plotly / Matplotlib (visualisation)
- Git & GitHub (version control)

---
 Key Design Decisions

- No anomalies initially 
  → Thresholds were tuned to reflect realistic business tolerance.

- Separation of layers  
  → Database, ML, API, and dashboard are decoupled.

- Production-style structure  
  → Mirrors real analytics & ML systems used in companies.



 What This Project Demonstrates

- End-to-end data thinking
- Business-focused anomaly detection
- Forecasting beyond notebooks
- Clear system design
- Interview-ready explanations



Author
Passionate Machokoto 
Aspiring Data Analyst transitioning into Data Science, Machine Learning, and AI Engineering through end-to-end projects.
GitHub: https://github.com/passionatemachokoto-cyber






