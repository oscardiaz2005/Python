"""
Elabore un algoritmo que lea 10 números y que calcule e imprima el promedio de dichos números
"""
#whilee
print("While loop\n")
accountant=0
sum_number=0
while accountant<10:
    number=int(input(f'enter  number {accountant+1} '))
    sum_number+=number
    accountant+=1
average=sum_number/10
print(f'your average is {average}')


# For loop
print("\nFor loop\n")
accountant=0
sum_number=0
for i in range (10): 
    number=int(input(f'enter  number {accountant+1} '))
    sum_number+=number
    accountant+=1
average=sum_number/10
print(f'your average is {average}')


