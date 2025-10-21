class Figura:
    def area(self):
        return 0
class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado
    def area(self):
        return self.lado*self.lado
f=Cuadrado(4)
print(f.area())
