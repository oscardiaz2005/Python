"""
Elabore un algoritmo que calcule una tabla N de multiplicar que inicia el multiplicando con un valor X hasta un valor Y
"""
# While loop
print("While loop\n")

multiplication=int(input("enter the multiplication table that you want "))
since= int(input("please enter the number since you want to start the multiplication table"))
end = int(input("please enter the number where you want to end the multiplication table "))
while end<since:
     print("please enter a number bigger than the number you want to start")
     end = int(input("please enter the number where you want to end the multiplication table "))


while since<=end:
     result =since*multiplication
     print(f'{multiplication} * {since} = {result}')
     since+=1
     

# For loop
print("\nFor loop\n")

multiplication=int(input("enter the multiplication table that you want "))
since= int(input("please enter the number since you want to start the multiplication tabl "))
end = int(input("please enter the number where you want to end the multiplication table "))
while end<since:
     print("please enter a number bigger than the number you want to start")
     end = int(input("please enter the number where you want to end the multiplication table "))

for i in range(since,end+1,+1):
    result =since*multiplication
    print(f'{multiplication} * {since} = {result}')
    since+=1
     