import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "aqi_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_aqi(data):
    """
    data should be a dictionary containing all features.
    """

    sample = pd.DataFrame([data])

    prediction = model.predict(sample)

    return round(float(prediction[0]), 2)