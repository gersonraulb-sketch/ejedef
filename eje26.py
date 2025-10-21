def filtrar_por_longitud(lista,n):
    return [s for s in lista if len(s)>=n]

print(filtrar_por_longitud(['a','ab','abc'],2))
