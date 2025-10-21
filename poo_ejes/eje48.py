class Logger:
    def __init__(self,level="INFO"):
        self.level=level
    def log(self,msg):
        print(f"[{self.level}] {msg}")
Logger("DEBUG").log("mensaje")
