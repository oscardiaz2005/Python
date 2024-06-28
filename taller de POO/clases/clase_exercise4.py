class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_stock(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity += quantity
                break

    def calculate_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value



        