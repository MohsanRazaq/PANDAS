import pandas as pd

# Step 1: Create sample dataset (like a CSV)
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
    'Product': ['Laptop', 'Mobile', 'Laptop', 'Tablet'],
    'Region': ['Lahore', 'Karachi', 'Lahore', 'Islamabad'],
    'Sales': [50000, 30000, 52000, None]  
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
lahore_data = df[df['Region'] == 'Lahore']


grouped = df.groupby('Product')['Sales'].sum()


sorted_data = df.sort_values(by='Sales', ascending=False)

df['Sales_After_Tax'] = df['Sales'] * 1.10

print("Cleaned Data:\n", df)
print("\nLahore Data:\n", lahore_data)
print("\nTotal Sales by Product:\n", grouped)
print("\nSorted Data:\n", sorted_data)
