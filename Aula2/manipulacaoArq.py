#!/usr/bin/pythin3

#######################
# manipulacao de arquivos
################333

### abrir um arquivo para modificação
# ### metodo nao recomendado
# ponteiro = open('nomedoarquivo.txt','r+') # abre um ponteiro para escrita de arquivos
# #, o modo utilizado é o read plus  (r+)(que ser para leitura e escrita.
# #  Possuimos varios modos de acesso), por exemplo:
# # w = escrita
# # r = leitura
# # r+ = leitura e escrita
# # +  = abre um arquivo para atualização (acrescenta e modifica)
# # a = complemento
# # x = criação
# #este método não é recomendado porque o ponteiro sempre necessita
# #ser encerrado com o close, isso foi substituido com a adção do comamdo with


# ponteiro.write('ola mundo\n')
# ponteiro.close()

## metodo usual
#arquivo em modo de escrita

with open('nomedoarquivo2.txt','w') as arquivo:
    arquivo.write('ola mundo\n')
#arquivo em modo de leitura
with open('nomedoarquivo2.txt', 'r') as arquivo:
    #arquivo.readlines()
    letras = arquivo.read()
print(letras)
