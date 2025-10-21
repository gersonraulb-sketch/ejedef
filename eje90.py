def rellenar_ceros(lst,n):
    return lst+[0]*(n-len(lst)) if len(lst)<n else lst[:n]

print(rellenar_ceros([1,2],5))
