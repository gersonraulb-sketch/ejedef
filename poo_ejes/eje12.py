class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def cumplir_anios(self):
        self.__edad += 1
        return self.__edad


p = Persona("Carlos", 20)
print(p.get_nombre())
print(p.cumplir_anios())
