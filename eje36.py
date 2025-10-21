def ordenar_por_ultimo(lista):
    return sorted(lista, key=lambda s: s[-1])

print(ordenar_por_ultimo(['casa','auto','barco']))
