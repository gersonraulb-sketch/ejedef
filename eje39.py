def desviacion_estandar(nums):
    mean=sum(nums)/len(nums)
    var=sum((x-mean)**2 for x in nums)/len(nums)
    return var**0.5

print(desviacion_estandar([1,2,3,4,5]))
