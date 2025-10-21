def combinar_listas(*listas):
    res=[]
    for l in listas:
        res+=l
    return res

print(combinar_listas([1,2],[3,4],[5]))
