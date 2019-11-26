# #!/usr/bin/python3

# ##############
# ##tratando excecoes
# ##########3

# try:
#     numero1 = int(input('digite um anumero a ser dividido: '))
#     numero2 = int(input('digite outro numero a ser dividido : '))
#     print(numero1 / numero2)
# #except ValueError:
#  #   print('insira somente numero')
# #except ZeroDivisionError as e:
#  #   print('nao foi possivel dividir',e)
# except Exception as e:
#     print('erro',e)
# #finally:
#  #       print('saindo do script')

############
#lançando exceções
#########3


#try:
opcao = int(input('nao digite 5!'))
if opcao == 5:
    raise ValueError('eu avisei para nao digitar 5 !')
#except ValueError as e:
 #   print('deu erro:', e)