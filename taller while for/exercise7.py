"""
Elabore un algoritmo que lea un valor N y que imprima un triángulo de asteriscos
"""
# While loop
print("While loop\n")
amount=int(input("how many asterisk do you want the triangle? "))
accountant=0

while accountant<amount :
    accountant+=1
    print("*"*accountant)



# For loop
print("\nFor loop\n")
amount=int(input("how many asterisk do you want the triangle? "))
accountant=0 
for i in range(amount):
    accountant+=1
    print("*"*accountant)

