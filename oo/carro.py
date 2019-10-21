class Motor:
    def __init__(self):
        velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE='Norte'
LESTE='Leste'
OESTE='Oeste'
SUL='Sul'

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        LESTE: NORTE, SUL: LESTE, OESTE: SUL, NORTE: OESTE
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = rotacao_a_direita_dict[self.valor]
    def girar_a_esquerda(self):
        self.valor = rotacao_a_esquerda_dict[self.valor]

class Carro(Motor, Direcao):
    def calcular_velocidade(self):
        motor = Motor()
        vel = motor.velocidade
        motor.acelerar(vel)
        motor.frear(vel)
        return vel

    def calcular_direcao(self):
        direcao = Direcao()
        val = direcao.valor
        direcao.girar_a_direita(val)
        direcao.girar_a_esquerda(val)


carro = Carro()
print(carro.calcular_direcao())
print(carro.calcular_velocidade())
