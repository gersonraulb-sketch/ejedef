class Banco:
    def __init__(self):
        self._clientes = {}

    def agregar(self, nombre, saldo=0):
        self._clientes[nombre] = saldo

    def deposito(self, nombre, c):
        if c > 0:
            self._clientes[nombre] += c
        return self._clientes.get(nombre)


b = Banco()
b.agregar("Ana", 100)
print(b.deposito("Ana", 50))
