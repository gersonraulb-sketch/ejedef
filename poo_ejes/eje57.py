class Plugin:
    def ejecutar(self): pass
class PluginA(Plugin):
    def ejecutar(self): return "A"
class PluginB(Plugin):
    def ejecutar(self): return "B"
plugins=[PluginA(),PluginB()]
print([p.ejecutar() for p in plugins])
