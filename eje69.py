def encontrar_subcadena_indices(s,sub):
    res=[]
    i=0
    while True:
        i=s.find(sub,i)
        if i==-1: break
        res.append(i)
        i+=1
    return res

print(encontrar_subcadena_indices('abababa','aba'))
