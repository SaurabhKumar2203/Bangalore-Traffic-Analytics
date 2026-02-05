import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. PAGE SETUP
st.set_page_config(page_title="Debug Mode", layout="wide")
st.title("🛠️ Debugging Dashboard")

# 2. DIAGNOSTICS: Check if file exists
st.subheader("1. File System Check")
current_files = os.listdir('.')
st.write("Files in current directory:", current_files)

if 'bangalore_traffic_2025.csv' not in current_files:
    st.error("❌ CRITICAL ERROR: 'bangalore_traffic_2025.csv' not found. Check filename case sensitivity!")
    st.stop()
else:
    st.success("✅ CSV file found.")

# 3. LOAD DATA WITHOUT CACHE (To ensure fresh load)
def load_data():
    try:
        df = pd.read_csv('bangalore_traffic_2025.csv')
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df['Hour'] = df['Timestamp'].dt.hour
        df['Day_Name'] = df['Timestamp'].dt.day_name()
        # Ensure Is_Weekend is 0 or 1
        df['Is_Weekend'] = df['Is_Weekend'].fillna(0).astype(int)
        return df
    except Exception as e:
        return str(e)

df = load_data()

# 4. DATA QUALITY CHECK
st.subheader("2. Data Load Check")
if isinstance(df, str):
    st.error(f"❌ Error loading CSV: {df}")
    st.stop()
else:
    st.write(f"✅ Data Loaded. Shape: {df.shape} (Rows, Columns)")
    st.write("First 5 rows of raw data:", df.head())

# 5. FILTER DEBUGGING
st.subheader("3. Filter Logic Check")
locations = df['Location'].unique()
st.write("Available Locations:", locations)

selected_location = st.selectbox("Select Traffic Corridor:", locations)
selected_day_type = st.radio("Day Type:", ["Weekday", "Weekend"])

is_weekend_filter = 1 if selected_day_type == "Weekend" else 0

# Apply Filter
filtered_df = df[(df['Location'] == selected_location) & (df['Is_Weekend'] == is_weekend_filter)]

st.write(f"Filtering for: Location='{selected_location}' AND Is_Weekend={is_weekend_filter}")
st.write(f"Rows found: {len(filtered_df)}")

if filtered_df.empty:
    st.warning("⚠️ No rows found! Checking why...")
    # Drill down: Check just location
    loc_check = df[df['Location'] == selected_location]
    st.write(f"Rows with Location '{selected_location}': {len(loc_check)}")
    # Drill down: Check just weekend
    weekend_check = df[df['Is_Weekend'] == is_weekend_filter]
    st.write(f"Rows with Is_Weekend '{is_weekend_filter}': {len(weekend_check)}")
else:
    st.success("✅ Filter works! Plotting chart...")
    
    # 6. PLOT
    hourly_trend = filtered_df.groupby('Hour')[['Avg_Speed_kmh']].mean().reset_index()
    fig = px.line(hourly_trend, x='Hour', y='Avg_Speed_kmh', title="Debug Chart")
    st.plotly_chart(fig)