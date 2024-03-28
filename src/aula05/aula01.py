class veiculos:
    def __init__(self, nome, quilometros_percorridos, velocidade_maxima):
        self.nome = nome
        self.quilomtros_percorridos = quilometros_percorridos
        self.velocidade_maxima = velocidade_maxima
    def to(self):
        print(f"nome={self.nome}")
        print(f"quilometros_pc= {self.quilomtros_percorridos}")
        print(f"volcidade_mx= {self.velocidade_maxima}")
class Onibus(veiculos):
    pass

carro = veiculos("prisma", 10, 180)
print(carro.to())
onibus = Onibus("scania", 120, 8)
print(onibus.to())