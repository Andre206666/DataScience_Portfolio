import pandas as pd
import matplotlib.pyplot as plt
from database import get_all_sales

def plot_sales():
    sales = get_all_sales()
    df = pd.DataFrame(sales, columns=['id', 'product', 'quantity', 'total', 'date'])
    df.groupby("product")["total"].sum().plot(kind="bar")
    plt.xlabel("Product")
    plt.ylabel("Quantity")
    plt.show()