from clases.clase_exercise9 import *


while True:
    show_menu()
    option = input("Select an option: ")

    if option == "1":
        print(package1.check_location())
    elif option == "2":
        new_status = input("Enter the new status of the package: ")
        package1.update_status(new_status)
    elif option == "3":
        print("Thank you for using our service.")
        break
    else:
        print("Invalid option. Please select a valid option.")
