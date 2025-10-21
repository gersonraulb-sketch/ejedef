class Orden:
    contador=0
    def __init__(self,items):
        Orden.contador+=1
        self.id=Orden.contador
        self.items=items
o1=Orden(["a","b"])
o2=Orden(["c"])
print(o1.id,o2.id)
