from abc import ABC,abstractmethod
class Pago(ABC):
    @abstractmethod
    def procesar(self): pass
class Tarjeta(Pago):
    def procesar(self): return "tarjeta procesada"
class Transferencia(Pago):
    def procesar(self): return "transferencia procesada"
sistema=[Tarjeta(),Transferencia()]
for p in sistema: print(p.procesar())
