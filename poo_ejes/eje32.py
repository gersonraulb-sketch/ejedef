from abc import ABC,abstractmethod
class Notificador(ABC):
    @abstractmethod
    def enviar(self,msg): pass
class Email(Notificador):
    def enviar(self,msg):
        return f"email: {msg}"
print(Email().enviar("hola"))
