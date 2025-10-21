class Ordenable:
    def clave(self): return 0
class Persona(Ordenable):
    def __init__(self,nombre,edad):
        self.nombre=nombre; self.edad=edad
    def clave(self): return self.edad
l=[Persona("A",40),Persona("B",20)]
l.sort(key=lambda x: x.clave())
print([(p.nombre,p.edad) for p in l])
