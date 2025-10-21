def producto_escalar(a,b):
    return sum(x*y for x,y in zip(a,b))

print(producto_escalar([1,2,3],[4,5,6]))
