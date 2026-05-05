import pandas as pd

data = {
    'Timestamp': ['2026-04-14', '2026-04-14', '2026-04-15', '2026-04-15'],
    'Source_IP': ['192.168.1.1', '10.0.0.5', '192.168.1.20', '10.0.0.5'],
    'Port': [80, 443, 22, 443],
    'Traffic_MB': [150, 1200, 45, 800]
}

df = pd.DataFrame(data)
high_traffic = df[df['Traffic_MB'] > 500]

traffic_summary = df.groupby('Source_IP')['Traffic_MB'].sum()

print("--- Full DataFrame ---")
print(df)

print("\n--- High Traffic Alerts ---")
print(high_traffic)

print("\n--- Total Traffic per IP ---")
print(traffic_summary)