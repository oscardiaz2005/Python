names=[]
ages=[]
adult_students=[]
oldest_students=[]
oldest_age = 0  

while True:
    name=input(" please enter the student's name (* to finish) ")
    if name=="*":
        break
    age=int(input("please enter the student's age "))
    while age<=0:
        print("please enter a valid age")
        age=int(input("please enter the student's age "))

    names.append(name)
    ages.append(age)
    if age > oldest_age:  
        oldest_age = age  

for i in range(len(names)):
    if ages[i]>=18:
        adult_students.append(names[i])
    if ages[i] == oldest_age:  
        oldest_students.append(names[i])

print("\nstudents = ", names)
print("adult_students = ", adult_students)
print("oldest_students = ", oldest_students)

