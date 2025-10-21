def mayor_edad(nombre,edad):
    if edad>=18:
        return f'{nombre} es mayor de edad'
    else:
        return f'{nombre} es menor de edad'

print(mayor_edad('Carlos',20))
print(mayor_edad('Ana',16))
