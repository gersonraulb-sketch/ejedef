def limites(lista):
    return (min(lista), max(lista)) if lista else (None,None)

print(limites([3,1,4,2]))
