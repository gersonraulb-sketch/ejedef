def suma_prefijos(nums):
    res=[]
    total=0
    for x in nums:
        total+=x
        res.append(total)
    return res

print(suma_prefijos([1,2,3,4]))
