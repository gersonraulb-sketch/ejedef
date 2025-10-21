def es_multiplo_de_any(n,divs):
    return any(n%d==0 for d in divs if d!=0)

print(es_multiplo_de_any(30,[2,3,7]))
