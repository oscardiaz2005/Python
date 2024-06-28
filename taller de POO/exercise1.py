from clases.clase_exercise1 import *

print("CALCULATOR\n")

n1=int(input("number one= "))
n2=int(input("number two= "))
operation = Calculator(n1,n2)

user_operation=int(input("1.sum\n2.rest\n3.multiplication\n4.division\nOPTION= "))

if user_operation==1:
    print(operation.Sum())
elif user_operation==2:
    print(operation.rest())
elif user_operation==3:
    print(operation.multiplicatiom())
elif user_operation==4:
    print(operation.division())
else:
    print("invalid option")                
    
    


