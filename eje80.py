def sumar_matrices(a,b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

print(sumar_matrices([[1,2],[3,4]],[[1,1],[1,1]]))
