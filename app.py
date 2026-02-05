import streamlit as st
import pandas as pd
import plotly.express as px

# 1. PAGE SETUP
st.set_page_config(page_title="Bangalore Traffic Advisor", layout="wide")

st.title("🚦 Bangalore Urban Mobility & Traffic Analytics")
st.markdown("### Smart City Dashboard | Q1 2025 Analysis")

# 2. LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv('bangalore_traffic_2025.csv')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Hour'] = df['Timestamp'].dt.hour
    df['Day_Name'] = df['Timestamp'].dt.day_name()
    # Ensure weekend flag is integer for cleaner filtering
    df['Is_Weekend'] = df['Is_Weekend'].fillna(0).astype(int)
    return df

try:
    df = load_data()

    # 3. SIDEBAR FILTERS
    st.sidebar.header("Commuter Filters")
    selected_location = st.sidebar.selectbox("Select Traffic Corridor:", df['Location'].unique())
    selected_day_type = st.sidebar.radio("Day Type:", ["Weekday", "Weekend"])

    # Filter Logic
    is_weekend_filter = 1 if selected_day_type == "Weekend" else 0
    filtered_df = df[(df['Location'] == selected_location) & (df['Is_Weekend'] == is_weekend_filter)]

    # 4. KPI METRICS (Top Row)
    col1, col2, col3 = st.columns(3)

    avg_speed = filtered_df['Avg_Speed_kmh'].mean()
    peak_traffic = filtered_df['Traffic_Volume'].max()
    rain_days = filtered_df[filtered_df['Rainfall_mm'] > 0].shape[0]

    col1.metric("Avg Speed (Selected Corridor)", f"{avg_speed:.1f} km/h")
    col2.metric("Peak Volume Recorded", f"{peak_traffic:,} vehicles")
    col3.metric("Rainy Days in Dataset", f"{rain_days} days")

    # 5. CHARTS

    # Chart 1: Hourly Traffic Trend
    st.subheader(f"Hourly Traffic Trends: {selected_location}")
    hourly_trend = filtered_df.groupby('Hour')[['Avg_Speed_kmh', 'Congestion_Level']].mean().reset_index()

    fig_line = px.line(hourly_trend, x='Hour', y='Avg_Speed_kmh', 
                    title="Average Speed by Hour of Day",
                    labels={'Avg_Speed_kmh': 'Speed (km/h)'},
                    markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

    # Chart 2: Rain Impact Analysis
    st.subheader("💧 The Monsoon Effect: Rain vs. Speed")
    
    # We use the full dataset for this specific location to show the contrast
    loc_df = df[df['Location'] == selected_location].copy()
    
    # Binning rainfall for clearer charts
    loc_df['Rain_Category'] = pd.cut(loc_df['Rainfall_mm'], bins=[-1, 0, 10, 50], labels=['No Rain', 'Light Rain', 'Heavy Rain'])
    rain_summary = loc_df.groupby('Rain_Category', observed=True)['Avg_Speed_kmh'].mean().reset_index()

    fig_bar = px.bar(rain_summary, x='Rain_Category', y='Avg_Speed_kmh', 
                    color='Rain_Category', 
                    title="Impact of Rain Intensity on Traffic Speed")
    st.plotly_chart(fig_bar, use_container_width=True)

    # 6. INSIGHT GENERATOR
    best_hour = hourly_trend.loc[hourly_trend['Avg_Speed_kmh'].idxmax()]['Hour']
    st.info(f"💡 **Analyst Insight:** On {selected_day_type}s at {selected_location}, the best time to travel is **{best_hour}:00**.")

except Exception as e:
    st.error(f"An error occurred while loading the data: {e}")