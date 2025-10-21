def map_dict_values(d,func):
    return {k:func(v) for k,v in d.items()}

print(map_dict_values({'a':1,'b':2},lambda x:x*10))
