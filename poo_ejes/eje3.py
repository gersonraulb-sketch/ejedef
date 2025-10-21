class Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, c):
        if c > 0:
            self.saldo += c
        return self.saldo

    def retirar(self, c):
        if 0 < c <= self.saldo:
            self.saldo -= c
            return self.saldo
        return None


cuenta = Cuenta(100)
print(cuenta.depositar(50))
print(cuenta.retirar(30))
