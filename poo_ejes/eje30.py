class Pago:
    def procesar(self):
        return "procesando pago"
class Tarjeta(Pago):
    def procesar(self):
        return "tarjeta"
class Efectivo(Pago):
    def procesar(self):
        return "efectivo"
for p in [Tarjeta(),Efectivo()]:
    print(p.procesar())
