import sqlite3
import pandas as pd

conn = sqlite3.connect("stocks.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS stock_prices (
        date TEXT,
        ticker TEXT,
        close REAL,
        volumen INTEGER
    )
""")

conn.commit()

def save_stock_data(df, ticker):
    df_save = pd.DataFrame({
        "data": df.index.astype(str),
        "ticker": ticker,
        "close": df["Close"][ticker].values,
        "volume": df["Volume"][ticker].values
    })
    df_save.to_sql("stock_prices", conn, if_exists="replace", index=False)

def get_stock_data(ticker):
    return pd.read_sql(f"SELECT * FROM stock_prices WHERE ticker='{ticker}'", conn)
