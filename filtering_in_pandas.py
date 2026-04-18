import pandas as pd

data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Mouse'],
    'Price': [1200, 25, 300, 75, 25],
    'Stock': [5, 50, 10, 20, 50],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Accessories']
}
df = pd.DataFrame(data)
cheap_products = df[df['Price'] < 100] #boolean filtering
category_stats = df.groupby('Category')['Price'].mean()

print("\n--- Average Price per Category ---")
print(category_stats)

