def lista_indices_minimos(nums):
    m=min(nums)
    return [i for i,x in enumerate(nums) if x==m]

print(lista_indices_minimos([2,1,3,1,4]))
