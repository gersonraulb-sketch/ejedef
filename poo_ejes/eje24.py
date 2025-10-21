class Empleado:
    def __init__(self,nombre):
        self.nombre=nombre
    def salario(self):
        return 1000
class Gerente(Empleado):
    def salario(self):
        return super().salario()+500
g=Gerente("Luis")
print(g.salario())
