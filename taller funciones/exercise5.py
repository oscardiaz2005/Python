from procesos.procesos_exercise5 import *
price_movie1 = float(input("Enter the price of the first movie: "))
price_movie2 = float(input("Enter the price of the second movie: "))
price_movie3 = float(input("Enter the price of the third movie: "))

total_price = calculate_price(price_movie1, price_movie2, price_movie3)

print("The amount to pay is:", total_price, "dollars")