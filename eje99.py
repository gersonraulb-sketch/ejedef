def validar_clave_segura(pw):
    import re
    return len(pw)>=8 and re.search(r'[A-Z]',pw) and re.search(r'[a-z]',pw) and re.search(r'\d',pw)

print(bool(validar_clave_segura('Aa123456')))
