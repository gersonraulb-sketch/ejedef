def split_por_tamano(s,n):
    return [s[i:i+n] for i in range(0,len(s),n)]

print(split_por_tamano('abcdefgh',3))
