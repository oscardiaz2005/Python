from procesos.procesos_exercise2 import *

num_vehiculos = int(input("Ingrese el número de vehículos a registrar: "))

registros = {}

for i in range(num_vehiculos):
    print(f"\nRegistro del vehículo {i+1}:")
    distancia = int(input("Ingrese la distancia entre cámaras en metros: "))
    velocidad_maxima = int(input("Ingrese la velocidad máxima permitida en Km/h: "))
    tiempo = int(input("Ingrese el tiempo en segundos que tardó el conductor en recorrer el trayecto: "))
    
    resultado = procesar_multa(distancia, velocidad_maxima, tiempo)
    registros[f"Vehículo {i+1}"] = resultado

print("\nResultados de los registros:")
for vehiculo, resultado in registros.items():
    print(f"{vehiculo}: {resultado}")

print(registros)