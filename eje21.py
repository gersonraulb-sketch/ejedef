def es_anagrama(a,b):
    return sorted(a.replace(' ','').lower())==sorted(b.replace(' ','').lower())

print(es_anagrama('roma','amor'))
print(es_anagrama('hola','adios'))
