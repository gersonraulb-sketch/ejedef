class ArchivoSim:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = ""

    def escribir(self, texto):
        self.contenido += texto

    def leer(self):
        return self.contenido


a = ArchivoSim("f")
a.escribir("hola")
print(a.leer())
