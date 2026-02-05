# 🚦 Bangalore Urban Mobility & Traffic Analytics

## 📌 Project Overview
Bangalore was ranked as the second most congested city globally in 2025. This project analyzes traffic patterns to identify bottlenecks, correlate congestion with external factors (rainfall, events), and propose optimal departure windows for commuters in major tech corridors like the Outer Ring Road (ORR).

## 🛠️ Tech Stack
* **Python:** Core language for analysis.
* **Pandas:** Data cleaning and aggregation.
* **Streamlit:** Frontend for the interactive dashboard.
* **Plotly & Matplotlib:** Dynamic and static data visualization.
* **Git:** Version control.

---

## 📸 Project Gallery

### 1. The Interactive Dashboard (Streamlit)
*A user-friendly web interface allowing commuters to filter by corridor (e.g., ORR, Silk Board) and day type to see real-time "Best Time to Leave" recommendations.*

**Dashboard View 1: Main Interface & KPIs**

<img width="1406" height="637" alt="streamlit1" src="https://github.com/user-attachments/assets/c2e4007e-f343-4ce8-8741-97fffabf9403" />

*(Figure 1: Overview of key metrics including average speed, traffic volume, and rain impact)*

**Dashboard View 2: Detailed Traffic Trends**

<img width="1408" height="598" alt="streamlit2" src="https://github.com/user-attachments/assets/7ccc04b6-d81f-4a7d-9715-0487bf653425" />

*(Figure 2: Granular hourly analysis showing speed drops during peak windows)*

---

### 2. Statistical Deep Dive (Matplotlib)
*Before building the dashboard, I performed Exploratory Data Analysis (EDA) to validate the "Weekend vs. Weekday" hypothesis.*

**Correlation Heatmap**

<img width="1421" height="744" alt="Screenshot 2026-02-05 155711" src="https://github.com/user-attachments/assets/9e73357a-5522-4460-aef1-56b44d526027" />

*(Figure 3: Weekly congestion heatmap showing clear "Red Zones" (High Congestion) during weekday rush hours vs. "Blue Zones" (Free Flow) on weekends)*

---

## 📊 Analytics Results
* **Synthetic Data Pipeline:** Generated a high-fidelity dataset simulating 8,760 hourly records of Bangalore traffic.
* **Monsoon Gridlock Analysis:** Quantified the impact of rainfall on average travel speeds (found a ~25% drop).
* **Commuter Advisory System:** Logic developed to calculate the "Best Time to Leave" to minimize commute time.

## 🚀 How to Run Locally
Since this is a portfolio project, you can run the dashboard locally on your machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Bangalore-Traffic-Analytics.git](https://github.com/YOUR_USERNAME/Bangalore-Traffic-Analytics.git)
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Launch the Dashboard:**
    ```bash
    streamlit run app.py
    ```
    *The app will open in your default web browser at http://localhost:8501*
