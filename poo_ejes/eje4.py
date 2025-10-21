class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, inc):
        if inc > 0:
            self.velocidad += inc
        return self.velocidad

    def frenar(self, dec):
        if dec > 0:
            self.velocidad = max(0, self.velocidad-dec)
        return self.velocidad


v = Vehiculo("Toyota", "Corolla")
print(v.acelerar(50))
print(v.frenar(20))
