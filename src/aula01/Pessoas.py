class Pessoas:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)
    def set_nome(self, nome):
        self.nome=nome
    def set_ender(self, ender):
        self. ender=ender
    def get_nome(self, nome):
        return  self.nome
    def get_ender(self, ender):
        return self.ender
pessoa1 = Pessoas("gabriel", "rua 201")
pessoa2 = Pessoas("vanessa", "rua 254")
print(f"ola {pessoa1.nome}, bem vindo")
