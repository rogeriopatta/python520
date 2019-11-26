#!/usr/bin/python3

#criar uma variavel idade que recebe
#via linha de comando, validar se essa
#pessoa pode beber ou nao se for habilitada


# idade = int(input('qual sua idade ? ')) 
# embriagado = input('vc bebeu ? responda sim (s) ou nao (n)')
# habilitacao = input('vc eh habilitada? sim (s) ou nao (n)')

# if  idade >= 18:
#     if embriagado != 's' and
#     val_carteira = True
# else:
#     val_carteira = False

# if idade >= 18 and val_carteira:  #faz um and com a variavel val_carteira que e True 1 
#       print('vc pode dirigir !')
#       embriagado = True
# else:
#     print('vc nao pode dirigir!!!!')

if idade >= 18:
    # If's validam se variável tem conteúdo
    habilitacao = input('Você possui Habilitação: [y para sim e n para não] ').strip().lower()
    if habilitacao == 'y':
        habilitacao = True
        bebeu = input('Você bebeu? digite algo para sim, enter para não ').strip()
        if bebeu:
            embriagado = True
        else:
            embriagado = False
    else:
        habilitacao = False
else:
    embriagado = False

if habilitação and not embriagado:
    print('voce pode dirigir')
else:
    print('voce nao pode dirigir')



  
