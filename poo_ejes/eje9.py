class Rectangulo:
    def __init__(self, largo, ancho):
        if largo <= 0 or ancho <= 0:
            raise ValueError
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo*self.ancho

    def perimetro(self):
        return 2*(self.largo+self.ancho)


r = Rectangulo(10, 5)
print(r.area())
print(r.perimetro())
