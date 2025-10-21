def promedio_condicional(nums,cond):
    f=[x for x in nums if cond(x)]
    return sum(f)/len(f) if f else 0

print(promedio_condicional([1,2,3,4], lambda x: x%2==0))
