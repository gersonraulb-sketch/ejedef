class Usuario:
    def __init__(self,usuario,clave):
        self.__clave=clave
        self.usuario=usuario
    def verificar(self,clave):
        return clave==self.__clave

u=Usuario("juan","secreto")
print(u.verificar("secreto"))
print(u.verificar("otro"))
