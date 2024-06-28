import csv

with open("nombreprueba.csv","r") as txt:
    content=txt.readlines()
    print(content)


with open("testing.txt" , "w") as txt:
    txt.write("hola")




