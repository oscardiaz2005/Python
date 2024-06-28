from clases.clase_exercise8 import *

cart = ShoppingCart()

while True:
    show_menu()
    option = input("Select an option: ")

    if option == "1":
        show_products()
        product_number = int(input("Select a product to add to the cart: ")) - 1
        quantity = int(input("Enter the quantity: "))
        selected_product = available_products[product_number]
        cart.add_product(selected_product, quantity)
    elif option == "2":
        print("Total to be paid:", cart.calculate_total())
    elif option == "3":
        amount_paid = float(input("Enter the amount paid: "))
        cart.make_payment(amount_paid)
        print("Thank you for your purchase. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")
