from functools import reduce

def producto(nums):
    return reduce(lambda a,b: a*b, nums, 1)

print(producto([2,3,4]))
