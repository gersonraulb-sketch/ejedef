class Punto:
    def __init__(self,x,y):
        self.x=x; self.y=y
    def distancia(self,otro):
        return ((self.x-otro.x)**2+(self.y-otro.y)**2)**0.5
p1=Punto(0,0); p2=Punto(3,4)
print(p1.distancia(p2))
