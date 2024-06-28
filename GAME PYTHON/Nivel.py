from Demonio import *

class Nivel:
    def __init__(self, preguntas,pistas):
        self.preguntas = preguntas
        self.pistas = pistas 

    def getPreguntas(self):
        return self.preguntas


    def getPistas(self):
        return self.pistas

Nivel1 = Nivel(
    {
        "¿Cuál es el país más grande del mundo?": "rusia",
        "¿En qué año llegó Cristóbal Colón a América?": "1492",
        "¿En qué país se usó la primera bomba atómica?": "japon",
        "¿Cuántos huesos tiene el cuerpo humano?": "206",
        "¿Cada cuántos años se realiza un mundial?": "4"
    },
    ["Pista: Este país es famoso por su vasto territorio y su frío clima.",
     "Pista: Cristóbal Colón llegó a América en un año muy conocido. 149-.",
     "Pista: El país en el que ocurrió el trágico evento de Hiroshima y Nagasaki.empieza con j",
     "Pista: Un adulto promedio tiene mas de 200 huesos.",
     "Pista: se celebro en el 2014,2018...."]
)

Nivel2 = Nivel(
    {
        "¿Cuál es el resultado de 2^3 + 5^2 ?": "33",
        "¿Cuál es el resultado de (100/2)+(4*3) ?": "62",
        "¿Cuál es el resultado de 1000+200*(3^3)? ": "6400",
        "¿Cuál es el resultado de la raíz cuadrada de 25 * 5 ?": "25",
        "¿Cuál es el resultado de 3+3*3": "12"
    },
    ["Pista: Realiza las operaciones de potenciación primero y luego suma los resultados.",
     "Pista: Divide 100 entre 2, multiplica 4 por 3 y suma los resultados.",
     "Pista: Eleva 3 al cubo y luego multiplica por 200, finalmente suma 1000.",
     "Pista: Encuentra la raíz cuadrada de 25 y luego multiplica por 2.",
     "Pista: Aplica la regla de precedencia de operadores para resolver esta expresión."]
)

Nivel3 = Nivel(
    {
        "¿Cual es la capital de rusia?": "moscu",
        "¿Cual es la capital de italia?": "roma",
        "¿Cual es la capital de peru?": "lima",
        "¿Cual es la capital de españa?": "madrid",
        "¿Cual es la capital de china?": "pekin"
    },
    ["Pista 1: Es la capital más grande de Europa.",
     "Pista 2: Fue la capital del antiguo Imperio Romano.",
     "Pista 3: Se encuentra en la costa del Pacífico, utencilio para las uñas.",
     "Pista 4: Es conocida por su rica historia colonial.",
     "Pista 5: Tiene una gran muralla que atraviesa su territorio."]
)

Nivel4 = Nivel(
    {
        "¿Cual es la fuerza de la gravedad en la tierra?": "9.8",
        "¿Quién inventó la ecuación de la vida y muerte?": "einstein",
        "¿Qué se le cayó a Newton en la cabeza?": "manzana",
        "¿Quién creó la bomba atómica?": "oppenheimer",
        "¿Cuál es la medida que le falta a las siguientes 2 = distancia, tiempo?": "velocidad"
    },
    ["Pista 1: es menor que que diez y mayor que 9 .",
     "Pista 2: Es conocido por su teoría de la relatividad.",
     "Pista 3: es el logo de apple.",
     "Pista 4: Fue conocido como el 'Padre de la bomba atómica , su pelicula compitio contra barbie'.",
     "Pista 5: Es la tasa de cambio de posición de un objeto en movimiento."]
)

Nivel5 = Nivel(
    {
        "¿Como se dice mas feliz en ingles?": "happier",
        "¿Cuál es el pasado del verbo cortar?": "cut",
        "¿Cuál es el significado de 'you are older than me'?": "tu eres mayor que yo",
        "¿Cuál es el plural de la palabra mujer en ingles?": "women",
        "¿Como se dice 'entre más rápido, mejor'?": "the faster the better"
    },
    ["Pista 1: Es una forma comparativa de 'happy'.",
     "Pista 2: Es vrbo se escribe igual en sus 3 tiempos y empieza con c.",
     "Pista 3: Es relacionado con la edad'.",
     "Pista 4: tienes que cambiar una vocal.",
     "Pista 5:  el uso de la estructura es = The (comparativo de rapido) the (comparativo de mejor)."]
)
