import random

class Flight:
    def __init__(self, flight_number, origin, destination, capacity,price):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.capacity = capacity
        self.available_seats = capacity
        self.price = price
        self.customers = {}

    def checkout(self, customer_name):
        return f"\nTotal price due for {customer_name}: ${self.price}"

    def book_seat(self, customer_name,destination):
        if self.available_seats > 0 and self.destination == destination:
            self.customers[customer_name] = True
            self.available_seats -= 1
            print(f"\nSeat booked successfully for {customer_name} on flight {self.flight_number} to {destination}")    
            checkout = self.checkout(customer_name)
            print(checkout)
            return f"\nYour booking is confirmed."
        elif self.destination != destination:
            return("Invalid destination")
        else:
            return("No seats available")

    def cancel_booking(self, customer_name, destination):
        if self.customers.get(customer_name) and self.destination == destination:
            self.available_seats += 1
            self.customers[customer_name] = False
            return f"\nBooking cancelled for {customer_name} on flight {self.flight_number} to {destination}"
        else:
            return "No booking found"

    def get_flight_status(self,origin,destination):
        options = ['on time', 'delayed', 'cancelled']
        status = random.choice(options)
        print(f"\nFlight {self.flight_number} from {self.origin} to {self.destination} is {status}.")
        if status == 'cancelled':
            return "Please contact the airline for further details."
        else:  
            return "Have a safe flight!"
flights = [
    Flight("UA148", "DFW", "JFK", 320,376.84),
    Flight("AA469", "DFW", "ORD", 240,289.87),
    Flight("SW181", "DFW", "SFO", 280,267.32)
]

# User interaction
while True:
    print("\n1. Book a seat")
    print("2. Cancel a booking")
    print("3. Check flight status")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        flight_destination = input("Enter flight destination: ")
        for f in flights:
            if f.destination == flight_destination.upper():
                print(f.book_seat(name,destination=flight_destination.upper()))
                break
    elif choice == 2:
        name = input("Enter your name: ")
        flight_number = input("Enter flight number: ")
        flight_destination = input("Enter flight destination: ")
        for f in flights:
            if f.flight_number == flight_number.upper() and f.destination == flight_destination.upper():
                print(f.cancel_booking(name,destination=flight_destination.upper()))
                break
    elif choice == 3:
        flight_number = input("Enter flight number: ")
        flight_destination = input("Enter flight destination: ")
        for f in flights:
            if f.flight_number == flight_number.upper():
                print(f.get_flight_status(origin='DFW',destination=flight_destination.upper()))
                break
    elif choice == 4:
        print("\nThank you for using our service\n")
        break
    else:
        print("Invalid choice. Please try again.")