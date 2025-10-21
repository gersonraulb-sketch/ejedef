class Cliente:
    def __init__(self,nombre,rut):
        self.nombre=nombre; self.rut=rut
    def __hash__(self):
        return hash(self.rut)
    def __eq__(self,other):
        return self.rut==other.rut
s=set([Cliente("A","1"),Cliente("B","2"),Cliente("A","1")])
print(len(s))
