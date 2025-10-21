class Banco:
    def __init__(self):
        self._cuentas={}
    def crear(self,titular,saldo=0):
        self._cuentas[titular]=saldo
    def transferir(self,a,b,cantidad):
        if self._cuentas.get(a,0)>=cantidad:
            self._cuentas[a]-=cantidad
            self._cuentas[b]=self._cuentas.get(b,0)+cantidad
            return True
        return False
b=Banco()
b.crear("A",100)
b.crear("B",50)
print(b.transferir("A","B",70))
print(b.transferir("A","B",50))
