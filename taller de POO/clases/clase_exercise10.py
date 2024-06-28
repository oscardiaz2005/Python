class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print(f"Contact '{name}' deleted.")
                return
        print(f"No contact found with the name '{name}'.")

    def list_contacts(self):
        if self.contacts:
            print("Contact list:")
            for contact in self.contacts:
                print(contact)
        else:
            print("No contacts in the list.")

def show_menu():
    print("\nMenu:")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. List contacts")
    print("5. Exit")