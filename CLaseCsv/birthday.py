import csv

with open ("nombres.csv","r" ) as txt:
    content=txt.readlines()
    findYear=input("enter the year you want to find ")
    year=[]
    name=[]

    for i in content[1:]:
        if len(year)>50:
            break
        x=i.split(",")
        if x[2]==findYear:
            year.append(x[2])
            name.append(x[3])

with open("testing.txt" , "w") as test:

    for i in range(len(year)):
            test.write(f"nacimiento={year[i]} nombre={name[i]}\n")

