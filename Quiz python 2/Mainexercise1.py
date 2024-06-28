from procesos.procesosexercise1 import*

chars=[]
frecuency={}
cadena=input("please enter the string ").lower()
chars=splitString(cadena,chars)
frecuency=counttimes(chars,frecuency)
print(frecuency)
