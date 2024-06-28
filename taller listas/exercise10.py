numbers = []
unique_numbers = []
print("Enter numbers to add to the list (enter a negative number to stop):")
while True:
    num = int(input("Enter a number: "))
    if num < 0:
        break
    numbers.append(num)

for i in range(len(numbers)):
    is_duplicate = False
    for j in range(len(unique_numbers)):
        if numbers[i] == unique_numbers[j]:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_numbers.append(numbers[i])

print("\nOriginal List:")
print(numbers)
print("\nList without duplicates:")
print(unique_numbers)
