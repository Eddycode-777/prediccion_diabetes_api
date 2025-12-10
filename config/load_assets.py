import joblib
import json
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
MODELS_PATH = os.path.join(os.path.dirname(BASE_PATH), "models")

def load_model():
    model = joblib.load(os.path.join(MODELS_PATH, "diabetes_model.pkl"))
    return model

def load_scaler():
    scaler = joblib.load(os.path.join(MODELS_PATH, "scaler.pkl"))
    return scaler

def load_columns():
    with open(os.path.join(MODELS_PATH, "columns.json"), "r") as f:
        return json.load(f)
