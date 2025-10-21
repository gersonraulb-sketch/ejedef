def fib_iter(n):
    a,b=0,1
    res=[]
    for _ in range(n):
        res.append(a)
        a,b=b,a+b
    return res

print(fib_iter(8))
