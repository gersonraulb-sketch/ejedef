def cuenta_vocales_conteo(s):
    from collections import Counter
    c=Counter(ch.lower() for ch in s if ch.isalpha())
    return sum(c[v] for v in 'aeiou' if v in c)

print(cuenta_vocales_conteo('Python'))
