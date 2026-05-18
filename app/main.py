from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# load trained model
model = joblib.load(
    "models/random_forest_model.pkl"
)

@app.get("/")
def home():

    return {
        "message": "Inventory Demand Forecasting API"
    }

@app.post("/predict")
def predict(data: dict):

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    return {
        "predicted_sales": float(prediction)
    }
