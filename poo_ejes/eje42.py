class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def validar(self):
        return isinstance(self.nombre, str) and 0 <= self.edad <= 150


p = Persona("Ana", 25)
print(p.validar())
