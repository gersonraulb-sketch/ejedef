import random

def muestra_aleatoria(lst,n):
    return random.sample(lst,n)

print(muestra_aleatoria(list(range(10)),3))
