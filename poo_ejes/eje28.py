class Animal:
    def sonar(self):
        return "sonido"
class Pato(Animal):
    def sonar(self):
        return "cuac"
def hacer_sonar(obj):
    print(obj.sonar())
hacer_sonar(Pato())
class Robot:
    def sonar(self):
        return "beep"
hacer_sonar(Robot())
