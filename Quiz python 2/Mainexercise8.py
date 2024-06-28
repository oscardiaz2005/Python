from procesos.procesosexercise8 import *
amount=int(input("how many words you want to add ? "))
words=[]
for i in range(amount):
    word=input(f'enter the word  {i+1} ').lower()
    words.append(word)

list=soter_list(words)
print(f'sorted list \n {list}')


