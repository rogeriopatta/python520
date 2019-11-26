#!/usr/bin/python3

#validar uma entrada com while, enquantonao digitar fica em loop

# sair = ''
# while (not sair == 'sair'):
#     sair = input('digite algo')

# i = 10
# while(True):
#     i+= 1
#     if i ==10:
#         break
#     if i == 5:
#         continue
#     print('teoricamente, um loop infinito')


# i = 100  #iterador regressivo
# while i > 0:
#     i -= 1
#     if i % 2 == 0:
#         continue
#     print(i)



#############
#laço for - percorre itens em determinado range de valores
###########


# lista = []
# for i in range(80,100,1): # de 80 a 10 de um em um
#     lista.append(i)
# print(lista)

# for i in lista:
#     if i % 2 ==0:
#         print(f"\033[91m{i}\033[0m", 'par')  # muda cor do caractere para vermelho
#     if i % 2 == 1:
#         print(f'\033[32m{i}\033[0m','impar') # muda para verde


#percorrer um dicionario

# dicionario = {
#     'nome':'daniel',
#     'sobrenome':'silva'
#     }

# for i in dicionario:
#     print(dicionario[i])

# for chave, valor in dicionario.items():
#     print(chave)
#     print(valor)

# lista = ['item', 'item2','item3','item4','item5', 'item6', 'item7']
# print(list(enumerate(lista)))



#list comprehension ( compreensão de listas)



lista = [ x*2 for x in range(100)]
print(lista)