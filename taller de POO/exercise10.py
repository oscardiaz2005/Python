from clases.clase_exercise10 import *

manager = ContactManager()

while True:
    show_menu()
    option = input("Select an option: ")

    if option == "1":
        name = input("Enter the contact's name: ")
        phone = input("Enter the contact's phone: ")
        email = input("Enter the contact's email: ")
        new_contact = Contact(name, phone, email)
        manager.add_contact(new_contact)
    elif option == "2":
        name_to_search = input("Enter the name of the contact to search: ")
        search_result = manager.search_contact(name_to_search)
        if search_result:
            print("\nContact information found:")
            print(search_result)
        else:
            print("\nContact not found.")
    elif option == "3":
        name_to_delete = input("Enter the name of the contact to delete: ")
        manager.delete_contact(name_to_delete)
    elif option == "4":
        manager.list_contacts()
    elif option == "5":
        print("Thank you for using the contact manager. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option.")
