class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.animo = "feliz"

    def alimentar(self):
        self.animo = "satisfecho"
        return self.animo

    def jugar(self):
        self.animo = "animado"
        return self.animo


m = Mascota("Luna", "gato")
print(m.alimentar())
print(m.jugar())
