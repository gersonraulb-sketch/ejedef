def rotar_lista(lst,k):
    k=k%len(lst)
    return lst[-k:]+lst[:-k]

print(rotar_lista([1,2,3,4,5],2))
