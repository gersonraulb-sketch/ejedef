def contar_sustituciones(s,old,new):
    return s.count(old), s.replace(old,new)

print(contar_sustituciones('aaaab','a','x'))
