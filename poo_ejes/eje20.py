class Cuenta:
    def __init__(self,saldo=0):
        self.__saldo=saldo
    def depositar(self,c):
        if c>0:
            self.__saldo+=c
    def obtener_saldo(self):
        return self.__saldo

c=Cuenta(10)
c.depositar(90)
print(c.obtener_saldo())
