from procesos.procesos_exercise9 import *

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

next_date = next_date(day, month, year)
if next_date:
    print("The next date is", next_date)