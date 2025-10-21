class Libro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
        self.prestado=False
    def prestar(self):
        if not self.prestado:
            self.prestado=True
            return True
        return False
    def devolver(self):
        if self.prestado:
            self.prestado=False
            return True
        return False

l=Libro("Cien años","GGM")
print(l.prestar())
print(l.prestar())
print(l.devolver())
