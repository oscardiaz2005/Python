class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monedas = 100
        self.puntos_de_vida = 100
        self.daño = 20
        self.nivel_actual = 1
    
    def get_nombre(self):
        return self.nombre

    def get_monedas(self):
        return self.monedas

    def get_puntos_de_vida(self):
        return self.puntos_de_vida
    
    def set_puntos_de_vida(self,cantidad):
        self.puntos_de_vida=cantidad


    def get_nivel_actual(self):
        return self.nivel_actual

    def restar_vida(self, cantidad):
        self.puntos_de_vida -= cantidad
        
    def restar_monedas(self ,cantidad):
        self.monedas -= cantidad

    def get_daño(self):
        return self.daño    

    def sumar_monedas(self, cantidad):
        self.monedas += cantidad

    def subir_nivel(self):
        self.nivel_actual += 1
        
    def retroceder_nivel(self):
        self.nivel_actual -= 1

    def sumar_vida(self ,vida):
        self.puntos_de_vida += vida

    def set_nivel_actual(self, nivel):
        self.nivel_actual = nivel
