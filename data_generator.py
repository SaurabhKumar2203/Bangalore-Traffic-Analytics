import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- CONFIGURATION ---
locations = ['Silk Board Junction', 'ORR - Bellandur', 'Whitefield Main Road', 'Hebbal Flyover', 'Tin Factory']
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
hours = pd.date_range(start=start_date, end=end_date, freq='H')

# --- HELPER FUNCTIONS ---
def get_time_of_day_factor(hour):
    # Morning Peak: 8-11 AM
    if 8 <= hour <= 11:
        return 0.85  # High congestion factor
    # Evening Peak: 17-21 PM
    elif 17 <= hour <= 21:
        return 0.95  # Severe congestion factor
    # Late Night: 23-5 AM
    elif hour >= 23 or hour <= 5:
        return 0.1   # Low congestion
    else:
        return 0.4   # Moderate

def get_rainfall(month):
    # Monsoon in Bangalore: June - Oct
    if 6 <= month <= 10:
        return np.random.choice([0, np.random.uniform(5, 50)], p=[0.6, 0.4]) # 40% chance of rain
    else:
        return np.random.choice([0, np.random.uniform(1, 10)], p=[0.95, 0.05]) # 5% chance of rain

# --- DATA GENERATION ---
data = []

for loc in locations:
    # Base speed limits per location (approx)
    base_speed = 60 if 'ORR' in loc else 40 
    metro_construction = 1 if loc in ['Silk Board Junction', 'ORR - Bellandur'] else 0
    
    for t in hours:
        # 1. Temporal Features
        hour = t.hour
        month = t.month
        is_weekend = 1 if t.weekday() >= 5 else 0
        
        # 2. Environmental Factors
        rainfall_mm = get_rainfall(month)
        
        # 3. Traffic Calculation Logic
        congestion_factor = get_time_of_day_factor(hour)
        
        # Adjust for weekend (less traffic)
        if is_weekend:
            congestion_factor *= 0.6
            
        # Adjust for Rain (Rain increases congestion, decreases speed)
        rain_penalty = 0
        if rainfall_mm > 0:
            rain_penalty = (rainfall_mm / 100) * 2.5 # Heavier rain = more penalty
            
        # Adjust for Metro Construction
        metro_penalty = 0.15 if metro_construction else 0
        
        # Final Congestion Level (0 to 1 scale, rarely hitting exactly 0 or 1)
        final_congestion = min(0.98, max(0.05, congestion_factor + rain_penalty + metro_penalty + np.random.normal(0, 0.05)))
        
        # Calculate Speed based on congestion
        # Higher congestion = Lower Speed
        avg_speed = max(5, base_speed * (1 - final_congestion))
        
        # Traffic Volume (Vehicle count per hour)
        volume = int(5000 * final_congestion)
        
        data.append({
            'Timestamp': t,
            'Location': loc,
            'Traffic_Volume': volume,
            'Avg_Speed_kmh': round(avg_speed, 1),
            'Congestion_Level': round(final_congestion * 100, 1), # as percentage
            'Rainfall_mm': round(rainfall_mm, 1),
            'Metro_Construction_Active': metro_construction,
            'Is_Weekend': is_weekend
        })

# --- DATAFRAME CREATION ---
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('bangalore_traffic_2025.csv', index=False)
print(f"Dataset generated successfully with {len(df)} rows.")
print(df.head())