vector = []

while True:
    number = int(input("Enter a number (enter a negative number to stop): "))
    if number < 0:
        break
    vector.append(number)

print("The vector is:", vector)
