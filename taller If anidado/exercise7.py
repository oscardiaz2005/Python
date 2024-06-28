print("Welcome to the vehicle rental system.")

vehicle = input("Enter the name of the vehicle to rent (BMW, MEGANE, MERCEDES, TWINGO, CHEVROLET AVEO): ").upper()
if vehicle == "BMW":
    base_price = 650000
elif vehicle == "MEGANE":
    base_price = 120000
elif vehicle == "MERCEDES":
    base_price = 700000
elif vehicle == "TWINGO":
    base_price = 100000
elif vehicle == "CHEVROLET AVEO":
    base_price = 150000
else:
    print("Invalid vehicle entered.")
    exit()


days = int(input("Enter the number of rental days: "))
while days<0 :
    print("invalid number of days")
    days = int(input("Enter the number of rental days: "))

insurance = input("Do you want to take the full coverage insurance? (yes/no): ").lower() == 'yes'



total_price=base_price*days
if insurance :
    total_price= total_price+total_price*5/100

if days>=3 and days<=5 :
    discount= total_price*10 /100
elif days>=6 and days<=10 :
    discount= total_price*15 /100
elif days>10 :
    discount= total_price*20/100

price_with_discount=total_price-discount


print("\nRental Summary:")
print(f"Vehicle: {vehicle}")
print(f"Rental days: {days}")
print(f"Base price per day: ${base_price}")
print(f"Full coverage insurance: {'Yes' if insurance else 'No'}")
print(f' total base : {total_price}')
print(f"Discount applied: ${discount}")
print(f"Total rental cost with discount: ${price_with_discount}")    



