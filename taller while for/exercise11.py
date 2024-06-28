"""
 El sueldo que perciben 10 vendedores de una empresa automotriz está integrado de la siguiente manera: el salario 
mínimo, mas $ 100.000 por cada auto vendido más el 2% del valor de los autos vendidos. Debe realizar un algoritmo 
que imprima el nombre del vendedor que tuvo el mayor sueldo, suponiendo que no hay cantidades iguales de total 
de venta"""

# While loop
print("While loop\n")

seller=1
salary=1300000
mayor_salary=-100000000

while seller<=3:
    print(f'seller number {seller}')
    actual_name=(input("what is his/her name? "))
    car=int(input(f'how many cars did {actual_name} sell? '))
    salary=salary+(100000*car)
    accountant=1
    while accountant<=car:
        price=int(input(f'please enter the price of the car number {accountant} '))
        accountant+=1
        salary=salary+(price*2/100)
        if salary>mayor_salary :
            mayor_salary = salary
            name=actual_name
    print( f'the {actual_name} salary is {salary}' )
    
    salary=1300000
    seller+=1    

print(f'the best seller is {name} due to his/her salary is {mayor_salary}')




# For loop
print("\nFor loop\n")

seller=1
salary=1300000
mayor_salary=-100000000

for i in range(seller,10+1,+1):
    print(f'seller number {seller}')
    actual_name=(input("what is his/her name? "))
    car=int(input(f'how many cars did {actual_name} sell? '))
    salary=salary+(100000*car)
    accountant=1
    for j in range(accountant,car+1,+1):
        price=int(input(f'please enter the price of the car number {accountant} '))
        accountant+=1
        salary=salary+(price*2/100)
        if salary>mayor_salary :
            mayor_salary = salary
            name=actual_name
    print( f'the {actual_name} salary is {salary}' )
    
    salary=1300000
    seller+=1    

print(f'the best seller is {name} due to his/her salary is {mayor_salary}')







   
    

