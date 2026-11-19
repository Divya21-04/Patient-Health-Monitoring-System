# Patient Health Monitoring System
**HCLTech Career Shaper Programme | Project 4 | Embedded IoT**

Learner: Divya Singh  
Roll Number: 2300320230025  
College: ABES Engineering College, Ghaziabad  
Mentor: Neredimalli Jagadeep

## Project overview
An educational Embedded IoT prototype concept for collecting heart-rate, body-temperature and SpO₂ readings, displaying readings locally and presenting sample data in a dashboard. The supplied project brief lists ESP32, MAX30100, DHT11, OLED, Bluetooth and SD Card as tools/components.

## Important data provenance
`dataset/dataset.csv` currently contains **5,000 reproducible synthetic demonstration rows** generated for analysis and dashboard development. It is not real patient data and must not be represented as measurements from a tested physical device. The conversation-provided dataset excerpt exposed 103 rows, not the stated 500-row source file; therefore this package does not falsely claim to have merged 500 verified original rows. Replace/merge with the official 500-row file if supplied by the programme coordinator, preserving provenance.

## Repository contents
- `dataset/`: synthetic CSV and data dictionary
- `notebooks/`: EDA notebook with 3+ visualisations
- `src/`: cleaning script and Streamlit dashboard
- `hardware/`: ESP32 integration starter sketch (check wiring and library versions before use)
- `docs/`: synopsis, report, architecture diagram, demo script and ethics declaration

## Run locally
```bash
pip install -r requirements.txt
streamlit run src/dashboard.py
```
The dashboard runs locally at the URL printed by Streamlit. A public live URL is **not yet deployed**; deploy this repository through Streamlit Community Cloud after pushing it to GitHub.

## EDA notebook
Open `notebooks/EDA_Analysis.ipynb` in Jupyter or Google Colab. Run all cells from top to bottom.

## Hardware status
The ESP32 sketch is a starter integration template, not verified hardware firmware. Confirm exact board, sensor modules, wiring, voltage levels, libraries and calibration before physical testing. Do not use this prototype for diagnosis or emergency care.

## Safety and privacy
Patient IDs in this demonstration are synthetic pseudonyms. Do not upload identifiable health information. Obtain informed consent for any real measurements, restrict access, and follow applicable institutional and Indian data-protection requirements.

## Team / academic integrity
This is an individual project. Review, run, test and understand every component before submission. Replace placeholders and report measured results only after conducting the corresponding tests.
