class Estudiante:
    def __init__(self,nombre,id):
        self.nombre=nombre
        self.id=id
        self.calificaciones=[]
    def agregar(self,n):
        if 0<=n<=100:
            self.calificaciones.append(n)
            return True
        return False
    def promedio(self):
        return sum(self.calificaciones)/len(self.calificaciones) if self.calificaciones else 0

e=Estudiante("Jorge","E01")
e.agregar(80)
e.agregar(90)
print(e.promedio())
