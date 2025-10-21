def merge_intervals(intervals):
    intervals=sorted(intervals,key=lambda x:x[0])
    merged=[]
    for start,end in intervals:
        if not merged or start>merged[-1][1]:
            merged.append([start,end])
        else:
            merged[-1][1]=max(merged[-1][1],end)
    return merged

print(merge_intervals([[1,3],[2,6],[8,10]]))
