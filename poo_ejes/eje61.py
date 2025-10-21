class Servicio:
    def __init__(self,nombre,precio):
        self.nombre=nombre; self.precio=precio
class Carrito:
    def __init__(self):
        self._servicios=[]
    def agregar(self,s):
        self._servicios.append(s)
    def total(self):
        return sum(s.precio for s in self._servicios)
c=Carrito()
c.agregar(Servicio("A",100))
c.agregar(Servicio("B",200))
print(c.total())
