def dividir_lista_en_chunks(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]

print(dividir_lista_en_chunks([1,2,3,4,5,6,7],3))
