def es_matriz_cuadrada(m):
    return all(len(row)==len(m) for row in m)

print(es_matriz_cuadrada([[1,2],[3,4]]))
