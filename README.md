# 🚦 Bangalore Urban Mobility & Traffic Analytics

## 📌 Project Overview
Bangalore was ranked as the second most congested city globally in 2025. This project analyzes traffic patterns to identify bottlenecks, correlate congestion with external factors (rainfall, events), and propose optimal departure windows for commuters in major tech corridors like the Outer Ring Road (ORR).

## 🛠️ Tech Stack
* **Python:** Core language for analysis.
* **Pandas:** Data cleaning and aggregation.
* **Streamlit:** Interactive web dashboard.
* **Plotly/Seaborn:** Data visualization.
* **Git:** Version control.

## 📊 Key Features
* **Synthetic Data Pipeline:** Generated a high-fidelity dataset simulating 8,760 hourly records of Bangalore traffic.
* **Monsoon Gridlock Analysis:** Quantified the impact of rainfall on average travel speeds (found a ~25% drop).
* **Commuter Advisory System:** An interactive tool to calculate the "Best Time to Leave" to minimize commute time.

## 🚀 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Bangalore-Traffic-Analytics.git](https://github.com/YOUR_USERNAME/Bangalore-Traffic-Analytics.git)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the dashboard:
    ```bash
    streamlit run app.py
    ```

## 📈 Insights
* **Weekend vs. Weekday:** Distinct visual patterns showing "High Stress Zones" during weekday peaks (9 AM & 6 PM).
* **Rain Penalty:** Even light rainfall (>5mm) triggers a quantifiable drop in traffic velocity on the ORR corridor.