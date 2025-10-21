class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."


p = Persona("Ana", 30)
print(p.saludar())
print(p.edad)
