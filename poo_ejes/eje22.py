class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
class Empleado(Persona):
    def __init__(self,nombre,edad,salario):
        super().__init__(nombre,edad)
        self.salario=salario
emp=Empleado("Ana",28,2000)
print(emp.nombre,emp.edad,emp.salario)
