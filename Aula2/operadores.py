#!/usr/bin/python3

###########
##operadores aritmeticos
#######


## variaveis por nomenclatura podem 
# ter no maximo 16 caracteres

num1 = 6
num2 = 8
adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
result_div_int = num1 // num2
resto_div_int = num1 % num2

#operadores forma abreviada
#pega o valor do numero e realiza um calculo
#atribuindo o resultado a variavel

numero = 1
numero += 3  ## 1 + 3           numero = numero +3
numero -= 4  # 4 - 3            numero = numero -3
numero *= 4  #1 * 4             numero = numero * 4
numero /= 2  #4 / 2             numero = numero / 2
numero %= 2  # 2 % 2 = 0        numero = numero % 2

############
## operadores relacionais
######
# revem para comparacao entre fatores

numero1 = 6
numero2 = 9
numero3 = numero1

print(numero1 == numero2) # false
print(numero1 != numero2) # diferencicacao True
print(numero1 < numero2)  # menor que true
print(numero1 <= numero2) # menor igual true
print(numero1 > numero2)  # maior que false
print(numero1 >= numero2) # maior igual False

print(numero1 is numero3) # compara se estao alocados 
                            #no mesmo bloco de memoria true * objetos

lista = ['item1', 'item2','item3']
print('item1' in lista) #







