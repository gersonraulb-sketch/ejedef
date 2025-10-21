def mayor_por_tupla(lista_tuplas):
    return max(lista_tuplas, key=lambda t: t[1])

print(mayor_por_tupla([('a',3),('b',5),('c',2)]))
