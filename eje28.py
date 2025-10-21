def contar_negativos(nums):
    return sum(1 for x in nums if x<0)

print(contar_negativos([1,-2,3,-4,0]))
