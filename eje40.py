def separar_pares_impares(nums):
    pares=[x for x in nums if x%2==0]
    imp=[x for x in nums if x%2!=0]
    return pares,imp

print(separar_pares_impares([1,2,3,4,5]))
