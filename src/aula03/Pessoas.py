from datetime import date
class Pessoas:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    def Calculaidadeano(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    def MaiorIdade(idade):
        return idade >= 18
pessoa1 = Pessoas("gabriel", 26)
print(pessoa1.idade)
print(Pessoas.MaiorIdade(16))