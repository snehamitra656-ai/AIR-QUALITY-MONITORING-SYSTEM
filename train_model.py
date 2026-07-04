import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =====================================
# Load Dataset
# =====================================

df = pd.read_csv("city_day.csv")

print("Dataset Loaded Successfully")
print(df.head())

# =====================================
# Data Cleaning
# =====================================

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Drop rows where AQI is missing
df.dropna(subset=["AQI"], inplace=True)

# Fill missing numerical values
df.fillna(df.mean(numeric_only=True), inplace=True)

# =====================================
# Date Feature Engineering
# =====================================

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

df.drop("Date", axis=1, inplace=True)

# =====================================
# Feature & Target
# =====================================

X = df.drop("AQI", axis=1)
y = df["AQI"]

# =====================================
# One Hot Encoding
# =====================================

X = pd.get_dummies(
    X,
    columns=["City", "AQI_Bucket"],
    drop_first=True
)

# Save feature names for Flask prediction
joblib.dump(list(X.columns), "feature_columns.pkl")

# =====================================
# Train Test Split
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# =====================================
# Train Model
# =====================================

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# =====================================
# Prediction
# =====================================

prediction = model.predict(X_test)

# =====================================
# Evaluation
# =====================================

mae = mean_absolute_error(y_test, prediction)
mse = mean_squared_error(y_test, prediction)
rmse = mse ** 0.5
r2 = r2_score(y_test, prediction)

print("\n========== Model Performance ==========")
print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R2   : {r2:.4f}")

# =====================================
# Save Model
# =====================================

joblib.dump(
    model,
    "aqi_model.pkl",
    compress=3
)

print("\nModel saved successfully as aqi_model.pkl")
print("Feature columns saved as feature_columns.pkl")