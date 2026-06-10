import joblib
import numpy as np

model = joblib.load("models/xgb_model.json")

def predict_surge(features):
    prob = model.predict_proba([features])[0][1]
    return float(prob)
