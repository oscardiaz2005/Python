from clases.clase_exercise3 import *

name =input("Enter the student's name = ")
age =input("Enter the student's age = ")
x=int(input("how many qualifications do you want to add? "))
qualificatios=[]
for i in range(x):
    note=float(input(f"enter note numer {i+1}= "))
    qualificatios.append(note)

student=Student(name,age,qualificatios)

print("Name:", student.name)
print("Age:", student.age)
print("Grades:", student.qualifications)
print("Average grade:", student.average())
