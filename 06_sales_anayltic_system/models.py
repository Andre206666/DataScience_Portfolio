from datetime import datetime

class Product:
    def __init__(self, name , price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Category: {self.category}"


class Sale:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.date = datetime.now()
        self.total = product.price * quantity

    def __str__(self):
        return f"Product: {self.product.name} | Quantity: {self.quantity} | Total: ${self.total:.2f} | Date: {self.date.strftime('%d/%m/%Y')}"

class SalesSystem:
    def __init__(self):
        self.products = []
        self.sales = []

    def add_product(self, product):
        self.products.append(product)

    def make_sale(self, product, quantity):
        self.sales.append(Sale (product=product, quantity=quantity))

    def show_products(self):
        for product in self.products:
            print(product)

    def show_sales(self):
        for sale in self.sales:
            print(sale)

