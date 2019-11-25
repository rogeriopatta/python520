#!/usr/bin/python3

# import random



# lista = ['Arroz', 'Feijão', 'Óleo', 'Sal', 'Açucar', 'Tempero']
# print(lista[0])
# #lista3d = [
# #    [2,3,4,5],
#  #   [5,6,7,8],
#   #  [9,0,2,input('digite numero')], # pode usar funções em matrizes

# #vetores multidimensionais
# lista3d = [
#     [2,3,4,5],
#     [5,6,7,8],
#     [9,0,2,6],
# ]
# print (lista3d)

# #adicionar um item no final da lista
# lista.append('carne')

# #ordena lista
# lista.sort()
# print(lista)

# #quantidade de elementos da lista
# print(len(lista))

# #mostra posição do item
# print(lista.index('Açucar'))

# #mostra a contagem de um item da lista
# print(lista.count('Arroz'))

# #remove o primeiro indice encontrado com o valor
# lista.remove('Arroz')


#####################################
## Tuplas

## tupla é como lista mas não permite modificação de seus itens





# #primeiro metodo para criar tupla
# tupla = ('maça', 'banana', 'laranja', 'abacaxi', 'uva')


# #segundo método para criar tuplas
# tupla2 = 'valor1', 2, True, 2j


# print(tupla[0])
# print(tupla2)

# #converter tupla para lista
# lista_da_tupla = list(tupla)
# print(lista_da_tupla)

# #ver tipo da lista / tupla
# print(type(lista_da_tupla))
# print(type(tupla2))

# #pode se modificar uma lista dentro de uma tupla
# tupla = (['indice 1'], 'nome')
# tupla[0].insert(1, 'indice 2')
# print(tupla)


# ###########
# ## dicionarios

# ##criando dicionario

# apresentacoes = {

#   'paulista' : 'salve',
#   'carioca' : 'eae',
#   'pirata' : 'Argh',
#   'mineiro':'pao de queijo',
#   'acre':'barulhos dinossauro',
# }
# #print(apresentacoes)

# #acessando dicionario
# #print(apresentacoes['paulista'])        

# #criando um dicionario com multi-valores internos

# linguagem_favorita = {

#     'daniel': {
#         'linguagem': 'pithon',
#         'tempo_de_experiencia': 5
#     },
#     'Olympio':{
#         'linguagem': 'R',
#         'linguagem2': 'VBA',
#         'tempo_de_experiencia': 10
#     },   

# }

# print(linguagem_favorita.get('daniel'))
# print(linguagem_favorita.get('daniel')['linguagem'])

# #acesso a todas as chaves
# print(linguagem_favorita.keys())

# #acesso aos valores
# print(linguagem_favorita.values())

# #acesso aos itens
# print(linguagem_favorita.items())

# print(valores.items())


##################
## numeros
###############

somar = 2 + 2
print(somar) # somar retorna um tipo inteiro

subtrair = somar - 2
print(subtrair) #subtrair retorna um tipo inteiro

multiplicar = subtrair * 3
print(multiplicar)   # multiplicar retorna um tipo inteiro

divisao = multiplicar / 5
print(divisao )  #divisão retorna ponto flutuante

potencia = 2**3
print(potencia)

raiz = 2** 0.5 # raiz quadrada
print(raiz)


letras = 'abcdefghji' + ' klmnopqrstu'
print(letras)


#conversão de tipo de dado, float no caso

print(float(input('digite numero: ')) + float(input('digite outro numero: ')))

git remote add origin https://github.com/rogeriopatta/python520.gi


