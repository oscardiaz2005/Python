"""
. Elabore un algoritmo que lea un valor N, entero y positivo, y que calcule e imprima su factorial. """

# While loop
print("While loop\n")
number=int(input("please enter a number "))
while number<0:
    print("please enter a number bigger than 0")
    number=int(input("please enter a number "))

accountant=0
factorial=1
while accountant<number:
    accountant+=1
    factorial=factorial*accountant
print(factorial)


# For loop
print("\nFor loop\n")
number=int(input("please enter a number "))
while number<0:
    print("please enter a number bigger than 0")
    number=int(input("please enter a number "))
accountant=0
factorial=1

for i in range (0,number,+1):
    accountant+=1
    factorial=factorial*accountant
print(factorial)
