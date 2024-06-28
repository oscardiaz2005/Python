numbers = []
while True:
    print("\n1. Add number to the list")
    print("2. Change number with position")
    print("3. Show length")
    print("4. Delete last number")
    print("5. Delete a number at position")
    print("6. Count a number")
    print("7. Show position of a number")
    print("8. Show numbers")
    print("9. Exit\n")

    option = int(input("choose an option "))
    while option < 1 or option > 9:
        print("invalid option ")
        option = int(input("choose an option "))

    if option == 1:
        number_to_add = int(input("enter the number to add "))
        numbers.append(number_to_add)

    elif option == 2:
        position = int(input("please enter the number's position "))
        if position <= len(numbers):
            new_number = int(input("enter the new number "))
            numbers[position - 1] = new_number
            print("the number has been changed successfully")
        else:
            print("the position has not been found")

    elif option == 3:
        print(f'the length is {len(numbers)}')

    elif option == 4:
        if numbers:
            last_number = numbers[-1] 
            numbers.remove(last_number)  
            print("the last number has been deleted successfully")
        else:
            print("List is empty")

    elif option == 5:
        position = int(input("Enter the position of the number to delete: "))
        if 1 <= position <= len(numbers):
            deleted_number = numbers[position - 1] 
            numbers.remove(deleted_number) 
            print(f"The number at position {position} ({deleted_number}) has been deleted successfully")
        else:
            print("Invalid position")

    elif option == 6:
        find = int(input("Please enter the searched number: "))
        accountant = 0
        for num in numbers:
            if num == find:
                accountant += 1
        print(f"The number {find} is {accountant} times in the list")

    elif option == 7:
        find = int(input("Please enter the number to search for: "))
        found_positions = []
        for i in range(len(numbers)):
            if numbers[i] == find:
                found_positions.append(i + 1)
        if found_positions:
            print(f'The number {find} is found at positions: {found_positions}')
        else:
            print(f'The number {find} has not been found in the list')

    elif option == 8:
        print(f'the numbers are = {numbers}')

    elif option == 9:
        break

print("Goodbye, thanks!")
