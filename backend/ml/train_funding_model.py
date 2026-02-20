import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

from sklearn.preprocessing import LabelEncoder
import joblib
import os

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "datasets", "startup_funding.csv")
MODEL_PATH = os.path.join(BASE_DIR, "backend", "ml", "models", "funding_model.pkl")

# ---------------- LOAD DATA ----------------
df = pd.read_csv(DATASET_PATH)

# ---------------- CLEAN COLUMN NAMES ----------------
df.columns = (
    df.columns
    .str.strip()
    .str.replace("  ", " ")
)

df = df.rename(columns={
    "Industry Vertical": "IndustryVertical",
    "City Location": "CityLocation",
    "City  Location": "CityLocation",
    "Amount in USD": "AmountInUSD"
})

print("Using columns:", df.columns.tolist())

# ---------------- SELECT REQUIRED COLUMNS ----------------
df = df[["IndustryVertical", "CityLocation", "AmountInUSD"]].dropna()

# ---------------- CLEAN AMOUNT COLUMN (CRITICAL FIX) ----------------
df["AmountInUSD"] = (
    df["AmountInUSD"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["AmountInUSD"] = pd.to_numeric(df["AmountInUSD"], errors="coerce")
df = df.dropna()

# ---------------- ENCODING ----------------
le_industry = LabelEncoder()
le_city = LabelEncoder()

df["IndustryVertical"] = le_industry.fit_transform(df["IndustryVertical"])
df["CityLocation"] = le_city.fit_transform(df["CityLocation"])

# ---------------- MODEL ----------------
X = df[["IndustryVertical", "CityLocation", "AmountInUSD"]]
y = df["AmountInUSD"]   # regression target

model = GradientBoostingRegressor()
model.fit(X, y)

# ---------------- SAVE MODEL ----------------
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)

print("\nFunding prediction model trained & saved successfully ✅")
print("Model saved at:", MODEL_PATH)
