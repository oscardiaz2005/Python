class Flight:
    def __init__(self, origin, destination, available_seats):
        self.origin = origin
        self.destination = destination
        self.available_seats = available_seats

    def reserve_seat(self, quantity=1):
        if quantity <= self.available_seats:
            self.available_seats -= quantity
            print(f"{quantity} seat(s) successfully reserved.")
        else:
            print(f"Not enough available seats. Available seats: {self.available_seats}")

    def check_availability(self):
        return f"Available seats: {self.available_seats}"

    def __str__(self):
        return f"Flight from {self.origin} to {self.destination}"
