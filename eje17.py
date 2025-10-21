def calcular_imc(peso,altura):
    return peso/(altura**2)

imc=calcular_imc(70,1.75)
print(f'IMC: {imc:.2f}')
