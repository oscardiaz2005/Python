from clases.clase_exercise4 import *

inventory = Inventory()

while True:
    print("\nWelcome to the inventory management system:")
    print("1. Show inventory")
    print("2. Add product")
    print("3. Update stock")
    print("4. Calculate inventory value")
    print("5. Exit")

    option = input("Select an option: ")

    if option == "1":
        if not inventory.products:
            print("The inventory is empty.")
        else:
            print("Inventory:")
            for product in inventory.products:
                print(f"Product: {product.name}, Price: ${product.price}, Quantity in stock: {product.quantity}")

    elif option == "2":
        name = input("Enter the product name: ")
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the quantity in stock: "))
        product = Product(name, price, quantity)
        inventory.add_product(product)
        print("Product added to inventory.")
    elif option == "3":
        product_name = input("Enter the name of the product to update: ")
        quantity = int(input("Enter the quantity to add to the stock: "))
        inventory.update_stock(product_name, quantity)
        print("Stock updated.")
    elif option == "4":
        total_inventory_value = inventory.calculate_inventory_value()
        print(f"The total inventory value is: ${total_inventory_value}")
    elif option == "5":
        print("Thank you for using the system. Goodbye!")
        break
    else:
             print("Invalid option. Please select a valid option.")
