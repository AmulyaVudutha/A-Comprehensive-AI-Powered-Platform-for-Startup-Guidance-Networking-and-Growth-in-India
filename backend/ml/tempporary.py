import pandas as pd
import os

# Go to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Correct dataset path
DATASET_PATH = os.path.join(BASE_DIR, "datasets", "startup_funding.csv")

print("Looking for dataset at:")
print(DATASET_PATH)

# Load dataset
df = pd.read_csv(DATASET_PATH)

print("\nDataset loaded successfully ✅")
print("\nColumn names:\n")
for col in df.columns:
    print(col)
