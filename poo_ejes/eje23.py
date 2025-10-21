class Vehiculo:
    def __init__(self, color):
        self.color = color


class Auto(Vehiculo):
    def __init__(self, color, puertas):
        super().__init__(color)
        self.puertas = puertas


a = Auto("rojo", 4)
print(a.color, a.puertas)
