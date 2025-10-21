def normalizar_texto(s):
    return ' '.join(s.strip().split()).lower()

print(normalizar_texto('  Hola   MUNDO  '))
