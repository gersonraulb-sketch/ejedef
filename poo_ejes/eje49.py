class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    def presentar(self):
        return f"Soy {self.nombre}"
class Robot:
    def __init__(self,id):
        self.id=id
    def presentar(self):
        return f"Robot {self.id}"
for x in [Persona("Ana"),Robot(101)]: print(x.presentar())
