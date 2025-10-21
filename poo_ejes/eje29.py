class Empleado:
    def __init__(self,nombre):
        self.nombre=nombre
    def trabajar(self):
        return f"{self.nombre} trabaja"
class Voluntario:
    def __init__(self,nombre):
        self.nombre=nombre
    def trabajar(self):
        return f"{self.nombre} ayuda gratis"
for x in [Empleado("Ana"),Voluntario("Luis")]:
    print(x.trabajar())
