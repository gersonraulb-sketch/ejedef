def eliminar_duplicados(lst):
    return list(dict.fromkeys(lst))

print(eliminar_duplicados([1,2,2,3,1]))
