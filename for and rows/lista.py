
mylist=[1,2,3 ,4,"hola","a","adios",True, [10,20,30]]
"""
#print(mylist)
#print(mylist[5][1])
print(mylist[4:])
print(mylist[:4])
print(mylist[4:9])
print(mylist[-1])#last digit

mylist[1]=("new date") #editaaar
print(mylist) 

"""
"""

for i in mylist:
    print(i) 

if 4 in mylist:
    print("si esta")
else:
    print("no esta") 

"""

mydata=[]
amount=int(input("how many number do you wan to enter "))
for i in range(amount):
    data=input("enter the data ")
    mydata.append(data)

print(mydata)
data_search=input("enter the searched data ")

"""
if data_search in mydata:
    print(data_search)
    inx=mydata.index(data_search)
    print(inx)
"""


if data_search in mydata:
    inx=mydata.remove(data_search)
    print(mydata)