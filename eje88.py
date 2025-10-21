def unico_mas_vezes(seq):
    from collections import Counter
    c=Counter(seq)
    return [x for x in seq if c[x]==1]

print(unico_mas_vezes([1,2,2,3,4,4,5]))
