#!/usr/bin/env python3
class Animal:
    nome = 'Animal'
    cabeca = 1

    def __init__(self):
        pass
        
    def viver(self):
        print('Estou vivo!!')

class Cachorro(Animal):

    '''abstração de uma cachorro

    cria cachorro baseado em conceitos definidos em sala '''

    _DNA =  'Cachorro'


    def __init__(self,nome,idade,cor,raca,porte= 'medio'):
        # atributos obrigatorios para existir um cachorro
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.raca = raca
        self.porte = porte
        
        #atributos padrao para cada cachorro
        self.patas = 4
        self.orelhas = 2
        self.focinho = True # valores unicos como true e false
        self.lingua = True
        self.olhos = 2
        self.rabo = True
        print(f'cachorro {nome}, construido com sucesso!')


        # o que faz - métodos
    def latir(self):
            if self.lingua:
                print(f'{self.nome} au, au, au')

    def comer(self):
            print('comendo')

    def defecar(self):
        print('defecando...')
        
    def dormir(self):
        print('dormindo...')
        
    def cheirar(self):
        if self.focinho:
             print('sniiff...sniif  ')

        
    def __del__(self):
        print(f'descanse em paz {self.nome}')
        

    def __str__(self):
        return 'constroi um cachorro'
        
        
        
        
print(Cachorro)
        

# rex = Cachorro()
# rex.viver()
# rex.latir()



