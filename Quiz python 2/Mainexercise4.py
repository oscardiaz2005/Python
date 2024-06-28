from procesos.procesosexercise4 import *
palabras =[]
cantidad = int(input("cuantas desea añadir "))
for i in range(cantidad):
    palabra=input("ingrese la palabra ")
    palabras.append(palabra)

resultado = palabras_con_letras_repetidas(palabras)


print("Palabras con letras repetidas:")
for letra, palabras in resultado.items():
    print(f"Letra '{letra}': {palabras}")


