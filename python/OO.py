"""
classe
objeto
construtor
metodos
atributos
heranca

sobrecarga de metodos
pomorfismo
destrutores
"""

class Casa(object):

    cor = 'Azul'
    altura = 3
    quartos = 4

    def __init__(self, cor, altura, quartos):
        self.cor = cor
        self.altura = altura
        self.quartos = quartos

    def pintar(self, cor):
        self.cor = cor

    def aumenta_quartos(self, quartos):
        self.quartos = quartos

    def imprime_casa(self):
        print(self.cor, self.altura, self.quartos)

minha_casa = Casa('Perola', 3, 5)

print(minha_casa.cor)
minha_casa.pintar('Roxa')
print(minha_casa.cor)

print('')

print(minha_casa.quartos)
minha_casa.aumenta_quartos(7)
print(minha_casa.quartos)

minha_casa.imprime_casa()

