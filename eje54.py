def agrupado_por_paridad(nums):
    pares=[x for x in nums if x%2==0]
    imp=[x for x in nums if x%2!=0]
    return {'pares':pares,'impares':imp}

print(agrupado_por_paridad([1,2,3,4,5]))
