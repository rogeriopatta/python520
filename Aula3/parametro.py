# # # #!/usr/bin/python3
# # # '''parametro python - titulo

# # #  esta aula ensina a criar e documentar funções

# # # '''

# # # ###############
# # # ## parametro de funcao
# # # #############

# # # def retorna_pessoa(nome, idade=99):
# # #     print(f'nome: {nome}\n idade: {idade}')

# # # retorna_pessoa(nome='rogerio', idade=220)


# # # ##especificar tipo de parametro e retorno @@@@faltou explicação

# # # def retorna_valor_int(variavel1: int, variavel2 : bool) :
# # #     ''' função com anotação de tipo

# # #     sempre pular uma linha

# # #     ''''
# # #     return 'valor'
    
# # # print(retorna_valor_int(1, False) 


# # ### args kwargs

# # #print('ola', 'mundo',',','prazer', 'sou', 'rogerio')


# # ### criando uma função que recebe multiplos valores - args

# # def funcao_multivalores(parametros_estaticos, *argumento_variavel):
# #     print(parametros_estaticos, 'parametro estatico')
# #     print(argumento_variavel)
# #     #fazendo acesso aos parametros
# # #    for argumento in argumento_variavel:
# #         #print(argumento)

# # # funcao_multivalores('valor_estatico_obrigatorio',
# # #                       'daniel', 'lucas', 'leonardo' , 'rogerio',
# # #                       )


# # ##argumentos com palavra chave - kwargs


# def parametros_chave_valor(**dados):
#     if dados['nome'] == 'daniel':
#     #print(dados)
#         print('acesso negado')
#     else:
#         print('permitido')

# # execucao - metodo 1
# print('metodo 1')

# parametros_chave_valor(nome='daniel', sobrenome='silva',idade=19,sexo='masculino')

# # execucao - metodo 2
# print('metodo 2')

# dados_requisicao = {'nome':'daniel','sobrenome':'silva','profissao':'operador de empilhadeira'}

# parametros_chave_valor(**dados_requisicao)

###decoradores de função - modifica o valor de outra função

# #declara uma funcao com uma variavel funcao obrigatoria
# def muda_cor(funcao):
#     def modifica_azul(funcao):
#         return f'\033[91m{funcao}\033[0m'
#     return modifica_azul

# #muda_cor(input('texto'))

# @muda_cor  # muda cor do caractere de branco para vermelho
# def log(texto):
#     return texto
# print(log('oi'))
