from datetime import datetime
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

class Transaction:
    def __init__(self, amount, category, type, description):
        self.amount =amount
        self.category = category
        self.type = type
        self.description = description
        self.date = datetime.now()

    def __str__(self):
        return f"Transaction: {self.amount} | {self.category} | {self.type} | {self.description} |{self.date.strftime('%Y-%m-%d')}"

t = Transaction(500, "Food", "Expense", "Lunch")
print(t)

class BudgetTracker:
    def __init__(self):
        self.transactions = []
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        income = sum(t.amount for t in self.transactions if t.type == "income")
        expenses = sum(t.amount for t in self.transactions if t.type == "expense")
        return income - expenses

    def show_transactions(self):
        for t in self.transactions:
            print(t)

tracker = BudgetTracker()
tracker.add_transaction(Transaction(1000, "Salary", "income", "Monthly salary"))
tracker.add_transaction(Transaction(500, "Food", "expense", "Groceries"))
tracker.add_transaction(Transaction(200, "Transport", "expense", "Bus pass"))

tracker.show_transactions()
print(f"Balance: ${tracker.get_balance()}")

class Report:
    def __init__(self, tracker):
        self.tracker = tracker

    def summary(self):
        income = sum(t.amount for t in self.tracker.transactions if t.type == "income" )
        expenses = sum(t.amount for t in self.tracker.transactions if t.type == "expense")
        print(f"Total Income: ${income}")
        print(f"Total Expenses: ${expenses}")
        print(f"Balance: ${income - expenses}")

    def spending_by_category(self):
        categories = {}
        for t in self.tracker.transactions:
            if t.type == "expense":
                if t.category not in categories:
                    categories[t.category] = 0
                categories[t.category] += t.amount
        for category, amount in categories.items():
            print(f"{category}: ${amount}")
tracker = BudgetTracker()
tracker.add_transaction(Transaction(1000, "Salary", "income", "Monthly salary"))
tracker.add_transaction(Transaction(500, "Food", "expense", "Groceries"))
tracker.add_transaction(Transaction(200, "Transport", "expense", "Bus pass"))
tracker.add_transaction(Transaction(100, "Entertainment", "expense", "Netflix"))

report = Report(tracker)
report.summary()
print()
report.spending_by_category()

conn = sqlite3.connect("budget.db")
cursor = conn.cursor()
cursor.execute("""
      CREATE TABLE IF NOT EXISTS transactions (
      id INTEGER PRIMARY KEY,
      amount REAL,
      category TEXT,
      type TEXT,
      description TEXT,
      date TEXT
      )
""")
conn.commit()
print("Database created")

def save_transactions(transaction):
    cursor.execute("INSERT INTO transactions (amount, category, type, description, date) VALUES (?, ?, ?, ?, ?)", (transaction.amount, transaction.category, transaction.type, transaction.description, transaction.date.strftime('%Y-%m-%d')))
    conn.commit()

save_transactions(Transaction(1000, "Salary", "income", "Monthly salary"))
save_transactions(Transaction(500, "Food", "expense", "Groceries"))

cursor.execute("SELECT * FROM transactions")
print(cursor.fetchall())

df = pd.read_sql("SELECT * FROM transactions", conn)
print(df)

expenses = df[df.type == "expense"]
print(expenses)

expenses.groupby("category")["amount"].sum().plot(kind="bar")
plt.title("Expenses by category")
plt.xlabel("Category")
plt.ylabel("Expenses")
plt.show()