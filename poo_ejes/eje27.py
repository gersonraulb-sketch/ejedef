class A:
    def metodo(self):
        return "A"
class B(A):
    def metodo(self):
        return "B"
class C(B):
    pass
print(C().metodo())
