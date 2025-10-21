class Contacto:
    def __init__(self,nombre,email):
        self.nombre=nombre; self.email=email
    def validar_email(self):
        return "@" in self.email and "." in self.email.split("@")[-1]
c=Contacto("Ana","a@b.com")
print(c.validar_email())
