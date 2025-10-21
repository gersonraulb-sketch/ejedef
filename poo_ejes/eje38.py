class Empleado:
    def __init__(self,nombre,horas,valor_hora):
        self.nombre=nombre
        self.horas=horas
        self.valor_hora=valor_hora
    def salario(self):
        return self.horas*self.valor_hora
e=Empleado("Ana",40,25)
print(e.salario())
