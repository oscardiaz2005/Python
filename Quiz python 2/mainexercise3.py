from procesos.procesosexercise3 import *
names_dic={}
names=int(input("how many names you wnat to add? "))

for i in range(names):
    name=input("enter the name ")
    age=int(input("enter the age "))
    names_dic[name]=age

young_person=young(names_dic)

print(f"the youngest person is {young_person}")