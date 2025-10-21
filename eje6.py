def contar_vocales(txt):
    voc='aeiouAEIOU'
    cont=0
    for letra in txt:
        if letra in voc:
            cont+=1
    return cont

print(contar_vocales('Python'))
