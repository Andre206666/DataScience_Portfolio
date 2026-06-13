from datetime import datetime, timedelta
import random
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt



class Transaction:
    def __init__(self, amount, category, type_, description, date=None):
        self.amount = amount
        self.category = category
        self.type_ = type_.lower()
        self.description = description
        self.date = date if date else datetime.now()

    def __str__(self):
        return (f"Transaction: {self.amount} | {self.category} | "
                f"{self.type_} | {self.description} | {self.date.strftime('%Y-%m-%d')}")


class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        income   = sum(t.amount for t in self.transactions if t.type_ == "income")
        expenses = sum(t.amount for t in self.transactions if t.type_ == "expense")
        return income - expenses

    def show_transactions(self):
        for t in self.transactions:
            print(t)


class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit

    def check(self, transactions):
        spent  = sum(t.amount for t in transactions
                     if t.category == self.category and t.type_ == "expense")
        diff   = self.limit - spent
        status = "OK" if spent <= self.limit else "OVER BUDGET"
        word   = "remaining" if diff >= 0 else "over"
        return (f"{self.category}: spent ${spent:.2f} / limit ${self.limit:.2f} "
                f"→ {status} (${abs(diff):.2f} {word})")


class Report:
    def __init__(self, tracker):
        self.tracker = tracker

    def summary(self):
        income   = sum(t.amount for t in self.tracker.transactions if t.type_ == "income")
        expenses = sum(t.amount for t in self.tracker.transactions if t.type_ == "expense")
        print(f"Total Income:   ${income:.2f}")
        print(f"Total Expenses: ${expenses:.2f}")
        print(f"Balance:        ${income - expenses:.2f}")

    def spending_by_category(self):
        categories = {}
        for t in self.tracker.transactions:
            if t.type_ == "expense":
                categories[t.category] = categories.get(t.category, 0) + t.amount
        for category, amount in categories.items():
            print(f"{category}: ${amount:.2f}")

def generate_sample_data(tracker):
    expense_categories = ["Food", "Transport", "Entertainment", "Utilities", "Health"]
    base = datetime.now() - timedelta(days=90)
    random.seed(42)

    for i in range(3):
        d = base + timedelta(days=i * 30)
        tracker.add_transaction(Transaction(15000, "Salary",     "income",  "Monthly salary", d))
        tracker.add_transaction(Transaction(3000,  "Freelance",  "income",  "Client project", d + timedelta(days=5)))
        tracker.add_transaction(Transaction(500,   "Investment", "income",  "Dividends",      d + timedelta(days=15)))

    for _ in range(40):
        cat    = random.choice(expense_categories)
        amount = round(random.uniform(100, 3000), 2)
        d      = base + timedelta(days=random.randint(0, 89))
        tracker.add_transaction(Transaction(amount, cat, "expense", f"{cat} purchase", d))

def create_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id          INTEGER PRIMARY KEY,
            amount      REAL,
            category    TEXT,
            type        TEXT,
            description TEXT,
            date        TEXT
        )
    """)
    conn.commit()
    print("Database created")

def save_transactions(tracker, conn):
    cursor = conn.cursor()
    for t in tracker.transactions:
        cursor.execute(
            "INSERT INTO transactions (amount, category, type, description, date) VALUES (?, ?, ?, ?, ?)",
            (t.amount, t.category, t.type_, t.description, t.date.strftime("%Y-%m-%d"))
        )
    conn.commit()
    print(f"Saved {len(tracker.transactions)} transactions to database")

def pandas_summary(df):
    print("\n── PANDAS SUMMARY ──────────────────────────")

    income   = df[df["type"] == "income"]["amount"].sum()
    expenses = df[df["type"] == "expense"]["amount"].sum()
    print(f"Total Income:   ${income:,.2f}")
    print(f"Total Expenses: ${expenses:,.2f}")
    print(f"Balance:        ${income - expenses:,.2f}")

    print("\nExpenses by category:")
    by_cat = (df[df["type"] == "expense"]
                .groupby("category")["amount"]
                .sum()
                .sort_values(ascending=False))
    print(by_cat.to_string())

    print("\nMonthly totals:")
    df["month"] = pd.to_datetime(df["date"]).dt.to_period("M")
    monthly = (df.groupby(["month", "type"])["amount"]
                 .sum()
                 .unstack(fill_value=0))
    print(monthly.to_string())

def plot_dashboard(df):
    df["date"]  = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle("Personal Finance Dashboard", fontsize=16, fontweight="bold")

    # 1 — Bar: expenses by category
    expenses = df[df["type"] == "expense"]
    expenses.groupby("category")["amount"].sum().plot(kind="bar", ax=axes[0, 0], color="#e74c3c")
    axes[0, 0].set_title("Expenses by Category")
    axes[0, 0].set_xlabel("Category")
    axes[0, 0].set_ylabel("Amount ($)")
    axes[0, 0].tick_params(axis="x", rotation=30)

    expenses.groupby("category")["amount"].sum().plot(
        kind="pie", ax=axes[0, 1], autopct="%1.1f%%", startangle=140
    )
    axes[0, 1].set_title("Expense Breakdown")
    axes[0, 1].set_ylabel("")

    monthly = (df.groupby(["month", "type"])["amount"]
                 .sum()
                 .unstack(fill_value=0))
    monthly.plot(kind="bar", ax=axes[1, 0], color=["#e74c3c", "#2ecc71"])
    axes[1, 0].set_title("Monthly Income vs Expenses")
    axes[1, 0].set_xlabel("Month")
    axes[1, 0].set_ylabel("Amount ($)")
    axes[1, 0].tick_params(axis="x", rotation=30)

    df_sorted = df.sort_values("date").copy()
    df_sorted["signed"]  = df_sorted.apply(
        lambda r: r["amount"] if r["type"] == "income" else -r["amount"], axis=1
    )
    df_sorted["balance"] = df_sorted["signed"].cumsum()
    axes[1, 1].plot(df_sorted["date"], df_sorted["balance"], color="#3498db", linewidth=2)
    axes[1, 1].fill_between(df_sorted["date"], df_sorted["balance"], alpha=0.15, color="#3498db")
    axes[1, 1].set_title("Balance Over Time")
    axes[1, 1].set_ylabel("Balance ($)")
    axes[1, 1].tick_params(axis="x", rotation=30)

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/dashboard.png", dpi=150, bbox_inches="tight")
    print("\nDashboard saved → dashboard.png")
    plt.show()


tracker = BudgetTracker()
generate_sample_data(tracker)

print("── TRANSACTIONS ─────────────────────────────")
tracker.show_transactions()

print("\n── REPORT ───────────────────────────────────")
report = Report(tracker)
report.summary()
print()
report.spending_by_category()

print("\n── BUDGETS ─")
budgets = [Budget("Food", 5000), Budget("Entertainment", 2000), Budget("Transport", 4000)]
for b in budgets:
    print(b.check(tracker.transactions))

print("\n── DATABASE ─")
conn = sqlite3.connect("budget.db")
create_db(conn)
save_transactions(tracker, conn)

cursor = conn.cursor()
cursor.execute("SELECT * FROM transactions LIMIT 5")
print("Sample rows:", cursor.fetchall())

df = pd.read_sql("SELECT * FROM transactions", conn)
pandas_summary(df)

plot_dashboard(df)

conn.close()