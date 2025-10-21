def union(list1,list2):
    return list(dict.fromkeys(list1+list2))

print(union([1,2],[2,3]))
