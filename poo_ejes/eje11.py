class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, c):
        if c > 0:
            self._saldo += c
        return self._saldo


cb = CuentaBancaria("Ana", 100)
print(cb.saldo)
cb.depositar(50)
print(cb.saldo)
