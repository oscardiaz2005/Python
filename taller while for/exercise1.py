"""
 Elabore un algoritmo que calcule e imprima la suma de los números pares del 2 hasta el 160.
"""
#while
print("While loop\n")
sum_number=0
number=0
number_for=0
while number<160:
    number+=2
    sum_number+=number
    print(sum_number)


# For loop   
print("\nFor loop\n")
sum_number=0
for i in range(0,160,+2):
    number_for+=2
    sum_number+=number_for
    print(sum_number)


        