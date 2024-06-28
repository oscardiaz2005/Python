from clases.clase_exercise6 import *

flight = Flight("Madrid", "New York", 100)

def show_menu():
    print("\nMenu:")
    print("1. Check seat availability")
    print("2. Reserve seat(s)")
    print("3. Exit")


while True:
    print("\n--- Flight Information ---")
    print(flight)
    show_menu()
    option = input("Select an option: ")

    if option == "1":
        print(flight.check_availability())
    elif option == "2":
        quantity = int(input("Enter the number of seats you want to reserve: "))
        flight.reserve_seat(quantity)
    elif option == "3":
        print("Thank you for using our service. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")
