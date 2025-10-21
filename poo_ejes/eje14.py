class Vehiculo:
    ruedas=4
    def __init__(self,marca):
        self.marca=marca
v=Vehiculo("Ford")
print(Vehiculo.ruedas)
print(v.marca)
