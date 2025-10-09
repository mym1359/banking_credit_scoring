# api.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Banking Credit Scoring API")

# Load model
model = joblib.load("models/credit_model.pkl")

# Input schema

class CustomerInput(BaseModel):
    income: float
    credit_score: float
    debt: float
    age: int
    employment_years: int

@app.post("/predict")

def predict_risk(data: CustomerInput):
    # Feature engineering inline
    debt_to_income = data.debt / (data.income + 1e-6)
    employment_stability = data.employment_years / data.age

    features = np.array([[data.income, data.credit_score, data.debt, debt_to_income, employment_stability]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "risk_class": int(prediction),
        "risk_probability": round(probability, 4)
    }
