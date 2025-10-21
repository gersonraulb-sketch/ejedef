class Queue:
    def __init__(self):
        self._q=[]
    def enqueue(self,x): self._q.append(x)
    def dequeue(self): return self._q.pop(0) if self._q else None
q=Queue(); q.enqueue(1); q.enqueue(2)
print(q.dequeue()); print(q.dequeue()); print(q.dequeue())
