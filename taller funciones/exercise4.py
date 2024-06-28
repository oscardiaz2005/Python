from procesos.procesos_exercise4 import *

number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))

if is_divisor(number1, number2):
    print(f"{number2} is a divisor of {number1}.")
elif is_divisor(number2, number1):
    print(f"{number1} is a divisor of {number2}.")
else:
    print("Neither number is a divisor of the other.")
