products = {
    1: ["Apples", 5000, 10],
    2: ["Pears", 7000, 5],
    3: ["Cookies", 3000, 25],
    4: ["Ham", 10000, 3]
}

def add_product(code, name, price, inventory):
    if code in products:
        return "The product already exists."
    products[code] = [name, price, inventory]
    return "Product added successfully."

def update_product(code, name, price, inventory):
    if code not in products:
        return "The product does not exist."
    products[code] = [name, price, inventory]
    return "Product updated successfully."

def delete_product(code):
    if code not in products:
        return "The product does not exist."
    del products[code]
    return "Product deleted successfully."

def get_max_price():
    max_price = -1
    for product in products.values():
        if product[1] > max_price:
            max_price = product[1]
    return max_price

def get_min_price():
    min_price = float('inf')
    for product in products.values():
        if product[1] < min_price:
            min_price = product[1]
    return min_price

def products_with_max_price():
    max_price = get_max_price()
    max_price_products = [name for name, price, inventory in products.values() if price == max_price]
    return max_price_products

def products_with_min_price():
    min_price = get_min_price()
    min_price_products = [name for name, price, inventory in products.values() if price == min_price]
    return min_price_products

def average_price():
    total_price = sum([product[1] for product in products.values()])
    return total_price / len(products)

def total_inventory_value():
    total_value = sum([product[1] * product[2] for product in products.values()])
    return total_value

def show_menu():
    print("\nInventory Management Menu")
    print("1. Add product")
    print("2. Update product")
    print("3. Delete product")
    print("4. Show products with the highest price")
    print("5. Show products with the lowest price")
    print("6. Show average prices")
    print("7. Show total inventory value")
    print("8. Exit")

def execute_menu():
    while True:
        show_menu()
        option = int(input("Select an option: "))
        
        if option == 1:
            code = int(input("Enter the product code: "))
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            inventory = int(input("Enter the inventory quantity: "))
            print(add_product(code, name, price, inventory))
        
        elif option == 2:
            code = int(input("Enter the product code: "))
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            inventory = int(input("Enter the inventory quantity: "))
            print(update_product(code, name, price, inventory))
        
        elif option == 3:
            code = int(input("Enter the product code: "))
            print(delete_product(code))
        
        elif option == 4:
            max_price_products = products_with_max_price()
            print("Products with the highest price:", ", ".join(max_price_products))
        
        elif option == 5:
            min_price_products = products_with_min_price()
            print("Products with the lowest price:", ", ".join(min_price_products))
        
        elif option == 6:
            print("Average prices:", average_price())
        
        elif option == 7:
            print("Total inventory value:", total_inventory_value())
        
        elif option == 8:
            print("Exiting the program...")
            break
        
        else:
            print("Invalid option. Please try again.")
