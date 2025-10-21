def convertir_base(n,base):
    digits='0123456789ABCDEF'
    if n==0:
        return '0'
    res=''
    negative=n<0
    n=abs(n)
    while n>0:
        res=digits[n%base]+res
        n//=base
    return ('-'+res) if negative else res

print(convertir_base(255,16))
