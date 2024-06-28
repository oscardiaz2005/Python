list_one=[]
list_two=[]
list_three=[]
for i in range(5):
    number=int(input(f'please enter the  number {i+1} for the list number one '))
    while number<0 :
        print("invalid number , please enter a number bigger than 0")
        number=int(input(f'please enter the  number {i+1} for the list number one '))
    list_one.append(number)
    number=int(input(f'please enter the  number {i+1} for the list number two '))
    while number<0 :
        print("invalid number , please enter a number bigger than 0")
        number=int(input(f'please enter the  number {i+1} for the list number two '))
    list_two.append(number)

for i in range(len(list_one)):
    list_three.append(list_one[i])
    list_three.append( list_two[i])


print( "list one = ",list_one)
print("list two = ",list_two)
print("list three = ",list_three)
