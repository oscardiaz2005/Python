"""
Elabore un algoritmo que solicite la cantidad de número que se van a procesar, luego que lea los números y calcule 
e imprima el promedio de dichos números
"""
# While loop
print("While loop\n")
amount = int(input("How many numbers do you want? "))
accountant = 0
sum_number = 0
while accountant < amount:
    number = int(input(f'Enter number {accountant+1}: '))
    sum_number += number
    accountant += 1
average = sum_number / amount
print(f'Your average is {average}')

# For loop
print("\nFor loop\n")
amount = int(input("How many numbers do you want? "))
accountant = 0
sum_number = 0
for _ in range(amount): 
    number = int(input(f'Enter number {accountant+1}: '))
    accountant += 1
    sum_number += number
average = sum_number / amount
print(f'Your average is {average}')

