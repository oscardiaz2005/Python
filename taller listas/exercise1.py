   
numbers=[]
import random
for  i in  range (10):
   number_random=random.randint(1,100)
   numbers.append(number_random)
print(numbers)
print("")


for i in range (10) :
    squared=numbers[i]**2
    cube=numbers[i]**3
    print(f'{numbers[i]} ^ 2 = {squared}')
    print(f'{numbers[i]} ^ 3 = {cube}')
    print(" ")


