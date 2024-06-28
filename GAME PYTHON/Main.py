from Jugador import Jugador
from Funciones_juegos import *

print("\nBIENVENIDO A DESAFÍO TRIVIA\n--- Viaje Por El Conocimiento ---")
nombre_jugador = input("\nPor favor, ingresa tu nombre: ")
jugador = Jugador(nombre_jugador)
print(f"¡Bienvenido, {jugador.get_nombre()}!")

while jugador.get_nivel_actual() <= 5:
    mostrar_nivel(jugador)
    if not jugar_nivel(jugador, retroceder_costo(jugador.get_nivel_actual())):
        if jugador.get_nivel_actual() == 3 or jugador.get_nivel_actual() == 4:
            costo_retroceder = retroceder_costo(jugador.get_nivel_actual())
            if jugador.get_monedas() >= costo_retroceder:
                print(f"\n¡Puedes retroceder al nivel anterior con 50 puntos de vida por {costo_retroceder} monedas!")
                print(f"Monedas restantes : {jugador.get_monedas()}")
                retroceder = input("¿Quieres retroceder? (si/no): ").lower()
                if retroceder == "si":
                    jugador.restar_monedas(costo_retroceder)
                    jugador.retroceder_nivel()
                    Nivel3Demonio.set_puntos_de_vida(100)
                    Nivel4Demonio.set_puntos_de_vida(100)
                    jugador.set_puntos_de_vida(50)
                    print("Has retrocedido al nivel anterior.")
                    continue
        break
    jugador.subir_nivel()

if jugador.get_nivel_actual() > 5:
    print(f"\n¡Has completado todos los niveles!\n {jugador.get_nombre()} Eres el rey Del conocimiento")
    print(f"Monedas ganadas: {jugador.get_monedas()}")
    print(f"Puntos de vida restantes: {jugador.get_puntos_de_vida()}")
else:
    print(f" {jugador.get_nombre()} Estas condenado a la perdicion")    

