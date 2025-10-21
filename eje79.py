def intercalar_listas(a,b):
    res=[]
    for x,y in zip(a,b):
        res.extend([x,y])
    res.extend(a[len(b):] or b[len(a):])
    return res

print(intercalar_listas([1,3,5],[2,4,6]))
