def es_anio_valido(s):
    try:
        y=int(s)
        return 0<y<10000
    except:
        return False

print(es_anio_valido('2020'))
