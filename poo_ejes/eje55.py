class Fabrica:
    def crear_persona(self,nombre):
        return {"nombre":nombre}
f=Fabrica()
print(f.crear_persona("Ana"))
