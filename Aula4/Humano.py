#!/usr/bin/env python3

import random
class Humano:
    #atributos
    #perna = 2
    #bracos = 2
    #cabeca =1
    _PI = 3.1415  # declarado como privado por __



#metodos magicos - para estruturas de classe

    def __init__(self, nome):  #metodo construtor
        self.perna = 2
        self.braco = 2
        self.nome = nome
        self.saldo = 0

    #metodo
    def acidente(self):
        self.perna -= 1
    def saldo_bancario(self):
        if self.perna < 2 and self.nome == 'Carlos':
            self.saldo -= 10000
            print('vc esta de ferias')
            if random.randint(1,10) == 9:
                self.saldo *= -1
        else: 
            print('vc nao e o carlos ok')
            self.saldo += 10000
            print(f'vc agora tem saldo {self.saldo}')


    
carlos = Humano('Carlos')


# carlos._PI = 4
# print(carlos._PI)
# print(Humano._PI)

print(carlos.perna)
carlos.acidente()
print(carlos.perna)
carlos.saldo_bancario()
print(carlos.saldo)





    
