def pertenece_numpy_style(x,arr):
    return any(x==y for y in arr)

print(pertenece_numpy_style(3,[1,2,3]))
