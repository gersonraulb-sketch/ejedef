def comprimir_rango(nums):
    if not nums: return []
    nums=sorted(set(nums))
    ranges=[]
    start=prev=nums[0]
    for n in nums[1:]:
        if n==prev+1:
            prev=n
        else:
            ranges.append((start,prev)); start=prev=n
    ranges.append((start,prev))
    return ranges

print(comprimir_rango([1,2,3,5,6,9]))
