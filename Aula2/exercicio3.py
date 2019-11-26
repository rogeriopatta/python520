#!/usr/bin/python3

#######
## Exercicio de excessões
#######

# Criar uma tela de cadastro de usuário em uma lista
# Essa tela não pode aceitar figuras públicas que geram polêmica
# ex = Bolsonaro, Lula, Adolf Hitler, Tiririca
# Esse Loop é infinito, onde só acaba quando colocado uma figura
# pública

# Arrays de nomes de figura publica
# bolsonaro = [
#     'bolsonaro',
#     'bozo',
#     'bolsanario',
#     'borsalino',
#     'bonoliro',
#     'facista'
#     ]
# lula = [
#     'lula',
#     'mula',
#     '9 dedos',
#     'nove dedos',
#     'ladrão',
#     'luladrão'
#     ]
# hitler = [
#     'adolf hitler',
#     'hitler',
#     'fuhr',
#     'bigodin',
#     'nazista',
#     'argentino'
# ]
# tiririca = [
#     'tiririca',
#     'palhaço',
#     'tiririca',
#     'florentina'
# ]

# #Atribuindo todas as figuras públicas para uma lista
# figuras_publicas = [bolsonaro, lula, hitler, tiririca]


# #atribuindo todas os apelidos a um arquivo de texto

# for figura in figuras_publicas:
#     for apelido in figura:
#         with open('politicos.txt', 'a') as arquivo:
#             arquivo.write(apelido + '\n')


#print(figuras_publicas)

#definindo lista de nomes
lista_nomes = []


with open('politicos.txt','r') as arquivo:
    figuras_publicas = arquivo.readline()
with open('nomes.txt','r') as nomes:
    lista_nomes = [nomes.replace('\n','')for nome in nomes.readlines()]


try:
    while True:
        #requisição pelo nome
        print(figuras_publicas)
        nome = input('Digite um nome: ').lower().strip()

        # para cada figura publica, vou validar o nome digitado
        
        if nome in figuras_publicas:
            cad_figura_publica = True
        
        else:
            cad_figura_publica = False
        #Criando lógica para cadastro
        if cad_figura_publica:
            raise ValueError('vc tentu inserir uma figura publica!!')
            #print('Lançando erro Cadastro de figuras')
        elif nome in lista_nomes:
            print('nome Já existe')
        elif nome == 'visualizar':
            for nome_cadastrado in lista_nomes:
                print(nome_cadastrado,end=', ')
            print('\n')
        else:
            print('\n'*50)
            with open('nomes.txt', 'a')as nome:
                nome.write(nome + '\n')
            print('Cadastro Realizado')
            #lista_nomes.append(nome)

except Exception:
    print('Você tentou cadastrar uma figura pública')
    print(lista_nomes)

