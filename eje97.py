def max_suma_subarray(nums):
    max_ending=max_so_far=nums[0]
    for x in nums[1:]:
        max_ending=max(x,max_ending+x)
        max_so_far=max(max_so_far,max_ending)
    return max_so_far

print(max_suma_subarray([-2,1,-3,4,-1,2,1,-5,4]))
