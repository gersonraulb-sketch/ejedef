def ordenar_por_vocal_final(lst):
    return sorted(lst, key=lambda w: w[-1] if w else '')

print(ordenar_por_vocal_final(['casa','auto','barco']))
