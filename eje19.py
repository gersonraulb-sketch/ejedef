def es_bisiesto(anio):
    return (anio%4==0 and anio%100!=0) or (anio%400==0)

print(es_bisiesto(2024))
print(es_bisiesto(2023))
