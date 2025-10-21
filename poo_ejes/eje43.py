class Empleado:
    def __init__(self,nombre,puesto):
        self.nombre=nombre; self.puesto=puesto
    def __eq__(self,other):
        return (self.nombre,self.puesto)==(other.nombre,other.puesto)
e1=Empleado("Ana","Dev"); e2=Empleado("Ana","Dev")
print(e1==e2)
