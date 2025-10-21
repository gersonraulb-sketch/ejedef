class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.__edad=edad
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,val):
        if 0<=val<=150:
            self.__edad=val

p=Persona("Ana",25)
print(p.edad)
p.edad=30
print(p.edad)
p.edad=200
print(p.edad)
