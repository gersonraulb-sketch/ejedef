def diccionario_por_longitud(palabras):
    return {p:len(p) for p in palabras}

print(diccionario_por_longitud(['hola','mundo']))
