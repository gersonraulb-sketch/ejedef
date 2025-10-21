def conteo_palabras(frase):
    d={}
    for w in frase.lower().split():
        d[w]=d.get(w,0)+1
    return d

print(conteo_palabras('hola hola mundo'))
