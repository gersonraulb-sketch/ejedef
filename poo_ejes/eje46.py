class Pago:
    def procesar(self):
        raise NotImplementedError
class Tarjeta(Pago):
    def procesar(self):
        return "pagado tarjeta"
class Efectivo(Pago):
    def procesar(self):
        return "pagado efectivo"
def procesar_pago(p:Pago):
    print(p.procesar())
procesar_pago(Tarjeta()); procesar_pago(Efectivo())
