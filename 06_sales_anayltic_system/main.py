import database
from models import Product, Sale, SalesSystem
from database import save_product, save_sale, get_all_products, get_all_sales
from analysis import analyze_sales
from visualizations import plot_sales



p1 = Product("Laptop", 999, "Electronics")
p2 = Product("Phone", 699, "Electronics")

system = SalesSystem()
system.add_product(p1)
system.add_product(p2)
system.make_sale(p1, 3)
system.make_sale(p2, 2)

save_product(p1)
save_product(p2)
save_sale(system.sales[0])
save_sale(system.sales[1])


system.show_products()
system.show_sales()

print("\n=== Products in Database ===")
for p in get_all_products():
    print(p)

print("\n=== Sales in Database ===")
for s in get_all_sales():
    print(s)

analyze_sales()

plot_sales()