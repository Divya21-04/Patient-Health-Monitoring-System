import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Patient Health Monitor", page_icon="🩺", layout="wide")
st.title("Patient Health Monitoring Dashboard")
st.caption("Educational prototype using synthetic sample data. Not for clinical decisions.")

data_path = Path(__file__).resolve().parents[1] / "dataset" / "dataset.csv"
df = pd.read_csv(data_path)
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

patient = st.selectbox("Select patient ID", ["All patients"] + sorted(df["patient_id"].dropna().unique().tolist()))
view = df if patient == "All patients" else df[df["patient_id"] == patient]
latest = view.sort_values("timestamp").tail(1)
if latest.empty:
    st.warning("No readings available.")
    st.stop()

r = latest.iloc[0]
c1,c2,c3,c4 = st.columns(4)
c1.metric("Heart rate", f"{r.heart_rate_bpm:.0f} BPM")
c2.metric("Temperature", f"{r.body_temp_C:.1f} °C")
c3.metric("SpO₂", f"{r.SpO2_pct:.0f}%")
c4.metric("Alert flag", "Alert" if int(r.alert_flag) else "Normal")

st.subheader("Vitals over time")
st.line_chart(view.sort_values("timestamp").set_index("timestamp")[["heart_rate_bpm","body_temp_C","SpO2_pct"]])
st.subheader("Recent readings")
st.dataframe(view.sort_values("timestamp", ascending=False).head(25), use_container_width=True)
alerts = view[view["alert_flag"] == 1]
st.subheader("Rule-based flagged samples")
st.write(f"{len(alerts)} of {len(view)} selected rows are flagged by the project's demonstration rules.")
st.dataframe(alerts.sort_values("timestamp", ascending=False).head(20), use_container_width=True)
st.info("Alert thresholds are illustrative project rules, not medical advice. Real deployment requires clinical validation, consent, security and sensor calibration.")
