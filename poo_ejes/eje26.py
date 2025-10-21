class Empleado:
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
    def __str__(self):
        return f"{self.nombre} - ${self.salario}"
emp=Empleado("Ana",2000)
print(str(emp))
