class Persona:
    especie="Humano"
    def __init__(self,nombre):
        self.nombre=nombre
p1=Persona("Ana")
p2=Persona("Luis")
print(Persona.especie)
print(p1.nombre,p2.nombre)
