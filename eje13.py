def es_primo(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

print(es_primo(17))
print(es_primo(15))
