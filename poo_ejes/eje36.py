class Orden:
    def __init__(self,id,items):
        self.id=id
        self.items=items
    def total(self):
        return sum(self.items)
o=Orden(1,[10,20,30])
print(o.total())
