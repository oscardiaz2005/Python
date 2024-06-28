months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_number = int(input("Enter the month number (1-12): "))

if 1 <= month_number <= 12:
    month_name = months[month_number - 1]
    num_days = days_per_month[month_number - 1]

    print(f"The month of {month_name} has {num_days} days.")
else:
    print("Invalid month number. It should be a number between 1 and 12.")

