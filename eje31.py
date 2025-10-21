import math

def distancia_euclidiana(a,b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

print(distancia_euclidiana((0,0),(3,4)))
