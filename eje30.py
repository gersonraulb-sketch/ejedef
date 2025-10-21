def ordenar_diccionario_por_valor(d):
    return sorted(d.items(), key=lambda kv:kv[1])

print(ordenar_diccionario_por_valor({'a':3,'b':1,'c':2}))
