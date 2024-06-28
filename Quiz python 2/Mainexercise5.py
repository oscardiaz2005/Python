from procesos.procesosexercise5 import *
lista_palabras = ["hola", "adios", "casa", "gato", "color"]
resultado = palabras_con_letra_a(lista_palabras)
print("Diccionario de palabras con letras:")
for letra, palabras in resultado.items():
    print(f"Letra '{letra}': {palabras}")
