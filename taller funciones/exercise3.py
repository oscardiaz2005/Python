from procesos.procesos_exercise3 import *

while True:
    print("\nMenu:")
    print("1. Determine even and odd numbers from a list of 10 integers")
    print("2. Show the first 100 perfect numbers")
    print("3. Reverse a four-digit integer")
    print("4. Exit")
    
    option = input("Select an option (1-4): ")
    
    if option == '1':
        numbers = [int(input(f"Enter integer #{i+1}: ")) for i in range(10)]
        evens, odds = determine_even_odd(numbers)
        print("Even numbers:", evens)
        print("Odd numbers:", odds)
    elif option == '2':
        perfect_numbers = first_100_perfect_numbers()
        print("The first 100 perfect numbers are:", perfect_numbers)
    elif option == '3':
        num = int(input("Enter a four-digit integer: "))
        result = reverse_number(num)
        print("Reversed number:", result)
    elif option == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

