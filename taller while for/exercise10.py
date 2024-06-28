"""
Elabore un algoritmo que calcule e imprima cuántos y cuáles son los números primos hay dentro de un rango dado 
por el usuario
"""
# While Loop
print("While loop\n")
begin = int(input("Please enter the beginning: "))
end = int(input("Please enter the end: "))

print(f'Prime numbers from {begin} to {end}:')

number = begin
while number <= end:
    if number > 1:
        prime = True
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            print(number)
    number += 1

# For Loop
print("\nFor loop\n")
begin = int(input("Please enter the beginning: "))
end = int(input("Please enter the end: "))

print(f'Prime numbers from {begin} to {end}:')
for number in range(begin, end + 1):
    if number > 1:
        prime = True
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                prime = False
                break
        if prime:
            print(number)



