def ordenar_por_suma_sublistas(lst):
    return sorted(lst,key=sum)

print(ordenar_por_suma_sublistas([[3],[1,2],[4,1]]))
