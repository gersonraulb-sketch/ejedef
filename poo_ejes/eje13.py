class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def salario_anual(self):
        return self.salario*12


emp = Empleado("Luisa", 2500)
print(emp.salario_anual())
