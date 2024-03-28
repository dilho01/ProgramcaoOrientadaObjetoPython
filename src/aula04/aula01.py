class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self ):
        return self.a + self.b
    def Multiplica(self):
        return self.a * self.b
class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a - self.b
    def dividri(self):
        return self.a / self.b
d = Derivada(10,20)
print(d.soma())

