def ancho_palabra_mas_larga(palabras):
    return max(len(w) for w in palabras) if palabras else 0

print(ancho_palabra_mas_larga(['hola','mundo','python']))
