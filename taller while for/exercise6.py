"""Elabore un algoritmo que le lea N números diferente y calcule e imprima el mayor y el menor. 
"""

# While loop
print("While loop\n")
amount=int(input("how many numbr do you want to compare? "))
minor_number=1000000000000
biggest_number=-300000
accountant=0

while accountant<amount:
    accountant+=1
    number=int(input("please enter a number " ))
    if number>biggest_number:
        biggest_number=number
    if number<minor_number:
        minor_number=number    

print(f'the biggest number is {biggest_number}')
print(f'the minor number is {minor_number}')


# For loop
print("\nFor loop\n")

amount=int(input("how many numbr do you want to compare? "))
minor_number=1000000000000
biggest_number=-300000
for i in range(amount):
    number=int(input("please enter a number " ))
    if number>biggest_number:
        biggest_number=number
    if number<minor_number:
        minor_number=number   
print(f'the biggest number is {biggest_number}')
print(f'the minor number is {minor_number}')