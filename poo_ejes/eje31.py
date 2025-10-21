from abc import ABC,abstractmethod
class Vehiculo(ABC):
    @abstractmethod
    def conducir(self): pass
class Coche(Vehiculo):
    def conducir(self):
        return "conduciendo coche"
c=Coche()
print(c.conducir())
