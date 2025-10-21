def capitalizar_palabras(s):
    return ' '.join(w.capitalize() for w in s.split())

print(capitalizar_palabras('hola mundo desde python'))
