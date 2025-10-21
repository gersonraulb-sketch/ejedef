def generar_claves_prefijo(pref,n):
    return [f'{pref}{i}' for i in range(n)]

print(generar_claves_prefijo('id',5))
