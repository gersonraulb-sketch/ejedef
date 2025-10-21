class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."


class Perro(Animal):
    def hablar(self):
        return "guau"


class Gato(Animal):
    def hablar(self):
        return "miau"


a = Perro("Fido")
b = Gato("Luna")
print(a.hablar())
print(b.hablar())
