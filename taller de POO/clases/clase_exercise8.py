class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        self.items.append((product, quantity))
        print(f"{quantity} {product.name}(s) added to the cart.")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total

    def make_payment(self, amount_paid):
        total = self.calculate_total()
        if amount_paid >= total:
            change = amount_paid - total
            print(f"Payment successful. Your change is: ${change:.2f}")
            self.items = []
        else:
            print("Insufficient amount to make the payment.")



product1 = Product("Shirt", 20.999)
product2 = Product("Pants", 39.999)
product3 = Product("Shoes", 59.999)
product4 = Product("Hat", 9.999)
product5 = Product("Socks", 4.999)

available_products = [product1, product2, product3, product4, product5]            

def show_products():
    print("\nAvailable products:")
    for i in range(len(available_products)):
        print(f"{i + 1}. {available_products[i]}")

def show_menu():
    print("\nMenu:")
    print("1. Add product to cart")
    print("2. Calculate total")
    print("3. Exit and make payment")
