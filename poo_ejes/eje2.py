class Calculadora:
    def sumar(self, a, b):
        return a+b

    def restar(self, a, b):
        return a-b

    def multiplicar(self, a, b):
        return a*b

    def dividir(self, a, b):
        return a/b if b != 0 else None


c = Calculadora()
print(c.sumar(5, 3))
print(c.dividir(10, 2))
