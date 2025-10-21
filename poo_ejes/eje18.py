class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self._precio=precio
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,val):
        if val>=0:
            self._precio=val

p=Producto("Camisa",30)
print(p.precio)
p.precio=25
print(p.precio)
