class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre; self.edad=edad
    def __lt__(self,other):
        return self.edad<other.edad
l=[Persona("A",30),Persona("B",25)]
l.sort()
print([(p.nombre,p.edad) for p in l])
