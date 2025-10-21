def suma_diagonal(m):
    return sum(m[i][i] for i in range(len(m)))

print(suma_diagonal([[1,2,3],[4,5,6],[7,8,9]]))
