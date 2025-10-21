def es_palindromo(txt):
    txt_limpio=''.join(ch.lower() for ch in txt if ch.isalnum())
    return txt_limpio==txt_limpio[::-1]

print(es_palindromo('anita lava la tina'))
