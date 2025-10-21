def promedio_ponderado(vals,weights):
    total=sum(v*w for v,w in zip(vals,weights))
    wsum=sum(weights)
    return total/wsum if wsum else 0

print(promedio_ponderado([3,4],[1,2]))
