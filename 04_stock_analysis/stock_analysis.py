import yfinance as yf
import matplotlib.pyplot as plt

stock = yf.download("AAPL", start="2023-01-01", end="2024-01-01")
print(stock.head())
print(f"\nShape: {stock.shape}")
print(f"\n{stock.info()}")

print(f"\n{stock.describe()}")

print(f"\n{stock.isnull().sum()}")

stock['Close']['AAPL'].plot(kind='line')
plt.title("Price overtime")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

stock['Close']['AAPL'].pct_change().plot(kind="line")
plt.title("Price changed each day")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

stock = yf.download(["AAPL", "MSFT", "GOOGL"], start="2023-01-01", end="2024-01-01")
print(stock.head())
print(f"\n{stock.info()}")
print(f"\n{stock.describe()}")
print(f"\n{stock.isnull().sum()}")

stock["Close"].plot(kind="line")
plt.title("Price changes by this 3 companies each day")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

normalized = stock["Close"] / stock["Close"].iloc[0] * 100
normalized.plot(kind="line")
plt.title("Percentage growth from the start")
plt.xlabel("Date")
plt.ylabel("Percentage")
plt.legend()
plt.show()

for ticker in ['AAPL', 'MSFT', 'GOOGL']:
    start_price = stock['Close'][ticker].iloc[0]
    end_price = stock['Close'][ticker].iloc[-1]
    growth = (end_price - start_price) / start_price * 100
    print(f"{ticker}: Start ${start_price:.2f} | End ${end_price:.2f} | Growth {growth:.1f}%")