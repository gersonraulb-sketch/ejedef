class Matriz:
    def __init__(self,datos):
        self.datos=datos
    def dimensiones(self):
        return (len(self.datos),len(self.datos[0]) if self.datos else 0)
m=Matriz([[1,2],[3,4]])
print(m.dimensiones())
