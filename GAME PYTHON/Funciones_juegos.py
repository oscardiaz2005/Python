from Demonio import Nivel1Demonio, Nivel2Demonio, Nivel3Demonio, Nivel4Demonio, Nivel5Demonio
from Nivel import *


def get_pregunta_respuesta(nivel_actual, pregunta_numero):
    preguntas = None
    if nivel_actual == 1:
        preguntas = Nivel1.getPreguntas()
    elif nivel_actual == 2:
        preguntas = Nivel2.getPreguntas()
    elif nivel_actual == 3:
        preguntas = Nivel3.getPreguntas()
    elif nivel_actual == 4:
        preguntas = Nivel4.getPreguntas()
    elif nivel_actual == 5:
        preguntas = Nivel5.getPreguntas()
    else:
        return None, None

    pregunta = list(preguntas.keys())[pregunta_numero - 1]
    respuesta = preguntas[pregunta]
    return pregunta, respuesta




def obtener_pista(nivel_actual, pregunta_numero):
    pistas = None
    if nivel_actual == 1:
        pistas = Nivel1.getPistas()
    elif nivel_actual == 2:
        pistas = Nivel2.getPistas()
    elif nivel_actual == 3:
        pistas = Nivel3.getPistas()
    elif nivel_actual == 4:
        pistas = Nivel4.getPistas()
    elif nivel_actual == 5:
        pistas = Nivel5.getPistas()
    else:
        return "No hay pistas disponibles para este nivel."

    return pistas[pregunta_numero - 1]


def mostrar_nivel(jugador):
    nivel_actual = jugador.get_nivel_actual()
    demonio = None
    if nivel_actual == 1:
        demonio = Nivel1Demonio
        print("\nNivel 1")
    elif nivel_actual == 2:
        demonio = Nivel2Demonio
        print("\nNivel 2")
    elif nivel_actual == 3:
        demonio = Nivel3Demonio
        print("\nNivel 3")
    elif nivel_actual == 4:
        demonio = Nivel4Demonio
        print("\nNivel 4")
    elif nivel_actual == 5:
        demonio = Nivel5Demonio
        print("\nNivel 5")

    print(f"¡Te enfrentas al {demonio.get_nombre()}!")
    print(f"Puntos de vida del demonio: {demonio.get_puntos_de_vida()}")
    print(f"Daño del demonio: {demonio.get_daño()}")
    print(f"Tus puntos de vida : {jugador.get_puntos_de_vida()}")
    print(f"Tus Monedas: {jugador.get_monedas()}")
    print("\n¡Responde las preguntas para atacar al demonio!")



def retroceder_costo(nivel_actual):
    if nivel_actual == 3:
        return 600
    elif nivel_actual == 4:
        return 800
    else:
        return 0

def jugar_nivel(jugador, costo_retroceder):
    nivel_actual = jugador.get_nivel_actual()
    demonio = None
    if nivel_actual == 1:
        demonio = Nivel1Demonio
        costo_pista = 50
        monedas_nivel = 200
    elif nivel_actual == 2:
        demonio = Nivel2Demonio
        costo_pista = 100
        monedas_nivel = 400
    elif nivel_actual == 3:
        demonio = Nivel3Demonio
        costo_pista = 200
        monedas_nivel = 600
    elif nivel_actual == 4:
        demonio = Nivel4Demonio
        costo_pista = 300
        monedas_nivel = 700
    elif nivel_actual == 5:
        demonio = Nivel5Demonio
        costo_pista = 400
        monedas_nivel = 1000

    for i in range(5):
        pregunta, respuesta = get_pregunta_respuesta(nivel_actual, i + 1)
        print(f"\nPregunta {i + 1}: {pregunta}")
        pista_usada = False  
        while True:
            if pista_usada:
                print("pista usada.")
            elif not pista_usada and jugador.get_monedas() >= costo_pista:
                pista = input(f"¿Deseas una pista? (costo: {costo_pista} monedas) [si/no]: ").lower()
                if pista == "si":
                    print(obtener_pista(nivel_actual, i + 1))
                    jugador.restar_monedas(costo_pista)
                    pista_usada = True 
                    print(f"Acabas de usar una pista.\nTus Monedas restantes: {jugador.get_monedas()}")
                    continue
            elif not pista_usada and jugador.get_monedas() < costo_pista:  
                print("No tienes suficientes monedas para comprar una pista.")
                pista_usada = True  

            respuesta_jugador = input("Respuesta: ").lower()
            if respuesta_jugador == respuesta:
                print("¡Respuesta correcta! ¡Atacas al demonio!")
                demonio.puntos_de_vida -= jugador.get_daño()
                print(f"Puntos de vida del demonio restantes: {demonio.puntos_de_vida}")
                break  # Salir del while
            else:
                print("¡Respuesta incorrecta! El demonio te ataca.")
                jugador.restar_vida(demonio.daño)
                print(f"Tus puntos de vida restantes: {jugador.get_puntos_de_vida()}")
                if jugador.get_puntos_de_vida() <= 0:
                    print(f"¡Has perdido! El {demonio.get_nombre()} te ha vencido.")
                    return False

    print(f"\n¡Has derrotado al {demonio.get_nombre()} y has pasado al siguiente nivel!")
    jugador.sumar_monedas(monedas_nivel)
    print(f"Monedas ganadas: {jugador.get_monedas()}")
    if nivel_actual<5:
        print("\n¿Deseas 300 monedas adicionales o 50 puntos de salud adicionales?")
        print(f"tus monedas : {jugador.get_monedas()} / tu salud {jugador.get_puntos_de_vida()}")
        eleccion = input("Escribe 'monedas' o 'salud': ").lower()
        if eleccion == "monedas":
            jugador.sumar_monedas(300)
            print(f"Ahora tienes {jugador.get_monedas()} monedas.")
        elif eleccion == "salud":
            jugador.sumar_vida(50)
            print(f"Ahora tienes {jugador.get_puntos_de_vida()} puntos de salud.")

    return True
