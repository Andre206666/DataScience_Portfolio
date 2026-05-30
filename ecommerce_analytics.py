import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

data = {
    'order_id': range(1, 501),
    'customer': [f'Customer_{i}' for i in np.random.randint(1, 51, 500)],
    'product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones', 'Watch'], 500),
    'category': np.random.choice(['Electronics', 'Accessories'], 500),
    'quantity': np.random.randint(1, 5, 500),
    'price': np.random.choice([999, 699, 499, 199, 299], 500),
    'date': pd.date_range('2024-01-01', periods=500, freq='D')
}

df = pd.DataFrame(data)
df.to_csv('orders.csv', index=False)
print(df.head())
print(f"\nDataset shape: {df.shape}")

print("'\n--- Dataset info ---")
print(df.info())

print("\n--- Basic statcs ---")
print(df.describe())

print("\n--- Any missing values? ---")
print(df.isnull().sum())


df['revenue'] = df['price'] * df['quantity']

print("\n--- Revenue Column Added ---")
print(df.head())
print(f"\nTotal Revenue: ${df['revenue'].sum():,.2f}")
print(f"Average Order Revenue: ${df['revenue'].mean():,.2f}")

revenue_by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
print("\n=== Revenue by product ===")
print(revenue_by_product)

revenue_by_category = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
print("\n=== Revenue by category ===")
print(revenue_by_category)

revenue_by_customer = df.groupby("customer")["revenue"].sum().sort_values(ascending=False).head(5)
print("\n=== Revenue by customer ===")
print(revenue_by_customer)

df['month'] = df['date'].dt.month

revenue_by_month = df.groupby("month")["revenue"].sum().sort_values(ascending=False)
print("\n=== Revenue by month ===")
print(revenue_by_month)

revenue_by_product.plot(kind='bar')
plt.title('Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.show()

revenue_by_month.plot(kind="bar")
plt.title("Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.show()


fig, axes = plt.subplots(1, 2, figsize=(12, 5))

revenue_by_product.plot(kind='bar', ax=axes[0], color='steelblue')
axes[0].set_title('Revenue by Product')
axes[0].set_xlabel('Product')
axes[0].set_ylabel('Revenue ($)')

revenue_by_month.plot(kind='bar', ax=axes[1], color='coral')
axes[1].set_title('Revenue by Month')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Revenue ($)')

plt.tight_layout()
plt.savefig('revenue_report.png')
plt.show()





import sqlite3

conn = sqlite3.connect('ecommerce.db')

df.to_sql('orders', conn, if_exists='replace', index=False)

print("Database created successfully!")


query = """
SELECT product, 
       SUM(revenue) as total_revenue,
       COUNT(*) as total_orders
FROM orders
GROUP BY product
ORDER BY total_revenue DESC
"""

result = pd.read_sql(query, conn)
print("\n=== SQL: Revenue by Product ===")
print(result)

query2 = """
SELECT category, 
       SUM(revenue) as total_revenue,
       COUNT(*) as total_orders
FROM orders
GROUP BY category
ORDER BY total_revenue DESC
"""

result2 = pd.read_sql(query2, conn)
print("\n=== SQL: Revenue by Category ===")
print(result2)

products_data = {
    'product': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Watch'],
    'brand': ['Dell', 'Apple', 'Samsung', 'Sony', 'Casio'],
    'warranty_years': [2, 1, 1, 1, 2]
}

products_df = pd.DataFrame(products_data)
products_df.to_sql('products', conn, if_exists='replace', index=False)
print("Products table created!")

query3 = """
SELECT o.customer, o.product, o.revenue, p.brand, p.warranty_years
FROM orders o
LEFT JOIN products p ON o.product = p.product
LIMIT 5
"""

result3 = pd.read_sql(query3, conn)
print("\n=== SQL: Orders with Product Details ===")
print(result3)

query4 = """
SELECT product,
       SUM(revenue) as total_revenue,
       RANK() OVER (ORDER BY SUM(revenue) DESC) as rank
FROM orders
GROUP BY product
"""

result4 = pd.read_sql(query4, conn)
print("\n=== SQL: Product Rankings ===")
print(result4)

print("\n" + "="*50)
print("=== FINAL BUSINESS REPORT ===")
print("="*50)
print(f"\nTotal Revenue: ${df['revenue'].sum():,.2f}")
print(f"Total Orders: {len(df)}")
print(f"Average Order Value: ${df['revenue'].mean():,.2f}")
print(f"\nTop Product: {revenue_by_product.index[0]}")
print(f"Top Customer: {revenue_by_customer.index[0]}")
print(f"Best Month: {revenue_by_month.index[0]}")
print("="*50)


revenue_by_product.to_csv('revenue_by_product.csv')
revenue_by_customer.to_csv('revenue_by_customer.csv')
revenue_by_month.to_csv('revenue_by_month.csv')
print("Results saved!")