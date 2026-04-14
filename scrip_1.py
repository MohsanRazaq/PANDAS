import pandas as pd

# 1. Create a DataFrame -- simple script
data = {
    'Timestamp': ['2026-04-14', '2026-04-14', '2026-04-15', '2026-04-15'],
    'Source_IP': ['192.168.1.1', '10.0.0.5', '192.168.1.20', '10.0.0.5'],
    'Port': [80, 443, 22, 443],
    'Traffic_MB': [150, 1200, 45, 800]
}

df = pd.DataFrame(data)

# 2. Filter data (e.g., find high traffic sessions > 500MB)
high_traffic = df[df['Traffic_MB'] > 500]

# 3. Grouping and Aggregation (Sum traffic by Source_IP)
traffic_summary = df.groupby('Source_IP')['Traffic_MB'].sum()

# 4. Results
print("--- Full DataFrame ---")
print(df)

print("\n--- High Traffic Alerts ---")
print(high_traffic)

print("\n--- Total Traffic per IP ---")
print(traffic_summary)