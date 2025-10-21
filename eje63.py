def es_capicua_numero(n):
    s=str(n)
    return s==s[::-1]

print(es_capicua_numero(1221))
