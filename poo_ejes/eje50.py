class DecoradorSimple:
    def __init__(self,fn):
        self.fn=fn
    def __call__(self,*a,**k):
        print("antes")
        res=self.fn(*a,**k)
        print("despues")
        return res
@DecoradorSimple
def saludar(n): return f"hola {n}"
print(saludar("Ana"))
