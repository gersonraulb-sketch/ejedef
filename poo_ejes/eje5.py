class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if 0 < cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False

    def valor_total(self, cantidad):
        return cantidad*self.precio if cantidad <= self.stock else None


p = Producto("Libro", 20, 5)
print(p.vender(2))
print(p.valor_total(2))
print(p.stock)
