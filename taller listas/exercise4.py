import random
numbers = [random.randint(1, 100) for i in range(10)]

print("Original list:", numbers)


for i in range(len(numbers)):
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Sorted list:", numbers)