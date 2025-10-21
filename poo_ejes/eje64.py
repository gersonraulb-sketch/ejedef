from abc import ABC,abstractmethod
class Repositorio(ABC):
    @abstractmethod
    def guardar(self,x): pass
class RepoMem(Repositorio):
    def __init__(self): self._d=[]
    def guardar(self,x): self._d.append(x)
    def listar(self): return list(self._d)
r=RepoMem(); r.guardar(1); r.guardar(2)
print(r.listar())
