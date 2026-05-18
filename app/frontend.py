import streamlit as st
import requests

# page configuration
st.set_page_config(
    page_title="Inventory Forecasting",
    page_icon="📈",
    layout="wide"
)

# title
st.title("📈 Inventory Demand Forecasting System")

# description
st.markdown("""
Forecast weekly sales demand using machine learning
and temporal forecasting features.
""")

st.divider()

# create columns
col1, col2 = st.columns(2)

# left column
with col1:

    store = st.number_input(
        "Store",
        value=1
    )

    holiday_flag = st.number_input(
        "Holiday Flag",
        value=0
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

# right column
with col2:

    year = st.number_input(
        "Year",
        value=2012
    )

    month = st.number_input(
        "Month",
        value=5
    )

    week = st.number_input(
        "Week",
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

# prediction button
if st.button("Predict Sales"):

    # input data
    data = {
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

    try:

        # send request to FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        prediction = response.json()

        # show prediction
        st.metric(
            label="Predicted Weekly Sales",
            value=f"${prediction['predicted_sales']:,.2f}"
        )

    except Exception as e:

        st.error(
            f"Error connecting to backend: {e}"
        )
