import pandas as pd

INPUT = "dataset/dataset.csv"
OUTPUT = "dataset/dataset_cleaned.csv"

df = pd.read_csv(INPUT)
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["patient_id"] = df["patient_id"].astype("string").str.strip()
for col in ["heart_rate_bpm", "body_temp_C", "SpO2_pct", "alert_flag"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["timestamp", "patient_id", "heart_rate_bpm", "body_temp_C", "SpO2_pct"])
df = df.drop_duplicates()
df["comm_channel"] = df["comm_channel"].astype("category")
df["alert_flag"] = (
    (df["heart_rate_bpm"] < 60) | (df["heart_rate_bpm"] > 100) |
    (df["SpO2_pct"] < 95) | (df["body_temp_C"] < 36.0) |
    (df["body_temp_C"] > 37.5)
).astype(int)
df.to_csv(OUTPUT, index=False)
print(f"Saved {len(df)} cleaned rows to {OUTPUT}")
