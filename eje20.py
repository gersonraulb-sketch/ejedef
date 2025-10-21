def calcular_descuento(precio,descuento=10):
    return precio*(1-descuento/100)

precio_final=calcular_descuento(1000,20)
print(precio_final)
