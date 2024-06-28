from exerccise1 import Student

doc = input("enter your document ")
name = input("enter your name ")
email = input("enter your email ")
phone = input("enter your phone ")
age = int(input("enter your age "))

Studentone = Student(doc, name, email, phone, age)

print(f'{Studentone.getname()}\n{Studentone.getdocument()}\n{Studentone.getemail()}\n{Studentone.getphone()}\n{Studentone.getage()}')
