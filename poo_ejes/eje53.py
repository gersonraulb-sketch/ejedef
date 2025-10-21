class Persona:
    def __init__(self,nombre,amigos=None):
        self.nombre=nombre
        self.amigos=amigos if amigos is not None else []
    def agregar(self,a):
        if a not in self.amigos: self.amigos.append(a)
p=Persona("A"); p.agregar("B"); print(p.amigos)
