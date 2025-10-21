def convertir_a_bool(vals):
    return [bool(x) for x in vals]

print(convertir_a_bool([0,1,'',[],'ok']))
