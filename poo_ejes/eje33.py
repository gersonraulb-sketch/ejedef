class Repositorio:
    def __init__(self):
        self._datos=[]
    def agregar(self,x):
        self._datos.append(x)
    def listar(self):
        return list(self._datos)
r=Repositorio()
r.agregar(1)
r.agregar(2)
print(r.listar())
