class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    def __repr__(self):
        return f"Persona({self.nombre})"
print(repr(Persona("Ana")))
