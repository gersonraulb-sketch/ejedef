def encontrar_pares_cercanos(nums,k):
    s=set()
    res=[]
    for x in nums:
        if x-k in s or x+k in s:
            res.append(x)
        s.add(x)
    return res

print(encontrar_pares_cercanos([1,4,5,7,9],2))
