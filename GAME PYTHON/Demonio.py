class Demonio:
    def __init__(self, nombre, puntos_de_vida, daño):
        self.nombre = nombre
        self.puntos_de_vida = puntos_de_vida
        self.daño = daño

    def get_nombre(self):
        return self.nombre

    def get_puntos_de_vida(self):
        return self.puntos_de_vida
    def set_puntos_de_vida(self,cantidad):
        self.puntos_de_vida=cantidad

    def get_daño(self):
        return self.daño
    


Nivel1Demonio = Demonio("Demonio de la Cultura General", 100, 10)
Nivel2Demonio = Demonio("Demonio de las Matemáticas", 100, 20)
Nivel3Demonio = Demonio("Demonio de las Capitales", 100, 30)
Nivel4Demonio = Demonio("Demonio del Conocimiento Científico", 100, 40)
Nivel5Demonio = Demonio("Demonio del Idioma Inglés", 100, 50)    

