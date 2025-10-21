def contar_ocurrencias(seq):
    d={}
    for x in seq:
        d[x]=d.get(x,0)+1
    return d

print(contar_ocurrencias('banana'))
