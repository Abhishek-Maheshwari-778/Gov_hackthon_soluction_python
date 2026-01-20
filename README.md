# Aadhaar Seva Pulse: Smart Resource Allocation System
**Team ID:** UIDAI_10441  
**Event:** Online Hackathon on Data-driven Innovation on Aadhaar 2026

![Project Status](https://img.shields.io/badge/Status-Submission%20Ready-success) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Project Overview
**"Tracking India's Pulse through Aadhaar Updates"**

This project transforms raw anonymous Aadhaar transaction logs into a **High-Frequency Decision Support System**. Traditional census data is static (updated every 10 years). Our solution uses **Real-Time Demographic & Biometric Updates** to provide immediate insights into:
1.  **Internal Migration:** Tracking urbanization trends via Address Updates.
2.  **Digital Inclusion:** Monitoring biometric updates to identify digitally excluded populations.
3.  **Anomaly Detection:** identifying districts with unusual stress on infrastructure.

---

## 🚀 Key Technical Features
We moved beyond basic dashboards to implement **Advanced Analytics & Machine Learning**:

### 1. Unsupervised Machine Learning
*   **Isolation Forest (Anomaly Detection):** Automatically checks thousands of data points to find "Outlier Districts" — locations with sudden, unexplainable spikes in migration or updates that require immediate government attention.
*   **K-Means Clustering:** Segments districts into "Growth Profiles" (e.g., *High Migration Hubs*, *Stable Rural Areas*) for targeted policy making.

### 2. Advanced Visualization
*   **Interactive Heatmaps:** State-vs-Metric matrix to compare performance instantly.
*   **Correlation Matrices:** Discovery of hidden relationships (e.g., *Does high mobile linkage correlate with lower migration?*).

---

## 📂 Repository Structure
This repository is clean and strictly organized for reproducibility:

```text
root/
├── work.ipynb                     # 🧠 MAIN ENGINE: Run this single file for end-to-end analysis.
├── AADHAARSEVAPULSE_Team_UIDAI_10441.docx  # 📄 FINAL REPORT: Comprehensive research paper & findings.
├── README.md                      # 📘 Documentation (You are here).
├── requirements.txt               # 📦 Dependencies list.
├── processed_district_data.csv    # 💾 Output dataset (Cleaned & Aggregated).
├── api_data_aadhar_biometric/     # 📂 Raw Data: Biometric update logs.
├── api_data_aadhar_demographic/   # 📂 Raw Data: Demographic update logs.
└── api_data_aadhar_enrolment/     # 📂 Raw Data: Enrolment logs.
```

---

## 🛠️ How to Run the Code
We have consolidated the entire pipeline (Data Cleaning -> ML Modeling -> Visualization) into **one Jupyter Notebook**.

### Step 1: Install Dependencies
```bash
pip install pandas plotly notebook numpy seaborn matplotlib scikit-learn
```

### Step 2: Launch the Notebook
1.  Open **`work.ipynb`**.
2.  If strictly necessary, ensure the data paths in `Cell 3` match the folder names above.
3.  Click **"Run All"**.

### Step 3: Explore Results
*   **Top of Notebook:** Data Loading & Cleaning stats.
*   **Middle:** Interactive Plotly Charts (Migration trends, Age composition).
*   **Bottom:** **Anomaly Detection Results** (List of Critical Districts).

---

## 📊 Sample Insights
*   **Migration Hotspots:** Identified "East Godavari" and "Guntur" as top districts for address updates.
*   **Anomalies:** Detected **23 Districts** behaving normally on macro-metrics but showing specific stress signals on micro-metrics.

---
*Submitted by Team UIDAI_10441*
