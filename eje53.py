def primeros_unicos(lst,n):
    res=[]
    seen=set()
    for x in lst:
        if x not in seen:
            res.append(x); seen.add(x)
        if len(res)==n:
            break
    return res

print(primeros_unicos([1,2,1,3,2,4],3))
