#!/usr/bin/python3

##############
##funções
#############


def mostrar_hello_world():
    print('hello world')
# mostrar_hello_world()


def menu():
    print('escolha opcao')
    print('1 - registrar Produto')
    print('2 - consultar saldo do caixa')
    print('3 - abrir caixa registradora')
    print('4 - fechamento mes')
    return input('digite a opacao desejada:')

#estrutura principal
print('Caixa resgistradora')

opcao = menu()
if opcao =='1':
    pass #funcao 1
elif opcao == '2':
    pass # funcao 2
elif opcao == '3':
    pass # funcao 3
elif opcao == '4':
    pass # funcao 4
else:
    pass # funcao 5

print(opcao)

