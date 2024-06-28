class Package:
    def __init__(self, tracking_number, origin, destination):
        self.tracking_number = tracking_number
        self.origin = origin
        self.destination = destination
        self.current_status = "In transit"

    def update_status(self, new_status):
        self.current_status = new_status
        print(f"Status of package {self.tracking_number} updated to: {new_status}")

    def check_location(self):
        return f"Origin: {self.origin}, Destination: {self.destination}, Current status: {self.current_status}"


def show_menu():
    print("\nMenu:")
    print("1. Check package location")
    print("2. Update package status")
    print("3. Exit")

package1 = Package("123456789", "City A", "City B")

