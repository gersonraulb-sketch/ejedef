def es_subconjunto(a,b):
    return set(a).issubset(set(b))

print(es_subconjunto([1,2],[1,2,3]))
