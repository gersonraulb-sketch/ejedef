from abc import ABC,abstractmethod
class Notificador(ABC):
    @abstractmethod
    def enviar(self,msg): pass
class SMS(Notificador):
    def enviar(self,msg): return f"sms:{msg}"
class Email(Notificador):
    def enviar(self,msg): return f"email:{msg}"
def enviar_todos(notifs,msg):
    for n in notifs: print(n.enviar(msg))
enviar_todos([SMS(),Email()],"hola")
