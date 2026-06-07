import pandas as pd
from database import get_all_products, get_all_sales

def analyze_sales():
    sales = get_all_sales()
    df = pd.DataFrame(sales, columns=['id', 'product', 'quantity', 'total', 'date'])
    print("\n=== Sales Analysis ===")
    print(f"Total Revenue: ${df['total'].sum():,.2f}")
    print(f"Total Sales: {len(df)}")
    print(f"Average Sale: ${df['total'].mean():,.2f}")
    return df