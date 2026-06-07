import pandas as pd
import numpy as np

df = pd.DataFrame({
    "sale_id": range(1, 1001),
    "date": pd.date_range('2024-01-01', periods=1000, freq='D'),
    "product": np.random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Watch'], 1000),
    "region": np.random.choice(['North', 'South', 'East', 'West'], 1000),
    "quantity": np.random.randint(1, 20, 1000),
    "price": np.random.choice([999, 699, 499, 199, 299], 1000),
    "target": np.random.randint(5000, 15000, 1000)
})

print(df.head())
print(f"\nDataset shape: {df.shape}")

df["revenue"] = df["price"] * df["quantity"]
print(df)

revenue_by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
revenue_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by product: ")
print(revenue_by_product)

print("\nRevenue by region: ")
print(revenue_by_region)

df["month"]  = df["date"].dt.month
revenue_by_month = df.groupby('month')['revenue'].sum().sort_values(ascending=False)
print("\nRevenue by month: ")
print(revenue_by_month)

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

revenue_by_product.plot(kind='bar', ax=axes[0][0])
axes[0][1].set_title("Revenu by product")

revenue_by_region.plot(kind='bar', ax=axes[0][1])
axes[0][1].set_title("Revenue by region")

revenue_by_month.plot(kind="bar", ax=axes[1][0])
axes[0][1].set_title("Revenue by month")

df.groupby('month')['revenue'].sum().plot(kind='bar', ax=axes[1][1])
axes[0][1].set_title("Revenue by month")

plt.tight_layout()
plt.savefig('sales_dashboard.png')
plt.show()