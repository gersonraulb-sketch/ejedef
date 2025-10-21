class GeneradorID:
    def __init__(self):
        self._n=0
    def siguiente(self):
        self._n+=1
        return self._n
g=GeneradorID()
print(g.siguiente(),g.siguiente())
