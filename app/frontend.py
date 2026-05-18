import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Inventory Forecasting",
    page_icon="📈",
    layout="wide"
)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load(
    "models/random_forest_model.pkl"
)

# ---------------- TITLE ---------------- #

st.title("📈 Inventory Demand Forecasting System")

st.markdown("""
Forecast weekly retail sales demand using
machine learning and temporal forecasting features.
""")

st.divider()

# ---------------- INPUT LAYOUT ---------------- #

col1, col2 = st.columns(2)

# ---------- LEFT COLUMN ---------- #

with col1:

    store = st.number_input(
        "Store",
        min_value=1,
        value=1
    )

    holiday_flag = st.selectbox(
        "Holiday Flag",
        [0, 1]
    )

    temperature = st.number_input(
        "Temperature",
        value=72.0
    )

    fuel_price = st.number_input(
        "Fuel Price",
        value=3.1
    )

    cpi = st.number_input(
        "CPI",
        value=220.0
    )

    unemployment = st.number_input(
        "Unemployment",
        value=7.2
    )

# ---------- RIGHT COLUMN ---------- #

with col2:

    year = st.number_input(
        "Year",
        min_value=2010,
        max_value=2030,
        value=2012
    )

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=5
    )

    week = st.number_input(
        "Week",
        min_value=1,
        max_value=52,
        value=20
    )

    lag_1 = st.number_input(
        "Lag 1",
        value=1400000.0
    )

    lag_2 = st.number_input(
        "Lag 2",
        value=1450000.0
    )

    lag_4 = st.number_input(
        "Lag 4",
        value=1500000.0
    )

    rolling_mean_4 = st.number_input(
        "Rolling Mean 4",
        value=1450000.0
    )

    rolling_std_4 = st.number_input(
        "Rolling Std 4",
        value=50000.0
    )

st.divider()

# ---------------- PREDICTION ---------------- #

if st.button("Predict Sales"):

    input_data = {
        "Store": store,
        "Holiday_Flag": holiday_flag,
        "Temperature": temperature,
        "Fuel_Price": fuel_price,
        "CPI": cpi,
        "Unemployment": unemployment,
        "Year": year,
        "Month": month,
        "Week": week,
        "Lag_1": lag_1,
        "Lag_2": lag_2,
        "Lag_4": lag_4,
        "Rolling_Mean_4": rolling_mean_4,
        "Rolling_Std_4": rolling_std_4
    }

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.success("Prediction Generated Successfully")

    st.metric(
        label="Predicted Weekly Sales",
        value=f"${prediction:,.2f}"
    )
