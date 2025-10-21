def contador_palabras_mas_50(frase):
    return sum(1 for w in frase.split() if len(w)>5)

print(contador_palabras_mas_50('esto es una prueba con varias palabras'))
