def rot13(s):
    def shift(c):
        if 'a'<=c<='z':
            return chr((ord(c)-97+13)%26+97)
        if 'A'<=c<='Z':
            return chr((ord(c)-65+13)%26+65)
        return c
    return ''.join(shift(c) for c in s)

print(rot13('Hola'))
