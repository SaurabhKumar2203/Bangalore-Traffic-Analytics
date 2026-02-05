# File Name: traffic_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD THE DATA
# Ensure 'bangalore_traffic_2025.csv' is in the same folder as this script
df = pd.read_csv('bangalore_traffic_2025.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Feature Engineering: Extract Hour and Day Name for easier grouping
df['Hour'] = df['Timestamp'].dt.hour
df['Day_Name'] = df['Timestamp'].dt.day_name()

print("--- ANALYTICAL INSIGHTS REPORT ---\n")

# --- ANALYSIS 1: The "Monsoon Factor" (Correlation) ---
# We filter for days where it actually rained to see the severity
rainy_days = df[df['Rainfall_mm'] > 0]
dry_days = df[df['Rainfall_mm'] == 0]

avg_speed_dry = dry_days['Avg_Speed_kmh'].mean()
avg_speed_rain = rainy_days['Avg_Speed_kmh'].mean()
drop_percentage = ((avg_speed_dry - avg_speed_rain) / avg_speed_dry) * 100

print(f"1. MONSOON IMPACT:")
print(f"   - Average Speed (Dry): {avg_speed_dry:.2f} km/h")
print(f"   - Average Speed (Rain): {avg_speed_rain:.2f} km/h")
print(f"   - Insight: Rainfall causes a {drop_percentage:.1f}% drop in average traffic speed.\n")

# --- ANALYSIS 2: Best Time to Leave (Hourly Trend) ---
# We focus on a specific corridor: ORR - Bellandur (Weekday Only)
orr_traffic = df[(df['Location'] == 'ORR - Bellandur') & (df['Is_Weekend'] == 0)]
hourly_speed = orr_traffic.groupby('Hour')['Avg_Speed_kmh'].mean()

# Find the hour with the minimum speed (worst time) and max speed (best time) in the 8 AM - 8 PM window
business_hours = hourly_speed.loc[8:20]
worst_hour = business_hours.idxmin()
best_hour = business_hours.idxmax()

print(f"2. COMMUTER ADVISORY (ORR - Bellandur):")
print(f"   - Worst Time to Leave: {worst_hour}:00 (Avg Speed: {business_hours.min():.1f} km/h)")
print(f"   - Best Time to Leave: {best_hour}:00 (Avg Speed: {business_hours.max():.1f} km/h)")
print(f"   - Insight: Leaving at {best_hour}:00 instead of {worst_hour}:00 increases travel speed by {business_hours.max() - business_hours.min():.1f} km/h.\n")

# --- ANALYSIS 3: VISUALIZATION (Heatmap) ---
# Create a pivot table: Days of Week vs. Hours for Congestion
pivot_table = df.pivot_table(values='Congestion_Level', index='Day_Name', columns='Hour', aggfunc='mean')

# Reorder days for the plot to make it readable (Mon -> Sun)
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_table = pivot_table.reindex(days_order)

plt.figure(figsize=(12, 6))
sns.heatmap(pivot_table, cmap='coolwarm', cbar_kws={'label': 'Congestion Level (%)'})
plt.title('Bangalore Traffic Heatmap: Weekly Congestion Patterns')
plt.xlabel('Hour of Day')
plt.ylabel('Day of Week')

# This command displays the chart
plt.show()