class Cache:
    def __init__(self):
        self._cache = {}

    def get(self, k, fn):
        if k not in self._cache:
            self._cache[k] = fn()
        return self._cache[k]


c = Cache()
print(c.get("x", lambda: sum(range(100))))
print(c.get("x", lambda: 0))
