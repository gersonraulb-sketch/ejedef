def primera_repeticion(seq):
    seen=set()
    for x in seq:
        if x in seen:
            return x
        seen.add(x)
    return None

print(primera_repeticion([2,5,1,2,3]))
