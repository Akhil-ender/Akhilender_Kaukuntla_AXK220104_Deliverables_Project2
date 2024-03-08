

class Scooters:
    def __init__ (self, Company_name, Availble_Scooters ):
        self.Company_name = Company_name
        self.Availble_Scooters = Availble_Scooters
    
    def return_Scooter (self, num_scooters):
        if num_scooters <= 0 or num_scooters > self.Availble_Scooters:
            return "invalid"
        print ("Recheck the rent_duration")
        rent_duration = input("Recheck the rental duration in Hours/Days/Weeks: ")
        if rent_duration=="hour" or rent_duration=="hours":
            time = int(input("Enter the number of hours not equal to zero"))
        elif rent_duration=="day" or rent_duration=="days":
            time = int(input("Enter the number of day"))
        elif rent_duration=="week" or rent_duration=="weeks": 
            time = int(input("Enter the number of weeks:-")) 
        else:
            return "Invalid rental duration"
        rental_rates = {"hour": 10, "day": 20, "week": 50}
        base_price = rental_rates[rent_duration] * num_scooters
        if num_scooters > 2:
            base_price = base_price * time
        discount = 0.15 * base_price
        total_price = base_price - discount
        return f"Invoice for {self.Company_name}:\nNumber of scooters: {num_scooters}\nRental Duration: {rent_duration}\nActual price Discount : {base_price}\n 15% Promotional coupon Added for booking more than 2 Scooters \n Effective Amount Due:${total_price}"
    
    def Checkout (self, customer_name, num_scooters, rent_duration, Availble_Scooters):
        if num_scooters <= 0 or num_scooters > Availble_Scooters:
            return "Invalid number of scooters. Please choose a valid number"
        if rent_duration not in ["hour", "day", "week"]:
            return "Invalid rental duration"
        rental_rates = {"hour": 10, "day": 20, "week": 50} 
        base_price = rental_rates[rent_duration] * num_scooters
        if num_scooters > 2:
            base_price = base_price * time
            discount = 0.15 * base_price
            total_price = base_price - discount
            return f"Invoice for {customer_name} from {self.Company_name}:\nNumber of scooters: {num_scooters}\nRental Duration: {rent_duration}\nActual price Discount: {base_price}\n15% Promotional coupon Added for booking more than 2 Scooters\nEffective Amount Due: ${total_price}"
        else:
            total_price = base_price * time
            # Add any additional code here if needed
        with open ("invoice.txt", "w") as file:
            file. write ("----------------------Invoice--------------------------")
            file. write ("\n----------------------LC Scooters----------------------")
            file. write (f"Invoice for {customer_name} from {self.Company_name}:\nNumber of scooters= {num_scooters}\nRental Duration= {str(time) + rent_duration}\nTotal_Amount Due= ${total_price}")
            #return f"invoice (total_price)"

if __name__ == "__main__":
    option = {1: "ABC Rentals", 2: "DEF Rentals", 3: "GHI Rentals"} 
    option2={1:20, 2:30, 3:50}
    l = [["1", "ABC Rentals", ":", "Available Scooters=20"],
         ["2", "DEF Rentals", ":", "Available Scooters=30"],
         ["3", "GHI Rentals", ":", "Available Scooters=50"],
        ]

    for service in l:
        print ("\t".join(service))
    M = int (input ("Enter the option to Select Store"))

    Available_Scooters = option2[M]
    Company_name =option[M]
    shop = Scooters(Company_name, Available_Scooters)

    print ("The Hourly cost for Each Scooter is $10", "\n The Per Day cost for Each Scooter is $20 \nWeekly cost for Each Scooter is $50") 
    customer_name=input ("Enter The Customer Name: ")
    rent_option=input ("Enter yes for Booking Enter No for Return: ")
    if rent_option.lower() == "yes":
        num_scooters = int(input("Enter the Required number of Scooters: "))
        rent_duration = input("Enter the rental duration in Hours/Days/Weeks: ")
        if rent_duration == "hour" or rent_duration == "hours":
            # print ("Hourly cost per Each scooters=$10")
            time = int(input("Enter the number of hours not equal to zero: "))
        if rent_duration == "day" or rent_duration == "days":
            time = int(input("Enter the number of day: "))
        if rent_duration == "week" or rent_duration == "weeks":
            time = int(input("Enter the number of weeks: "))
        print(shop.Checkout(customer_name, num_scooters, rent_duration, Available_Scooters))
    else:
        returned_Scooters = int(input("How many scooters are your returning: "))
        print(shop.return_Scooter(returned_Scooters))
