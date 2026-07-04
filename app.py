from flask import Flask, render_template, request

from utils.predictor import predict_aqi
from utils.recommendation import get_aqi_category

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = {

        "PM2.5": float(request.form["PM25"]),
        "PM10": float(request.form["PM10"]),
        "NO": float(request.form["NO"]),
        "NO2": float(request.form["NO2"]),
        "NOx": float(request.form["NOx"]),
        "NH3": float(request.form["NH3"]),
        "CO": float(request.form["CO"]),
        "SO2": float(request.form["SO2"]),
        "O3": float(request.form["O3"]),
        "Benzene": float(request.form["Benzene"]),
        "Toluene": float(request.form["Toluene"]),
        "Xylene": float(request.form["Xylene"])

    }

    prediction = predict_aqi(data)

    category, advice = get_aqi_category(prediction)

    return render_template(
        "index.html",
        prediction=prediction,
        category=category,
        advice=advice
    )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)