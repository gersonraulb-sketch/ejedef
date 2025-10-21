class Agenda:
    def __init__(self):
        self._contactos={}
    def agregar(self,nombre,telefono):
        self._contactos[nombre]=telefono
    def buscar(self,nombre):
        return self._contactos.get(nombre)
ag=Agenda(); ag.agregar("Ana","300"); print(ag.buscar("Ana"))
