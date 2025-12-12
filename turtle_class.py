class Tortuga:
    def __init__(self):
        self.posicion = 0

    def adelante(self, n):
        print(" " * self.posicion + "-" * n + ">")
        self.posicion += n  

    def abajo(self, n):
        vertical = self.posicion 
        if n >= 1: 
            print(" " * vertical + "|")
        if n >= 2:
            print(" " * vertical + "|")
        if n >= 3:
            print(" " * vertical + "|")
        if n >= 4:
            print(" " * vertical + "|")
        if n >= 5:
            print(" " * vertical + "|")
        print(" " * vertical + "V")

    def reiniciar(self):
        self.posicion = 0  