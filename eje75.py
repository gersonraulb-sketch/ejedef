def comparar_versiones(a,b):
    A=list(map(int,a.split('.')))
    B=list(map(int,b.split('.')))
    return (A>B) - (A<B)

print(comparar_versiones('1.2.3','1.2.0'))
