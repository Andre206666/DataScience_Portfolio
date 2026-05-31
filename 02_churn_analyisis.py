import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "age": np.random.randint(18, 70, 1000),
    "tenure": np.random.randint(1, 60, 1000),
    "monthly_spend": np.random.randint(20, 500, 1000),
    "num_purchases": np.random.randint(1, 50, 1000),
    "churned": np.random.choice([0, 1], 1000),
    "customer_id": range(1,1001)

})
print(df)

print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df['churned'].value_counts())

print("\n=== Average age of churned vs non churned ===")
print(df.groupby("churned")["age"].mean())

print("\n=== Average tenure of churned vs non-churned customers ===")
print(df.groupby("churned")["tenure"].mean())

print("\n=== Average monthly spend of churned vs non-churned customers ===")
print(df.groupby("churned")["monthly_spend"].mean())

import sqlite3

conection = sqlite3.connect("churn_analysis.db")
df.to_sql("churn_analysis", con=conection, if_exists='replace')

print("The database has been created successfully")

query = """
SELECT churned,
       AVG(age) AS avg_age,
       AVG(tenure) AS avg_tenure,
       AVG(monthly_spend) AS avg_monthly_spend,
       COUNT (*) AS num_churned
       FROM churn_analysis
       GROUP BY churned
       ORDER BY churned"""

result = pd.read_sql(query, con=conection)
print(result)

df['churned'].value_counts().plot(kind="bar")
plt.title("Churn data analysis")
plt.xlabel("Churned")
plt.ylabel("Count")
plt.show()

df.groupby("churned")["monthly_spend"].mean().plot(kind="bar")
plt.title("Average monthly spend by churned")
plt.xlabel("Churned")
plt.ylabel("monthly spend")
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

df['churned'].value_counts().plot(kind='bar', ax=axes[0])
df.groupby('churned')['monthly_spend'].mean().plot(kind='bar', ax=axes[1])

plt.tight_layout()
plt.show()

axes[0].set_title("Churn data analysis")
axes[0].set_xlabel("Churned")
axes[0].set_ylabel("Monthly spend")

axes[1].set_title("Average monthly spend by churned")
axes[1].set_xlabel("Churned")
axes[1].set_ylabel("Monthly spend")

plt.tight_layout()
plt.savefig("Churn analysis plot.png")
plt.show()

print("\n=== Churn analysis report ===")

print("="*50)
print("=== CHURN ANALYSIS REPORT ===")
print("="*50)
print(f"Total customers: {len(df)}")
print(f"Total churned: {df['churned'].sum()}")
print(f"Churn rate: {df['churned'].sum() / len(df) * 100:.1f}%")
print(f"Avg age of churned: {df[df['churned']==1]['age'].mean():.1f}")
print(f"Avg spend of churned: ${df[df['churned']==1]['monthly_spend'].mean():.2f}")
print("="*50)