class Figura:
    def area(self): raise NotImplementedError


class Circulo(Figura):
    def __init__(self, r): self.r = r
    def area(self): return 3.1416*self.r*self.r


class Rect(Figura):
    def __init__(self, b, h): self.b = b; self.h = h
    def area(self): return self.b*self.h


for f in [Circulo(2), Rect(3, 4)]:
    print(f.area())
