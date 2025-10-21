class Banco:
    def __init__(self):
        self._saldo=0
    def __iadd__(self,other):
        self._saldo+=other
        return self
    def __str__(self):
        return str(self._saldo)
b=Banco(); b+=100; b+=50; print(b)
