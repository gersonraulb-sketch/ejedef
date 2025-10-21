def generar_multiples(n,m):
    return [i for i in range(n, m+1) if i%n==0]

print(generar_multiples(3,20))
