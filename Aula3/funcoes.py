 #!/usr/bin/python3

# ##############
# ##funções
# #############


# def mostrar_hello_world():
#     print('hello world')
# # mostrar_hello_world()

# # criando estrtura de funcao
# def menu():
#     print('escolha opcao\n')
#     print('1 - registrar Produto')
#     print('2 - consultar saldo do caixa')
#     print('3 - abrir caixa registradora')
#     print('4 - fechamento mes\n')
#     return input('digite a opacao desejada:\n')

# #estrutura principal
# def registrar_produto():
#     print('produto registrado  ')

# def consultar_saldo():
#     print('saldo de X R$  ')

# def abrir_caixa():
#     print('abrindo caixa  ')

# def fechamento():
#     print('fechando caixa  ')

# while True:
    
#     print('\nCaixa resgistradora\n  ')

#     opcao = menu()

#     if opcao =='1':
#         registrar_produto() #funcao 1

#     elif opcao == '2':
#         consultar_saldo()   # funcao 2

#     elif opcao == '3':
#         abrir_caixa()       # funcao 3

#     elif opcao == '4':
#         fechamento()        # funcao 4
#     else:
#         break 
#     input()

# print(opcao)



##funções anomimas
var = lambda x : x*2
print(var(2))

numeros = list(range(1,100))
print(numeros)
# def dobro(x):
#     return x * 2


#print(list(map(dobro, numeros)))

#map atribui uma lista de valores (numeros) a uma função (dobro) e mostra o resultado de cada iteração

print(list(map(lambda x : 2 * x, numeros))) # lambda faz a mesma coisa que map