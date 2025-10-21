def flatten_deep(lst):
    res=[]
    for x in lst:
        if isinstance(x,list):
            res+=flatten_deep(x)
        else:
            res.append(x)
    return res

print(flatten_deep([1,[2,[3,4]],5]))
