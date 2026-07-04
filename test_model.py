import joblib

model = joblib.load("aqi_model.pkl")

print(type(model))
print(model)